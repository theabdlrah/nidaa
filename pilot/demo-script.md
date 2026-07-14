# Nidaa — 90-Second Demo Video Script

Goal: prove the survival property in 90 seconds — "Nidaa stays usable when connectivity doesn't."

## Scene 1 — Online (0:00–0:10)
[Internet ON. Phone screen. Open Nidaa PWA.]
"Here's Nidaa — an offline-first coordination board for communities under
connectivity stress. Let's go offline and keep using it."
Show the board populating with real, region-filtered entries.

## Scene 2 — Offline post (0:10–0:30)
[Enable Airplane Mode. OS indicator shows no signal.]
"Now airplane mode — no internet at all."
Tap "New post" → choose type "need" → category "medical" → city → Arabic + English title.
Submit.
On-screen badge: **"Saved locally — will sync when connection returns."**
"Nothing lost. The post lives on the device."

## Scene 3 — Offline browse (0:30–0:50)
[Still airplane mode. Scroll the board. Open an entry. Switch to the map.]
"While offline I can still browse every saved entry, read details, and view the map.
The board is fully usable — it just can't reach the server yet."

## Scene 4 — Sync on reconnect (0:50–1:10)
[Disable Airplane Mode. Connection returns.]
"Internet's back. Watch."
The locally-saved post animates to "Synced." Pull the board — the entry now appears
server-side. "Zero data loss. The network dropped; the post didn't."

## Scene 5 — Verify (1:10–1:30)
[Switch to a Verifier account. Open the post. Tap "Verify."]
"A trusted verifier confirms it. The entry now shows a verified trust mark;
unverified posts stay clearly unconfirmed."
[Hold on the verified badge.]
"Nidaa remains usable even when connectivity doesn't."

## Production notes
- Record on a real Android phone, screen + tap. Arabic UI visible.
- Keep text overlays minimal; show the "Saved locally" and "Synced" badges prominently.
- No ffmpeg needed; use the phone's built-in screen recorder, then trim to 90s.
- If a verifier login UI isn't wired yet, show the verified state via the secured
  endpoint call in a short inset, and note UI login is the next pilot prerequisite.
