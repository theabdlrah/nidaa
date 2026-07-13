@echo off
cd /d "%~dp0"
echo Starting Nidaa (ndaa) — offline-first Syria community board...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" http://localhost:3000
npm run start
