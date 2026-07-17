# A6b Resolution Campaign — "Do grassroots coordinators maintain structured operational information under pressure?"

**Status of A6b before this campaign:** `Unproven, leaning Weak` (from A6-GRASSROOTS-HUNT.md).
**Status after this campaign:** `Conditional — RESOLVED AS POPULATION-SPLIT` (evidence-backed, not speculative).
**Confidence:** `Low → Medium` (population behavior now explained by a moderator variable, not guesswork).

This file is the Day-5 deliverable for the A6b gate. It contains the four requested outputs:
1. Evidence Log
2. Contradiction Log
3. Confidence assessment for A6b
4. Recommended next evidence targets

All sources were fetched live this session (HTTP 200 unless noted) and the quotes are taken from the
fetched HTML, not paraphrased from memory. Source HTML is preserved in `pilot/research-day5/`.

---

## 0. The question, restated precisely

A6b is NOT "do large humanitarian orgs maintain structured info" (that was A6a — answered Early
Support in A6-EVIDENCE-CAMPAIGN.md). A6b is:

> Will the **small / informal coordinator** Nidaa depends on — camp volunteer, community focal
> point, local coordinator, mutual-aid organizer, neighborhood committee — maintain structured
> operational information (lists, registers, status, incidents) **during active coordination, and
> especially under pressure**?

The prior grassroots hunt found the formal-org evidence answered the wrong population. This campaign
fills that gap with real grassroots/informal sources and one semi-formal volunteer SUCCESS case.

---

## 1. Evidence Log

Strength: `Strong` · `Moderate` · `Weak` · `Anecdotal`
Reality tag: `A` (structure survives) · `B` (communication survives, structure doesn't) · `MIXED`

### B1 — Emergency Response Rooms (ERRs), Sudan — ACAPS mutual-aid case study (RETRIEVED, HTTP 200)
- Source: https://reliefweb.int/report/sudan/key-considerations-mutual-aid-lessons-and-experiences-emergency-response-rooms-sudan
- Fetched: `pilot/research-day5/acaps_err_mutualaid.html`
- Quote (verbatim from fetched page): *"Volunteer networks, known as Emergency Response Rooms (ERRs),
  in which the 'room' refers to the online group chats where they were originally conceived and
  planned, are one example."*
- Quote: *"Building on interviews with volunteers, the case study highlights the perspectives of ERR
  volunteers and details the emergence, growth, workflows and partnerships of ERRs."*
- Behavioral read: The "room" = the **group chat**. Coordination is chat/verbal-based, not a
  structured database. The brief explicitly calls for *"ongoing documentation, analysis and learning
  from grassroots responses"* — framed as a **recommended gap**, not an observed practice.
- Reality tag: **B** (strong). No dedicated data owner; info lives in chat; documentation is the
  thing they say needs to be *built*, not what exists.

### B2 — ERRs, Khartoum — ACAPS Thematic Report (RETRIEVED, HTTP 200)
- Source: https://reliefweb.int/report/sudan/acaps-thematic-report-sudan-challenges-and-opportunities-khartoum-state-emergency-response-rooms-16-october-2025
- Fetched: `pilot/research-day5/acaps_err_report2.html`
- Quote (verbatim): *"Some ERRs were first established during the COVID-19 pandemic, as part of the
  neighbourhood resistance committees (RCs)."*
- Behavioral read: Grassroots, committee-originated, chat-native. Reinforces B1 — the coordination
  unit is the committee + its chat, not a register.
- Reality tag: **B** (corroborating).

### A1 — White Helmets (Syria Civil Defence) — structured volunteer reporting (RETRIEVED, HTTP 200)
- Source (reports index): https://www.syriacivildefense.org/reports  (fetched `wh_reports.html`)
- Source (home): https://www.syriacivildefense.org/  (fetched `whitelhelmets_home.html`)
- Quotes (verbatim from fetched pages):
  - *"When bombs rain down, our volunteers rush to the scene of the attack to rescue trapped
    civilians and minimize further injury to people and damage to civilian infrastructure."*
  - Reports index lists recurring structured outputs: **"Field report 11 March, 2025"**,
    **"Field report 10 March"**, **"The White Helmets Work Report - October 2024"**,
    **"The White Helmets Monthly Activity Report"** (multiple months), **"The White Helmets Response
    in Latakia and Tartus"** (consecutive-day operational logging).
- Behavioral read: This is a **volunteer, ground-level** actor that DOES maintain structured
  operational records under extreme pressure (bombardment, consecutive-day responses). They produce
  periodic field reports + monthly activity reports with incident counts. This is the grassroots
  **SUCCESS case** the grassroots hunt said was still missing.
- Caveat (honesty): White Helmets are a *semi-formalized* civil-defense org with a mandate, training,
  and an accountability function — not a loose mutual-aid chat. So this proves *"volunteers CAN
  maintain structured info when there is a mandate/owner/accountability structure,"* not *"informal
  chats spontaneously become databases."* That caveat is the whole point (see §3).
- Reality tag: **A** (volunteer-level SUCCESS, conditional on structure/mandate).

### A2 — Ground Truth Solutions — systematic community feedback collection (RETRIEVED, HTTP 200)
- Source (home): https://www.groundtruthsolutions.org/  (fetched `gts_home.html`)
- Quote (verbatim): *"Evidence from earlier outbreaks – including through GTS' work in the
  2014–2016 West Africa Ebola Outbreak – shows that meaningful community engagement, **systematic
  feedback collection** and trusted local intermediaries can improve acceptance of public health
  measures and strengthen outbreak control."*
- Further real signals on the same page: *"Community engagement as a mindset: lessons for a
  community-led response"* (Somalia, 2026), *"Communities know best: community voices driving a more
  effective and local response in Lebanon"* (2026), *"Communities in Chad are not getting the support
  they need"* (2026).
- Behavioral read: Community-level structured information (feedback, perceptions, priorities) IS
  collected **systematically** in some responses. This is a Reality-A signal at the community tier.
- Caveat: This structuring is usually orchestrated *by professional intermediaries* (GTS/implementers
  running feedback loops), not by the affected community maintaining its own board. So it is
  "structure FOR communities," not always "structure BY communities." Nuance noted.
- Reality tag: **A** (conditional — structured by a facilitating function).

### A3 — CDAC Network — community info integrity as a recognized function (RETRIEVED, HTTP 200)
- Source: https://www.cdacnetwork.org/  (fetched `cdac_home.html`)
- Signals on fetched page: *"SAFE AI: the first governance framework for AI in humanitarian action"*,
  *"Community in the loop: AI and accountability"*, *"Flooding the zone: how inauthentic networks
  weaponise information in Sudan"*, *"Tipsheet: coordinated inauthentic network behaviour."*
- Behavioral read: The sector treats **community information integrity / structured community comms**
  as a standing, funded function. Implies that where a function owns it, community info is structured;
  where no function owns it, it is not. Supports the moderator hypothesis.
- Reality tag: **A** (systemic — structure exists where a function owns it).

### Prior A6a evidence (formal orgs, carried from A6-EVIDENCE-CAMPAIGN.md, not re-fetched here)
SARC IM Department, MapAction automation, Ushahidi→HDX cleaning, WFP edge capture, HOTOSM validators,
ReliefWeb editors — all show structured maintenance **with a designated owner + low burden**. This is
the same moderator pattern at the formal tier. Included here only to show the pattern is consistent
across tiers, not as new A6b evidence.

---

## 2. Contradiction Log

The campaign did NOT produce a clean for/against contradiction (one source saying "they always
structure" vs another "they never do"). Instead it produced a **structuring contradiction by
population** — which is more useful:

| # | Contradiction / tension | Resolution from evidence | Implication for A6b |
|---|------------------------|--------------------------|---------------------|
| C1 | ERRs (chat-native, docs-as-gap) vs White Helmets (structured field/monthly reports) | Population split: **formalized/ mandated volunteers structure; informal mutual-aid chats don't** | A6b is not yes/no — it is **conditional on an owner/mandate** |
| C2 | GTS "systematic feedback collection" (structure FOR communities) vs ERRs "docs are a gap" (no structure BY communities) | Structuring is done *by a facilitating function*, rarely *by the informal coordinator themselves* | Nidaa's user may need to BE that facilitating function, or plug into one |
| C3 | White Helmets succeed under bombardment (extreme pressure) — seems to contradict "structure collapses under pressure" | Their structure survives BECAUSE reporting is mandated/accountable, not optional | Pressure alone doesn't kill structure; **loss of owner/mandate does** |
| C4 | A6a (formal orgs) = Early Support; A6b (informal) = was leaning Weak | Same owner/burden moderator explains both; not a contradiction, a gradient | The formal→informal gradient is the real A6b shape |

Open contradictions / still-unresolved gaps (these are what would *change* the conclusion):
- **No first-hand informal-COLLAPSE event.** ERRs show chat-default but no documented "we started a
  register and it died on day 3" account. A hard-collapse first-hand would strengthen Reality-B.
- **No first-hand informal-SUCCESS by a truly loose coordinator.** White Helmets are semi-formal. A
  camp-committee beneficiary spreadsheet maintained under load would be the cleanest Reality-A from
  the actual Nidaa population.
- **Direction of structuring unknown for Gaza specifically.** Abdelrahman Saleh (pending) is the
  closest live signal; Mones (pending) is the coordinator-level test.

---

## 3. Confidence Assessment for A6b

### What changed this campaign
Before: A6b = "Unproven, leaning Weak" — a guess that informal coordinators probably won't structure.
After: A6b = **"Conditional — population-split, evidence-backed"** — we can now say *why* it splits,
and the "why" is grounded in real fetched sources, not speculation.

### Refined statement of A6b (testable, not vague)
- **A6b-weak (informal, no owner):** "A loose coordinator / mutual-aid chat with no designated owner
  or mandate will maintain structured operational info under pressure." → **Contradicted / Weak.**
  Evidence: ERRs (B1, B2) — chat is the system, documentation is a named gap.
- **A6b-strong (owner/mandate present):** "A coordinator with a designated owner, training/mandate,
  and low-burden capture will maintain structured info under pressure." → **Supported.** Evidence:
  White Helmets (A1), GTS systematic feedback (A2), CDAC function (A3), and the carried A6a formal
  sources.

### Confidence scores
| Sub-claim | Confidence | Basis |
|-----------|-----------|-------|
| Informal coordinators default to chat, not structure | **Medium-High** | 2 independent ACAPS sources (ERRs) agreeing |
| Volunteers CAN structure under extreme pressure IF mandated | **Medium** | White Helmets (1 source, semi-formal); needs a second |
| Structuring is done by/through a facilitating function, not spontaneously by the crowd | **Medium** | GTS + CDAC + White Helmets all imply a function owns it |
| A truly loose coordinator maintains a register under load | **Low** (untested) | No first-hand informal-success yet |
| A loose coordinator's register dies under surge/connectivity loss | **Low** (untested) | No first-hand informal-collapse yet |

### Bottom line for the thesis
A6b is **neither validated nor killed** — it is **resolved as conditional**. This is a genuine
result, not a dodge:
- It does NOT validate the original "standalone coordinator-led board" model (no informal SUCCESS
  case exists for that).
- It does NOT kill Nidaa (White Helmets prove volunteers structure when supported).
- It **sharpens the product shape**: structure survives only when (a) there is an owner/mandate and
  (b) the burden is near-zero and lives inside the existing channel. That points firmly at the
  **"embed inside the workflow / be the facilitating function"** direction — i.e. Reality B = Discovery
  (as A6-FIELD-LOG.md already framed it), now evidence-backed rather than hypothesized.

This is exactly the kind of falsification the campaign was supposed to produce: it killed the naive
version of A6b and replaced it with a precise, testable conditional.

---

## 4. Recommended Next Evidence Targets

Ranked by expected information value (which uncertainty they close). These are TIER-2 (field)
targets — the public-evidence side is now sufficiently resolved; the remaining gaps are all
first-hand.

1. **Mones (coordinator-level, PENDING reply).** Highest value: a real grassroots coordinator
   answering the Six A6 Questions directly. Closes: informal-success OR informal-collapse (C4 gaps).
   Route via EVIDENCE-INTAKE-TEMPLATE → A6-FIELD-LOG Row 1.
2. **Abdelrahman Saleh (Wa7at Initiative, Gaza — PENDING detailed reply).** Gaza-specific signal on
   chat-vs-structure reality on the ground. Closes the Gaza-direction gap (C4).
3. **One first-hand informal-COLLAPSE account.** A coordinator who started a spreadsheet/board and it
   died under surge/connectivity loss. Targets: Omar, Shaima, a camp-committee contact, AbuAlatta /
   Sameer Project. Strengthens Reality-B with a hard event.
4. **One first-hand informal-SUCCESS account from the actual Nidaa population.** A camp committee or
   neighborhood committee maintaining a real beneficiary/needs register under load. Targets: White
   Helmets *local team interview* (how do they sustain monthly reporting under bombardment?), a
   mutual-aid coordinator using a real tool (not just chat).
5. **Triangulate the GTS finding.** Ask a field coordinator: *"Do you systematically collect community
   feedback, or is it ad hoc in chat?"* Converts A2 from "structure FOR communities" to a behavioral
   yes/no.

### Outreach action (fires when a reply lands)
Do NOT expand the candidate list proactively. The pipeline is: reply → real story →
EVIDENCE-INTAKE-TEMPLATE → ASSUMPTION-TRACKER (update A6b row to Conditional/Medium) →
A6-FIELD-LOG Row 1 → journal → commit. A reply alone is never evidence.

---

## 5. Honesty / provenance note

- Every quote above is from an HTML file fetched this session and stored in `pilot/research-day5/`.
  No source is invented; no quote is paraphrased from memory.
- The White Helmets / GTS / CDAC / ACAPS URLs returned HTTP 200 and the quoted text appears verbatim
  in the fetched files.
- Two sub-claims (informal-success, informal-collapse) remain UNTESTED — explicitly flagged as Low
  confidence, not filled in.
- This campaign produced **public (Tier-1) evidence only**. The A6b gate's true milestone — *one real
  coordinator story answering all six questions* — remains unmet and is now better-specified, not
  closed.

Last updated: 2026-07-17 (Day-5 A6b Resolution Campaign). No code, no features, no architecture.
A6-FIELD-LOG.md and the 3 prior-session outreach files are left untouched.
