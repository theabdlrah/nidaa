# Nidaa — Day Log Template (E1 deliverable, Day 8)

Type: STANDARDIZED daily continuity log. Use for every Nidaa day-log so NIDAA-LOAD
stays fast and desync is caught early. Replace <PLACEHOLDERS>. Do NOT modify A6b/
G1/G2/OQ status here — only record deltas; the source-of-truth artifacts hold
canonical status.

==================================================================
DATE: <YYYY-MM-DD>   DAY: <N>   AUTHOR: <who>
==================================================================

STATE DELTA (vs last load — what CHANGED today, bullet form)
- <new contact reached / replied>
- <new evidence row added (G1/G2)>
- <new referral>
- <dispatch verified / still-unconfirmed>
- <desync found & flagged>

EVIDENCE (observed, sourced — not analysis)
- <source, org, role, what they said verbatim-ish, case type, confidence>
- (If none: write "NONE — monitoring day.")

HYPOTHESES (testable claims; status unchanged unless new evidence)
- A6b: Conditional (Medium) — per canonical v1.0 (docs/Nidaa-Day10-A6b-Canonical-v1.0.md) — <any nuance>
- (No new hypotheses created.)

ASSUMPTIONS (held pending evidence; none promoted to conclusions)
- <list; if unchanged, write "No change.">

OPEN QUESTIONS (genuine uncertainty; status)
- OQ-1 (acute/protracted): OPEN <+ pressure note>
- OQ-2 (formal fail/coexist): OPEN <+ pressure note>
- OQ-3 (G1 missing): OPEN
- OQ-4 (G2 missing): OPEN

DISPATCH EVENTS (new today — MANDATORY: log every send the moment it happens)
| Timestamp | Contact | Channel | Status |
| <YYYY-MM-DD> | <name> | Email/LinkedIn/form/DM | prepared/sent-unconfirmed/sent-verified/bounced |
RULE: No outreach is considered complete until a dispatch event exists here.
"Send occurred -> reality changed -> artifacts did not" is the Mohammed failure
mode (Day 8). Recording the send at dispatch time is what closes the
reality->artifact loop; D1 (nidaa-artifact-sync) only catches what is written down.

DISPATCH AUDIT (every named contact — send-state enum)
| Contact | Sent? | Date | Channel | Response | Ledger status |
| <name>  | prepared/sent-unconfirmed/sent-verified/bounced | <d> | <ch> | none/reply | <status> |
FLAG: any row "prepared" or "sent-unconfirmed" = unknown-status, NOT reached.

REFERRAL DELTA (new this day)
| Referrer | Referred | Confirmed/Potential | Contacted? | Status |
| <name>   | <name>   | C / P                | Y/N/U     | <note> |

DESYNC REGISTER (contradictions vs source-of-truth — must be resolved, not hidden)
- <artifact A says X; artifact B says Y — flag for user verification>

NEXT HIGHEST-VALUE ACTION (one)
- <the single move that reduces the most uncertainty; usually a practitioner case
  via the six-question gate, or a falsification run on the weakest OQ>

EVIDENCE LAYER (unchanged unless a case closed a gap)
| A6b | G1 | G2 | Indep. corrob. | Disconfirming | OQ-1 | OQ-2 | Validation |
| Plausible | Missing | Missing | n=1 (Aaron) | Missing | Open | Open | Not achieved |
