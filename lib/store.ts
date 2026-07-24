import { promises as fs } from "fs";
import path from "path";
import { NidaaEntry, DbShape, VerificationAudit, AssignmentAudit } from "./types";

const AUDIT_PATH = path.join(process.cwd(), "data", "verify-audit.json");

const DB_PATH = path.join(process.cwd(), "data", "db.json");

// In-process write lock: file read-modify-write is not atomic, and two
// concurrent POSTs could each read the old db and clobber the other's upsert.
// Serialize writes through a promise chain.
let writeChain: Promise<any> = Promise.resolve();
function withWriteLock<T>(fn: () => Promise<T>): Promise<T> {
  const run = writeChain.then(fn, fn);
  // keep the chain alive but swallow errors so one failure doesn't block others
  writeChain = run.then(
    () => undefined,
    () => undefined
  );
  return run;
}

// Separate lock for the verification audit log so audit writes are safe even if
// appendAudit is ever called outside the main db write lock.
let auditChain: Promise<any> = Promise.resolve();
function withAuditLock<T>(fn: () => Promise<T>): Promise<T> {
  const run = auditChain.then(fn, fn);
  auditChain = run.then(
    () => undefined,
    () => undefined
  );
  return run;
}

async function ensureDb(): Promise<void> {
  try {
    await fs.access(DB_PATH);
  } catch {
    // Honesty guard: NEVER fabricate data. Start empty and tell the operator to
    // load real data. (Previously this seeded illustrative/demo entries, which
    // made the prototype imply data it did not actually have.)
    const initial: DbShape = { entries: [] };
    await fs.mkdir(path.dirname(DB_PATH), { recursive: true });
    await fs.writeFile(DB_PATH, JSON.stringify(initial, null, 2), "utf-8");
    console.warn(
      "[nidaa] data/db.json not found — starting with an EMPTY board (no fabricated demo data). " +
        "Run `npm run import-hdx` to load real HDX / HOT OSM facility data."
    );
  }
}

export async function readDb(): Promise<DbShape> {
  await ensureDb();
  const raw = await fs.readFile(DB_PATH, "utf-8");
  const parsed = JSON.parse(raw) as DbShape;
  if (!Array.isArray(parsed.entries)) parsed.entries = [];
  return parsed;
}

export async function writeDb(db: DbShape): Promise<void> {
  await fs.mkdir(path.dirname(DB_PATH), { recursive: true });
  await fs.writeFile(DB_PATH, JSON.stringify(db, null, 2), "utf-8");
}

export async function listEntries(): Promise<NidaaEntry[]> {
  const db = await readDb();
  // newest first; backward-compat defaults for pre-M3 entries (no owner/assignedTo)
  return [...db.entries]
    .map((e) => ({
      ...e,
      owner: e.owner ?? e.authorRole,
      assignedTo: e.assignedTo ?? [],
    }))
    .sort(
      (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
    );
}

export async function upsertEntry(entry: NidaaEntry): Promise<NidaaEntry> {
  return withWriteLock(async () => {
    const db = await readDb();
    const idx = db.entries.findIndex((e) => e.clientId === entry.clientId);
    if (idx >= 0) {
      db.entries[idx] = entry;
    } else {
      db.entries.push(entry);
    }
    await writeDb(db);
    return entry;
  });
}

export async function setVerified(
  id: string,
  verified: boolean,
  actorRole: string
): Promise<NidaaEntry | null> {
  return withWriteLock(async () => {
    const db = await readDb();
    const entry = db.entries.find((e) => e.id === id || e.clientId === id);
    if (!entry) return null;
    const priorVerified = entry.verified;
    entry.verified = verified;
    await writeDb(db);

    // Audit log: every verification is logged and reversible (records prior state).
    const record: VerificationAudit = {
      entryId: entry.id,
      clientId: entry.clientId,
      actorRole,
      action: verified ? "verify" : "unverify",
      priorVerified,
      newVerified: verified,
      at: new Date().toISOString(),
    };
    await appendAudit(record);
    return entry;
  });
}

async function appendAudit(record: VerificationAudit): Promise<void> {
  return withAuditLock(async () => {
  let log: VerificationAudit[] = [];
  try {
    const raw = await fs.readFile(AUDIT_PATH, "utf-8");
    log = JSON.parse(raw) as VerificationAudit[];
    if (!Array.isArray(log)) log = [];
  } catch {
    log = [];
  }
  log.push(record);
  await fs.mkdir(path.dirname(AUDIT_PATH), { recursive: true });
  await fs.writeFile(AUDIT_PATH, JSON.stringify(log, null, 2), "utf-8");
  });
}

export async function readAudit(): Promise<VerificationAudit[]> {
  try {
    const raw = await fs.readFile(AUDIT_PATH, "utf-8");
    const log = JSON.parse(raw) as VerificationAudit[];
    return Array.isArray(log) ? log : [];
  } catch {
    return [];
  }
}

const ASSIGN_AUDIT_PATH = path.join(process.cwd(), "data", "assign-audit.json");

// M3 — privileged assignment (owner / assignedTo). Mirrors setVerified: gated by
// caller (route checks the token), writes the fields, and logs a reversible audit.
export async function setAssignment(
  id: string,
  patch: { owner?: string; assignedTo?: string[] },
  actorRole: string
): Promise<NidaaEntry | null> {
  return withWriteLock(async () => {
    const db = await readDb();
    const entry = db.entries.find((e) => e.id === id || e.clientId === id);
    if (!entry) return null;
    const records: AssignmentAudit[] = [];
    if (patch.owner !== undefined && patch.owner !== entry.owner) {
      records.push({
        entryId: entry.id,
        clientId: entry.clientId,
        actorRole,
        field: "owner",
        prior: entry.owner ?? null,
        next: patch.owner,
        at: new Date().toISOString(),
      });
      entry.owner = patch.owner;
    }
    if (patch.assignedTo !== undefined) {
      const prior = entry.assignedTo ?? [];
      if (JSON.stringify(prior) !== JSON.stringify(patch.assignedTo)) {
        records.push({
          entryId: entry.id,
          clientId: entry.clientId,
          actorRole,
          field: "assignedTo",
          prior,
          next: patch.assignedTo,
          at: new Date().toISOString(),
        });
        entry.assignedTo = patch.assignedTo;
      }
    }
    await writeDb(db);
    for (const r of records) await appendAssignAudit(r);
    return entry;
  });
}

async function appendAssignAudit(record: AssignmentAudit): Promise<void> {
  return withAuditLock(async () => {
    let log: AssignmentAudit[] = [];
    try {
      const raw = await fs.readFile(ASSIGN_AUDIT_PATH, "utf-8");
      log = JSON.parse(raw) as AssignmentAudit[];
      if (!Array.isArray(log)) log = [];
    } catch {
      log = [];
    }
    log.push(record);
    await fs.mkdir(path.dirname(ASSIGN_AUDIT_PATH), { recursive: true });
    await fs.writeFile(ASSIGN_AUDIT_PATH, JSON.stringify(log, null, 2), "utf-8");
  });
}

export async function readAssignAudit(): Promise<AssignmentAudit[]> {
  try {
    const raw = await fs.readFile(ASSIGN_AUDIT_PATH, "utf-8");
    const log = JSON.parse(raw) as AssignmentAudit[];
    return Array.isArray(log) ? log : [];
  } catch {
    return [];
  }
}
