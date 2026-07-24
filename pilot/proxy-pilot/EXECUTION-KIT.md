# Nidaa — Proxy Pilot Execution Kit

Date: 2026-07-23
Type: RUNNABLE TEMPLATES for docs/Nidaa-Day12-Pilot-Definition.md (Phase 1)
Use: copy the blocks below into live logs as the pilot runs. Raw entries only;
     no summary-as-evidence (PR-1 ENTER / PR-2 PRESERVE).
Source-of-truth order: raw transcript/log > intake > field log > ledger > brief.

Files to create alongside this kit (one home each):
  proxy-pilot/COORDINATION-EVENT-LOG.md   <- paste Template A
  proxy-pilot/STEWARD-TIME-LOG.md         <- paste Template B
  proxy-pilot/PARTICIPANT-CHECKINS.md     <- paste Template C (mid + end surveys)
  proxy-pilot/ARTIFACT-SNAPSHOTS/         <- save dated copies of the shared doc
  proxy-pilot/PRESSURE-EVENT-RECORD.md    <- paste Template D
  proxy-pilot/PROXY-GROUP-PRECOMMIT.md    <- paste Template E (R3, lock before day 1)

------------------------------------------------------------------
TEMPLATE E — PROXY GROUP PRE-COMMIT  (R3; fill BEFORE day 1, do not change after)
------------------------------------------------------------------
Group name: __________________________________________________________
Group type (cleanup crew / club / meetup / OSS / other): ______________
Why this group (one line — must state a REAL, observable coordination
problem, not "convenient"): __________________________________________
Channels where coordination happens (list >=3): ______________________
Foreseeable pressure/stress event during the window: _________________
Independent observer recruited? (Y/N): ____  If N, this run is
  EXPLORATORY, single-observer, founder-collected (state this in outputs).
Locked date: __________  (changing the group after this date invalidates the result.)

------------------------------------------------------------------
TEMPLATE A — COORDINATION-EVENT LOG  (fill for BOTH phases)
------------------------------------------------------------------
Log EVERY coordination event seen across ALL channels. This is the capture-rate
denominator. In Phase 1 (no steward) "Entered?" is always N — that's the baseline
fragmentation record. In Phase 2 it should be mostly Y.

If an independent observer is recruited (R1), THE OBSERVER fills the "Observed by"
+ "Observer: entered?" columns; the steward does NOT grade his own capture rate.

| Date/Time | Channel (WA/email/verbal/FB/Slack/other) | Type (request/offer/decision/gap/other) | 1-line description | Entered artifact? (Y/N) | If N: reason | Captured-at | Min to capture | Observed-by / Observer: entered? |
|-----------|------------------------------------------|-----------------------------------------|--------------------|-------------------------|--------------|-------------|----------------|------------------------------------|
|           |                                          |                                         |                    |                         |              |             |                |                                    |

Weekly rollup (compute, don't eyeball):
  Phase capture rate = (Y rows) / (total rows) for that week.
  Collapse gap = longest run of days with >=1 expected event but 0 captures.
  OBJECTIVE OUTCOME (R4): dropped-request / unresolved-gap count and duplicate-work
    count, Phase 1 vs Phase 2. This is the higher-tier A8 signal; perceived value
    (surveys) is secondary to it.

------------------------------------------------------------------
TEMPLATE B — STEWARD TIME LOG  (Phase 2 only; A8 cost numerator)
------------------------------------------------------------------
Founder logs ALL minutes daily. If weekly total exceeds the pre-set cap (suggest
5 hrs/week), that itself becomes A8 cost evidence.

| Date | Capture min | Digest min | Match/nudge min | Fix/repair min | Total min | Notes |
|------|-------------|------------|-----------------|----------------|-----------|-------|
|      |             |            |                 |                |           |       |

Weekly rollup:
  Steward cost (week) = sum of Total min.
  Compare to participant value (Template C) for the value:cost ratio.

------------------------------------------------------------------
TEMPLATE C — PARTICIPANT CHECK-INS  (2 surveys; preserve verbatim)
------------------------------------------------------------------
Send mid-Phase-2 (~day 14) and end (~day 21). Save each reply verbatim in
raw-transcripts/ or inline here; do NOT paraphrase as the record.

INTRO LINE (same both times):
  "This is a coordination observation, not a study. Honest answers make it
   useful. ~2 minutes."

Q1. Did you consult the shared coordination doc in the last 7 days?
    [ ] Yes, about ___ times   [ ] No
Q2. Did it save you time or effort? If yes, estimate how many minutes total.
    [ ] Yes, ~___ min   [ ] No   [ ] Not sure
Q3. Did you act on a need or match you saw in the doc? (e.g. took a task, reached out)
    [ ] Yes — what: ________________________   [ ] No
Q4. Did anything still fall through the cracks that the doc did NOT catch?
    Open text: ________________________________________________________
Q5. What, if anything, changed about how the group coordinated?
    Open text: ________________________________________________________

Compute (end survey):
  Participant value = (sum of Q2 minutes across respondents) + (count of Q3 "Yes").
  Value:cost ratio = Participant value (min) / Steward cost (Template B, same week).
  OBJECTIVE OUTCOME (R4, higher-tier): dropped-request rate Phase 1 vs Phase 2 from
    the Event Log — this is the real "did value exceed cost" evidence; perceived
    value is supporting, not primary.
  Novelty decay = compare mid (week-1) vs end (week-2) on Q1% and capture rate.
    Drop >30% = decay signal (feeds A6b weaken / A8 weaken).

------------------------------------------------------------------
TEMPLATE D — PRESSURE-EVENT RECORD  (days 14–16)
------------------------------------------------------------------
A real or staged surge during Phase 2. Tests whether W1–W3 hold under load.

- Event description: __________________________________________________
- Date window: ____________________
- Volume vs baseline (e.g. "3x normal requests"): ____________________
- Did capture continue? (Y/N)  Capture rate that window: ___%
- Did digest/match cadence hold? (Y/N)
- Steward minute spend that window: ___ min (vs typical ___ min)
- Any collapse / dropped entries? Describe: __________________________
- Recovery within 3 days? (Y/N)

Decision input: a >20% capture drop at pressure that does NOT recover within 3
days = A6b FALSIFY condition (per Day 12 def §F).

------------------------------------------------------------------
TEMPLATE F — PHASE 0 INSTRUMENT VALIDATION LOG  (rehearsal team only)
------------------------------------------------------------------
Used ONLY in Phase 0 (instrument validation). Records instrument breakage, NOT
hypothesis data. Per the Phase 0 quarantine rule, findings here may modify the
instrument only — they NEVER touch A6b/A8/OQ/G or the ledger.

| ID | Instrument area (instructions/template/steward-SLA/pressure/survey/metric/other) | Issue observed | Severity (block/major/minor) | Fix applied / required | Re-run needed? |
|----|----------------------------------------------------------------------------------|----------------|--------------------------------|------------------------|---------------|
|    |                                                                                  |                |                                |                        |               |

Closeout (required): state explicitly —
  "Phase 0 produced no A6b/A8/OQ/G evidence; all findings are instrument-only."
  Go/No-Go: [ ] instrument validated, proceed to P1   [ ] revised, re-run P0   [ ] blocked, redesign

------------------------------------------------------------------
RUN RULES (constitution-aligned)
------------------------------------------------------------------
- Log in real time or same day. A reply/event not in these files = not ingested.
- Snapshot the shared artifact at end of each Phase-2 week + right after the
  pressure event; save versioned copies in ARTIFACT-SNAPSHOTS/.
- No assumption may cite a summary when these raw logs exist.
- At pilot end, compute §F/H thresholds from these logs and record the verdict
  in docs/Nidaa-Day12-Pilot-Definition.md + the ledger. A falsify = write the
  negative result up; that is a successful pilot.
