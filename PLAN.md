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

## PHASE 6 — Offline-Native: Mesh Sync + Decentralized Trust
**Goal:** survive a TOTAL internet shutdown, not just intermittent connectivity.

- **Device-to-device sync (10.1):** WebRTC data-channel gossip over local
  WiFi/hotspot (or Bluetooth) so devices in the same room/camp exchange posts
  directly. Server is no longer a single point of failure for the board to update.
- **Idempotency (10.2):** already implemented (upsert by clientId) — server-side
  dedupe makes mesh forwarding and retries safe.
- **Priority-ordered, compressed sync (10.3):** medical/urgent sync first; gzip
  payloads; defer images until WiFi.
- **Field-level merge (10.4):** three-way field merge auto-resolves most offline
  edit clashes; only true same-field divergences escalate to NGO review.
- **Decentralized trust (10.5):** N community corroborations raise an entry's
  trust tier (PARTIAL → CORROBORATED → VERIFIED) so trust isn't gated on a
  possibly-unreachable NGO account.

**Verify:** two devices on a local network exchange a post with WiFi/internet off
(bridge via hotspot); entry appears on both; retry doesn't duplicate; corroboration
tier rises with confirmations.
**Effort:** ~3–4 days (mesh is the hard part).

---

## PHASE 7 — Advanced Differentiating Mechanisms (the uniqueness push)
**Goal:** move Nidaa from "competent offline app" to a genuinely novel coordination
primitive. Each mechanism is established in its own field but essentially unused in
conflict-zone coordination boards (verified via GitHub landscape scan, July 2026):

- **SSB-style signed append-only feeds (10.6):** each device keeps a cryptographically
  signed, append-only log of its posts/edits; replication = gossip of log tails.
  Tamper-evidence + natural conflict detection for free, no server. SSB (patchwork,
  3.5k★) proves it works offline; no humanitarian board uses it. *Deepest differentiator.*
- **CRDT field-merge (10.4 → upgrade):** replace hand-rolled three-way merge with a
  real CRDT (Automerge / Loro / Yjs, all >5k★) so concurrent offline edits merge
  deterministically with no central arbitrator.
- **Geo-indistinguishable location (differential privacy):** add calibrated noise to
  posted coordinates (Google/Meta/IBM DP libs exist) so true point stays within ~k m
  with a crypto guarantee — defeats location-targeting (Threat 12.1) while keeping
  "nearest aid" ranking. Safety mitigation becomes a math property.
- **Proof-of-personhood sybil resistance:** cap corroborations (10.5) per unique human
  via zero-knowledge proof (Anon Aadhaar / ZK), not per device — closes trust-forgery
  without a central ID authority. Critical when no government is trusted.
- **On-device LLM triage & translation (WebLLM / transformers.js):** a small model,
  downloaded once, translates posts Arabic↔English↔Ukrainian etc. and flags urgent
  medical posts offline. No cloud, no data leaving the device.

**Verify:** signed-feed replication between two offline devices converges to identical
state; CRDT merge of divergent edits is deterministic; geo-noise bounds location error;
ZK proof gates corroboration; offline model translates a posted need.
**Effort:** ~4–6 days (SSB feed + CRDT are the core).

---

## COMPETITIVE LANDSCAPE (are we first?)
Exhaustive GitHub + humanitarian-OSS scan (July 2026). Authors are NOT from Syria/Gaza;
Nidaa is a generalizable offline-first board — claim must hold across ALL regions.
- **Exists:** crisis-mesh-messenger (192★, mesh *messaging* only), HTBox/allReady
  (885★, stale 2022, preparedness), ayudapy (118★, peacetime mutual aid), Sahana Eden
  (409★, IMS), Kiwix (1.4k★, offline content), MapSwipe/fAIr (mapping).
- **Does NOT exist:** "needs board + offline" → 0 results; Arabic-RTL humanitarian
  board → 1 result (a UNHCR doc template, 1★); region-specific crisis boards
  (Ukraine/Haiti/Myanmar/Sudan/Yemen) → none.
- **Verdict:** first-in-combination, not first-in-principle. The absence is global, not
  regional — strengthens the claim. Execution, not novelty, is the real risk.

## THREAT MODEL & DO-NO-HARM (cross-cutting, design-time)
Dual-use: false "shelter" posts (entrapment), location/contact surveillance, sybil
trust-forgery, spam-DoS amplified by mesh, admin compromise, device seizure.
Mitigations by design: on-device encryption at rest; no mandatory PII; city-granularity
location; rate-limit + proof-of-work; device-weighted corroboration; audit log +
reversible verifies; mesh hop caps; "unverified = unconfirmed" UI. Do-no-harm default:
safety over convenience.

---

## STRETCH (post-Phase 7, optional)
- **WhatsApp/SMS bridge:** post needs via message ( Twilio / WhatsApp Business
  API). Reaches the ~64% who won't install an app. Handle PII carefully.
- **Multi-region deploy:** same code, `region=syr|gza` scoping, shared
  offline-first core.
- **ReliefWeb context cards:** pull v2 reports for a city as situational context.

---

## SEQUENCING SUMMARY
P0 Baseline → **P1 Real Data** → P2 Maps → **P3 Auth** → **P4 SQLite** → P5 Conflicts
→ **P6 Offline-Native (mesh + decentralized trust)** → **P7 Advanced Mechanisms
(SSB feeds + CRDT + DP location + ZK personhood + on-device LLM)** → Stretch.

Build order prioritizes the trio that moves Nidaa from "fake-data prototype" to
"real, safe, scalable tool": **P1 (real data) + P3 (auth) + P4 (SQLite)**.
P2 and P5 are depth/robustness. P6 is the offline-native endgame; P7 is what makes
the combination genuinely novel rather than a re-assembly of known parts.

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
- [ ] P6 — offline-native (mesh + decentralized trust)
- [ ] P7 — advanced mechanisms (SSB feeds + CRDT + DP + ZK + on-device LLM)
- [x] Competitive landscape documented (first-in-combination verdict)
- [x] Threat model & do-no-harm documented (cross-cutting)
