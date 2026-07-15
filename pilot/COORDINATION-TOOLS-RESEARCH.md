# Nidaa — Existing Coordination Tools: What We Can Learn (not copy)

**Why this exists:** understand how mature tools handle *who posts*, *who verifies*,
and *how adoption happens* — so our interview questions and pilot design match reality.
Researched 2026-07-15 via live fetch of each platform's own pages. Sources linked.

## Ushahidi — crowdsourced mapping
- Model: anyone can submit reports (SMS, web, social, email); a *deployment owner*
  manages and triages them. Open-source, mobile-first, used for disaster response
  (Haiti, Nepal), elections, public-health.
- Who posts: the crowd + the deploying organization. Who verifies: the deployment
  owner / moderators (not a separate public "verifier" role by default).
- Lesson: a deployment always has an OWNER. Nidaa needs a deployment owner per site,
  not an anonymous board. Adoption = an org adopts it as its instance.
- Source: https://www.ushahidi.com/features (self-description).

## HOTOSM / Tasking Manager — crowdsourced mapping with real verification
- Model: volunteers *map* (trace buildings/roads from satellite); a separate class of
  *validators* reviews and approves the mapped work before it is accepted.
- Who posts: volunteer mappers. Who verifies: **validators — a distinct, earned role.**
- Lesson: the "validator" concept Nidaa assumes ALREADY EXISTS and is accepted in
  humanitarian mapping. Organizations are comfortable with designated verifiers.
  This supports A6 (cautiously) — but note it's mapping quality, not aid-info truth.
- Source: https://tasks.hotosm.org/ (app; about page is JS-rendered, confirms the
  mapper→validator split is core to the product).

## ReliefWeb — OCHA-curated information service
- Model: UN OCHA service; "expert editorial review with AI-powered tagging and
  automated content import" from 4,000+ sources (NGOs, governments, research).
- Who posts: vetted contributing organizations; OCHA *editors* curate. Who verifies:
  editorial review before publish.
- Lesson: at the institutional layer, posting is a STAFFED editorial function, not
  crowd-sourced. Beneficiaries don't post; orgs contribute; editors verify.
- Source: https://reliefweb.int/about (self-description).

## HDX (Humanitarian Data Exchange) — OCHA data platform
- Model: datasets contributed mainly by organizations; curated by OCHA data managers;
  "Data Responsibility" principles govern sharing. Common Operational Datasets (CODs)
  are the authoritative baselines.
- Who posts: organizations (not individuals). Who verifies: OCHA data stewardship.
- Lesson: reference facility data (what Nidaa imports) is ORG-contributed and
  steward-curated, with a capture date. This validates our provenance/sourceDate
  approach — imported data is reference, not "verified."
- Source: https://data.humdata.org/about (self-description).

## Cross-cutting takeaways (to refine interviews + pilot)
1. **Someone always owns posting.** Crowd-submit tools still have a deployment owner /
   moderator / editor. Nidaa's adoption depends on identifying that owner per partner.
2. **Verification is a recognized role** (HOTOSM validators, ReliefWeb editors). A6 is
   plausible IF the verifier maps to an existing trusted role — ask orgs to name it.
3. **Beneficiaries rarely post into systems; orgs and coordinators do.** This sharpens
   the "who posts?" risk: Nidaa's user is the coordinator/info-officer, not the
   beneficiary. Design and pitch accordingly.
4. **Reference data carries provenance, not a verification tick.** Our import-hdx
   change (source + sourceDate, no false `verified`) matches how HDX itself treats data.
5. **Adoption = an institution adopts an instance**, not individuals downloading an app.
   Pilot framing should be "we help YOUR coordination cell run an offline board," not
   "here's a tool for everyone."

## Not yet investigated (parked, evidence not needed yet)
- Ushahidi's actual deployment/case-study pages for failure modes.
- HOTOSM validator training/permission model specifics.
- How ERRs (Sudan) and White Helmets run their internal posting/verification (best
  asked in Conversation #2/#3 directly — higher value than more reading).
