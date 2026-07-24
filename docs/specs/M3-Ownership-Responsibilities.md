# M3 — Ownership & Defined Responsibilities (design specification)

> **STATUS: FROZEN (2026-07-24).** Approved for handoff to Antigravity. Implement
> only what this spec defines. Do not expand scope. M4 (institutional linkage) and
> M5 (operational validation) follow later.

Basis: **A6b** (structured information management — clear ownership, defined
responsibilities). Evidence: Omar Ghazal (community/initiative, Gaza) and Mones
(MSF Field Coordinator Support, formal cluster) — both independently cite
"clearly defined roles / clear ownership / defined responsibilities" as a success
mechanism, and "unclear task distribution" as a failure mode. Gap report
`docs/specs/M0-Evidence-Impl-Gap.md` identified ownership + defined responsibilities
as the **first genuinely unbuilt A6b mechanism**.
Companion: `docs/specs/M1-Offline-Core.md` (merge/conflict pattern reused here).
Author: Hermes. Generated: 2026-07-24.

> Evidence note (two-dimensional rule): this milestone closes an A6b *mechanism
> gap*; it does NOT change hypothesis confidence. A6b stays Medium-High until M5
> (operational validation / 2nd community practitioner).

---

## 1. What `owner` represents

The actor **accountable** for the entry's follow-up / coordination — who "owns"
seeing it through. Distinct from `authorRole` (who *submitted* it). In the field,
Omar's "clear ownership" means someone is named as accountable, not just the
original poster.

- Type: `string` label (e.g. `"Red Crescent – North Gaza"`, `"Local committee – Sector 3"`,
  or the author's own role when self-owned).
- NOT a foreign key to a user account — the app has no user system. It is a
  human-readable accountability label, consistent with the evidence (roles are
  named, not authenticated identities).

## 2. What `assignedTo` represents

The actor(s) **responsible for acting** on the entry (the "defined responsibility").
Distinct from `owner` (accountable) vs `assignedTo` (doer) — mirrors real coordination
where one org owns an item but tasks are distributed.

- Type: `string[]` (multiple assignees allowed — a need can be handled by several
  volunteers/orgs). Empty array = unassigned.

## 3. Who is allowed to assign responsibility

Privileged, like verification. Reuse the existing role gate: only a holder of a
verifier/admin token (the same gate as `/api/verify`) may set `owner` or
`assignedTo`. Rationale: Omar/Mones emphasize *clearly defined* roles — assignment
must be a trusted, auditable action, not editable by any passer-by. (No new role
system; reuse `NIDAA_VERIFIER_TOKENS` / `NIDAA_ADMIN_TOKENS`.)

## 4. Can an entry have multiple assignees?

Yes — `assignedTo: string[]`. The UI allows adding/removing labels. Display joins
them (e.g. "Assigned: A, B").

## 5. What happens if no one is assigned?

- `owner` defaults to `authorRole` at submission (explicit, not implicit) so every
  entry has a visible accountable party.
- `assignedTo` defaults to `[]` → card shows "Unassigned" (Arabic: "غير معيّن").
- No error, no blocker. Unassigned is a valid, visible state (surfaces the gap so a
  coordinator can pick it up).

## 6. How is assignment displayed in the UI?

On each entry card, below the verify tag:
- `Owner: <label>` (Arabic: "المسؤول:").
- `Assigned: <labels>` or "Unassigned".
- A coordinator (token present) sees "Set owner / Assign" controls (small inputs or
  prompt), gated exactly like the existing verify button.

## 7. Does assignment work offline?

Yes — it is offline-first like everything else:
- `owner` / `assignedTo` are fields on `NidaaEntry`, so they are saved locally on
  submit and travel with the entry through `saveLocal` → `pushPending` → upsert.
- Privileged *changes* made while offline are cached locally; the gated assignment
  call (§9) fires on reconnect (queued, like verify). The local board reflects the
  assignment immediately; server reconciliation happens on sync.

## 8. Synchronization & conflict resolution

Reuse the M1/T2 pattern — protect privileged fields from silent overwrite:
- Merge rule (client `merged` view, page.tsx ~206): `owner` and `assignedTo` follow
  the same rule as `verified` — **take the server value if it is set, unless the
  client explicitly changed it this session.** This prevents a stale local copy
  from clobbering a coordinator's assignment during sync.
- Server `upsertEntry` is keyed by `clientId` (last-write-wins) — acceptable for
  low-frequency privileged assignment. No new merge logic on the server beyond
  persisting the two fields.

## 9. API surface

Add `app/api/assign/route.ts`, mirroring `app/api/verify/route.ts`:
- `POST`: role-gated (verifier/admin token, 401 otherwise). Body:
  `{ id: clientId, owner?: string, assignedTo?: string[] }`.
  Sets the provided fields on the entry (partial update; only given fields change).
- Writes an `AssignmentAudit` (new type, mirrors `VerificationAudit`):
  `{ entryId, clientId, actorRole, field: "owner"|"assignedTo", prior, next, at }`.
- `GET`: public read of the assignment audit (transparency, like verify audit).
- Persist via a `setAssignment(id, owner, assignedTo, actorRole)` in `lib/store.ts`
  (mirror `setVerified`), writing the entry + appending the audit under a write lock.

No change to `app/api/entries` beyond persisting the two new fields on upsert.

## 10. Data-model change (`lib/types.ts`)

```ts
export interface NidaaEntry {
  // ...existing fields...
  authorRole: "individual" | "ngo" | "volunteer" | "unknown";
  owner: string;          // M3: accountable actor (default = authorRole label)
  assignedTo: string[];   // M3: responsible actors (default [])
  // ...rest unchanged...
}

export interface AssignmentAudit {
  entryId: string;
  clientId: string;
  actorRole: string;
  field: "owner" | "assignedTo";
  prior: string | string[] | null;
  next: string | string[] | null;
  at: string; // ISO
}
```

Backward compatibility: existing entries have no `owner`/`assignedTo`. On read,
default `owner` to `authorRole` and `assignedTo` to `[]` if absent (no migration
script needed — handled in `listEntries`/merge).

## 11. Acceptance criteria

- [ ] `owner` + `assignedTo` present on `NidaaEntry`; default `owner=authorRole`,
      `assignedTo=[]` for old entries.
- [ ] Submit works offline; new entry carries `owner` (from author) + `assignedTo=[]`.
- [ ] Coordinator (token) can set `owner` and add/remove `assignedTo` via UI.
- [ ] Assignment audit logged on every change; `GET /api/assign` returns it publicly.
- [ ] Non-coordinator (no token) cannot set assignment (401 on POST).
- [ ] Offline assignment reflects locally; survives reconnect sync without being
      clobbered by a stale local copy (merge rule §8).
- [ ] `npm run lint` + `npm run build` pass.

## 12. Explicitly OUT OF SCOPE (next milestones)

- **M4 — Institutional Linkage**: linking an entry to a *recognized organisation*
  (a structured org registry). M3 uses free-text owner/assignee labels; M4 adds
  org linkage. Do not build org registry here.
- **M5 — Operational Validation**: real-world case study / 2nd practitioner.
- No ML, federation, analytics, or comms features (would be drift).

## 13. Guardrails (evidence governance)

- Every change maps to A6b (ownership / defined responsibilities). No new features
  beyond those two fields + their privileged management + audit.
- Assignment is privileged + auditable, mirroring verification (consistency with
  existing architecture).
- After implementation, Hermes audits against this spec before merge.

## 14. Evidence mapping (why this, not something else)

- Omar (community): "clear ownership, defined responsibilities" = success;
  "unclear task distribution" = failure. → M3 gives every entry a named owner and
  explicit assignees.
- Mones (MSF formal): structured info flow + defined responsibilities central to
  effective coordination. → M3 operationalises "defined responsibilities" as a
  first-class, assignable field.
- Both are *mechanism* convergence (they independently identify the same need), not
  agreement with Nidaa's specific UI — so M3 builds the mechanism, not a claim.
