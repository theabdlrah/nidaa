# Phase 0 – Friction Log

Purpose: capture what it feels like to *use* Nidaa as a coordinator — not as
its builder. Driven during the first real walkthrough (the "would I actually
coordinate work with this?" test), not a bug hunt.

Rule: **log first, fix later.** Finish the walkthrough, then prioritize.
Each item records the observation + the scenario it showed up in + whether it
would block real adoption. Fixes are proposed, not applied, until prioritized.

Status vocabulary: Identified → Reproduced → Prioritized → Fixing → Fixed

---

## F1
Audit / transparency trail button is hidden from normal coordinators.
- Scenario: Scenario 3 (enter verifier mode, open audit log).
- Observation: the "Audit (N)" button only renders when verifier mode is ON
  (i.e. after a token is entered). A plain coordinator with no token never
  sees the button.
- Evidence: GET /api/verify returns the full audit with NO auth
  (live: 5 rows). The data is public; only the UI button is gated.
- Why it matters: the audit log is the core trust mechanism (A4). The people
  who most need to see "who verified what, when" are the coordinators
  *consuming* the info — not only verifiers. Hiding it defeats transparency.
- Would it block adoption? Partially — trust is the product's thesis.
- Status: Identified.
- Proposed fix (NOT applied): move the Audit button outside the
  `{verifyToken && ...}` block so it is always visible; keep only the
  Verify / Unverify *action* token-gated. ~3-line change.

---

## F2

## F3

## F4

---

## Tomorrow's success criterion (from plan)
By end of walkthrough day, aim for:
1. Complete Friction Log (F1–Fn, prioritized).
2. Phase B committed.
3. Short Phase 0 readiness note written.
4. Decision: instrument ready for participants, or one more refinement pass.

Goal: move from "we built something" to "we're ready to validate it with people."
