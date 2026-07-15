# A6 Evidence Campaign — "Will coordinators actually maintain structured information?"

**Why this campaign now.** A1 is paused at its bounded conclusion (coordination is a binding
constraint when capacity+access exist but mobilization/sequencing/verification/info-flow fail;
secondary when physical/political/security dominate). The next existential risk is A6:

> **A6 = Organizations (coordinators) would maintain structured information during operations.**

If A6 fails — coordinators will not sustain structured info maintenance — then the
coordinator-led model, the state-card concept, and Nidaa itself die, *even if A1 survives*.
Per the user's risk ranking (2026-07-15), A6 is now the **highest** risk.

This file answers ONE question only: *is structured information maintenance a realistic
behavior?* No Nidaa, no features, no UI, no architecture.

---

## The behavioral questions A6 must answer

1. **Who actually enters information?** (dedicated IM dept? surge analyst? coordinator? volunteer? beneficiary?)
2. **How often?** (real-time? daily? per shift? only during surges?)
3. **Under what conditions?** (dedicated capacity? training? mandate? tools?)
4. **What information is considered worth the effort?** (operational decisions? maps? needs? incidents?)
5. **What gets abandoned first under pressure?** (manual cleaning? verification? updating the board?)

## What would have to be true for a coordinator to WILLINGLY maintain structured info during a crisis?

- A **designated data owner** exists (not "whoever is free").
- The org has **IM capacity / training / mandate** (it is someone's job).
- The **burden is low enough** to survive a surge (automation, templates, lightweight capture).
- The info is **used for decisions** (maintenance is rewarded by relevance, not imposed).
- **Verification is built in** but not so heavy it stalls updates.

If those hold, A6 is plausible. If coordinators have no designated owner, no training, and the
board is abandoned the moment bandwidth drops, A6 fails.

---

## A6 Evidence Matrix (real sources retrieved; URLs verified HTTP 200)

| Source | Data Owner | Frequency | Burden | Evidence (for/against A6) |
|--------|-----------|-----------|--------|---------------------------|
| SARC (Syrian Arab Red Crescent) IM Department — IFRC, 2019 | Dedicated IM Department across 14 field branches; ~40 trained analysts; new MEAL unit | Continuous, branch-level; analyst-trained | High without training — requires a 6-day Humanitarian Information Analysis course to build | **FOR** — coordinators DO maintain structured info, but only with a *dedicated department + capacity building*. Owner exists. |
| MapAction Automated Data Pipeline — ReliefWeb, Nov 2024 | GIS/IM teams; pipeline automates acquisition | Real-time/continuous (automated) | Burden explicitly the problem: automation exists "so GIS teams focus on analysis rather than manual data collection" | **FOR (with caveat)** — structured maintenance is real AND burdensome; orgs invest in automation to sustain it. Burden is the live risk. |
| Ushahidi → HDX integration — Centre for Humanitarian Data | Platform users; human cleaning step before HDX push | Per campaign; cleaning before publish | Cleaning is manual ("cleaning it, adding…") — human triage required | **FOR (mixed)** — community data IS structured and shared, but needs human cleaning/triage; abandoned if no one cleans. |
| WFP custom mapping workflow — ReliefWeb | Logistic Cluster + truck drivers (edge capture) | Continuous field capture | Low/intuitive: drivers mark road status on laminated maps | **FOR** — lightweight, intuitive capture at the edge works; structured info maintained because the effort is tiny. |
| HOTOSM validation workflow — established (learn.hotosm.org, 200) | Designated validators check OSM edits | Continuous, per edit | Moderate: validation is a required human step | **FOR** — orgs accept designated verifiers (relevant to A4 too); structured maintenance sustained by role, not volunteer whim. |
| ReliefWeb editorial workflow — established (reliefweb.int, 200) | OCHA editorial team | Continuous curation | Moderate: human editorial oversight/triage | **FOR** — a standing human function curates/structures info; it is someone's job. |

> Honesty note: SARC, MapAction, Ushahidi→HDX, WFP are retrieved and quoted from real ReliefWeb
> pages (HTTP 200). HOTOSM and ReliefWeb rows are established/known workflows (sites reachable,
> 200) but their deeper primary documents are `[TO RETRIEVE]` for fuller quotation. No source is
> invented. All six point the SAME way: structured info maintenance is a **real, observed
> behavior** — but it survives only when there is a designated owner, training/mandate, and
> burden kept low (often via automation).

---

## Reading the matrix (2026-07-15)

- **All six real sources support A6.** Coordinators/orgs DO maintain structured information —
  in SARC via a department, in MapAction via automation, in Ushahidi/HDX via human cleaning, in
  WFP via edge capture, in HOTOSM/ReliefWeb via designated roles.
- **The binding condition is burden + ownership.** The single recurring risk across sources is
  that structured maintenance is *burdensome* and gets dropped without a designated owner or
  automation. MapAction's pipeline exists *because* manual collection is the bottleneck.
- **A6 is therefore not "will they?" but "under what conditions?"** — exactly the five behavioral
  questions above. The evidence says: yes, when there is an owner + low burden; no, when it is
  nobody's job during a surge.
- **This bounds A6 the way A1 was bounded:** A6 holds where a data owner + low burden exist; it
  fails where maintenance is unpaid, untrained, and abandoned under pressure.

## Current status

- **A6: Early support (not yet convergence).** 6 real/established sources, all FOR, but mostly
  *organizational* IM (Red Cross, MapAction, WFP, OCHA) — not small grassroots coordinators.
- **Gap:** the grassroots/small-coordinator case (the actual Nidaa user) is NOT yet evidenced.
  SARC/WFP are large orgs with departments. The harder test is whether a *small* coordinator
  maintains structure without a department. That needs either a small-org IM case study or a
  coordinator interview (the §5 contacts from A1 still apply).
- **Contradiction hunt not yet run for A6.** Per discipline, after early support we should seek
  the strongest case where structured maintenance collapsed under pressure. Candidate: a response
  where the IM function was abandoned during peak load (e.g. a surge where the single IM person was
  overwhelmed). To be pursued before declaring A6 converged.

## What would weaken A6 (to hunt next)

- A case where the only IM person was pulled to direct response and the board went stale.
- A small coordinator saying "we never update it; WhatsApp is faster."
- Evidence that structured maintenance is abandoned first when bandwidth drops.

---

## Deliverable statement

> Based on current evidence, A6 is: **Strengthened (early).**
> Six real/established sources show coordinators and orgs DO maintain structured information —
> but only where a designated data owner, training/mandate, and low burden (often automation)
> exist. The live risk is burden + ownership, not willingness. A6 is plausible for organized
> responders and unproven for small/under-resourced coordinators. A contradiction hunt (maintenance
> collapse under surge) is still required before convergence.

No design work. A1 preserved at its bounded conclusion. Next: run the A6 contradiction hunt and
seek one small-coordinator / grassroots IM case or interview.
