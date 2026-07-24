# Nidaa — Pilot Design RED TEAM (Day 11 Afternoon framing)

Date: 2026-07-23
Type: EXPERIMENTAL-DESIGN CRITIQUE (governance deliverable). NOT evidence.
Role: determine whether the pilot is scientifically capable of falsifying A6b and A8.
Loaded: Day6 Constitution, Evidence Ledger, A6b Canonical v1.0 (§5–§6), Day11 Pilot Def,
        Day12 Pilot Def, Phase Roadmap, Execution Kit, PR-1, PR-2.
Stance: assume flawed unless evidence convinces otherwise. Attack only experimental design.

==================================================================
EXECUTIVE SUMMARY
==================================================================
VERDICT: NOT READY (fixable; concept is sound, instrument is weak).

The pilot is a reasonable NECESSARY probe, but as designed it CANNOT produce a
trustworthy conclusion in EITHER direction:

- A POSITIVE result (A6b/A8 "strengthen") is confounded by the founder-steward
  effect, Hawthorne/observer effect, social-desirability in self-report, and
  circular self-measurement (the steward measures his own capture rate). It would
  show "this one motivated founder kept a doc in one benign group," not "a
  designated steward CAN maintain structured info under pressure" as a mechanism.
- A NEGATIVE result ("falsify") is equally uninterpretable: the proxy is not the
  canonical population (A6b Canonical v1.0 §5 requires a first-hand coordinator
  from connectivity-stressed / protracted-crisis context), the "pressure" is
  benign, and the owner/mandate is self-assigned, not a real group mandate. A
  collapse here does NOT meet the canonical falsification criterion (§6: a real
  coordinator WITH owner/mandate who still collapsed). So a proxy fail does not
  falsify A6b.

The Day-12 def already says "necessary-but-not-sufficient for the THESIS." That
correctly blocks humanitarian claims. But it does NOT acknowledge the deeper gap:
the proxy result is ALSO weak evidence for the narrower MECHANICS claim it set out
to test. That under-acknowledged weakness is the core finding.

Net: neither outcome is scientifically credible yet. The fixes are bounded and
design-only (no product, no scope expansion). After they are applied, this becomes
READY WITH CHANGES.

==================================================================
CRITICAL ISSUES (materially threaten validity of ANY conclusion)
==================================================================
C1. FOUNDER = STEWARD, UNCONTROLLED (founder effect).
  The steward is the founder, self-assigned as owner. Canonical A6b's "owner/
  mandate" is a real coordinator with a real group mandate. Here it is one
  unusually-motivated person. The within-subject A/B (Phase1 no-steward, Phase2
  steward) controls the GROUP's fragmentation but NOT the person. The pilot cannot
  distinguish "owner/mandate + low-burden capture causes maintenance" from "this
  specific diligent person caused it." A strengthen is therefore uninterpretable
  as a mechanism. Fix: run a SECOND proxy with a NON-founder steward (see R2).

C2. CIRCULAR SELF-MEASUREMENT (A6b capture rate).
  The steward fills the Event Log: he decides what counts as a "coordination event,"
  whether he "entered it," and the capture minutes — with NO independent observer.
  "Capture rate >=80%" can be reached by under-counting missed events or
  over-counting captures. The person under test defines his own denominator. This
  is a measurement circularity, not a minor wrinkle. Fix: an independent observer
  logs events + whether the steward captured them (see R1).

C3. A8 VALUE METRIC IS PURELY PERCEIVED (no objective anchor).
  Value = sum of self-reported "minutes saved" + self-reported "matches acted on."
  Self-reports are vulnerable to social desirability (please the founder),
  misestimation, and decoupling from reality (people feel helped while the event
  log shows the same dropped requests as Phase 1). There is NO objective
  coordination-outcome measure to cross-check perceived value against. If A8
  "passes," confidence should be LOW. Fix: add an objective outcome measure
  (dropped-request rate Phase1 vs Phase2) so value is not perception-only (R4).

C4. PROXY CANNOT INSTANTIATE THE CANONICAL CONSTRUCTS.
  - "Under pressure": a community-cleanup deadline is not a coordination-surge-under-
    stress in a connectivity-stressed environment. The pressure construct is not
    equivalent, so "holds under pressure" doesn't transfer.
  - "Owner/mandate": self-assigned by founder, not granted by the group. The
    mechanism variable is faked, not tested.
  - Population: benign/non-humanitarian, explicitly excluded from OQ-1/OQ-2/G1/G2.
  Consequence: the proxy tests a cartoon of the canonical claim, not the claim.

==================================================================
MEDIUM ISSUES (improve design integrity)
==================================================================
M1. NO PRE-COMMITTED PROXY GROUP (selection bias).
  Founder may pick a friendly group (inflate consultation) or a cold one (doom it).
  Nothing prevents post-hoc group selection. Fix: pre-commit the group + a one-line
  rationale BEFORE day 1, recorded in the kit (R3).

M2. PHASE BOUNDARY GAP: ONE PROXY -> NGO IS A LEAP.
  The roadmap treats one proxy "strengthen" as licensing Phase 2. But the first
  proxy is internally weak (C1–C3). Jumping to a real NGO inherits the same
  measurement flaws (steward=outsider, self-report value). The roadmap's "second
  proxy replication" is optional; it should be REQUIRED and must use a different
  steward + independent observer. (Aligns with C1/C2.)

M3. LOGGING FATIGUE CAN INFLATE CAPTURE RATE.
  If the steward logs less diligently in week 2, the denominator shrinks and
  capture rate looks artificially high. No control. Fix: daily logging discipline
  with a "did I log today?" checkpoint; missing days flagged, not silently dropped.

M4. A8 FALSE-NEGATIVE RISK NOT GUARDED.
  If the proxy group has no real coordination bottleneck (one of the Day-11 risks:
  "information may not be the primary bottleneck"), value<cost trivially, and A8
  "falsifies" for a reason that says nothing about A8 in a real setting. The design
  lists this as a falsify condition but doesn't require confirming the group
  actually HAD a costly coordination problem first.

==================================================================
MINOR ISSUES (nice-to-have)
==================================================================
m1. Participant Survey Q3 ("acted on a match") is unverified self-report; pair with
    an artifact cross-check ("is that match in the doc?") to reduce noise.
m2. Pressure-Event "recovery within 3 days" is steward-judged; define it as
    "capture rate back within 20% of Phase-2 baseline" to remove judgment.
m3. Event Log "Min to capture" is steward-self-timed; acceptable but label as
    estimate, not measured.
m4. Snapshot the artifact weekly (good) but also snapshot at the FIRST sign of a
    lapse, not just scheduled points, to catch decay early.

==================================================================
REQUIRED CHANGES BEFORE DAY 12 (only these materially improve validity)
==================================================================
R1. Add an INDEPENDENT OBSERVER (not the steward) who logs coordination events
    across channels AND whether the steward captured each. The capture-rate
    denominator becomes observer-derived, breaking the circularity (C2). The
    observer need not be a second founder — any trusted third party watching the
    group's channels.

R2. Require a SECOND proxy with a NON-founder steward before any NGO approach
    (upgrades the roadmap's optional replication to mandatory; closes C1/M2). This
    isolates the founder effect: if both proxies hold, the mechanism (not the
    person) is implicated.

R3. Pre-commit the proxy group + a one-line "why this group has a real coordination
    problem" rationale BEFORE day 1; record in the kit (M1). Blocks selection bias
    and the A8 false-negative path (M4).

R4. Add ONE objective coordination-outcome measure: dropped-request / unresolved-gap
    rate in Phase 1 (baseline) vs Phase 2. This anchors A8 value in observed
    outcome, not just perception, and doubles as the real test of "did structure
    change anything" (C3/M4).

R5. Add an INTERPRETIVE GUARDRAIL to the pilot def + roadmap: explicitly state that
    a proxy A6b result (strengthen OR falsify) does NOT resolve or falsify the
    canonical A6b (per Canonical v1.0 §5–§6, which require a first-hand coordinator
    from the actual population). The proxy is a mechanism probe only; misreading a
    proxy falsify as "A6b falsified" would be a governance failure.

==================================================================
FAILURE MODES
==================================================================
FALSE POSITIVE (says strengthen, isn't true):
  - Founder diligence mistaken for mechanism (C1).
  - Hawthorne: participants perform for the observer.
  - Social desirability: over-report value to please founder (C3).
  - Circular measurement inflates capture rate (C2).
  - Novelty not fully decayed in 14 days.
  - Benign group has no real bottleneck, so any structure looks helpful.

FALSE NEGATIVE (says falsify, actually holds):
  - Proxy group had no coordination problem -> value<cost trivially (M4).
  - Benign pressure too weak to stress system -> can't test "under pressure."
  - Founder had a busy week -> stewardship lapsed -> collapse gap (C1 person, not
    mechanism).
  - Small N: one disengaged participant tanks consultation %.

AMBIGUOUS:
  - "Strengthen" that is actually founder-effect — can't separate person/mechanism.
  - A8 value ~1–2x cost — weak either way.
  - Proxy fail/succeed but real setting inverts — uninterpretable without R5.

==================================================================
GOVERNANCE REVIEW
==================================================================
STRENGTHS (keep):
  - Pre-registered thresholds block post-hoc wiggle on the DECISION.
  - "Necessary-but-not-sufficient" correctly blocks humanitarian claims.
  - Hard stop rule: A8 falsify -> write up negative. Good scientific discipline.
  - Surveys preserved verbatim (PR-2 compliant).
  - Concurrency principle (don't pause pipeline during proxy). Good.

WEAKNESSES (fix):
  - Governance treats a proxy "strengthen" as licensing Phase 2, but given C1–C3 a
    proxy strengthen is barely informative. Should require R2 (second proxy) first.
  - No blinding / independent observation mandated; assumes steward self-logging is
    acceptable evidence. Self-observation should be explicitly lower-tier.
  - "Stop when negative" is explicit for A8 but SILENT on the proxy-A6b-falsify
    misinterpretation risk (R5). A reader could wrongly conclude "A6b falsified."
  - No pre-commit of proxy group -> selection bias ungoverned (M1).

==================================================================
FINAL VERDICT (as originally concluded): NOT READY
==================================================================
Justification (from design + governance artifacts only):
  The experiment cannot isolate the owner/mandate mechanism from the founder
  (C1), the steward measures his own success (C2), A8 value is perception-only
  (C3), and the proxy can't instantiate the canonical "under pressure" /
  "real mandate" / population constructs (C4). Therefore a positive OR negative
  result is scientifically untrustworthy for both A6b and A8. The design's own
  honesty covers the thesis gap but not the mechanics gap.

  This is NOT a doomed concept. The five required changes (R1–R5) are design-only,
  bounded, and product-free. After R1–R5 the instrument becomes READY WITH
  CHANGES, then READY. Until then, running it would generate a result no one
  should trust — which violates the Operating Constitution's "honest about the
  evidence" mandate more than running no pilot at all.

Recommendation: apply R1–R5 to Day12 Pilot Def + Phase Roadmap + Execution Kit,
then re-run this red team on the patched design.

==================================================================
PHASE 0 ORTHOGONALITY (post-Phase-0-addition note, 2026-07-23)
==================================================================
The red-team critique targets the PHASE 1 proxy experiment's ability to falsify
A6b/A8. Phase 0 (Instrument Pilot, docs/Nidaa-Phase0-Instrument-Pilot-Spec.md) is
inserted BEFORE Phase 1 as instrument validation only and does NOT address the
C1–C4 threats — by design. Phase 0 can surface instrument breakage (unusable
templates, uncollectable metrics) that would have weakened a real Phase 1, but it
does NOT de-risk the founder-effect (C1), circular measurement (C2), perceived
value (C3), or proxy-construct gaps (C4). Those remain live Phase-1 threats and are
NOT mitigated by Phase 0. The red-team verdict (READY WITH REQUIRED DESIGN CHANGES)
and its R1–R5 dispositions are unchanged and apply to Phase 1, not Phase 0.

==================================================================
DIRECTOR RECONCILIATION (2026-07-23, post-red-team — SUPERSEDES go/no-go)
==================================================================
The director accepted the critique's substance but split the findings and adjusted
the verdict. This section is the governing decision; the NOT READY above is retained
as the unmodified critique, not as the go/no-go.

FINDING DISPOSITION (director):
  FULLY ACCEPTED:
    R4 (objective outcome measure) — "strongest recommendation."
    R5 (interpretive guardrail) — proxy result never reads as "A6b true/false."
    R3 (pre-commit group) — blocks selection bias.
  ACCEPTED WITH QUALIFICATION:
    R1 (independent observer) — recruit if feasible; if not, DON'T block — explicitly
      downgrade evidential weight to "exploratory, single-observer, founder-collected."
      Honest weaker-than-ideal is acceptable; silent weakness is not.
  PUSHBACK (downgraded from mandatory):
    R2 (mandatory second proxy) — replaced with a CONDITIONAL gate: required only if
      first proxy is ambiguous or shows strong founder effects; if first proxy is
      strong + well-documented + an NGO is willing on a limited observational trial,
      proceed while noting limitations. A Phase-2 NGO field trial is itself an
      experiment, not a validation declaration.

GO/NO-GO (director's verdict): READY WITH REQUIRED DESIGN CHANGES.
  The issues are about strengthening the EXPERIMENT, not the underlying hypothesis.
  Required before run: R4, R5, R3 (mandatory) + R1 (if feasible, else documented
  downgrade). R2 is recommended, not blocking.
  This keeps the project moving through evidence rather than freezing it until
  ideal conditions exist — consistent with the evidence-first philosophy.

APPLIED: R3/R4/R5/R1/R2(conditional) now patched into
  docs/Nidaa-Day12-Pilot-Definition.md (§E, Pre-commit, Observer, Guardrail, §I,
  Limitations) and pilot/PHASE-ROADMAP.md (conditional second-proxy gate) and
  pilot/proxy-pilot/EXECUTION-KIT.md (Template E pre-commit, observer column, R4
  outcome measure). The pilot is now READY WITH REQUIRED DESIGN CHANGES.
