import { promises as fs } from "fs";
import path from "path";
import { NidaaEntry, DbShape, VerificationAudit } from "./types";
import { SEED_ENTRIES } from "../data/seed";

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

async function ensureDb(): Promise<void> {
  try {
    await fs.access(DB_PATH);
  } catch {
    const initial: DbShape = { entries: SEED_ENTRIES };
    await fs.mkdir(path.dirname(DB_PATH), { recursive: true });
    await fs.writeFile(DB_PATH, JSON.stringify(initial, null, 2), "utf-8");
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
  // newest first
  return [...db.entries].sort(
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
