// lib/tileCache.ts
// Offline tile cache: stores map tile blobs in IndexedDB so the board map
// keeps rendering after the network disappears (Phase 2 offline-map goal).
import { openDB } from "idb";

const DB_NAME = "nidaa-tiles";
const STORE = "tiles";

let dbPromise: Promise<any> | null = null;
function getDb() {
  if (!dbPromise) {
    dbPromise = openDB(DB_NAME, 1, {
      upgrade(db) {
        if (!db.objectStoreNames.contains(STORE)) {
          db.createObjectStore(STORE); // keyPath = tile url
        }
      },
    });
  }
  return dbPromise;
}

export async function getTile(url: string): Promise<Blob | undefined> {
  try {
    const db = await getDb();
    return (await db.get(STORE, url)) as Blob | undefined;
  } catch {
    return undefined;
  }
}

export async function putTile(url: string, blob: Blob): Promise<void> {
  try {
    const db = await getDb();
    await db.put(STORE, blob, url);
  } catch {
    /* quota / private mode — ignore, map just falls back to network */
  }
}

// Build a Leaflet TileLayer that reads from cache first, then network,
// and writes successful fetches back into the cache.
export async function makeCachedTileLayer(urlTemplate: string, options: any) {
  const L = (await import("leaflet")).default;
  const Layer = L.TileLayer.extend({
    createTile(coords: any, done: any) {
      const tile = document.createElement("img");
      const url = this.getTileUrl(coords);
      const finish = (err: any) => {
        if (err) tile.onerror?.(err);
        else tile.onload?.(new Event("load"));
        done?.(err, tile);
      };
      getTile(url)
        .then((blob) => {
          if (blob) {
            const objUrl = URL.createObjectURL(blob);
            tile.onload = () => URL.revokeObjectURL(objUrl);
            tile.src = objUrl;
            finish(null);
            return;
          }
          // not cached: load + cache
          const img = new Image();
          img.crossOrigin = "anonymous";
          img.onload = () => {
            fetch(url, { mode: "cors" })
              .then((r) => r.blob())
              .then((b) => putTile(url, b))
              .catch(() => {});
            tile.src = url;
            finish(null);
          };
          img.onerror = (e) => finish(e);
          img.src = url;
        })
        .catch(() => {
          tile.src = url;
          finish(null);
        });
      return tile;
    },
  });
  return new (Layer as any)(urlTemplate, options);
}
