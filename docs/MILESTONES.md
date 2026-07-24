# Nidaa — Milestone Tracker (live engineering status)

Single source of truth for implementation progress. Distinct from:
- `docs/Nidaa-Build-Governance.md` — process/governance (stable, frozen).
- `docs/specs/M0-*.md` / `M1-*.md` — analysis + per-milestone specs.
- `pilot/EVIDENCE-JOURNAL.md` — evidence events.

Update this file as milestones move. Keep it honest: a milestone is ✅ only when
its spec's acceptance criteria are verified, not when code is merely written.

| Milestone                          | Status                 | Spec / Notes |
| ---------------------------------- | ---------------------- | ------------ |
| M0 – Evidence-vs-Impl Gap Analysis | ✅ Complete             | `docs/specs/M0-Evidence-Impl-Gap.md` (FROZEN) |
| M1 – Offline Core Hardening        | ⏳ In Progress          | `docs/specs/M1-Offline-Core.md` (FROZEN). T1 persist lastSync, T2 verification survives sync. Handed to implementation agent; acceptance pending integrator test + Hermes audit. |
| M2 – Verification Model            | ✅ Already Implemented  | Role-gated verify (`lib/auth.ts`, `app/api/verify`) + verifier UI (`app/page.tsx`). Met; no M1-era change required. |
| M3 – Ownership & Responsibilities  | ⏸ Waiting on M1         | First unbuilt A6b mechanism (gap analysis). Author spec only after M1 passes audit. Adds `owner` + `assignedTo`. |
| M4 – Institutional Linkage         | ⏸ Planned              | Final A6b mechanism; links entries to orgs. After M3. |
| M5 – Operational Validation        | ⏸ Planned (gate)        | Real-world case study / 2nd practitioner before assumptions further strengthened. |

## Status legend
- ✅ Complete — acceptance criteria verified.
- ⏳ In Progress — implementation underway or in test/audit.
- ⏸ Waiting / Planned — not started; blocked on a predecessor.

## Repo visibility
Private until at least M3 lands (per integrator decision). Do not make public
before then.
