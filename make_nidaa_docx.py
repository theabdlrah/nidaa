from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# ---- base styles ----
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)

# RTL on the whole document (Arabic + Latin mix)
sect = doc.sections[0]
sectPr = sect._sectPr
bidi = OxmlElement("w:bidi")
sectPr.append(bidi)

TEAL = RGBColor(0x0F, 0x76, 0x6E)
DARK = RGBColor(0x11, 0x18, 0x27)
MUTED = RGBColor(0x6B, 0x72, 0x80)


def add_heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = TEAL if level <= 1 else DARK
        run.font.name = "Calibri"
    return h


def add_para(text, italic=False, bold=False, color=None, size=11):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = italic
    r.bold = bold
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color
    # RTL run property so Arabic renders correctly
    rPr = r._element.get_or_add_rPr()
    rtl = OxmlElement("w:rtl")
    rPr.append(rtl)
    return p


def add_bullets(items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(it)
        rPr = r._element.get_or_add_rPr()
        rPr.append(OxmlElement("w:rtl"))


# ===== Title =====
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
tr = title.add_run("Nidaa (نداء)")
tr.bold = True
tr.font.size = Pt(26)
tr.font.color.rgb = TEAL

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sr = sub.add_run("An Offline-First Community Coordination Board for Conflict- and Crisis-Affected Populations")
sr.font.size = Pt(13)
sr.italic = True
sr.font.color.rgb = MUTED

meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
mr = meta.add_run("A project journal — abstract through purpose, uniqueness, and field intent\n"
                  "Author: Abdul Rahman (@theabdlrah)  ·  Repository: github.com/theabdlrah/nidaa\n"
                  "Status: Working prototype (offline-first PWA, Arabic-RTL)  ·  Also applicable to: Gaza")
mr.font.size = Pt(9.5)
mr.font.color.rgb = MUTED
mrPr = mr._element.get_or_add_rPr()
mrPr.append(OxmlElement("w:rtl"))

doc.add_paragraph()

# ===== 1. Abstract =====
add_heading("1. Abstract", 1)
add_para(
    "Nidaa (نداء — \"call\" or \"appeal\") is an offline-first, Arabic-first community coordination "
    "board designed for populations living under constrained or destroyed connectivity. Unlike "
    "conventional web platforms that assume a stable internet connection, Nidaa treats the device "
    "as the source of truth: a new post is written to local storage first and synchronized to a "
    "server only when a connection becomes available. The application shell is cached by a service "
    "worker, so the board remains fully usable — browse, read, and compose — with zero connectivity "
    "after the first visit."
)
add_para(
    "The problem Nidaa addresses is not \"lack of an app\"; it is that the people who most need "
    "coordination (displaced families, local committees, volunteers, under-resourced clinics) are "
    "precisely the ones for whom online-only tools fail. By inverting the normal model — offline by "
    "default, online when possible — Nidaa stays operational through internet shutdowns, damaged "
    "infrastructure, and slow or expensive mobile data."
)

# ===== 2. Context & Motivation =====
add_heading("2. Context & Motivation", 1)
add_para("Current conditions in Syria (2025) define the design constraints directly:")
add_bullets([
    "~64% of the population is effectively offline; internet penetration is only ~35.8% (9.01M users of 25.2M people).",
    "Median mobile download speed is ~12.7 Mbps, intermittent and costly.",
    "Roughly half of all hospitals, schools, and water systems are severely damaged or destroyed (WHO, 2025).",
    "A new interim government and a national digital-transformation strategy to 2030 signal appetite for digital public services — but the field reality remains low-connectivity and device-constrained.",
])
add_para(
    "These are not edge cases; they are the baseline. Any tool that cannot function under them is, in "
    "practice, unavailable to the people it claims to serve. The same baseline describes Gaza, where "
    "connectivity is repeatedly severed, civilian infrastructure is devastated, and coordination of aid, "
    "medical care, and family reconnection happens under extreme disruption. Nidaa's architecture is "
    "purpose-built for exactly this class of environment, which is why the design transfers directly."
)

# ===== 3. Purpose =====
add_heading("3. Purpose", 1)
add_para(
    "Nidaa exists to let a community self-coordinate local needs and resources without depending on "
    "central infrastructure or constant connectivity. Concretely, it enables:"
)
add_bullets([
    "Discovery — browsing community needs and offers (medical, food, water, shelter, education, transport, other) by city.",
    "Local posting under any condition — a volunteer or committee member can post while offline; the entry is queued on-device and pushed automatically on reconnect.",
    "Trust signals — entries can be marked verified by trusted NGOs/admins, so unverified community reports are visibly distinguished from confirmed ones.",
    "Resilience by default — online/offline and pending-sync status are always shown; no action is ever lost because the network dropped.",
])
add_para(
    "The intent is not to replace national humanitarian information systems (e.g. Sahana EDEN, UN "
    "coordination platforms). Those serve a different scale. Nidaa is the neighborhood-level board — "
    "lightweight, owned by the community, and survivable when everything else goes dark."
)

# ===== 4. Why Unique =====
add_heading("4. Why This Application Is Unique", 1)
add_para(
    "Most existing tools in this space fall into two camps, and Nidaa sits deliberately between and "
    "apart from them:"
)
add_bullets([
    "Heavy national IMS platforms (Sahana EDEN, HDX pipelines) are powerful but require training, connectivity, and institutional backing a local committee does not have.",
    "Offline first-aid / EMR tools (ReliefGPT, QuickAid, Project Buendia) solve specific medical scenarios and carry liability constraints.",
])
add_para("Nidaa's distinct contribution is the offline-first community board — a general, low-friction coordination surface that:")
add_bullets([
    "Runs on cheap Android devices as an installable PWA — no app-store friction, no native build.",
    "Is Arabic-RTL first, not a translated afterthought.",
    "Guarantees no data loss on disconnect via local-first write + retry sync.",
    "Uses zero native dependencies on the server (a JSON store) so it deploys anywhere Node runs — and the API shape already supports upgrading to Postgres.",
    "Is buildable and auditable by a small team, which matters for trust in sensitive contexts.",
])
add_para(
    "The uniqueness is architectural, not feature-count: it assumes the network will fail, and is "
    "correct anyway."
)

# ===== 5. What We Are Looking For =====
add_heading("5. What We Are Looking For", 1)
add_para(
    "Nidaa is a prototype, not a deployed service. To move from prototype to something a community can "
    "rely on, we are explicitly looking for:"
)
add_bullets([
    "Verified data sources. Seed data today is illustrative only. Real value requires NGO- and committee-sourced, fact-checked entries — not scraped or assumed information.",
    "Authentication & role-gated verification. The /api/verify route is open in the prototype. In production it must be behind auth so only trusted actors can mark entries verified (prevents misinformation / manipulation).",
    "Offline maps. Coordinates are stored; the next layer is Leaflet with offline-capable tiles so locations render without a live connection.",
    "Field testing. The only real validation is use by an actual committee or volunteer network under real conditions — including Gaza.",
    "Privacy & safeguarding. Especially if extended toward sensitive categories (e.g. family reconnection), strong privacy and consent controls are mandatory, not optional.",
])
add_para(
    "We are not looking to build a surveillance-adjacent or data-extractive tool. The model is "
    "local-first, community-owned, and resilient against interception."
)

# ===== 6. Gaza =====
add_heading("6. Applicability to Gaza", 1)
add_para(
    "Gaza is the clearest sibling deployment of this design. The constraints Nidaa was built around — "
    "severed connectivity, devastated infrastructure, urgent need for local coordination of aid, "
    "medical care, water, and shelter, and a predominantly Arabic-speaking population — are present "
    "there in acute form."
)
add_para("Nidaa's transfer to Gaza requires no architectural change; it requires:")
add_bullets([
    "Gaza-specific seed/verified data from trusted local actors.",
    "Arabic (and where useful, bidirectional) content.",
    "Offline map tiles for the local geography.",
    "The same auth/verification hardening described above.",
])
add_para(
    "The same codebase can serve both Syria and Gaza as region-scoped instances, sharing the "
    "offline-first core while differing only in data and localization."
)

# ===== 7. Limitations =====
add_heading("7. Honest Limitations (stated up front)", 1)
add_bullets([
    "Seed content is illustrative, not operational.",
    "The verification endpoint is open in this build and must be secured.",
    "The server store is a JSON file (chosen for zero-dependency portability); scale demands Postgres.",
    "No live map rendering yet; coordinates only.",
    "This is a portfolio / learning prototype demonstrating offline-first architecture for constrained-connectivity humanitarian contexts.",
])

# ===== 8. Phased Build Plan =====
add_heading("8. Phased Build Plan", 1)
add_para(
    "The roadmap from prototype to a field-usable tool. Each phase ends with a verification gate "
    "that must pass before the next begins. Research basis: HDX (236 Syria datasets, including 3,060 "
    "real health facilities as GeoJSON), ReliefWeb API v2 (live, free), Auth.js v5, better-sqlite3, "
    "and Leaflet offline. Guiding principle: the network will fail, and the tool must be correct anyway."
)

add_heading("Phase 0 — Harden & Verify Baseline (prerequisite)", 2)
add_para(
    "Lock the prototype with a real API test (GET returns array, POST creates, verify flips flag). "
    "Gate: build green; API smoke test passes; Arabic round-trip OK.", italic=False)

add_heading("Phase 1 — Real Seed Data from HDX  (highest impact, lowest effort)", 2)
add_para(
    "Replace illustrative seeds with verified, real Syrian (then Gaza) data. A scripts/import-hdx.ts "
    "downloader maps OSM amenities to Nidaa categories and upserts them as verified 'offer' entries: "
    "Health Facilities of Syria (3,060 rows, Arabic+English names, geometry), then Education "
    "Facilities, Waterways, and IDP Sites. A 'region' field (syr | gza) enables multi-region scoping."
)
add_para("Gate: importer run populates the board; a known facility (مستشفى درعا الوطني) is present and searchable by city.", italic=True, color=MUTED, size=10)

add_heading("Phase 2 — Offline Maps (Leaflet + cached tiles)", 2)
add_para(
    "Add Leaflet (client-only, dynamic import) and cache viewed tiles in IndexedDB when online, "
    "serving them offline — only for visited areas to stay light on cheap devices. List/Map toggle; "
    "tap a card to center the map. Gaza reuses the same component."
)
add_para("Gate: map renders online; after visiting an area, going offline still shows tiles with no console errors.", italic=True, color=MUTED, size=10)

add_heading("Phase 3 — Auth + Role-Gated Verification (closes security gap)", 2)
add_para(
    "Adopt Auth.js v5 with roles (individual | volunteer | ngo | admin). POST /api/verify now "
    "requires an ngo|admin session (401 otherwise) — closing the open verify route flagged in Section 7. "
    "Local posts from unverified users stay 'unverified' until an NGO confirms. An NGO review queue "
    "lets trusted actors verify or reject with a reason."
)
add_para("Gate: unauthenticated verify → 401; ngo session → 200 and flag flips; individual → 401.", italic=True, color=MUTED, size=10)

add_heading("Phase 4 — Server Store Upgrade: JSON → SQLite", 2)
add_para(
    "Introduce better-sqlite3 (synchronous, zero-config) behind lib/store.ts with identical function "
    "signatures. Handles thousands of HDX rows and concurrent writes safely. Postgres only if "
    "multi-instance/HA is later required. Existing API shape is unchanged."
)
add_para("Gate: all Phase 1–3 behaviors pass against SQLite; bulk import of 3,060 rows completes without corruption; concurrent POSTs lose no writes.", italic=True, color=MUTED, size=10)

add_heading("Phase 5 — Sync Conflict Resolution (hard offline-first problem)", 2)
add_para(
    "Handle multiple volunteers editing the same entry offline. Server assigns the canonical id on "
    "first sync; merge rule uses updatedAt (wins), and if a client edited after its last pull the "
    "entry is flagged 'conflict' with both versions surfaced to an NGO reviewer. A sync log records "
    "each push/pull for audit."
)
add_para("Gate: two simulated offline edits to one entry are both preserved, conflict flagged, and resolvable with no data loss.", italic=True, color=MUTED, size=10)

add_heading("Stretch (post-Phase 5, optional)", 2)
add_bullets([
    "WhatsApp/SMS bridge: post needs via message (Twilio / WhatsApp Business API) — reaches the ~64% who will not install an app; handle PII carefully.",
    "Multi-region deploy: same code, region=syr|gza scoping, shared offline-first core.",
    "ReliefWeb context cards: pull v2 reports for a city as situational context.",
])

add_para(
    "Sequencing: P0 → P1 real data → P2 maps → P3 auth → P4 SQLite → P5 conflicts → stretch. The "
    "trio that moves Nidaa from fake-data prototype to real, safe, scalable tool is P1 + P3 + P4.",
    bold=True,
)

def add_code(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.font.name = "Consolas"
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x1f, 0x29, 0x37)
    # shade the paragraph
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "F2F4F7")
    pPr.append(shd)
    return p


# ===== 10. Architecture Notes: mechanism-level improvements =====
add_heading("10. Architecture Notes: Mechanism-Level Improvements", 1)
add_para(
    "Five mechanism-level upgrades move Nidaa from offline-tolerant toward offline-native. They are "
    "listed roughly in order of field impact. Items 1 and 4 include pseudocode sketches.",
)

add_heading("10.1 Device-to-device sync (the biggest gap)", 2)
add_para(
    "Current sync is device↔server only — it assumes the server is reachable when connectivity "
    "returns. But the stated worst case is a total internet shutdown, where the server is unreachable "
    "for everyone at once. Local mesh sync lets devices in the same room, building, or camp exchange "
    "posts directly over local WiFi/hotspot (WebRTC) or Bluetooth, so the community board keeps "
    "updating with zero internet. This is the difference between 'offline-tolerant' and 'offline-native.'"
)
add_para("Sketch — WebRTC data-channel gossip between peers on a local network:", bold=True)
add_code(
    "// each device runs a lightweight gossip peer\n"
    "const peer = new GossipPeer({ id: localClientId });\n"
    "\n"
    "peer.on('entry', (remote) => {\n"
    "  if (alreadyHave(remote.clientId)) return;          // idempotent\n"
    "  if (isNewer(remote, localCopy(remote.clientId))) {\n"
    "    upsertLocal(remote);                             // write to IndexedDB\n"
    "    peer.gossip(remote, { exclude: remote.from });   // forward once\n"
    "  }\n"
    "});\n"
    "\n"
    "// on reconnect, push the merged local set to the server\n"
    "window.addEventListener('online', () => pushPending());"
)

add_heading("10.2 Idempotency on retry", 2)
add_para(
    "When a queued post finally syncs and the request partially fails (times out after the server "
    "received it but before the client got the ack), a naive retry duplicates the entry. Every "
    "local-first post already carries a client-generated UUID at creation; the server must dedupe on "
    "that key (upsert by clientId). This is already implemented in lib/store.ts — it is called out "
    "here because it is the invariant that makes 10.1 and 10.5 safe under retries."
)

add_heading("10.3 Sync prioritization, not just queuing", 2)
add_para(
    "With 12.7 Mbps median and costly data, the sync queue should be priority-ordered, not FIFO: "
    "medical/urgent categories sync first; general posts batch later. Compress payloads and defer any "
    "images until the device is on WiFi (or drop them in a true blackout)."
)
add_para("Sketch — priority-ordered drain:", bold=True)
add_code(
    "const PRIORITY = { medical: 0, water: 1, shelter: 2, food: 3, education: 4, other: 9 };\n"
    "async function drain() {\n"
    "  const q = (await pendingLocal()).sort(\n"
    "    (a, b) => PRIORITY[a.category] - PRIORITY[b.category]);\n"
    "  for (const e of q) {\n"
    "    if (e.hasImage && !onWifi()) continue;            // defer heavy media\n"
    "    await postCompressed(e);                          // gzip before send\n"
    "  }\n"
    "}"
)

add_heading("10.4 Field-level conflict merge, not whole-entry flagging", 2)
add_para(
    "The Phase 5 plan flags the whole entry as 'conflict' if two people edit offline. For simple "
    "cases (one adds a phone number, another updates status) that is overkill. A field-level "
    "three-way merge resolves most conflicts automatically and only escalates true clashes (same "
    "field, different values) to an NGO reviewer."
)
add_para("Sketch — three-way field merge:", bold=True)
add_code(
    "function merge(base, local, remote) {\n"
    "  const out = { ...base };\n"
    "  const clashes = [];\n"
    "  for (const k of keys(local, remote)) {\n"
    "    if (local[k] === remote[k]) { out[k] = local[k]; }\n"
    "    else if (local[k] === base[k]) { out[k] = remote[k]; }   // only remote changed\n"
    "    else if (remote[k] === base[k]) { out[k] = local[k]; }   // only local changed\n"
    "    else clashes.push(k);                                    // both diverged -> human\n"
    "  }\n"
    "  out.clashes = clashes;                                     // [] => auto-resolved\n"
    "  return out;\n"
    "}"
)

add_heading("10.5 Decentralized trust, not single-gate verification", 2)
add_para(
    "Verification is currently binary: an NGO/admin marks an entry verified. In a real blackout the "
    "NGO account may be unreachable too — a single point of failure for trust. A lightweight "
    "corroboration model fixes this: N independent community members confirming an entry raises its "
    "trust tier even before an NGO acts. Trust becomes a gradient, not a gate, so the board stays "
    "useful when central authorities are dark."
)
add_para("Sketch — corroboration tiers:", bold=True)
add_code(
    "function trustTier(entry) {\n"
    "  const n = entry.corroborations.length;        // distinct community confirmations\n"
    "  if (entry.verifiedByNgo) return 'VERIFIED';\n"
    "  if (n >= 3) return 'CORROBORATED';\n"
    "  if (n >= 1) return 'PARTIAL';\n"
    "  return 'UNVERIFIED';\n"
    "}"
)

add_para(
    "These five are not add-ons; they complete the offline-native premise. 10.1 (mesh) is the "
    "structural one — without it, a total shutdown still blinds the board. 10.2–10.5 make retries, "
    "bandwidth, edits, and trust survive that same blackout.",
    bold=True,
)

add_heading("10.6 Advanced & Differentiating Mechanisms (push for uniqueness)", 2)
add_para(
    "The five improvements above make Nidaa offline-native. To be genuinely novel rather than a "
    "re-assembly of known parts, four mechanisms from adjacent research fields can be adopted — each "
    "is established in its own domain but essentially unused in conflict-zone coordination boards:"
)
add_bullets([
    "Signed append-only feeds (Secure Scuttlebutt / SSB pattern): instead of mutable entries, each "
    "device keeps an append-only, cryptographically signed log of its posts and edits; replication is "
    "gossip of log tails. This gives tamper-evidence and natural conflict detection for free, and "
    "needs no server. SSB itself (patchwork, 3.5k★) proves the pattern works offline — but no "
    "humanitarian board uses it. This is the deepest differentiator.",
    "CRDT field-merge (Automerge / Loro / Yjs, all >5k★): replace the hand-rolled three-way merge in "
    "10.4 with a real CRDT so concurrent offline edits to different fields merge automatically and "
    "deterministically, with no central arbitrator — the mathematical guarantee 10.4 only approximates.",
    "Geo-indistinguishable location (differential privacy, Google/Meta/IBM libs exist): when a post "
    "carries a coordinate, add calibrated noise so the true point stays within ~k meters with "
    "cryptographic guarantee, defeating location-targeting (Threat 12.1) while keeping the post useful "
    "for 'nearest aid' ranking. Turns the safety mitigation into a math property.",
    "Proof-of-personhood for sybil resistance (privacy-preserving, e.g. Anon Aadhaar / ZK): cap "
    "corroborations (10.5) per unique human, not per device/account, with a zero-knowledge proof that "
    "does not reveal identity. Closes the trust-forgery threat without a central ID authority — "
    "critical when no government is trusted.",
    "On-device LLM triage & translation (WebLLM / transformers.js, runs in-browser): a small model, "
    "downloaded once, translates posts between Arabic/English/ Ukrainian/etc. and flags urgent medical "
    "posts offline — no cloud, no data leaving the device. Unique for a crisis board and resilient to "
    "shutdown.",
])
add_para(
    "Why these raise the bar: individually each is known; combined into one offline-first, "
    "Arabic-RTL, trust-decentralized board, they push Nidaa from 'a competent offline app' toward a "
    "genuinely novel coordination primitive. The SSB-style signed-feed + CRDT-merge pair, in "
    "particular, is the technical heart that would make 'first-in-combination' a real claim, not a "
    "marketing one.",
    bold=True,
)

# ===== 11. Competitive Landscape — are we first? =====
add_heading("11. Competitive Landscape — Are We First?", 1)
add_para(
    "An exhaustive scan (GitHub repository search + humanitarian-OSS landscape, July 2026) to test the "
    "'we might be first' question. Important framing: the authors are NOT from Syria or Gaza. Nidaa is "
    "therefore scoped as a GENERALIZABLE offline-first humanitarian board — Syria/Gaza are the first "
    "deployment targets, not the only ones. The 'first' claim must therefore hold across ALL conflict "
    "and crisis regions (Ukraine, Sudan, Myanmar, Haiti, Yemen, Afghanistan, plus natural disasters), "
    "not two. The scan below covers exactly that."
)
add_para("What exists today (the real neighbors, by evidence):", bold=True)
add_bullets([
    "crisis-mesh-messenger (192★, active Oct 2025) — decentralized, infrastructure-free MESSAGING via Bluetooth/WiFi Direct, E2E-encrypted. Solves communication when infra fails. But it is chat, NOT a coordination board: no needs/offers posts, no verification, no map, no Arabic.",
    "HTBox/allReady (885★, but last push 2022) — disaster PREPAREDNESS campaigns for orgs. Not conflict-zone, not Arabic, not offline-first board.",
    "melizeche/ayudapy (118★, active) — Spanish 'help people help people' platform. Peacetime mutual aid, not conflict/offline.",
    "Sahana Eden (409★) — national-scale IMS. Needs institutional backing a local committee lacks.",
    "Kiwix (1,382★) / Rushlight — offline CONTENT (Wikipedia, maps), not live coordination.",
    "HotOSM MapSwipe (170★) / fAIr (137★) — crowdsourced MAPPING, not posting/coordination.",
    "Mutual-aid OSS (factn/resilience-app 85★, rubyforgood/mutual-aid 55★, Crown Heights 26★) — peacetime community organizing, online-only.",
    "Disaster-response AI repos (Gemma/CRISIS-AI etc.) — all 2–13★ hackathon projects, none mature, none Arabic boards.",
])
add_para(
    "Targeted negative evidence (what does NOT exist):", bold=True
)
add_bullets([
    "\"mutual aid / needs board / community board + offline\" → 0 GitHub results. No public OSS project combines those exact concepts.",
    "Arabic-RTL + refugee/aid/offline search → 1 result, and it is a UNHCR refugee-treaty DOC TEMPLATE (1★). No Arabic-RTL humanitarian coordination board exists on GitHub.",
    "Region-specific crisis boards (Ukraine, Haiti, Myanmar, Sudan, Yemen) → none found; Ukraine tech is cybersecurity (uashield 1,077★) and dev tooling, not civilian coordination.",
    "Mesh + coordination (not just messaging) → only 12★ hobby repos (Relief-Mesh, THOR); none matured into boards.",
])
add_para(
    "Verdict: Nidaa is not 'first' in the abstract — offline sync, mesh messaging, aid boards, and "
    "Arabic i18n all exist separately (crisis-mesh-messenger proves mesh-for-crisis is real and "
    "valuable). But the specific COMBINATION it targets — an offline-first, Arabic-RTL community "
    "needs-&-offers BOARD, seeded with real HDX facility data, with mesh sync (Phase 6), decentralized "
    "trust (10.5), and a written threat model (12) — does not appear to exist as a public, deployable "
    "tool in ANY conflict/crisis region. Nearest neighbors are either messaging-only (crisis-mesh-"
    "messenger) or peacetime mutual aid (ayudapy, allReady). So the honest, defensible claim is: "
    "first-in-combination, not first-in-principle — and the gap is wide enough that execution, not "
    "novelty, is the real risk. The multi-region scan (not just Syria/Gaza) strengthens this claim "
    "rather than weakens it: the absence is global, not regional.",
    bold=True,
)

# ===== 12. Threat Model & Do-No-Harm =====
add_heading("12. Threat Model & Do-No-Harm", 1)
add_para(
    "A coordination board in a conflict zone is a dual-use system: it helps civilians find aid, but "
    "the same board can be weaponized — false posts can misdirect or trap, location data can be used "
    "to target, and a 'verified' label can be forged to manufacture trust. Section 10.5 (decentralized "
    "trust) reduces single-point capture but also lowers the bar for bad actors to seed plausible "
    "lies. This section is the deliberate counterweight. It is written before scale, because retrofitting "
    "safety into a trusted tool is far harder than designing for it."
)

add_heading("12.1 Threats", 2)
add_bullets([
    "Misinformation / entrapment: a falsified 'shelter' or 'aid point' post draws civilians to a location. Highest harm, easiest to execute.",
    "Surveillance / targeting: posted coordinates, contact numbers, and movement patterns can be harvested by hostile actors to target aid seekers or volunteers.",
    "Trust forgery: in decentralized trust (10.5), sybil accounts mass-corroborate a fake entry to push it to CORROBORATED/VERIFIED tier.",
    "Denial of service: floods of junk posts bury real needs; mesh forwarding (10.1) can amplify a spam storm across devices.",
    "Server / NGO account compromise: a captured admin account flips verifies en masse or deletes real entries.",
    "Device seizure: a confiscated phone reveals a user's posting history and contacts if stored in the clear.",
])

add_heading("12.2 Mitigations (by design, not afterthought)", 2)
add_bullets([
    "On-device encryption at rest (IndexedDB/OPFS) so a seized device does not leak history (Amplified Access field principle).",
    "No mandatory PII: contact fields are optional; default posts carry no phone/location unless the author chooses. Location shown at city granularity, not street.",
    "Rate-limit + proof-of-work on post creation to blunt spam floods and sybil corroboration.",
    "Corroboration weighting: require distinct device/network fingerprints (not just accounts) for trust tiers; cap one corroboration per device.",
    "Audit log + reversible verifies: every verify/corroboration is logged with actor + time; a compromised admin's actions are visible and revertible.",
    "Mesh forwarding caps (10.1): max hops + duplicate suppression so a spam storm cannot loop forever across the local network.",
    "Clear 'unverified = unconfirmed' UI language so users never treat an unverified post as fact (already in the card design).",
])

add_para(
    "Do-no-harm principle: when a feature trades off safety against convenience (e.g. precise "
    "locations, open posting, lightweight auth), the default MUST favor safety. Nidaa is a civilian "
    "aid tool; it must never become a targeting or misinformation vector. The verification endpoint "
    "(Section 7) and decentralized trust (10.5) are explicitly gated behind this threat model.",
    bold=True,
)

# ===== 13. Conclusion =====
add_heading("13. Conclusion", 1)
add_para(
    "Nidaa is built on a single, defensible principle: the people who need coordination most are the "
    "ones with the least connectivity, so the tool must work without it. By making the device the "
    "source of truth and the network an opportunistic extra, Nidaa stays useful through shutdowns, "
    "damage, and intermittent service — in Syria today, and in Gaza tomorrow."
)
add_para(
    "The path forward is not more features; it is trust, verification, and field use. Those are the "
    "gaps between a working prototype and a tool a community can depend on."
)

# ===== footer note =====
doc.add_paragraph()
fn = doc.add_paragraph()
fr = fn.add_run(
    "Build verification: npm run build passes; runtime API verified (GET/POST/verify, Arabic UTF-8 "
    "round-trip confirmed). Repo: github.com/theabdlrah/nidaa."
)
fr.italic = True
fr.font.size = Pt(9)
fr.font.color.rgb = MUTED
frPr = fr._element.get_or_add_rPr()
frPr.append(OxmlElement("w:rtl"))

out = r"C:\Users\theab\Desktop\Nidaa-Journal.docx"
doc.save(out)
print("saved:", out)
