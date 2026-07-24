# M1 — Offline Core (repository-grounded)

> **STATUS: FROZEN (2026-07-24).** Approved for handoff to Antigravity. Implement
> T1 + T2 only. Do not expand scope. M3 (ownership/responsibilities) is deferred
> until this milestone passes Hermes audit.

Status: **Substantially implemented.** This milestone formalizes closure + minimal
hardening, then hands off. It does NOT redesign what exists.
Basis: **A3** (offline capability matters — Moderate in tracker).
Evidence anchors: docs/Nidaa-Day6-Brief.md, pilot/ASSUMPTION-TRACKER.md (A3),
docs/Nidaa-Build-Governance.md.
Companion analysis: docs/specs/M0-Evidence-Impl-Gap.md.
Author: Hermes. Generated: 2026-07-24.

---

## 1. Current implementation (do NOT rebuild)

The offline-first contract already exists. Antigravity should extend, not rewrite:

- `lib/offlineQueue.ts` — IndexedDB queue; device is source of truth; entries saved
  locally FIRST; `pendingLocal()` / `markSynced()` track sync state by `clientId`.
- `public/sw.js` — app-shell cached; API GETs are network-first with cache fallback
  so the board still renders when offline; navigations network-first.
- `app/page.tsx` — `submit()` saves local first, then `pushPending()` if online;
  auto-sync fires on the `online` event; live online/offline + pending indicators.
- `app/api/entries/route.ts` — POST upserts by `clientId` (idempotent across
  reconnect retries); GET returns all entries + `setupRequired` honesty signal.

This satisfies the A3 requirement: core create/read works with zero connectivity and
syncs automatically on reconnect.

---

## 2. Scope of M1

Deliver: offline-capable create/read of coordination entries, local-first
persistence, automatic sync on reconnect, **with verification integrity preserved
across sync**. (A3, plus protecting A4 during sync.)

---

## 3. Tasks to close M1

**T1 — Persist last-sync timestamp.**
`app/page.tsx` keeps `lastSync` only in React state; it is lost on reload. Persist
to `localStorage` and restore on mount so operators can see when the last successful
sync occurred. Supports trust in "works offline."
Acceptance: reload after a sync still shows the prior "last synced" time.

**T2 — Sync must not clobber server-side verification.**
Today a local (unverified) edit can overwrite a server `verified=true` on push
(local-wins merge + upsert). Before pushing, compare the local entry against the
last pulled server state; only send `verified` when the client explicitly toggled it
(this session), otherwise preserve the server `verified` value.
Acceptance: a verifier marks an entry verified on the server; a client that holds an
older unverified local copy edits + repushes; the entry remains `verified=true`.

**T3 — Acceptance (whole milestone).**
- Create a post while the browser is offline → it appears in the local board with a
  "pending sync" tag.
- Restore connectivity → it auto-pushes and appears in a fresh server pull.
- A verification set by a trusted verifier survives a client edit + repush (T2).
- `lastSync` persists across a page reload (T1).

---

## 4. Explicitly OUT OF SCOPE (next milestones)

- **Ownership** (`owner` field), **defined responsibilities** (`assignedTo` /
  task assignment), **institutional linkage** (link entries to orgs) → these are
  M3 / M4, the first *unbuilt* A6b mechanisms. M1 closure does NOT include them.
- No ML, federation, analytics, payments, or broadcast features (would be drift).

---

## 5. Guardrails (evidence governance)

- No new features beyond A3 hardening (T1/T2). Every change maps to A3 (or to
  protecting A4 during sync).
- Preserve the offline-first contract: the device remains the source of truth.
- After implementation, Hermes audits against this spec + the gap report before merge.

---

## 6. Handoff

After M1 closes and passes Hermes audit, the next spec to author is
**M3 — Ownership & Defined Responsibilities**: add `owner` + `assignedTo` to
`NidaaEntry`, surface assignment in the post form + card, and reflect ownership in
the merged view. This is the first net-new build and the highest-value evidence-
aligned step (closes the largest unbuilt A6b mechanism). M2 (verification) is
already met and requires no M1-era change.
