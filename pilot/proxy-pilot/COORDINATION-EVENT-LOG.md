# Coordination Event Log (Template A)

RULE: log EVERY coordination event seen across ALL channels, in BOTH phases.
This is the capture-rate denominator. In Phase 1 (no steward) "Entered?" is always
N — that is the baseline fragmentation record. In Phase 2 it should be mostly Y.

If an independent observer is recruited (R1), THE OBSERVER fills the "Observed-by /
Observer: entered?" column; the steward does NOT grade his own capture rate.
If no observer, the steward fills both, and this run is flagged EXPLORATORY.

NOT STARTED — fill PROXY-GROUP-PRECOMMIT.md first. Do not enter rows until day 1.

| Date/Time | Phase (1/2) | Channel (WA/email/verbal/FB/Slack/other) | Type (request/offer/decision/gap/other) | 1-line description | Entered artifact? (Y/N) | If N: reason | Captured-at | Min to capture | Observed-by / Observer: entered? |
|-----------|-------------|------------------------------------------|-----------------------------------------|--------------------|-------------------------|--------------|-------------|----------------|------------------------------------|
|           |             |                                          |                                         |                    |                         |              |             |                |                                    |

------------------------------------------------------------------
WEEKLY ROLLUPS (compute, don't eyeball)
------------------------------------------------------------------
[Fill at end of each week. Phase 1 baseline = fragmentation reference (Reality B).]

Week __ : capture rate = __/__ = ___%   |   collapse gap (longest days w/ event, 0 captures) = ___d
Objective outcome (R4): dropped-request / unresolved-gap count = ___   |   duplicate-work count = ___
