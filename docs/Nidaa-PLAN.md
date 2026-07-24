# Nidaa (نداء) — Build Plan & Phases

Phased roadmap from prototype → field-usable tool. Each phase ends with a
**verification gate** that must pass before the next phase starts. Research
basis: HDX (236 Syria datasets, incl. 3,060 real health facilities as GeoJSON),
ReliefWeb API v2 (live, free), Auth.js v5, better-sqlite3, Leaflet offline.

Guiding principle (from the journal): *the network will fail, and the tool must
be correct anyway.* Every phase preserves offline-first behavior.

---

## PHASE 0 — Harden & Verify Baseline  (prerequisite)
**Goal:** lock the prototype so later phases have a stable, tested base.

- Add a minimal test for the API contract (GET returns array, POST creates,
  verify flips flag) runnable with `npm test`.
- Pin `package-lock.json` (done), document Node version.
- README + JOURNAL already present.

**Verify:** `npm run build` green; API smoke test passes; Arabic round-trip OK.
**Effort:** ~0.5 day.

---

## PHASE 1 — Real Seed Data from HDX  ★ highest impact / lowest effort
**Goal:** replace illustrative seeds with verified, real Syrian (then Gaza) data.

- `scripts/import-hdx.ts`: downloads HDX GeoJSON by ISO3 (SYR first), maps OSM
  `amenity` → Nidaa category (hospital/clinic → medical, school → education,
  water_* → water, etc.), upserts as `verified: true` "offer" entries.
- Seed verified: Health Facilities of Syria (3,060 rows, Arabic+English names,
  geometry), then Education Facilities, Waterways, IDP Sites.
- Keep illustrative entries clearly tagged `source: "demo"` and removable.
- Add `region` field (syr | gza) to entries for multi-region scoping.

**Verify:** importer run produces N entries in db; GET returns them; a known
facility ("مستشفى درعا الوطني") is present and searchable by city.
**Effort:** ~1 day.

---

## PHASE 2 — Offline Maps (Leaflet + cached tiles)
**Goal:** turn stored lat/lng into a usable, offline-capable map.

- Add Leaflet (client-only, dynamic import to keep bundle small).
- Tile caching: cache viewed tiles in IndexedDB (localforage) when online;
  serve from cache when offline. Only cache visited areas (device-light).
- List/Map toggle in the board UI; tap a card → centers map.
- Gaza offline tiles reuse the same component.

**Verify:** map renders online; after visiting an area, go offline (devtools)
and confirm tiles still show; no console errors.
**Effort:** ~1.5 days.

---

## PHASE 3 — Auth + Role-Gated Verification  (closes security gap)
**Goal:** only trusted actors can mark entries verified.

- Adopt **Auth.js v5**. Roles: individual | volunteer | ngo | admin.
- `POST /api/verify` now requires session with role ngo|admin (401 otherwise).
- Local posts from unverified users stay "unverified" until an NGO confirms.
- Store users/sessions in DB (see Phase 4).
- NGO admin UI: queue of unverified entries → verify/reject with reason.

**Verify:** unauthenticated verify → 401; ngo session verify → 200 + flag flips;
individual session verify → 401. Build green.
**Effort:** ~2 days.

---

## PHASE 4 — Server Store Upgrade: JSON → SQLite
**Goal:** safe concurrent writes + scale to thousands of HDX rows + users.

- Introduce `better-sqlite3` (synchronous, zero-config) behind `lib/store.ts`
  (same function signatures: listEntries / upsertEntry / setVerified + new
  users/sessions/sync_log tables).
- Migration: import existing db.json entries into SQLite on first run.
- Postgres only if multi-instance/HA is needed later (documented, not built now).

**Verify:** all Phase 1–3 behaviors still pass against SQLite; bulk import of
3,060 rows completes without corruption; concurrent POSTs don't lose writes.
**Effort:** ~1.5 days.

---

## PHASE 5 — Sync Conflict Resolution (hard offline-first problem)
**Goal:** multiple volunteers editing offline don't silently clobber each other.

- Server-assigned canonical id on first sync (already done).
- Merge rule: `updatedAt` wins; if client edited *after* its last pull, mark
  entry `conflict: true` and surface both versions to an NGO reviewer.
- Client shows a "conflict" badge + diff; user picks or defers.
- Sync log table (Phase 4) records each push/pull for audit.

**Verify:** simulate two offline edits to same entry → both preserved, conflict
flagged, reviewer can resolve; no data loss.
**Effort:** ~2 days.

---

## STRETCH (post-Phase 5, optional)
- **WhatsApp/SMS bridge:** post needs via message ( Twilio / WhatsApp Business
  API). Reaches the ~64% who won't install an app. Handle PII carefully.
- **Multi-region deploy:** same code, `region=syr|gza` scoping, shared
  offline-first core.
- **ReliefWeb context cards:** pull v2 reports for a city as situational context.

---

## SEQUENCING SUMMARY
P0 Baseline → **P1 Real Data** → P2 Maps → **P3 Auth** → **P4 SQLite** → P5 Conflicts
→ Stretch.

Build order prioritizes the trio that moves Nidaa from "fake-data prototype" to
"real, safe, scalable tool": **P1 (real data) + P3 (auth) + P4 (SQLite)**.
P2 and P5 are depth/robustness on top of that foundation.

## STATUS
- [x] Prototype built & verified (build green, API + Arabic round-trip OK)
- [x] Repo on github.com/theabdlrah/nidaa (public)
- [x] Journal written (Desktop .docx)
- [ ] P0 — baseline tests
- [ ] P1 — HDX importer
- [ ] P2 — offline maps
- [ ] P3 — auth + gated verify
- [ ] P4 — SQLite store
- [ ] P5 — conflict resolution
