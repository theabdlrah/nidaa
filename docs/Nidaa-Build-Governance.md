# Nidaa — Build Governance

> Process-only document. Stable across code changes. Milestone *specifications*
> live in separate files (see "Where specs live"); this file defines HOW decisions
> are made, not WHAT is built next.

## Purpose

Build Nidaa without deviating from validated research. Keep implementation
disciplined and aligned with the evidence base, even as the code evolves rapidly.

## Roles

- **Hermes (engineering lead, default owner of direction)** — research interpretation,
  architecture, evidence alignment, protocol/sync/security decisions, milestone
  *specification*, and *implementation of small/medium features directly* (data-model
  changes, sync logic, gated endpoints, audits). Owns the confidence framework and
  the audit gate. Self-reviews its own implementations and discloses that a self-audit
  is weaker than an independent one.
- **Antigravity (implementation specialist, opt-in)** — brought in for large/repetitive
  coding: big code transformations, boilerplate, tedious refactors, UI polishing,
  performance optimization. Executes within a spec defined by Hermes. No autonomous
  scope expansion. Used when the coding volume exceeds what Hermes should hand-write,
  not by default.
- **You (project lead)** — final decision-maker and integrator. Approve merges and
  resolve disagreements. For Nidaa, Hermes implements most milestones directly; you
  still review and approve before a feature is marked complete.

## Development Cycle

1. **Define milestone / spec** — Hermes produces a tight, evidence-cited milestone
   spec. (Lives in a separate spec doc, not here.)
2. **Implement** — Hermes implements small/medium features directly; Antigravity is
   engaged only for large/repetitive lifts, against the same frozen spec.
3. **Self-review + audit** — Hermes reviews the implementation against the spec and
   the evidence guardrails, and reports PASS or FAIL-with-deviations. When Antigravity
   implemented, Hermes audits independently (stronger); when Hermes implemented, the
   audit is self-audit (disclosed as such).
4. **Independent review** — a reviewer who did NOT write the code (you, or another
   assistant) checks the implementation against the frozen spec, focusing on sync/
   conflict logic, authorization on every mutating path, and backward compatibility.
   This gate sits BETWEEN self-audit and merge; defects found here are fixed and
   re-verified before closing. Self-audit is NOT sufficient to close a milestone.
5. **Integrator review** — you inspect and approve.
6. **Merge only after passing review** — no code lands without steps 3–5 complete.

## Evidence Guardrails

- Implementation must **not** introduce unsupported features. Anything outside the
  evidence-backed mechanism set requires new evidence first, or must be explicitly
  labeled as a hypothesis, not presented as validated.
- Research confidence is **independent** of implementation progress. Shipping code
  does not raise hypothesis confidence; only new/broader evidence does (per the
  two-dimensional rule in `pilot/ASSUMPTION-TRACKER.md` and the Day 12 governance
  section of `docs/Nidaa-Day6-Brief.md`).
- New functionality requires **corresponding evidence** or an **explicitly labeled
  hypothesis** (with the assumption it tests stated up front).

## Milestone Gates

- **M1–M4** — engineering milestones (offline core, verification model,
  ownership/responsibilities, institutional linkage). Move through these as code
  lands and passes audit.
- **M5** — operational validation: real-world feedback from a dated operational
  case study (or a second independent practitioner) before treating assumptions as
  further strengthened. This gate is evidence-driven, not code-driven.

## Where specs live

Milestone specifications (M1 Offline Core, M2 Mesh Transport, etc.) are kept in
separate files under `docs/specs/` (e.g. `docs/specs/M1-Offline-Core.md`). This
governance document does not change when a spec changes.

## Separation of Concerns

- **Governance** (`docs/Nidaa-Build-Governance.md`) — how decisions are made.
- **Evidence** (`docs/`, `pilot/`) — why decisions exist.
- **Implementation specs** (`docs/specs/`) — what gets built next.
- **Code** — the actual implementation (separate repo; not in this evidence tree).

This separation keeps the project coherent as it grows: the evidence governs the
specs, the specs govern the code, and the governance doc stays stable.
