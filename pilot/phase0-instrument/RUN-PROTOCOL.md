# Phase 0 — Run Protocol (Instrument Validation, NOT hypothesis validation)

Status: protocol defined, NOT YET RUN.
Governs: pilot/phase0-instrument/ (rehearsal). Must be read before any Phase 0 session.
Supersedes "proving Nidaa works." The ONLY job in Phase 0 is to prove the EXPERIMENT
works — i.e., the instrument is understandable, usable, and ready for Phase 1.

==================================================================
THE QUARANTINE (read aloud at briefing)
==================================================================
Per the standing Phase 0 rule (PHASE-ROADMAP.md + docs/Nidaa-Phase0-Instrument-Pilot-Spec.md):
  Evidence produced during Phase 0 may modify the experimental instrument only.
  It MUST NOT strengthen, weaken, validate, or falsify A6b, A8, OQ-1, OQ-2, G1, G2,
  or the evidence ledger.
Phase 0 is an operational rehearsal. It answers "is our instrument runnable?" — NOT
"does the coordination model work?" Those questions belong to Phase 1+.

==================================================================
BEFORE THE SESSION
==================================================================
- Recruit 3–6 people (see NOTE on size at bottom of file).
- Tell them explicitly: this is an EXPERIMENT REHEARSAL, not a product demo.
- Give them ONE realistic coordination scenario in advance (stand-in, e.g., mock
  "plan a community event" or "respond to a localized outage"). The scenario should
  generate: multiple incoming requests, several potential helpers, changing
  situations, tasks to assign, and status updates.
- Fill proxy-pilot/PROXY-GROUP-PRECOMMIT.md with Group type = "Phase 0 rehearsal
  team", explicitly marked synthetic. R3 selection-bias guard applies: pick a
  workable scenario, not one rigged to look smooth.

==================================================================
DURING THE SESSION
==================================================================
1. BRIEF (5–10 min)
   - Explain the W1–W5 board (Need / Offer / Situation / Task / Status).
   - Explain the steward role (one person maintains the board; capture discipline).
   - State clearly: "You are evaluating the INSTRUMENT, not the idea."

2. SCENARIO
   - Hand them the coordination problem. Do NOT tell them how to solve it beyond the
     basic board rules. Let them discover the workflow.

3. OBSERVE (do not teach)
   Watch for and log (instrument-only):
   - Where do they hesitate?
   - Which fields confuse them?
   - Which information do they keep asking for?
   - Do they ignore certain fields?
   - Do they invent information the board can't capture? (=> gap in instrument)
   - How long does each entry take? (=> steward SLA practicality)
   - Does the steward naturally keep the board updated? (=> workflow adherence)
   Do NOT intervene unless they are completely stuck. Observations go in the
   Instrument Validation Log (Template F) + a facilitator notes file. No hypothesis
   language allowed in those notes.

4. DEBRIEF (ask, do not lead)
   - What was confusing?
   - What information was missing?
   - Which fields were unnecessary?
   - What would you change?
   - What felt natural?
   - What felt like unnecessary work?

==================================================================
AFTER THE SESSION — TWO OUTPUTS
==================================================================
A) INSTRUMENT ISSUES (-> become changes to the MEP)
   Examples: "Field X is unclear"; "Need field Y"; "W3 wording confused everyone";
   "Owner field should be mandatory"; "Priority should use fixed levels".
   Logged in Template F (pilot/proxy-pilot/EXECUTION-KIT.md). Each issue -> either a
   fix to MEP v0+ or a recorded "no evidence yet, stays out" decision.

B) METHODOLOGY CHECK (-> improve the experiment itself)
   Examples: "Instructions too long"; "Scenario unrealistic"; "Session timing poor";
   "Need better facilitator guidance".
   Logged separately from instrument issues. These refine Phase 0 and inform Phase 1
   facilitation — they are NOT MEP changes and NOT hypothesis data.

==================================================================
WHAT YOU MUST NOT CONCLUDE (hard禁令)
==================================================================
Do NOT say, write, or imply:
   - "A6b is validated."
   - "The mechanism works."
   - "Users found it useful."
   - "People liked Nidaa."
Phase 0 is not designed to answer those. It only certifies instrument readiness.

==================================================================
SUCCESS — ONLY THIS MAY BE SAID
==================================================================
> "The instrument is understandable, usable, and ready for Phase 1. The issues
>  discovered have been incorporated into the instrument."
Then: freeze the revised instrument (version-bump in MEP README) and move to the
pre-committed Phase 1 proxy group, where real A6b evidence begins. That separation
is what preserves the integrity of the evidence-first methodology.

==================================================================
NOTE ON PARTICIPANT SIZE
==================================================================
This protocol specifies 3–6 (per director run guidance). The spec doc
- The spec doc (docs/Nidaa-Phase0-Instrument-Pilot-Spec.md) states N=6–8. Superseded: N=3–6
  is canonical (director, this session). RUN-PROTOCOL.md is authoritative on size.
