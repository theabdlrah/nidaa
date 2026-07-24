# Nidaa — Phase 0 Instrument Pilot (Instrument Validation Specification)

Date: 2026-07-23
Type: PILOT METHODOLOGY SPEC (design addition). NOT evidence; NOT hypothesis validation.
Author: Hermes (pilot designer), per director directive (insert Phase 0 before Phase 1).
Source linkage: pilot/PHASE-ROADMAP.md (Phase 0 added) + docs/Nidaa-Day12-Pilot-Definition.md
  (Phase 1 design, UNCHANGED) + pilot/proxy-pilot/EXECUTION-KIT.md (templates A–E reused;
  F added) + docs/Nidaa-Day12-Pilot-RedTeam.md (critique of Phase 1; Phase 0 orthogonal).
Standing governance: Day6 Constitution, PR-1/PR-2, Source-of-Truth hierarchy, A6b Canonical.

==================================================================
0. QUARANTINE (the defining property of Phase 0)
==================================================================
Phase 0 is INSTRUMENT VALIDATION ONLY. It is an operational rehearsal.

It MUST NOT:
- strengthen, weaken, validate, or falsify A6b (any wording) or A8.
- touch OQ-1, OQ-2, G1, G2.
- change any Evidence Ledger state or assumption status.
- produce any humanitarian inference.
- validate or falsify the MECHANISM.

The ONLY legitimate outcome of Phase 0 is improving the quality and runnability of
the experimental instrument (instructions, templates, steward workload, event-log
procedure, pressure protocol, surveys, metrics). Findings may modify the instrument
only. Phase 0 evidence is quarantined from the hypothesis layer by a standing rule
(recorded in PHASE-ROADMAP.md).

Consequence for red-team threats: the founder-steward confound (red-team C1),
circular self-measurement (C2), and perceived-value issues (C3) are IRRELEVANT in
Phase 0 — we are not measuring the mechanism, only whether the tooling functions.
Phase 0 CAN, however, surface instrument breakage that would have weakened a real
Phase 1 (e.g., unusable templates, uncollectable metrics), which is exactly why it
runs first.

==================================================================
1. OBJECTIVE
==================================================================
Determine whether the experimental instrument is operationally runnable and usable
BEFORE it is applied to a real proxy group (Phase 1).
Answer ONLY operational questions:
- Are instructions understandable?
- Is steward workload practical (<=2 min/row SLA)?
- Are templates usable?
- Can participants consistently follow the workflow?
- Are event logs practical?
- Does the pressure-event protocol function?
- Are surveys understandable?
- Are metrics collectable from the logs?
- Does the operational process break anywhere?

==================================================================
2. PARTICIPANTS
==================================================================
- One dedicated team created specifically for this experiment (synthetic/rehearsal).
- Target N = 3–6 (rehearsal-sized; confirmed canonical per director, this session).
- Participants KNOWINGLY join an experimental coordination exercise (informed it is a
  rehearsal, not real coordination, not humanitarian, not an NGO).
- No humanitarian framing. No NGO involvement.
- Founder acts as steward (same as Phase 1). Acceptable in Phase 0 because we are NOT
  testing the mechanism; the founder-effect confound does not apply here.
- Independent observer (R1) RECOMMENDED in Phase 0 too — to validate the observer
  column / grading procedure itself as part of instrument testing.

==================================================================
3. WORKFLOW
==================================================================
Run the SAME 5 actions (W1–W5) and SAME templates (A Event Log, B Steward Time Log,
C Check-ins, D Pressure Record) as Phase 1, on a STAND-IN coordination scenario
(e.g., a mock "plan a community event" exercise) so the team generates realistic-but-
invented coordination events that exercise the instrument end-to-end.

- Pre-commit (Template E) is still filled, but Group type = "Phase 0 rehearsal team"
  and explicitly marked synthetic. The R3 selection-bias guard still applies (pick a
  workable rehearsal scenario, not one rigged to look smooth).
- Within-subject A/B compressed: ~2-day baseline (no steward) + ~5-day steward-active,
  with a STAGED pressure event on the final day to test the pressure protocol.
- Templates A–E are used exactly as in Phase 1; the Instrument Validation Log (F)
  records every usability/breakage issue found.

==================================================================
4. DURATION
==================================================================
7 days (compressed rehearsal). Rationale: instrument validation needs only enough
cycles to surface breakage; the 21-day Phase-1 window is for novelty-decay and
mechanism detection, which are OUT OF SCOPE for Phase 0. If instrument issues are
found and fixed, a re-run of Phase 0 (also ~7 days) may be required before Phase 1.

==================================================================
5. METRICS (instrument-only)
==================================================================
- Instruction comprehension: % participants who correctly describe the workflow after
  reading the brief (open question / short check).
- Template usability: time-to-complete first Event Log row; count of fields confusing/
  left blank.
- Steward workload practicality: steward self-reported burden vs the <=2 min/row SLA;
  is the SLA achievable in rehearsal?
- Workflow adherence: % of synthetic events the team followed the capture protocol on.
- Event-log practicality: were rows consistently fillable? gaps? ambiguities?
- Pressure-event protocol function: did the staged surge trigger and get logged?
- Survey understandability: % participants answering Q1–Q5 without clarification.
- Metric collectability: were all Phase-1 metrics actually producible from the logs
  (e.g., could capture rate be computed from the rehearsal Event Log)?
- Process breakage: any step where the team got stuck / the instrument failed.

==================================================================
6. SUCCESS CRITERIA (instrument)
==================================================================
Phase 0 SUCCEEDS (instrument validated) when:
- All templates completed by >=80% of participants without founder rework.
- Steward SLA (<=2 min/row) achievable in rehearsal.
- Pressure-event protocol executed and logged.
- All Phase-1 metrics confirmed collectable from the logs.
- Zero process-breakage points, OR all breakages identified with fixes specified.
Outcome: "Instrument is runnable; proceed to Phase 1." This is NOT a hypothesis result.

==================================================================
7. FAILURE CRITERIA (instrument)
==================================================================
Phase 0 FAILS (instrument requires revision) when:
- Templates unusable (participants cannot complete without major rework).
- Metrics not collectable from the logs as designed.
- Pressure protocol cannot be executed/logged.
- Steward workload impractical beyond the SLA with no viable fix.
Outcome: "Instrument requires revision before Phase 1." This is an INSTRUMENT fail,
explicitly NOT an A6b/A8 fail. Revise templates, re-run Phase 0.

==================================================================
8. DELIVERABLES
==================================================================
- Phase 0 Instrument Validation Log (Execution Kit Template F): every issue found,
  severity, fix applied/required.
- Revised templates (if fixes needed) — version-bumped in the Execution Kit.
- Go/No-Go for Phase 1: "instrument validated, proceed" | "instrument revised, re-run
  Phase 0" | "instrument blocked, redesign required."
- Explicit closing statement: "Phase 0 produced no A6b/A8/OQ/G evidence; all findings
  are instrument-only and quarantined from the hypothesis layer."

==================================================================
9. GOVERNANCE LINK
==================================================================
Standing rule (recorded in PHASE-ROADMAP.md):
  "Evidence produced during Phase 0 may modify the experimental instrument only.
   Phase 0 evidence MUST NOT strengthen, weaken, validate, or falsify any Nidaa
   assumption, hypothesis, canonical claim, OQ, or evidence ledger state. Its only
   legitimate outcome is improving the quality and runnability of the experiment."
Phase 0 logs are raw evidence per PR-1/PR-2 (the Instrument Validation Log is raw;
summaries may not replace it).
