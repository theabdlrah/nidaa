import { openDB } from "idb";
import { NidaaEntry } from "./types";

// IndexedDB queue. The device is the source of truth (offline-first):
// new posts are written locally FIRST, then synced to the server when online.

const DB_NAME = "nidaa";
const STORE = "queue";

let dbPromise: Promise<any> | null = null;

function getDb() {
  if (!dbPromise) {
    dbPromise = openDB(DB_NAME, 1, {
      upgrade(db) {
        if (!db.objectStoreNames.contains(STORE)) {
          db.createObjectStore(STORE, { keyPath: "clientId" });
        }
      },
    });
  }
  return dbPromise;
}

// An entry lives locally and may have a `syncedAt` of null (pending).
export interface QueuedEntry extends NidaaEntry {
  syncedAt: string | null;
}

export async function saveLocal(entry: QueuedEntry): Promise<void> {
  const db = await getDb();
  await db.put(STORE, entry);
}

export async function allLocal(): Promise<QueuedEntry[]> {
  const db = await getDb();
  const all = (await db.getAll(STORE)) as QueuedEntry[];
  return all.sort(
    (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
  );
}

export async function pendingLocal(): Promise<QueuedEntry[]> {
  const all = await allLocal();
  return all.filter((e) => !e.syncedAt);
}

export async function markSynced(clientId: string, syncedAt: string): Promise<void> {
  const db = await getDb();
  const existing = (await db.get(STORE, clientId)) as QueuedEntry | undefined;
  if (existing) {
    existing.syncedAt = syncedAt;
    await db.put(STORE, existing);
  }
}

export async function removeLocal(clientId: string): Promise<void> {
  const db = await getDb();
  await db.delete(STORE, clientId);
}
