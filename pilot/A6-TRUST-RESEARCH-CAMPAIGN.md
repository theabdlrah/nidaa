# Nidaa — A6-Trust Research Campaign

Type: RESEARCH CAMPAIGN artifact (NOT a PR-1/2/3 intake; NOT an assumption closure).
Created: 2026-07-22 (afternoon, after G2 campaign).
Author: Hermes (research synthesis, under Nidaa evidence discipline).
Companion governance: pilot/ASSUMPTION-TRACKER.md (A6-trust row), docs/Nidaa-Source-of-Truth-Hierarchy.md.

==================================================================
0. GOVERNANCE BOUNDARY — READ FIRST
==================================================================
- A6-trust is currently UNTESTED (Low confidence) in ASSUMPTION-TRACKER.md. This campaign supplies
  LITERATURE + PRACTITIONER-ACCOUNT evidence on trust in coordination environments. It does NOT close
  A6-trust (closing requires a first-hand practitioner statement that organizations would trust
  designated verifiers / why they trust some sources and not others).
- No assumption is promoted. The A6-trust row remains Low/Untested unless/until a practitioner reply
  moves it. This artifact is Tier-1 (public/practitioner-account) accumulation; it reduces uncertainty,
  it does not resolve.
- Sources retrieved live 2026-07-22 via Brave Search through the local Brave CDP harness (9223, paced
  11–25s intervals, zero bot-wall) + direct curl of fetchable authoritative pages. Raw log:
  pilot/a6_trust_search_log.txt; raw HTML: pilot/a6-trust-sources/.

==================================================================
1. EXECUTIVE SUMMARY
==================================================================
A6-Trust asks: why do people trust one coordination source and ignore another? The campaign assembled
21 trust-relevant cases/excerpts across Tracks A–D (community trust; humanitarian info trust; trust
collapse; trust transfer). The convergent picture:

TRUST ANCHORS (what makes a source trusted — the A6-Trust test):
1. PROXIMITY / LOCAL LEGITIMACY — being known, local, and embedded (local leaders, community groups,
   diaspora intermediaries). Recurs across disaster-preparedness, mutual-aid, and protracted-conflict lit.
2. REPEATED ACCURACY / PERFORMANCE — trust is built by being right over time ("trust must be built
   before a disaster"; consistent reliable actions rebuild it).
3. VERIFICATION PROCESS — a visible workflow that discredits/validates info (UNHCR/Internews rumor
   tracking; "trusted stakeholders" consultation).
4. ORGANIZATIONAL REPUTATION — established orgs (ICRC, UNHCR) carry baseline trust but it is NOT
   automatic and can be lost.
5. COMMUNITY ENDORSEMENT — peer/community validation of a source.
6. PERSONAL RELATIONSHIP — direct tie to the coordinator.

TRUST BREAKERS (what destroys it):
- MISINFORMATION that outpaces official comms → users flee to unofficial sources, eroding trust in
  official channels (ScienceDirect 2024; PMC natural-disaster misinformation review).
- TRANSPARENCY/ACCOUNTABILITY FAILURE — mutual-aid groups lose trust via internal conflict, unclear
  handling of funding, aid fraud/capture concerns (CSF-Sudan).
- TOP-DOWN / EXTERNAL IMPOSITION — communities ignore externally-imposed info they didn't co-produce;
  "authorities must EARN it" (Nature 2025).
- SOURCE DISTRUST OVERRIDES ACCURACY — technically correct info is ignored when the SOURCE is
  distrusted (arXiv/PMC source-discreditation studies). This is the key disconfirming finding: truth
  content is necessary but NOT sufficient; source trust is the gate.

A6-TRUST READING: the canonical A6b premise ("organizations would trust designated verifiers") is
SUPPORTED in direction by the literature — verification process + local legitimacy are exactly the
anchors that generate trust — BUT the literature also shows trust is FRAGILE and context-bound: a
designated verifier is trusted only if locally legitimate, accurate over time, and transparent. A
verifier imposed without those properties will be ignored (the "technically correct but ignored" cases).
So A6-trust is plausible-but-conditional, which is exactly why it must be confirmed by a real practitioner,
not assumed.

DISCONFIRMING EVIDENCE (actively sought, found):
- Technically correct info ignored due to source distrust (arXiv 1911.05825; PMC source-discreditation).
- Formal authority failing to generate trust (Nature 2025 "authorities must earn it"; CSF-Sudan donor
  wariness of community groups).
These are the most valuable findings: they show A6-trust is NOT automatic and that a verifier's
institutional status alone is insufficient.

==================================================================
2. TRUST TAXONOMY (anchors)
==================================================================
| Anchor | Definition | Evidence (cases) | A6b relevance |
|--------|------------|-----------------|--------------|
| Local legitimacy / proximity | Source is known, embedded, local | Local leaders (Frontiers 2023), diaspora intermediaries (ScienceDirect 2025), community groups (Nature 2025) | Maps to A6b "loose-informal coordinator" premise — trust flows to local, not external |
| Repeated accuracy | Source proven right over time | "trust must be built before disaster" (PMC 2013), rebuild via consistent actions (mytrustbuilder 2026) | Verifier credibility requires track record |
| Verification process | Visible validation/discredit workflow | UNHCR/Internews rumor tracking; Sentinel Project IVM | This is the A6b "designated verifier" mechanism itself |
| Organizational reputation | Institutional standing | ICRC/Red Cross, UNHCR baseline trust | Semi-formal orgs carry trust A6b already assumes |
| Community endorsement | Peer/community validation | CSF-Sudan community perception of neutral delivery | Loose-tier trust signal |
| Personal relationship | Direct tie to coordinator | community groups, mutual aid | Ties to A6b owner-being-known |

==================================================================
3. TRUST FAILURE TAXONOMY
==================================================================
| Failure mode | Mechanism | Evidence | Track |
|--------------|-----------|----------|-------|
| Misinformation outpaces official | False info spreads faster → users abandon official channels | ScienceDirect 2024; PMC natural-disaster review | C |
| Source-distrust overrides truth | Correct info ignored because source untrusted | arXiv 1911.05825; PMC source-discreditation | C/D (disconfirming) |
| Accountability/transparency loss | Funding/fraud ambiguity, internal conflict | CSF-Sudan; mutual-aid conflict | A/C |
| Imposed/top-down rejection | External info not co-produced → ignored | Nature 2025 "earn it" | A/D |
| Verification breakdown | No workflow to discredit rumors → community loses trust | UNHCR "lose trust of community" if rumor system fails | B/C |
| Reputation loss | Org falls from grace | general (donor wariness of unknown groups) | D |

==================================================================
4. CASE CATALOG (21 excerpts, structured extraction)
==================================================================
Each: Context / Actor / Source / Why trusted / Maintained / Damaged / Consequence / Lesson.
Classification: LIT (literature), PAC (practitioner-account), STR (structural).

--- C1 — Diaspora as trusted intermediary (Track D) — LIT ---
Context: Humanitarian assistance, diaspora communities. Actor: Diaspora members.
Source: Diaspora networks bridging communities ↔ external actors.
Why trusted: "Direct access and trusted networks"; outside traditional humanitarian frameworks.
Maintained: Pre-existing community ties + repeated brokerage.
Damaged: If perceived as capture/external-aligned.
Consequence: Diaspora serve as trusted conduits where formal orgs cannot.
Lesson: Trusted intermediaries are often informal/embedded, not institutional.
Source: ScienceDirect "Trusted intermediaries? The role of diasporas in humanitarian assistance" (2025).
A6-Trust anchor: Local legitimacy / personal relationship.

--- C2 — Role of Trust in Disaster Risk Reduction (critical review) (Track A/D) — LIT ---
Context: DRR generally. Actor: Communities, responders.
Source: Trust relationships.
Why trusted: Built pre-disaster via engagement; "trust must be built before a disaster."
Maintained: Sustained investment of time + consistent reliable action.
Damaged: Top-down imposition; lack of co-production.
Consequence: Without pre-built trust, response less effective.
Lesson: Trust is a precondition, not an output — must be cultivated beforehand.
Source: PMC10815059 "The Role of Trust in Disaster Risk Reduction: A Critical Review" (Brave, 2026).
A6-Trust anchor: Repeated accuracy / local legitimacy.

--- C3 — Local leaders bridging complexity (Track D) — LIT ---
Context: Disaster resilience. Actor: Local leaders + SRUCs (self-reliant community units).
Source: Locally based institutions.
Why trusted: Locally based; translate complexity; co-produce knowledge with communities.
Maintained: Iterative engagement, buy-in, ownership of solutions.
Damaged: If external experts override local knowledge.
Consequence: Builds "shared understanding, buy-in and ownership."
Lesson: Local institutions that co-produce are trusted; extractive expertise is not.
Source: Frontiers 2023 "Translating the complexity of disaster resilience with local leaders."
A6-Trust anchor: Local legitimacy / community endorsement.

--- C4 — CSF-Sudan mutual-aid trust & accountability (Track A/C) — PAC/STR ---
Context: Sudan conflict, mutual aid (ERRs, Resistance Committees). Actor: Community groups.
Source: Community mutual-aid delivery.
Why trusted: "community groups perceived to have sustained neutral delivery of humanitarian assistance."
Maintained: Neutral, consistent delivery.
Damaged: Reputational risk — donors wary of RCs' political ties; "aid fraud and capture: whether
  relatively unknown groups, many unfamiliar in handling funding, can be trusted."
Consequence: Unknown groups struggle for trust/funding; capture concerns fracture legitimacy.
Lesson: Neutral delivery builds trust; opacity around funding/politics destroys it. Directly Nidaa-
  relevant (loose-informal, protracted, neutrality-as-trust-anchor).
Source: CSF-Sudan "Supporting Mutual Aid in Sudan" (Brave, 2025).
A6-Trust anchor: Community endorsement / accountability (transparency).

--- C5 — UNHCR/Internews rumor-tracking workflow (Track B) — STR ---
Context: Community-based protection / humanitarian info. Actor: Agencies + communities.
Source: Rumour tracking system.
Why trusted (when it works): Defined process to verify rumors; "decision matrices for verifying."
Maintained: Continuous workflow with defined response + efficient sharing.
Damaged: "Without clearly defined ways to respond... your project will very quickly lose the trust of
  the community." Verification breakdown = trust collapse.
Consequence: Trust is the key to addressing rumours.
Lesson: A visible verification workflow is itself a trust anchor — and its absence destroys trust.
Source: UNHCR CBP Social Media Guide Ch.6; Internews Rumour Tracking Methodology (Brave, 2022/2021).
A6-Trust anchor: Verification process.

--- C6 — Sentinel Project conflict rumour verification (Track B/D) — STR ---
Context: Conflict, rumour verification. Actor: Verification team + trusted stakeholders.
Source: IVM (integrated verification mechanism) consulting pre-identified trusted parties.
Why trusted: Consultation with "area chief, international NGO, government security official" — trusted
  stakeholders pre-mapped.
Maintained: Relationship-based verification.
Damaged: If trusted stakeholders are themselves contested.
Consequence: Enables rumour verification via known-good nodes.
Lesson: Trust transfers through pre-identified trusted stakeholders — a concrete "designated verifier"
  model that works because the verifiers are locally legitimate.
Source: The Sentinel Project (Brave, 2020).
A6-Trust anchor: Verification process + local legitimacy.

--- C7 — Misinformation erodes official trust (Track C) — LIT ---
Context: Crisis, social media. Actor: Affected populations, official channels.
Source: Official vs unofficial info.
Why trusted (official, initially): Institutional standing.
Damaged: Misinformation outpaces official comms → "users of official channels may seek information from
  unofficial sources" → "eroding trust... amplifies misinformation spread."
Maintained: Only if official comms keep pace + are seen as accurate.
Consequence: Reduced trust, exacerbated anxiety, flight to unofficial sources.
Lesson: Once misinformation outpaces, official trust collapses and is hard to recover.
Source: ScienceDirect "Social media trust: Fighting misinformation in the time of crisis" (2024);
  PMC natural-disaster misinformation narrative review (2025).
A6-Trust anchor: (failure) source-distrust / misinformation.

--- C8 — Technically correct info ignored due to source distrust (Track C/D — DISCONFIRMING) — LIT ---
Context: Misinformation correction. Actor: Information consumers.
Source: Corrected (true) info from a source.
Why trusted: content is correct.
Damaged/ignored: "consumers may choose to ignore the correct information, due to distrust in the
  [correcting] source." Also: source intentions affect what counts as true (PMC source-discreditation).
Consequence: Corrections fail when the SOURCE is distrusted, regardless of accuracy.
Lesson (KEY DISCONFIRMING): truth content is necessary but insufficient; source trust is the gate. A
  designated verifier is trusted only if the recipient trusts the verifier, not merely because it is
  correct. Directly qualifies A6-trust.
Source: arXiv 1911.05825; PMC11345350; PMC10182088 (Brave, 2019–2024).
A6-Trust anchor: (failure) source-distrust overrides truth.

--- C9 — Nature: "Disaster relief needs community trust — authorities must earn it" (Track A/D) — STR ---
Context: Disaster relief governance. Actor: Governments/institutions vs communities.
Source: Authorities' information/direction.
Why trusted: only if authorities "shift from top-down approaches to collaborations with local
  communities" and earn it.
Damaged: Top-down imposition → ignored.
Consequence: Without earned trust, official coordination info is disregarded.
Lesson: Institutional authority does NOT auto-generate trust; it must be earned via collaboration.
Source: Nature World View (Brave, June 2025).
A6-Trust anchor: (failure) imposed/top-down rejection.

--- C10 — Community engagement: trust before disaster (Track A/D) — LIT ---
Context: Disaster prep/recovery (LA vs New Orleans). Actor: Responders, community residents.
Source: Local agencies trusted among impacted populations.
Why trusted: Local agencies "trusted among the most impacted populations."
Damaged: When funding flows to orgs with financial track record but no community trust, "the
  opportunity to build capacity among the most affected agencies... can be lost."
Maintained: Pre-disaster collaboration (FEMA whole-of-community).
Consequence: Trusted local orgs deliver; distrusted external orgs don't.
Lesson: Fund the trusted-local, not just the financially-credible — trust is the delivery mechanism.
Source: PMC3780560 "Community Engagement in Disaster Preparedness and Recovery" (Brave, 2013).
A6-Trust anchor: Local legitimacy / community endorsement.

--- C11 — Local humanitarian knowledge in protracted conflict (Track B/D) — LIT ---
Context: Central African Republic, protracted conflict. Actor: Local knowledge producers.
Source: Situational/contextual + indigenous know-how + locally held data.
Why trusted: Grounded in local historical/geographical/cultural factors.
Damaged: When external "knowledge" overrides local.
Consequence: Locally-produced knowledge is more legitimate/actionable.
Lesson: Local knowledge authority > external expertise for trust.
Source: Taylor & Francis "What knowledge counts?" (Brave, CAR case).
A6-Trust anchor: Local legitimacy.

--- C12 — Rebuilding trust after conflict (Track C) — PAC ---
Context: Organizational/relational. Actor: Groups in conflict.
Source: Restored trust.
Why trusted (rebuilt): "consistent, reliable actions that show genuine commitment to improvement."
Maintained: Transparency about interests + reliability.
Damaged: Inconsistent or self-interested actions.
Consequence: Trust recoverable via demonstrated reliability.
Lesson: Trust is rebuilt by repeated reliable action — same mechanism as initial build.
Source: mytrustbuilder.com (Brave, 2026).
A6-Trust anchor: Repeated accuracy / transparency.

--- C13 — Mutual-aid chart (Dean Spade): trust-undermining tendencies (Track A/C) — PAC ---
Context: Mutual aid practice. Actor: Mutual-aid groups.
Source: Group's own practices.
Why trusted: qualities in "trusted" column (transparency, accountability, decentralization).
Damaged: "drift toward" opposite tendencies (opacity, hierarchy, coercion) "undermines potential."
Consequence: Internal governance quality determines trust.
Lesson: Trust is a function of internal practice, not just intent.
Source: deanspade.net Mutual Aid Chart (Brave, 2019).
A6-Trust anchor: Accountability / transparency.

--- C14 — DR Congo Mpox: building community trust (Track A) — PAC/STR ---
Context: DR Congo + 7, Mpox outbreak, hard-to-reach communities. Actor: CDC/IRC + communities.
Source: Response comms.
Why trusted: "Building community trust, ensuring humanitarian access" treated as key to response.
Maintained: Community engagement as foundational.
Damaged: If access/trust not built, response fails in hard-to-reach areas.
Consequence: Trust = access = response effectiveness.
Lesson: Trust is the precondition for reaching populations.
Source: ReliefWeb/WHO "Building community trust" brief (Brave, 2024) + ReliefWeb rw_trust.html.
A6-Trust anchor: Local legitimacy / community endorsement.

--- C15 — Interorganizational coordination trust (ICS limits) (Track D) — LIT ---
Context: Emergency response. Actor: First-responder orgs.
Source: ICS (Incident Command System).
Why trusted (within trained orgs): Effective for "well-trained and integrated communities of first
  responder organizations."
Damaged: "not... where social and cultural emergence is at a minimum" — ICS fails where local emergence
  dominates; trust breaks across org/culture boundaries.
Consequence: Formal systems trusted only within their trained in-group.
Lesson: Trust in formal systems is bounded by shared training/culture — external to that, it must be
  earned locally.
Source: ScienceDirect "Interorganizational coordination during emergencies" (2025).
A6-Trust anchor: Organizational reputation (bounded).

--- C16 — Social media misinformation natural-disaster narrative review (Track C) — LIT ---
Context: Natural disasters, social media. Actor: Affected populations.
Source: Official + social media.
Why trusted (official): standing.
Damaged: "misleading messages... outpaced official communications, resulting in reduced trust."
Consequence: Anxiety/stress rise; unofficial info dominates.
Lesson: Speed gap between rumor and official response is the trust-killer.
Source: PMC12313155 / JMIR Infodemiology (Brave, 2025).
A6-Trust anchor: (failure) misinformation outpaces official.

--- C17 — Community approach to disaster preparedness (Track A) — LIT ---
Context: Disaster prep. Actor: Local residents/groups.
Source: Local connection.
Why trusted: "Local residents and groups can... provide a sense of connection, decrease isolation."
Maintained: Local embeddedness.
Damaged: Isolation/abandonment felt when external-only.
Consequence: Local groups reduce abandonment, increase trust.
Lesson: Local presence itself is a trust anchor.
Source: Penn State Extension (Brave, 2025).
A6-Trust anchor: Local legitimacy / personal relationship.

--- C18 — Trustworthy disaster response tech (Track D) — STR ---
Context: Disaster response tech/policy. Actor: Authorities + constituents.
Source: Mutual trust between gov and constituents.
Why trusted: Enables "efficient deployment of emergency services."
Maintained: Reciprocal trust.
Damaged: When tech is imposed without trust.
Consequence: Trust aids deployment; distrust hinders.
Lesson: Tech coordination succeeds only atop existing trust.
Source: Berkeley CSP "Trustworthy Disaster Response" (Brave, 2023).
A6-Trust anchor: Organizational reputation / local legitimacy.

--- C19 — Information source intentions shape truth (Track D — DISCONFIRMING) — LIT ---
Context: Info-processing experiments. Actor: Recipients.
Source: Info from various sources.
Why trusted/accepted: "intentions of information sources can affect what information people think
  qualifies as true" — even technically true reports classified false based on source.
Damaged: Source intent perception overrides content.
Consequence: Same content trusted or rejected by source framing.
Lesson (DISCONFIRMING): source framing is decisive; reinforces C8.
Source: PMC10182088 (Brave).
A6-Trust anchor: (failure) source-distrust overrides truth.

--- C20 — Disaster-risk trust critical review (Track A) — LIT ---
Context: DRR. Actor: Communities.
Source: Trust relationships generally.
Why trusted: Pre-disaster engagement + performance.
Maintained: Consistent action.
Damaged: Abandonment of co-production.
Consequence: Trust precondition for DRR.
Lesson: Converges with C2 — trust is pre-condition, not output.
Source: (same family as PMC10815059; Brave).
A6-Trust anchor: Repeated accuracy / local legitimacy.

--- C21 — Aid fraud / capture concerns in mutual aid (Track A/C) — PAC ---
Context: Sudan/conflict mutual aid. Actor: Donors, community groups.
Source: Unknown groups' aid delivery.
Why trusted: Neutral delivery (cf C4).
Damaged: "whether relatively unknown groups, many unfamiliar in handling funding, can be trusted" —
  fraud/capture fears.
Consequence: Unknown groups barred from trust/funding.
Lesson: Familiarity + accountability track record gate trust.
Source: CSF-Sudan (Brave, 2025).
A6-Trust anchor: Accountability / community endorsement.

==================================================================
5. A6-TRUST ASSESSMENT
==================================================================
- A6-trust current status (tracker): UNTESTED / Low. This campaign supplies convergent literature support
  but does NOT close it.
- Direction: SUPPORTIVE but CONDITIONAL. The literature shows the mechanisms A6b relies on (verification
  process, local legitimacy) ARE genuine trust anchors — so "organizations would trust designated
  verifiers" is plausible. BUT trust is fragile and context-bound: a verifier is trusted only if locally
  legitimate + accurate-over-time + transparent. Imposed/external/unaccountable verifiers are ignored
  even when correct (C8, C9, C19).
- Confidence after campaign: Low → Low-Medium (direction supported, but practitioner confirmation still
  required; no assumption promoted pending that).
- Most Nidaa-relevant insight: the "technically correct but ignored" disconfirming cases (C8, C19) mean
  A6-trust cannot rest on verifier ACCURACY alone — it rests on verifier LEGITIMACY. For Nidaa's loose-
  informal population, this implies a designated verifier is trusted only if it is a known local actor,
  not an external system. This is consistent with Hisem's coexistence observation and Mones' owner+mandate.

==================================================================
6. CONTRADICTIONS / DISCONFIRMING
==================================================================
- DISCONFIRMING (found, not resolving A6-trust): C8, C19 — technically correct info ignored due to source
  distrust; source intentions shape truth-classification. These show A6-trust is NOT automatic and that
  institutional/verifier status alone is insufficient. They qualify A6-trust toward "conditional," they
  do not falsify it (a locally-legitimate verifier could still be trusted).
- NO resolved contradiction: no case shows a locally-legitimate, accurate, transparent designated verifier
  being rejected. The disconfirming cases are about UNtrusted sources, which is exactly what A6b would
  predict (untrusted sources are ignored).
- Tension to test with a practitioner: would a Gaza/Syria loose-informal coordinator trust a verifier that
  is (a) local + known, vs (b) external/formal? The literature predicts (a); a practitioner statement
  confirms or refutes.

==================================================================
7. PRACTITIONER QUESTIONS (top, to reduce A6-trust uncertainty)
==================================================================
(Non-leading, behavioral; per interview discipline. Aim: a first-hand A6-trust statement.)
1. "When you got coordination info during a crisis, how did you decide which source to believe — was it
   the official one, or someone you already knew locally?"
2. "Tell me about a time correct information was shared but people didn't act on it — what made them
   ignore it?"
3. "If a designated person/group was checking and sharing verified info, would your community have
   trusted them — and did they have to be local/known for that?"
4. (Disconfirming) "Have you seen a formal/external source that people refused to trust even when it was
   right? Why?"
5. (Disconfirming) "What made a coordination channel lose your community's trust completely?"

These map to a future A6-trust closure statement (why some sources trusted, others ignored — in their own
words). Until that reply, A6-trust remains untested; this campaign is the literature scaffold.

==================================================================
APPENDIX — SOURCES (live 2026-07-22, paced, zero bot-wall)
==================================================================
Brave (9223 harness): diaspora trusted intermediaries (ScienceDirect 2025); Trust in DRR critical review
(PMC10815059); local leaders bridging (Frontiers 2023); CSF-Sudan mutual-aid trust/accountability;
UNHCR/Internews rumor tracking; Sentinel Project IVM; misinformation erodes official trust (ScienceDirect
2024; PMC12313155); source-distrust overrides truth (arXiv 1911.05825; PMC11345350; PMC10182088);
Nature "authorities must earn it" (2025); community engagement trust-before-disaster (PMC3780560);
local knowledge CAR (Taylor&Francis); rebuild trust (mytrustbuilder); Dean Spade mutual-aid chart;
DRC Mpox community trust (ReliefWeb/WHO); ICS coordination trust (ScienceDirect 2025); Penn State
community approach; Berkeley trustworthy tech; aid fraud/capture (CSF-Sudan).

Direct curl (fetchable): ReliefWeb rw_trust.html; Wikipedia Misinformation, Rumor.
(RAW log: pilot/a6_trust_search_log.txt)

==================================================================
END OF A6-TRUST RESEARCH CAMPAIGN (literature/practitioner-account level)
A6-trust remains UNTESTED. Uncertainty reduced. No assumption promoted.
==================================================================
