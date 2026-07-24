# M0 — Evidence-vs-Implementation Gap Report (Nidaa)

> **STATUS: FROZEN (2026-07-24).** Final analysis. Do not re-run or extend until
> new evidence or a post-M1 implementation constraint warrants. M1 is the agreed
> next action; M3 is deferred until M1 passes Hermes audit.

Generated: 2026-07-24. Author: Hermes (research/architecture lead).
Basis (evidence/governance): docs/Nidaa-Build-Governance.md, docs/Nidaa-Day6-Brief.md,
pilot/ASSUMPTION-TRACKER.md, docs/Nidaa-A6b-Evidence-Ledger.md.
Surveyed (app source): app/ (page.tsx, layout.tsx, api/entries/route.ts,
api/verify/route.ts), lib/ (offlineQueue.ts, store.ts, types.ts, auth.ts),
components/BoardMap.tsx, public/sw.js.

Purpose: compare the running implementation against the validated research, then
determine the smallest forward milestone. This is analysis only — no app code was
modified.

---

## 1. Assumption / mechanism coverage matrix

| Item | Evidence expectation | Current implementation | Status |
|------|----------------------|------------------------|--------|
| **A2** info-organization bottleneck | App organizes info flow / verify / ownership, not raw comms | Structured entries + verification + offline queue | MET (design aligns) |
| **A3** offline matters | Core CRUD works at ZERO connectivity; auto-sync on reconnect | `lib/offlineQueue.ts` (IndexedDB, save-first, pending tracking); `public/sw.js` (app-shell + API cache fallback so board shows offline); `app/page.tsx` (local-first submit, auto-push on `online` event, pending indicators) | MET |
| **A4** verification matters | Explicit verify by trusted role; transparent audit | `lib/auth.ts` (role gate: verifier/admin only); `api/verify` (POST 401 for non-verifier, GET public audit); `lib/store.ts` `setVerified` (reversible audit log w/ prior state); UI audit panel | MET |
| **A6b — structured information flow** | Coordinated info flow | Entries + offline queue + filters/search | MET |
| **A6b — verification** | Trusted verification | As A4 above | MET |
| **A6b — defined responsibilities** | Clear, assigned responsibilities | `NidaaEntry.authorRole` exists (who *submitted*: individual/ngo/volunteer/unknown) but there is **no assigned-responsible-actor / task-assignment** field. Evidence (Omar, Mones) cites "clearly defined roles" as a success factor and "unclear task distribution" as a failure mode. | PARTIAL — GAP |
| **A6b — clear ownership** | Someone accountable per item | No explicit `owner` field; ownership is implicit = author. Evidence cites "clear ownership" as a success mechanism. | PARTIAL — GAP |
| **A6b — institutional linkage** | Community entries link to a recognized institution | `source`/`sourceDate` exist for *imported* HDX data only; **no field links a user/posted entry to an institution**. Evidence cites "direct communication channels with institutions" + "institutional linkage" as success mechanisms. | MISSING — GAP |

---

## 2. Built vs. the milestone gate sequence

| Gate | Scope | State in repo |
|------|-------|---------------|
| **M1** Offline Core (A3) | Offline CRUD + local-first + auto-sync | **BUILT** |
| **M2** Verification Model (A4, A6b-verify) | Role-gated verify + public audit | **BUILT** |
| **M3** Ownership & Defined Responsibilities (A6b) | owner + assignedTo | **NOT BUILT** (gaps in §1) |
| **M4** Institutional Linkage (A6b) | link entries to orgs | **NOT BUILT** |
| **M5** Operational Validation | real-world case study / 2nd practitioner | not reached |

---

## 3. Remaining gaps *within already-built scope* (hardening, not redesign)

These are real, small, and evidence-aligned — they should be closed to formally
complete M1/M2, but none require architectural change:

- **G1 (verification integrity across sync).** The merged view lets *local win by
  `clientId`*; `pushPending` then upserts the local copy to the server. If a trusted
  verifier set `verified=true` on the server while a client holds an older unverified
  local edit, the client's push can silently overwrite `verified` back to false.
  This risks A4 during sync. Fix: preserve server `verified` on push unless the
  client explicitly toggled it. (Small, no redesign.)
- **G2 (lastSync not persisted).** `setLastSync` is in-memory; on reload the
  "last synced" time is lost. Minor trust/UX gap. Fix: persist to `localStorage`.
- **G3 (cross-device edit conflict).** Upsert key is `clientId`; concurrent offline
  edits on two devices resolve last-write-wins with no merge. Noted as a *limitation*,
  not a closure requirement for M1.
- **G4 (push has no concurrency cap / retry backoff).** `pushPending` loops entries
  sequentially; acceptable at current scale. Minor.

---

## 4. Drift / out-of-scope check

- No unsupported features present. The app does **not** implement ML matching,
  multi-org federation, analytics, payments, or broadcast/comms. Good — no drift
  beyond the evidence-backed mechanism set.
- RTL / Arabic enforced (`app/layout.tsx` `dir="rtl" lang="ar"`; `titleAr` required
  on POST). Good.

---

## 5. Recommendation

The repository is **not** at "M1 not started." M1 (offline) and M2 (verification)
are essentially complete. The smallest *forward* milestone is therefore:

1. Formally **close M1** with the two small hardening items (G1 verification-
   preserving sync, G2 lastSync persistence) — see `docs/specs/M1-Offline-Core.md`.
2. Confirm M2 is met (no code change required).
3. Build **M3 — Ownership & Defined Responsibilities**, the first *unbuilt* A6b
   mechanism (adds `owner` + `assignedTo` to `NidaaEntry`; assignment UI). This is
   the next net-new engineering work and the highest-value evidence-aligned build.

Do **not** fold M3/M4 work into M1. Keep each milestone tightly scoped.
