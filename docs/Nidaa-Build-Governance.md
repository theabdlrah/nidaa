# Nidaa — Build Governance

> Process-only document. Stable across code changes. Milestone *specifications*
> live in separate files (see "Where specs live"); this file defines HOW decisions
> are made, not WHAT is built next.

## Purpose

Build Nidaa without deviating from validated research. Keep implementation
disciplined and aligned with the evidence base, even as the code evolves rapidly.

## Roles

- **Hermes** — architecture, evidence alignment, protocol/BT-mesh decisions,
  code review. Owns the confidence framework; audits every implementation against
  the evidence.
- **Antigravity** — implementation, test generation, refactoring, bug fixes.
  Executes within a spec defined by Hermes. No autonomous scope expansion.
- **You (project lead)** — final decision-maker and integrator. Hands specs to
  Antigravity, reviews its output, approves merges, and resolves disagreements
  between the two.

## Development Cycle

1. **Define milestone / spec** — Hermes produces a tight, evidence-cited milestone
   spec. (Lives in a separate spec doc, not here.)
2. **Implement** — Antigravity builds to the spec.
3. **Review** — you inspect the code.
4. **Audit against evidence** — Hermes audits for correctness, architecture, and
   alignment with the evidence/guardrails.
5. **Merge only after passing review** — no code lands without steps 3–4 complete.

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
