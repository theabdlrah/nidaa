# Nidaa (نداء) — Project Overview & FAQ

*Version: 2026-07-14 · Status: active development · Suitable for external sharing*

---

## Project Status

**Nidaa is currently in active development.** This document describes the project's vision, architecture, design principles, development direction, and intended capabilities. Some features described may still be under development, experimental, or awaiting validation through pilot deployments.

Throughout this document we use three explicit labels so readers can tell what is real today from what is intended:

- **[BUILT]** — implemented and present in the current codebase.
- **[IN DEV]** — partially implemented, experimental, or actively being built; not yet production-ready.
- **[PLANNED]** — designed or intended, but not yet built. No claim is made that it works.
- **[ASSUMPTION]** — a belief about the real world that has not yet been validated by deployment.

Where a claim is uncertain, this document says so directly.

---

## 1. What is Nidaa?

Nidaa (نداء, "call" or "appeal" in Arabic) is an offline-first, Arabic-first community coordination board. It is a web application where a local community can post and browse **needs** and **offers** — for example, a clinic posting free care, or a family posting that they need water — and where trusted coordinators can mark entries as **verified**.

The core design principle is that the board must remain **usable when there is no internet connection**, because the environments it targets (Gaza, the West Bank, Syria) routinely experience connectivity loss, network shutdowns, and damaged infrastructure.

Nidaa is **open source** and intended to be self-hostable by the communities or organizations that use it.

It is **not** a chat app, a social network, a national reporting system, or a surveillance tool. **[BUILT as prototype; see limitations]**

---

## 2. Why does Nidaa exist?

Because coordination of local help breaks down precisely when it is needed most. In crises, the channels people rely on — messaging groups, central servers, social platforms — become unreliable at exactly the moment needs spike. Information scatters across closed group chats that newcomers cannot see, gets lost when phones die or accounts are banned, and cannot be trusted because anyone can post anything.

Nidaa is an attempt to give a community a **durable, local, verifiable** record of who needs what and who can help — one that does not depend on a single company, a single server, or a working connection at the moment of need. **[MOTIVATION; not yet validated in deployment — ASSUMPTION]**

---

## 3. What problem is Nidaa trying to solve?

The underlying problem is **coordination under unreliable infrastructure and unverifiable information**.

Stripped of features, the user pain is:

> "I am in a place where connectivity is unreliable, and I need to know, trust, and share what help exists nearby — but the tools I have lose that information or cannot be trusted."

Nidaa addresses three sub-problems:

1. **Availability** — information must survive disconnection. **[BUILT: offline-first local store]**
2. **Trust** — readers need a way to know an entry was confirmed by a responsible party. **[BUILT: role-gated verification + audit; early]**
3. **Coordination** — a shared, browsable board代替 scattered private chats. **[BUILT as prototype]**

It does **not** attempt to solve logistics, physical delivery, funding, or security of people — only the information-coordination layer.

---

## 4. Who is Nidaa designed for?

Primary audiences (intended):

- **Local coordination communities** in connectivity-stressed environments (Gaza, West Bank, Syria named as first deployment targets). **[PLANNED deployment; not yet piloted]**
- **Grassroots aid groups and diaspora mutual-aid organizations** coordinating on the ground or remotely.
- **Verifiers** — trusted coordinators, NGO field staff, or community leaders who confirm entries.
- **Technical partners and mappers** (e.g. OSM/HOT contributors) who can validate the data pipeline.
- **Researchers** studying humanitarian information systems.

It is **not** designed for individual private communication, nor as a replacement for emergency services.

---

## 5. How does Nidaa work?

Current implementation **[BUILT, prototype]**:

- A Next.js web app (Progressive Web App) that runs in a browser and can be installed on a phone.
- Entries (needs/offers) are written to the device first (IndexedDB), so posting works with **no connection**. **[BUILT: lib/offlineQueue.ts]**
- When a connection is available, queued entries sync to a server, which stores them in a JSON file (`data/db.json`). **[BUILT: app/api/entries/route.ts]**
- The board displays entries by type, category, region, and verification status. **[BUILT]**
- A trusted verifier can mark an entry verified through a protected endpoint; the action is recorded in an audit log and is reversible. **[BUILT: app/api/verify/route.ts, lib/auth.ts, lib/store.ts]**

The map view seeds facility locations from humanitarian datasets (HDX / OpenStreetMap). **[BUILT: import-hdx script + gaza-boundary.geojson]**

What is **not** yet built: real user identity, mesh/peer-to-peer sync, CRDT conflict resolution, and multi-device convergence. See sections 22–25.

---

## 6. What makes Nidaa different from WhatsApp, Telegram, Signal, Ushahidi, and similar systems?

| System | Primary model | Offline survival | Verification model | Nidaa's difference |
|---|---|---|---|---|
| WhatsApp / Telegram / Signal | Private/group messaging | Messages need a connection to send; history is per-device/account | None (anyone can claim anything) | Nidaa is a **shared, browsable board**, not a chat; posts persist locally without connection and are verifiable |
| Ushahidi | Crowdmapping / reporting platform | Typically requires connection to submit | Often reporter-based, variable verification | Nidaa is offline-first at the device level and verification is role-gated + audited + reversible **[IN DEV vs Ushahidi's maturity]** |
| Spreadsheets / shared docs | Manual lists | Need connection + account | Manual | Nidaa is purpose-built, Arabic-first, offline-by-default |

Honest caveat: Ushahidi and similar platforms are **far more mature and field-tested** than Nidaa. Nidaa's only claimed differentiator today is the **offline-first, device-is-source-of-truth** design and the **audited, reversible verification** model. Those are implementation choices, not proven advantages. **[ASSUMPTION that they matter — unvalidated]**

---

## 7. How does verification work?

**[BUILT — early stage]**

- There are roles: anonymous/user, verifier, admin. **[BUILT: lib/auth.ts]**
- Marking an entry verified (or unverified) requires a verifier or admin token. Anonymous users and ordinary users **cannot** forge a verification. This was tested: anonymous → 401, user → 401, verifier/admin → 200. **[BUILT + runtime-tested]**
- Every verification action is written to an audit log (`data/verify-audit.json`) recording: entry id, actor role, action, prior state, new state, timestamp. **[BUILT]**
- Verification is **reversible** — a verifier can undo a mark, and the change is audited. **[BUILT]**

What is **not** built: a real user-account/identity system (tokens are server-side env secrets today), federated verification across organizations, or reputation scoring.

**Limitation (important): verification requires a connection to the Host.** During a network shutdown — the exact condition Nidaa is built for — the "verified" state cannot be updated, so trust signals go stale precisely when crisis peaks. Nidaa preserves unverified local posts; it does **not** solve trust under a total blackout. Mitigation requires at least two independent verifiers per deployment and an out-of-band override the org defines; a single verifier has no automated fallback.

---

## 8. How does trust work?

Trust in Nidaa is **institutional, not cryptographic or algorithmic**.

- A reader trusts a "verified" mark because it was made by a party the deploying organization designated as a verifier. **[BUILT mechanism; trust in the verifier is organizational, not technical]**
- The audit log makes every verification attributable and reversible, so abuse can be detected and corrected. **[BUILT]**
- There is **no** automated fact-checking, no AI verification, and no decentralized consensus yet. **[PLANNED concepts, not built]**

The hard truth: **Nidaa cannot make information true. It can only make the act of verification accountable.** Whether a verifier is trustworthy is a governance question, not a software one. **[ASSUMPTION: partner orgs will operate verification responsibly — unvalidated]**

---

## 9. How does synchronization work in low-connectivity environments?

**[BUILT — basic; not yet field-tested]**

- New posts are saved on the device (IndexedDB) immediately, with `syncedAt = null` (pending). **[BUILT]**
- When connectivity returns, the app sends pending entries to the server. **[BUILT: client queue]**
- The server appends them to `data/db.json`. **[BUILT]**

Current limitations: sync is **client→server only** in the basic implementation; there is **no** conflict resolution between two devices that edited the same entry, **no** mesh/peer sync, and **no** CRDT. If two offline devices both modify state, the result is last-write-wins on the server, which can lose data. **[KNOWN LIMITATION — see 15]**

A more robust sync model (CRDTs, mesh) is **[PLANNED]**, not built.

---

## 10. What happens when information conflicts?

Today: **last-write-wins** on the server for the basic fields. **[BUILT but naive]**

This is a known weakness. If two verifiers or two offline devices disagree, there is no merge logic yet — the later write overwrites. Verification status changes are audited, so the *history* is visible, but the *current value* is not the result of a defined conflict policy.

Proper conflict handling (CRDTs, version vectors, or explicit human resolution) is **[PLANNED]** and not yet implemented. **[ASSUMPTION: real conflict rates are unknown until pilot]**

---

## 11. How is misinformation handled?

Honestly: **mostly by human process, not by software.**

- Verification by trusted parties is the primary mitigation. **[BUILT mechanism]**
- Unverified entries are visually distinguished from verified ones. **[BUILT]**
- There is **no** automated detection of false information, no content moderation AI, and no fact-checking pipeline. **[Not built]**
- Expected future handling: community reporting of suspect entries, verifier revocation, and audit review. **[PLANNED; not built]**

Nidaa can reduce *accidental* misinformation (lost, duplicated, or unverifiable posts) but cannot stop *deliberate* misinformation by a bad actor with posting access. That risk is real and discussed in section 17. **[ASSUMPTION: misuse vectors not yet observed — unvalidated]**

---

## 12. How does Nidaa protect privacy?

**[BUILT — design intent; partially implemented]**

- No mandatory personal data to post or browse. Posts are about needs/offers, not identities. **[DESIGN; fields are optional]**
- Organizations can self-host, keeping all data on their own infrastructure. **[PLANNED deployment model; self-hosting code exists as standard Next.js app, not yet packaged for non-technical operators]**
- Data is exportable. **[PLANNED tooling; not built as a UI feature yet]**

What is **not** yet implemented: end-to-end encryption, anonymous credential systems, and a privacy threat model validated by a security auditor. **[Not built]**

---

## 13. What data does Nidaa collect?

Current implementation collects, per entry **[BUILT]**:

- type (need/offer), category (medical/food/water/shelter/education/other)
- title and body (Arabic + English)
- city, approximate coordinates (lat/lng), region
- author role (ngo / volunteer / individual / other) — self-declared, **not verified**
- createdAt, clientId, syncedAt
- verification status + audit history

Contact fields are optional. **[BUILT: optional]**

**Note on seed data:** the sample entries shipped with the app are **illustrative** (Syria cities) and explicitly **not** real operational data. The production dataset is intended to come from humanitarian sources (HDX/OSM) and live community posts. **[BUILT: data/seed.ts is illustrative]**

---

## 14. What data does Nidaa avoid collecting?

By design **[INTENDED; partially enforced]**:

- No mandatory names, phone numbers, or national IDs to use the board.
- No real-time location tracking of users; only the approximate location of a *posted need/offer*.
- No behavioral profiling or advertising.
- No data sold or shared with third parties by the software itself.

These are **design commitments**. The current prototype does not yet enforce them with a validated privacy architecture (e.g. no server-side minimization audit). **[ASSUMPTION: commitments hold under real deployment — unvalidated]**

---

## 15. What are the technical limitations?

**[CURRENT, HONEST]**

1. **Single-server store.** `data/db.json` is one JSON file; not built for high concurrency or large scale. **[BUILT but not production-grade]**
2. **No real identity.** Verification uses server-side tokens, not user accounts. Token leakage = verification compromise. **[BUILT interim; weak]**
3. **Naive conflict resolution.** Last-write-wins; no CRDT/mesh. **[BUILT but weak]**
4. **No mesh / offline peer sync.** Devices cannot sync with each other without the server. **[Not built]**
5. **No end-to-end encryption.** **[Not built]**
6. **Client fetch of live API is blocked in some sandboxed environments**, meaning a headless render may show empty boards. This is an environment limitation, not a product claim. **[OBSERVED]**
7. **Scale untested.** 10k+ seed entries exist, but real concurrent load, latency, and sync under poor networks are **not yet measured**. **[ASSUMPTION]**

---

## 16. What are the operational limitations?

- **No pilot yet.** Every assumption about usefulness is unvalidated. **[ASSUMPTION]**
- **Depends on a trusted verifier existing.** If no reputable party operates verification, the "verified" mark means nothing. **[ASSUMPTION]**
- **Depends on someone running the server.** Nidaa is not yet a zero-infrastructure mesh; it needs at least one host. **[BUILT requires host; mesh PLANNED]**
- **Digital divide.** Users still need a phone and a browser; Nidaa does not reach people with no device. **[INHERENT]**
- **Governance burden.** Someone must define verifier roles, handle disputes, and own the audit. That labor is real and unfunded. **[ASSUMPTION: orgs will absorb this — unvalidated]**

---

## 17. What are the ethical risks?

Nidaa is a dual-use information system. Risks we acknowledge:

1. **Harm from inaccurate verification.** A wrongly-verified entry could send people to a false resource or away from real help. **[MITIGATION: audit + reversibility; not a guarantee]**
2. **Surveillance / targeting.** A board of who-needs-what could be weaponized if captured by a hostile actor. Nidaa must avoid becoming a targeting list. **[DESIGN PRIORITY: minimal personal data; self-hosting; no mandatory IDs]**
3. **Chilling effect.** If posting is perceived as risky, communities may self-censor. **[ASSUMPTION]**
4. **False sense of safety.** A polished board may imply coordination capacity that does not exist on the ground. **[RISK of the tool itself overstating reality]**
5. **Dependency.** If a community comes to rely on Nidaa and the host disappears, coordination may collapse. **[INHERENT to hosted model]**
6. **Weaponized misinformation.** A bad actor with posting access can flood the board; current mitigation is human verification only. **[LIMITED MITIGATION]**

These are not theoretical to us; they shape the "safe by default" principle. **[DESIGN; not yet audited by external ethics review]**

---

## 18. What are the biggest challenges facing the project?

1. **Validation.** No pilot means no evidence the design fits real behavior. **[BLOCKER-level risk]**
2. **Identity without surveillance.** How to let verifiers be accountable without collecting personal data. **[OPEN technical+governance problem]**
3. **Sync without central dependence.** Mesh/CRDT is hard and unbuilt. **[TECHNICAL]**
4. **Trust bootstrap.** Who is the first verifier, and why should anyone trust them? **[GOVERNANCE]**
5. **Sustainability.** Hosting, maintenance, and governance labor with no funding model. **[STRATEGIC]**
6. **Adoption vs novelty.** The risk of building impressive tech nobody uses. **[PRODUCT]**

---

## 19. What assumptions still need validation?

**[ALL UNANSWERED UNTIL PILOT]**

- That communities will actually post and browse in a crisis.
- That a trusted verifier role is sustainable locally.
- That offline-first matters as much in practice as in theory.
- That the board improves coordination versus existing group chats.
- That sync survives real network conditions (not just the sandbox).
- That misuse remains manageable with human-only verification.
- That self-hosting is feasible for the orgs that need it.

Each is an **[ASSUMPTION]**, not a fact.

---

## 20. What does success look like?

A modest, defensible definition:

- At least one community uses Nidaa operationally for a defined period (e.g. 4–8 weeks) and reports it **helped coordinate information** more reliably than their prior method. **[PLANNED pilot metric]**
- Verification is operated responsibly by a real verifier, with an audit trail that survives review.
- The board remains usable through at least one real connectivity disruption during the pilot. **[TARGET; not yet demonstrated]**

Success is **evidence**, not features shipped.

---

## 21. What does failure look like?

Failure modes, ranked by likelihood **[OPINION, unvalidated]**:

1. **No adoption** — built, but communities keep using WhatsApp. (Most likely.)
2. **Pilot never launches** — blocked on trust, hosting, or permissions.
3. **Verification captured/abused** — a bad verifier undermines trust.
4. **Technical failure under real conditions** — sync loses data when it matters.
5. **Ethical harm** — board used for targeting or misinformation at scale.
6. **Abandonment** — no sustainability, project stalls.

Any of these would mean Nidaa remains an idea, not evidence.

---

## 22. What is the current development status?

**Active development. Prototype stage.** Core coordination + offline + verification-audit exist; identity, mesh, CRDT, AI, and real pilot are not built. **[BUILT as described; rest PLANNED/IN DEV]**

---

## 23. What has already been built?

**[BUILT — verified in codebase, 2026-07-14]**

- Offline-first PWA (Next.js 14 + React). **[BUILT]**
- Local device store (IndexedDB queue); posts survive disconnection. **[BUILT: lib/offlineQueue.ts]**
- Server entries API + JSON store. **[BUILT: app/api/entries, lib/store.ts]**
- Role-gated verification endpoint (anonymous/user blocked; verifier/admin allowed). **[BUILT: lib/auth.ts, app/api/verify/route.ts]** + runtime-tested.
- Verification audit log, reversible. **[BUILT: lib/store.ts, data/verify-audit.json]**
- Arabic-first UI + RTL. **[BUILT]**
- Map seeded from HDX/OSM facility data + Gaza boundary. **[BUILT: import-hdx, gaza-boundary.geojson]**
- ~10,000 seed entries (illustrative) for demonstration. **[BUILT; illustrative, not operational]**

**Governance roles are defined in code (verifier/admin); the operating model is PLANNED / unvalidated — not "governance implemented."** **[BUILT roles; model IN DEV]**

**Deployed controls vs promised (safety/liability honesty):** actually present today = optional fields, no mandatory personal data, single-host JSON store (readable by host operator). Promised, NOT built = self-hosting packaging, end-to-end encryption, confirmed open-source license, external security/ethics review. Do not treat Nidaa as private or self-controlled until the promised controls ship. A pilot should not proceed without a do-no-harm review, a basic data-protection assessment (DPIA), and a data-processing agreement stating ownership and deletion. (A do-no-harm summary exists; DPIA and agreement are still to be completed.)

---

## 24. What is currently being developed?

**[IN DEV — not yet production-ready]**

- A proper verifier login / identity layer (intended: Auth.js) replacing env tokens.
- Pilot configuration and a lightweight training/onboarding flow.
- Metrics instrumentation to measure whether the board helps.
- Hardening of the sync path for poor networks.

None of these are complete as of this document.

---

## 25. What is planned for future phases?

**[PLANNED — not built; no working claim]**

- Mesh / peer-to-peer sync (devices sync without the server).
- CRDT-based conflict resolution.
- Decentralized trust / federated verification across orgs.
- Signed, attributable feeds.
- AI-assisted (not autonomous) triage, translation, and duplicate detection — strictly as aids to human verifiers.
- Self-hosting packaging for non-technical operators.
- External ethics/privacy review.

These are directions, not promises.

---

## 26. How will pilot deployments work?

**[PLANNED — not yet executed]**

Intended approach:

- A low-risk, instrumented pilot with one reachable coordination community (diaspora mutual-aid orgs are the current outreach target; Gaza NGOs are deferred as currently unreachable).
- 4–8 weeks, low burden, <1 hour training.
- The deploying org defines verifier roles and owns the audit.
- Nidaa team provides the host + metrics, and co-authors a field report.
- Success = evidence the board helped; failure = documented lessons.

No pilot has started. Outreach is prepared but not yet sent. **[STATUS: pre-pilot]**

---

## 27. What questions remain unanswered?

- Will real communities adopt it over existing tools?
- Who bears the governance labor long-term?
- Does offline-first materially change outcomes, or just feel good?
- Can verification stay trustworthy without professional moderation?
- Is self-hosting realistic for the orgs that need it?
- What is the actual misuse rate, and can human verification contain it?
- What legal/neutralidade constraints apply in each deployment context?

These are open. The pilot is the instrument for answering them.

---

## 28. Frequently Asked Questions

*Grouped by theme. Every answer states uncertainty where it exists. [BUILT]/[IN DEV]/[PLANNED]/[ASSUMPTION] labels used throughout.*

### A. Basics & Purpose

**Q1. Is Nidaa a messaging app?**
No. It is a shared, browsable board for needs and offers — not a chat. **[BUILT as board]**

**Q2. Is it a replacement for WhatsApp or Telegram?**
No, and it is not intended to be. It can complement them (e.g. receive posts from a group). **[DESIGN]**

**Q3. Why "offline-first"?**
Because the target environments lose connectivity routinely. The board must work when the connection doesn't. **[BUILT principle]**

**Q4. Is Nidaa finished?**
No. It is an active-development prototype. **[STATUS]**

**Q5. Is it open source?**
Yes, intended to be. **[BUILT as standard Next.js app; license to be confirmed in repo]**

**Q6. What does "نداء" mean?**
"Call" or "appeal" in Arabic. **[NAME]**

**Q7. Is this a commercial product?**
No current commercial model. **[STATUS]**

**Q8. Can I use it for my neighborhood, not a war zone?**
The design is general; first deployment targets are Gaza/West Bank/Syria, but the model is reusable. **[ASSUMPTION: generalizability unproven]**

### B. Users & Access

**Q9. Do I need an account to browse?**
Currently, browsing is open in the prototype. **[BUILT; may change with identity layer — IN DEV]**

**Q10. Do I need an account to post?**
Today, posting works client-side without login; a server-side identity layer is in development. **[BUILT interim; IN DEV]**

**Q11. Can I stay anonymous?**
Posting does not require personal data. **[DESIGN; not yet privacy-audited]**

**Q12. What if I have no smartphone?**
Nidaa requires a browser-capable device. It does not reach people with no device. **[INHERENT limitation]**

**Q13. Is it available on iOS/Android?**
As a PWA (installable web app) today. **[BUILT PWA]**

**Q14. What languages does it support?**
Arabic (RTL) primary, with English fields. **[BUILT]**

**Q15. Can non-Arabic speakers use it?**
Entries carry Arabic + English text fields. **[BUILT; full i18n PLANNED]**

### C. Verification & Trust

**Q16. Who can mark something "verified"?**
Only designated verifiers/admins with a token. Ordinary users cannot. **[BUILT + tested]**

**Q17. Can a normal user fake a verification?**
No — the endpoint rejects anonymous and user tokens (returns 401). **[BUILT + runtime-tested]**

**Q18. What if a verifier is wrong?**
The action is reversible and audited; another verifier can undo it — provided at least two independent verifiers exist. With a single verifier there is no automated fallback; the org must define an out-of-band override. Trust in the verifier is organizational, not a software guarantee. **[BUILT mechanism; single-verifier gap acknowledged]**

**Q19. Can verification be audited later?**
Yes — every action is in an audit log with actor, prior/new state, timestamp. **[BUILT]**

**Q20. Is verification done by AI?**
No. It is human, by designated verifiers. AI assistance is only a future aid, not autonomous. **[BUILT: human-only; AI PLANNED as aid]**

**Q21. How do I become a verifier?**
Through the deploying organization's governance; not self-assigned. **[PLANNED governance; not yet built]**

**Q22. What stops a verifier from abusing power?**
Audit + reversibility + the org's own accountability. No technical guarantee beyond attribution. **[BUILT mechanism; trust is organizational — ASSUMPTION]**

**Q23. Is "verified" a guarantee the info is true?**
No. It means a designated party confirmed it. Nidaa cannot make information true. **[HONEST LIMIT]**

**Q24. Can verification be federated across orgs?**
Planned, not built. **[PLANNED]**

### D. Data & Privacy

**Q25. What personal data is required?**
None required to post or browse. **[DESIGN; optional contact only]**

**Q26. Is my location tracked?**
Only the approximate location of a posted need/offer, not continuous user tracking. **[DESIGN]**

**Q27. Who can see my posts?**
Anyone who can access the board (depends on deployment). **[DEPLOYMENT-DEPENDENT]**

**Q28. Is data encrypted?**
Not end-to-end yet. **[NOT BUILT]**

**Q29. Can I export my data?**
Intended (self-hosting/export). Export UI not built yet. **[PLANNED]**

**Q30. Can I delete my post?**
Deletion/moderation flows are planned, not fully built. **[PLANNED]**

**Q31. Where is the data stored?**
On the host server (JSON today) and on your device. Self-hosting planned. **[BUILT + PLANNED]**

**Q32. Do you sell data?**
No. The software does not share data with third parties. **[DESIGN commitment; unvalidated in deployment]**

**Q33. What about GDPR / local laws?**
Not yet assessed per deployment. **[ASSUMPTION: needs legal review]**

**Q34. Could the board become a targeting list?**
Yes — this is the PRIMARY ethical risk, not a side note. A geolocated board of who-needs-what can be weaponized. Today's only real mitigations are optional precise coordinates (flagged as potentially unsafe) and no mandatory personal data. Self-hosting and E2E — often cited as the fix — are NOT built yet. Deployments should minimize precise coordinates and weigh this risk explicitly before launch. **[RISK; see 17; mitigations mostly PLANNED]**

### E. Technical & Architecture

**Q35. What is the tech stack?**
Next.js 14, React, TypeScript, IndexedDB (client), JSON store (server), Leaflet (map). **[BUILT]**

**Q36. How does offline posting work?**
Written to device IndexedDB first; synced when online. **[BUILT]**

**Q37. What happens if two devices edit the same entry offline?**
Last-write-wins on server; no merge yet. **[KNOWN LIMITATION]**

**Q38. Is there mesh networking?**
No, not yet. **[PLANNED]**

**Q39. Do you use CRDTs?**
No, not yet. **[PLANNED]**

**Q40. How does sync handle conflicts?**
Naively today; CRDT/mesh planned. **[BUILT weak; PLANNED]**

**Q41. How scalable is it?**
Unknown at real load; single JSON store is not production-grade. **[ASSUMPTION]**

**Q42. Can it run without the internet entirely?**
Posting/browsing locally: yes. Syncing across devices: needs a host or (future) mesh. **[BUILT local; mesh PLANNED]**

**Q43. Is there an API?**
Yes — entries and verify endpoints. **[BUILT]**

**Q44. Can I self-host?**
The app is a standard Next.js app; full non-technical packaging is planned, not done. **[BUILT code; PLANNED packaging]**

**Q45. What are the known bugs?**
Concurrency/sync edge cases and no real identity are the main known weaknesses. **[KNOWN]**

**Q46. Has it been security-reviewed?**
No external review yet. **[ASSUMPTION: needed before pilot]**

**Q47. Does it work in low-end phones?**
As a web app, depends on the browser; not yet benchmarked on low-end devices. **[ASSUMPTION]**

**Q48. Is there a database or just a file?**
Current server uses a JSON file; a real DB is planned for scale. **[BUILT file; PLANNED DB]**

### F. Misinformation & Moderation

**Q49. How do you stop fake posts?**
Human verification + unverified labeling. No automated detection yet. **[BUILT partial; not built: automated]**

**Q50. What if someone posts harmful misinformation?**
Reporting + verifier action planned; today only human verification exists. **[LIMITED]**

**Q51. Can entries be reported?**
Reporting flow planned, not built. **[PLANNED]**

**Q52. Who moderates?**
The deploying org's verifiers. **[PLANNED governance]**

**Q53. Is there content moderation AI?**
No. **[NOT BUILT]**

**Q54. What about duplicates?**
Duplicate detection is a planned AI aid, not built. **[PLANNED]**

**Q55. Can verified status be gamed?**
If a verifier token leaks, yes — which is why tokens are server-side secrets and a real identity layer is in development. **[BUILT interim; IN DEV improvement]**

### G. Deployment & Pilots

**Q56. Is there a live deployment I can try?**
Not yet publicly. Pre-pilot. **[STATUS]**

**Q57. How do I request a pilot?**
Outreach is being prepared; no pilot has launched. **[STATUS: pre-pilot]**

**Q58. What does a pilot require from my org?**
At least two independent verifiers, low burden, 4–8 weeks, <1h training (intended). The partner owns local governance and the audit; the Nidaa team provides hosting, software, and metrics. **[PLANNED]**

**Q59. Will Nidaa cost money?**
No current cost model; hosting is the main expense. **[STATUS]**

**Q60. Can we self-host for privacy?**
Intended; packaging not finished. **[PLANNED]**

**Q61. What regions are targeted first?**
Gaza, West Bank, Syria named; Gaza NGOs currently unreachable, so diaspora orgs are first outreach. **[PLANNED; not yet reached]**

**Q62. What if connectivity is fully gone for weeks?**
Local browse/post works; cross-device sync needs host/mesh (mesh unbuilt). **[BUILT local; limitation otherwise]**

**Q63. Who owns the data in a pilot?**
Intended: the deploying org (self-host/export). **[DESIGN; not yet contractual]** A pilot data-processing agreement stating ownership and deletion is still to be completed, and a basic data-protection assessment (DPIA) should precede any pilot. Until self-host packaging ships, data would sit on the Nidaa team's host.

**Q64. Will there be training material?**
Planned (lightweight). **[PLANNED]**

**Q65. How is success measured in a pilot?**
Operational use + a field report; metrics instrumentation in development. **[PLANNED]**

### H. Governance & Ethics

**Q66. Who governs Nidaa?**
Currently the project maintainer; pilot governance by deploying org. **[STATUS]**

**Q67. Is there a code of conduct / do-no-harm policy?**
A do-no-harm summary exists; formal policy pending. **[BUILT doc; policy PLANNED]**

**Q68. What happens if Nidaa is used for harm?**
Acknowledged risk; mitigations are minimal-data + audit + reversibility, not guarantees. **[RISK]**

**Q69. Could a government compel the data?**
If hosted by them or on their infrastructure, yes — which is why self-hosting is emphasized. **[DEPLOYMENT-DEPENDENT]**

**Q70. How are disputes between verifiers resolved?**
Human governance by the org; no software policy yet. **[PLANNED governance]**

**Q71. Is there a bias risk in verification?**
Yes — verifier selection embeds bias. Mitigation is transparent, reversible audit. **[ACKNOWLEDGED]**

**Q72. Will Nidaa take a position on conflicts?**
No. It is infrastructure, not a participant. **[PRINCIPLE]**

### I. Roadmap & Contributions

**Q73. What is the next big feature?**
A real verifier identity layer, then pilot instrumentation. **[IN DEV]**

**Q74. Can I contribute code?**
Intended (open source); contribution process to be defined. **[PLANNED]**

**Q75. Can I contribute data or verification?**
Via a pilot org's governance; not directly yet. **[PLANNED]**

**Q76. Is there a public roadmap?**
This document is the current direction; no dated public roadmap yet. **[STATUS]**

**Q77. When will mesh/CRDT ship?**
No date; dependent on pilot evidence that they are needed. **[PLANNED; date unknown]**

**Q78. Will there be an AI feature?**
Only as a human-assisted aid (translation, triage, dedup), never autonomous verification. **[PLANNED; constrained]**

**Q79. How do I stay updated?**
Not yet established (no public channel). **[STATUS]**

**Q80. What is the single biggest risk to Nidaa?**
Ranked by harm to affected people: (1) **physical/safety harm** — if the board is misused for targeting or misinformation, or if stale facility data sends people into danger; (2) **no real-world validation** — building infrastructure communities do not adopt. The pilot is the instrument for answering (2); the safety items (targeting risk, stale-data banner, DPIA, data agreement, ≥2 verifiers) must be addressed before the first pilot. **[OPINION; ASSUMPTION unvalidated]**

---

*End of document. This overview reflects the project as of 2026-07-14 and will be revised as development and any pilot proceed. Where this document and running code disagree, the code is the source of truth and the document should be updated.*
