# نداء · Nidaa

**Offline-first, Arabic-RTL community needs & services board for Syria.**

Nidaa (نداء = "call / appeal") is a humanitarian aid coordination board built for
how Syria actually is in 2025: **~64% of the population is offline**, internet
penetration is ~36%, infrastructure is damaged, and connectivity is slow,
intermittent, and expensive.

So Nidaa is **offline-first by design**:

- The device is the source of truth. New posts are saved **locally first**
  (IndexedDB) and synced to the server **only when a connection appears**.
- The app shell is cached by a service worker, so the board still loads and
  works with **zero connectivity** after the first visit.
- Arabic is the default language with full **RTL** layout; an English toggle
  is included.

## What it does

- Browse community **needs** and **offers** (medical, food, water, shelter,
  education, transport, other) by city.
- Post a new entry **even when offline** — it queues locally and pushes on reconnect.
- NGOs/admins can mark entries **verified** via `POST /api/verify`.
- Live online/offline + pending-sync status indicators.

## Stack

- **Next.js 14** (App Router) + **TypeScript**
- **Zero native dependencies** — server uses a JSON file store
  (`data/db.json`), so it runs anywhere with just Node. Swap for Postgres later.
- **idb** (IndexedDB) for the offline queue on the client.
- Service worker for app-shell offline caching.

## Run it

```bash
npm install
npm run dev      # http://localhost:3000
# or production:
npm run build && npm run start
```

There is also `start-nidaa.bat` — double-click it to install deps, launch the
server, and open it in Google Chrome.

## Important notes

- **Seed data is illustrative only** — it is NOT live operational information.
  Real deployments must source verified data from NGOs / local committees.
- The `/api/verify` route is open in this prototype. In production it **must**
  be gated behind authentication and authorization (only trusted NGOs/admins
  can mark entries verified).
- This is a portfolio / learning prototype, not a deployed service.

## API

| Method | Route           | Purpose                                     |
|--------|-----------------|---------------------------------------------|
| GET    | `/api/entries`  | Pull all entries (used by client sync)      |
| POST   | `/api/entries`  | Upsert one entry (offline-first sync push)  |
| POST   | `/api/verify`   | Mark an entry verified (auth-gated in prod) |

---

Built as a personal project to learn offline-first architecture and serve
communities with constrained connectivity.
