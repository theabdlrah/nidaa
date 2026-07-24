# Nidaa — Psiphon Watchlist Technology Review

Type: WATCHLIST TECHNOLOGY REVIEW (non-evidence, non-A6b).
Created: 2026-07-22 (resumed post-Day-10 governance close).
Purpose: understand the technology and determine whether Psiphon is relevant enough to REMAIN on
Nidaa's infrastructure watchlist. NOT a build/integration decision. NOT a Nidaa feature, hypothesis,
or A6b evidence.

Scope per the queued research questions:
1. Architecture (client/server model, control infrastructure)
2. Transport mechanisms (VPN / SSH / proxy / obfuscation)
3. Censorship resistance (how it survives blocking; domain fronting; techniques)
4. Failure conditions (what breaks it; infra dependencies; gov countermeasures)
5. Humanitarian relevance (connectivity-constrained environments; comms-resilience assumptions;
   watchlist recommendation)

Source discipline (Day-6 constitution): primary/authoritative sources only; literature/reviews flagged
as secondary. Sources retrieved live 2026-07-22:
- Psiphon Inc. GitHub meta-repo README (PRIMARY — architecture, transports, security properties).
- Psiphon Inc. "About Us" page (PRIMARY — org, scale, Citizen Lab origin).
- Wikipedia "Psiphon" (SECONDARY — history, architecture summary, citations to Citizen Lab).
- Wikipedia "Domain fronting" (SECONDARY — censorship-resistance technique context).
- Citizen Lab site search for "psiphon" (attempted; results JS-rendered, not retrievable — no
  specific Citizen Lab report was extracted; treated as a gap, not filled by inference).

LIMITATION (honest): Psiphon's own FAQ/How-It-Works pages are JS-accordion rendered; the answer
bodies were NOT present in the fetched static HTML. Protocol-level specifics (exact tunnel protocol,
obfuscation module names) are therefore drawn only from the GitHub README + Wikipedia, and explicitly
NOT invented. If a deeper protocol audit is later required, fetch the GitHub README of
Psiphon-Labs/psiphon-tunnel-core directly.

==================================================================
1. ARCHITECTURE
==================================================================
Per Psiphon Inc. GitHub README (PRIMARY):

- "The Psiphon Circumvention System is a relay-based Internet censorship circumventer."
- Components: (a) a CLIENT application that configures the user's device to direct Internet traffic;
  (b) a SET OF SERVERS that proxy client traffic to the Internet. "As long as a client can connect to a
  Psiphon server, it can access Internet services that may be blocked to the user via direct connection."
- Centralized, geographically diverse network of thousands of proxy servers, with a performance-oriented
  single- and multi-hop routing architecture (Wikipedia, citing Psiphon).
- Automatic server discovery: clients ship with a known server set; over time discover additional
  servers into a backup list. As older servers are blocked, the client draws from the reserve list on
  reconnect. Server discovery per client is rate-limited so an adversary cannot enumerate+block the
  whole network.
- Cross-platform: Windows, Android, iOS. "Zero install" — small-footprint app delivered by webpage,
  file-sharing, email, or USB; avoids install overhead.
- Chain of trust: client instances digitally signed; embedded server certificates authenticate the
  Psiphon servers a client connects to.
- Origin: Psiphon 1.0 developed at the Citizen Lab (University of Toronto), launched open-source 1 Dec
  2006; Psiphon, Inc. established 2007 as independent Ontario corp. Psiphon Inc. + Citizen Lab
  collaborate via "Psi-Lab." Scale (About page): "over 3 million people every week."
- Funding history (Wikipedia): US State Dept Internet Freedom program (DRL) + European Parliament, via
  Internews/SESAWE sub-grants. (Relevant to humanitarian/geopolitical context, not technical.)

CONTROL INFRASTRUCTURE: not a pure peer/P2P mesh — it is a centrally managed, Psiphon-Inc-operated
server network with client-side discovery + signed trust. This is a managed-service topology, not a
decentralized one.

==================================================================
2. TRANSPORT MECHANISMS
==================================================================
Per Wikipedia (SECONDARY) + Psiphon README (PRIMARY):

- Combination of secure communication + obfuscation: "uses a combination of ... a VPN, SSH, and a Web
  proxy" (Wikipedia).
- "Agile transport": pluggable architecture with MULTIPLE transport mechanisms. "In the case where one
  transport protocol is blocked by a censor, Psiphon automatically switches over to another mechanism."
  (Psiphon README — this auto-fallback is the core resilience property.)
- Web proxy component: link-rewriting web proxy (launchpad.net/psiphon per README).

EXPLICIT NON-CLAIM (limitation): the exact default tunnel protocol name and the specific obfuscation
module set (e.g. whether it uses meek/TLS camouflage, Obfs4-style, or Psiphon-proprietary) could NOT be
confirmed from the retrieved static sources (FAQ bodies JS-rendered). The README confirms "pluggable
multiple transports + automatic switchover" but not the precise protocol list. Flagged, not invented.

==================================================================
3. CENSORSHIP RESISTANCE (how it survives blocking)
==================================================================
Mechanisms evidenced:

- Transport agility (above): automatic switchover when one transport is blocked.
- Server diversity + discovery rate-limiting: a censor cannot trivially enumerate and block the whole
  server fleet; blocked servers are replaced from each client's reserve list.
- Obfuscation of traffic: encryption/authentication between client and proxy is used to "evade
  censorship based on deep-packet inspection" (Psiphon README, Confidentiality section).
- Signed chain of trust: defends against rogue-server impersonation by the censor.

DOMAIN FRONTING (technique context, Wikipedia "Domain fronting", SECONDARY):
- Domain fronting discreetly connects to a target via a trusted CDN front, so censors "are typically
  unable to differentiate circumvention traffic from overt non-fronted traffic." Censors are forced to
  either allow all traffic to the front domain or block it entirely.
- 2018 precedent: when Russia blocked Telegram (April 2018) by ISP-blocking the CDNs Telegram used as
  fronts, ~15.8M Google/Amazon CDN IPs were collaterally blocked, causing major outages. This shows the
  technique's strength (CDN blocking is economically/politically costly) AND its fragility (front
  providers can withdraw support — Google/Amazon/Cloudflare all restricted domain fronting in 2018).
- Psiphon's relationship to domain fronting: not confirmed from retrieved sources whether current
  Psiphon uses fronting specifically. Psiphon's stated resilience rests on transport agility +
  server diversity, not solely on fronting. Treated as context, not asserted as Psiphon feature.

==================================================================
4. FAILURE CONDITIONS (what breaks Psiphon)
==================================================================
From Psiphon README security properties + architecture:

- ENDPOINT DETECTION: "The censor will know the user is using Psiphon" — Psiphon does not hide that a
  user is running it. In a hostile jurisdiction, mere use can be incriminating. (Confidentiality section.)
- NO ANONYMITY: explicitly "not an anonymity solution such as Tor." The Psiphon proxy knows the user's
  source, unencrypted traffic, and destination. User necessarily trusts the proxy operator. (Anonymity
  section.) -> A trusted/compromised proxy is a single point of trust failure.
- TRAFFIC-ANALYSIS: does not defend against traffic-analysis attacks on flows to Psiphon proxies.
- PLAINTEXT EGRESS: encryption is client<->proxy only; egress from the proxy to the Internet is
  plaintext unless the destination itself uses HTTPS. Psiphon "does not add HTTPS where it is not already
  in place." (Confidentiality section.)
- TRANSPORT-SPECIFIC BLOCKING: if ALL available transports are blocked (or the agile set is exhausted by
  a censor who fingerprinting each), connectivity fails. The auto-switchover helps but is finite.
- SERVER BLOCKING AT SCALE: if a censor can enumerate+block the server fleet faster than discovery
  replenishes, service degrades. Rate-limiting discovery mitigates but does not eliminate this.
- FRONTING WITHDRAWAL: if Psiphon relied on a CDN front that the provider withdrew (2018 precedent),
  that vector closes.
- CONNECTIVITY PREREQUISITE: Psiphon requires an underlying Internet connection to a Psiphon server.
  It is NOT an offline/mesh technology. In a total connectivity blackout (no route to any server), it
  cannot function. This is the decisive limitation for Nidaa's reference environments (see §5).

==================================================================
5. HUMANITARIAN RELEVANCE (watchlist determination)
==================================================================
Question: could Psiphon matter in connectivity-constrained environments? Does it change assumptions
about communications resilience? Does it belong on Nidaa's infrastructure watchlist?

RELEVANCE TO NIDAA'S STATED CONTEXT (Gaza / Syria / protracted conflict, connectivity-stressed):
- Psiphon addresses CENSORSHIP / blocking of specific destinations — NOT generalized connectivity loss.
  Its value proposition is "access content blocked by your government," not "reach the Internet when the
  network is down."
- Nidaa's comms-resilience problem (per Mones evidence: connectivity/electricity outage degrades Teams/
  WhatsApp; satellite backup used for emergency-only) is a CONNECTIVITY/AVAILABILITY failure, not a
  censorship failure. Psiphon does NOT solve a blackout. It presupposes a working (if censored) link to
  a Psiphon server.
- Therefore Psiphon is OUT OF SCOPE as a Nidaa resilience building block: it does not address the failure
  mode Nidaa targets (connectivity collapse / offline operation). It addresses a different failure mode
  (selective destination blocking under a live link).

WHAT IT DOES tell us (negative/structural learning, still useful for the watchlist):
- It is evidence that "comms resilience under stress" has at least TWO distinct problem classes:
  (a) availability collapse (network gone) — Nidaa's target; (b) censorship/blocking (network present,
  destinations filtered) — Psiphon's target. Conflating them would be a category error. Nidaa's design
  assumptions (embed-in-workflow, offline buffer, satellite/backup path) address (a), not (b).
- It is a live, well-maintained, 3M-weekly-user circumvention system with a Citizen Lab pedigree. If a
  future Nidaa deployment operates inside a censoring (not merely connectivity-collapsed) environment,
  Psiphon (or Tor, or a similar tool) becomes relevant as an ADJACENT reference, not a component.

WATCHLIST RECOMMENDATION:
- KEEP on the watchlist, but reclassify from "infrastructure candidate" to "ADJACENT REFERENCE /
  OUT-OF-SCOPE TECHNOLOGY." Reason: it is a credible, current circumvention system worth knowing about
  for environments where censorship (not blackout) is the constraint, but it does NOT address Nidaa's
  target failure mode and must not be mistaken for an offline/resilience solution.
- DO NOT treat as a build/integration candidate. The original queue item explicitly excluded
  "should Nidaa integrate/build on/Add circumvention features" — this review upholds that exclusion on
  technical grounds (different failure mode; centralized managed topology; no offline capability).
- Re-review trigger: if Nidaa's deployment context shifts to a primarily-censoring (vs connectivity-
  collapsed) environment, or if a partner org asks about reaching blocked coordination resources,
  promote Psiphon from watchlist to active reference and pull the tunnel-core README for protocol detail.

==================================================================
6. CONFIDENCE & GAPS
==================================================================
- Architecture / transports / failure modes: Medium-High confidence — drawn from Psiphon Inc's own
  GitHub README (primary) + Wikipedia (secondary, cited to Citizen Lab).
- Domain-fronting relationship to current Psiphon: Low confidence — context only; not confirmed whether
  Psiphon uses fronting today.
- Exact obfuscation/protocol list: GAP (FAQ bodies JS-rendered, not retrieved). Do not assert.
- Citizen Lab specific Psiphon research: GAP (site search JS-rendered). If a deep technical audit is
  later required, target Psiphon-Labs/psiphon-tunnel-core README + any Citizen Lab publication directly.

This review is a technology-understanding artifact. It is NOT Nidaa evidence, NOT an A6b input, and NOT
a feature/architecture decision. It answers only: "is Psiphon relevant enough to stay on the watchlist?"
Answer: yes, as an adjacent reference / out-of-scope technology — not as an infrastructure component.

END OF PSIPHON WATCHLIST REVIEW.
