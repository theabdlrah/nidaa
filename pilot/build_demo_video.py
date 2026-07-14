#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nidaa — operational partner video (Palantir/NYT-inspired, camera-free).

Spec (from creative brief):
  * 85–95s total, portrait 1080x1920.
  * 0:00–0:12  silent open: dark Gaza map, offline indicator, cursor, first post.
                On-screen line: "Coordination cannot depend on connectivity."
  * 0:12–~1:22 calm English VO (edge-tts AriaNeural), Arabic+English burned subs.
  * End card (silent): "Coordination survives the blackout." + Nidaa wordmark.
  * Map = protagonist, but COORDINATION/VERIFICATION language, NOT surveillance.
  * Visible actions: offline -> submit -> stays available -> reconnect -> sync ->
    verify (unverified->verified) -> audit entry. Slow, deliberate, one sentence
    on screen at a time. No military/radar/targeting aesthetics. No dramatic music.
  * Reproducible; no camera, no browser, no live API. Real Gaza facility names
    from data/db.json; pins anchored to real Gaza districts (stylized, not surveyed).
"""
import json, os, math, asyncio, tempfile, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import edge_tts
import imageio_ffmpeg

ROOT = r"C:\Users\theab\nidaa"
OUT  = os.path.join(ROOT, "pilot", "demo-video.mp4")
W, H = 1080, 1920
FPS  = 30
TOTAL = 92.0  # seconds

# ---- palette: operational navy/teal (from manifest #0f172a / #0f766e) ----
NAVY   = "#0b1220"
NAVY2  = "#0f172a"
PANEL  = "#111a2b"
INK    = "#e6edf6"
MUTED  = "#8da2bd"
TEAL   = "#0f766e"
TEAL_L = "#5eead4"
LINE   = "#1e2d44"
PIN    = "#38bdf8"
OK     = "#34d399"
WARN   = "#fbbf24"
BAD    = "#f87171"
AMBER  = "#f59e0b"

FONT = r"C:\Windows\Fonts"
def f(p, s): return ImageFont.truetype(os.path.join(FONT, p), s)
F_EN  = "segoeui.ttf"
F_EN_B= "segoeuib.ttf"
F_EN_L= "segoeuil.ttf"
F_AR  = "segoeui.ttf"     # Segoe UI renders Arabic; GARABD tofu'd in PIL
F_AR_B= "segoeuib.ttf"

# ---- real Gaza facility names + districts (stylized coordinates) ----
with open(os.path.join(ROOT, "data", "db.json"), encoding="utf-8") as fh:
    DB = json.load(fh)
gza = [e for e in DB["entries"] if e.get("region") == "gza"]
FAC = [e["titleAr"] for e in gza if e.get("titleAr")][:40]

# Gaza districts (lat, lon) — anchor points for a stylized relief map
DISTRICTS = {
    "Gaza City":   (31.5017, 34.4668),
    "Khanyounis":  (31.3400, 34.3060),
    "Rafah":       (31.2900, 34.2500),
    "Deir al Balah":(31.4167, 34.3500),
    "Beit Lahia":  (31.5450, 34.5030),
    "Jabalia":     (31.5230, 34.4850),
}
# map lon/lat -> screen (portrait, Gaza fills frame with margin)
LON_MIN, LON_MAX = 34.20, 34.55
LAT_MIN, LAT_MAX = 31.25, 31.58
MAP_X0, MAP_X1 = 70, W-70
MAP_Y0, MAP_Y1 = 360, 1240
def proj(lon, lat):
    x = MAP_X0 + (lon - LON_MIN)/(LON_MAX - LON_MIN) * (MAP_X1 - MAP_X0)
    y = MAP_Y1 - (lat - LAT_MIN)/(LAT_MAX - LAT_MIN) * (MAP_Y1 - MAP_Y0)
    return x, y

# pick a real Gaza facility to verify
VERIFY_FAC = FAC[0] if FAC else "صيدلية د. سامح"
VERIFY_DIST = "Khanyounis"
VLON, VLAT = DISTRICTS[VERIFY_DIST]

# audio helpers ----------------------------------------------------------------
def tone(freq, dur, sr=44100, vol=0.18, fade=0.02):
    t = np.linspace(0, dur, int(sr*dur), False)
    env = np.ones_like(t)
    f = int(sr*fade); 
    if f>1:
        env[:f] = np.linspace(0,1,f); env[-f:] = np.linspace(1,0,f)
    s = vol*np.sin(2*np.pi*freq*t)*env
    return (s*32767).astype(np.int16)

def write_wav(path, s, sr=44100):
    import struct
    with open(path,"wb") as w:
        w.write(b"RIFF"); w.write(struct.pack("<I",36+len(s)*2)); w.write(b"WAVE")
        w.write(b"fmt "); w.write(struct.pack("<IHHIIHH",16,1,1,sr,2*sr,2,16))
        w.write(b"data"); w.write(struct.pack("<I",len(s)*2)); w.write(s.tobytes())

def mix(seg):  # seg: list of np.int16 at sr=44100
    m = np.concatenate(seg) if seg else np.zeros(1,np.int16)
    return np.clip(m,-32767,32767).astype(np.int16)

# Ambient: low drone + slow LFO, ~total seconds
def ambient(total, sr=44100):
    n = int(sr*total)
    t = np.arange(n)/sr
    base = 0.05*(np.sin(2*np.pi*55*t) + 0.6*np.sin(2*np.pi*82.5*t))
    lfo = 0.02*np.sin(2*np.pi*0.07*t)
    s = (base+lfo)*np.hanning(n)*0.9
    return (s*32767).astype(np.int16)

# Draw helpers ----------------------------------------------------------------
def rounded(d, box, r, fill=None, outline=None, width=2):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

import arabic_reshaper, bidi.algorithm
def ar(s):
    """Proper RTL shaping for Arabic in PIL (fixes mirrored/glyph-order bugs)."""
    try:
        return bidi.algorithm.get_display(arabic_reshaper.reshape(s))
    except Exception:
        return s

def text_ar(d, s, pos, size, fill, anchor="mm", bold=False):
    d.text(pos, ar(s), font=f(F_AR_B if bold else F_AR, size), fill=fill, anchor=anchor)

def text_en(d, s, pos, size, fill, anchor="mm", bold=False, light=False):
    d.text(pos, s, font=f(F_EN_B if bold else (F_EN_L if light else F_EN), size), fill=fill, anchor=anchor)

def one_line(d, en, ar, en_y=H-120, ar_y=H-180, size_en=34, size_ar=40):
    """Exactly one sentence on screen: Arabic above, English below (burned subs)."""
    text_ar(d, ar, (W//2, ar_y), size_ar, INK, anchor="mm", bold=True)
    text_en(d, en, (W//2, en_y), size_en, MUTED, anchor="mm", light=True)

def top_title(d, s, sub=None):
    d.rectangle([0,0,W,140], fill=NAVY2)
    text_en(d, s, (W//2, 64), 30, INK, anchor="mm", bold=True)
    if sub:
        text_en(d, sub, (W//2, 104), 18, MUTED, anchor="mm", light=True)

def status_pill(d, x, y, label, color):
    w = 60 + len(label)*15
    rounded(d, [x, y, x+w, y+46], 23, fill=color)
    text_en(d, label, (x+w//2, y+23), 22, "#0b1220", anchor="mm", bold=True)

def indicator(d, x, y, on, label):
    col = OK if on else BAD
    d.ellipse([x, y, x+22, y+22], fill=col)
    text_en(d, label, (x+34, y+11), 22, INK if on else BAD, anchor="lm")

def map_base(d, zoom=1.0, pan=(0,0)):
    # panel
    rounded(d, [40, 320, W-40, 1280], 18, fill=PANEL, outline=LINE, width=2)
    # subtle grid
    for gx in range(int(MAP_X0), int(MAP_X1), 70):
        d.line([(gx, MAP_Y0), (gx, MAP_Y1)], fill=LINE, width=1)
    for gy in range(int(MAP_Y0), int(MAP_Y1), 70):
        d.line([(MAP_X0, gy), (MAP_X1, gy)], fill=LINE, width=1)
    # stylized coastline (Gaza strip - simplified, friendly, NOT military)
    coast = [(MAP_X0, MAP_Y0+40),(340, 560),(520, 760),(700, 980),(MAP_X1, 1180)]
    d.line(coast, fill="#27405e", width=3, joint="curve")
    # region label
    text_en(d, "GAZA", (W//2, 340), 18, MUTED, anchor="mm", light=True)

def pin(d, lon, lat, state, r=26, pulse=0.0, label=None):
    x, y = proj(lon, lat)
    if pulse>0:
        d.ellipse([x-(r+14)*pulse, y-(r+14)*pulse, x+(r+14)*pulse, y+(r+14)*pulse],
                  outline=PIN, width=2)
    col = {"unverified": WARN, "verified": OK, "pending": MUTED}[state]
    d.ellipse([x-r, y-r, x+r, y+r], fill=col)
    d.ellipse([x-7, y-7, x+7, y+7], fill="#0b1220")
    if label:
        text_ar(d, label, (x, y-r-26), 26, INK, anchor="mm", bold=True)

# scene functions: return list of (start,end,draw_fn(t_local)) ----------------
def bg():
    img = Image.new("RGB",(W,H), NAVY)
    d = ImageDraw.Draw(img)
    return img, d

def ease(t): return t*t*(3-2*t)

# --- Scene 1: silent open 0..12 ---
def sc1(d, t):
    top_title(d, "NIDAA", "coordination under unreliable connectivity")
    map_base(d)
    # district pins (muted) fade in
    for i,(name,(la,lo)) in enumerate(DISTRICTS.items()):
        a = min(1, max(0, t-1.0-i*0.6)/1.2)
        if a>0:
            pin(d, lo, la, "pending", r=16, label=None)
    # offline indicator appears ~3s
    if t>3:
        indicator(d, 70, 150, False, "OFFLINE")
    # cursor + first post ~6s
    if t>6:
        cx, cy = proj(VLON, VLAT)
        # device card
        rounded(d, [W//2-260, 1330, W//2+260, 1460], 14, fill=PANEL, outline=LINE)
        text_ar(d, VERIFY_FAC[:18], (W//2, 1370), 26, INK, anchor="mm", bold=True)
        text_en(d, "new entry · saved locally", (W//2, 1420), 20, MUTED, anchor="mm", light=True)
        # cursor dot moving to pin
        cp = min(1,(t-6)/2.0)
        cur = (W//2, 1330+(cy-(1330))*ease(cp))
        d.ellipse([cur[0]-10,cur[1]-10,cur[0]+10,cur[1]+10], fill=TEAL_L)
    # title line bottom
    one_line(d, "Coordination cannot depend on connectivity.",
                "لا يمكن للتنسيق أن يعتمد على الاتصال.", en_y=H-130, ar_y=H-195, size_en=36, size_ar=42)

# --- Scene 2: record offline ~12..24 ---
def sc2(d, t):
    top_title(d, "RECORD OFFLINE", None)
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=16)
    indicator(d, 70, 150, False, "OFFLINE")
    pin(d, VLON, VLAT, "unverified", r=24)
    # local save card
    rounded(d, [W//2-300, 1330, W//2+300, 1480], 14, fill=PANEL, outline=LINE)
    text_ar(d, VERIFY_FAC[:18], (W//2, 1375), 28, INK, anchor="mm", bold=True)
    text_en(d, "saved on device · no network required", (W//2, 1428), 20, MUTED, anchor="mm", light=True)
    text_en(d, "● stored locally", (W//2, 1462), 18, OK, anchor="mm")
    one_line(d, "Information can be recorded and organized without the network.",
                "يمكن تسجيل المعلومات وتنظيمها دون اتصال.", size_en=33, size_ar=40)

# --- Scene 3: stays available ~24..36 ---
def sc3(d, t):
    top_title(d, "REMAINS AVAILABLE", None)
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=16)
    indicator(d, 70, 150, False, "OFFLINE")
    pin(d, VLON, VLAT, "unverified", r=24)
    # list of two entries still visible
    for i,en in enumerate(["متاح محلياً","متاح محلياً"]):
        y0 = 1330 + i*70
        rounded(d, [W//2-300, y0, W//2+300, y0+56], 12, fill=PANEL, outline=LINE)
        text_ar(d, (VERIFY_FAC if i==0 else FAC[2])[:18], (W//2-150, y0+28), 22, INK, anchor="lm", bold=True)
        text_en(d, en, (W//2+260, y0+28), 18, OK, anchor="rm")
    one_line(d, "Changes remain available locally until connectivity returns.",
                "تبقى التغييرات متاحة محلياً حتى عودة الاتصال.", size_en=33, size_ar=40)

# --- Scene 4: reconnect + sync ~36..52 ---
def sc4(d, t):
    top_title(d, "SYNCHRONIZE", None)
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=16)
    # connectivity returns at 38
    on = t>2
    indicator(d, 70, 150, on, "ONLINE" if on else "OFFLINE")
    # sync sweep
    if on:
        sw = min(1,(t-2)/4.0)
        sx = MAP_X0 + sw*(MAP_X1-MAP_X0)
        d.line([(sx,MAP_Y0),(sx,MAP_Y1)], fill=TEAL_L, width=4)
        pin(d, VLON, VLAT, "unverified", r=24, pulse=1-sw)
    else:
        pin(d, VLON, VLAT, "unverified", r=24)
    rounded(d, [W//2-300, 1330, W//2+300, 1460], 14, fill=PANEL, outline=LINE)
    text_en(d, "updates synchronized automatically", (W//2, 1375), 22, OK, anchor="mm", bold=True)
    text_en(d, "zero data loss", (W//2, 1422), 20, MUTED, anchor="mm", light=True)
    one_line(d, "When a connection is restored, updates synchronize automatically.",
                "عند استعادة الاتصال، تتم مزامنة التحديثات تلقائياً.", size_en=33, size_ar=40)

# --- Scene 5: verification (slow) ~52..74 ---
def sc5(d, t):
    top_title(d, "VERIFICATION", "controlled · auditable · reversible")
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=16)
    indicator(d, 70, 150, True, "ONLINE")
    # phase: 52-58 unverified; 58-66 transition; 66-74 verified
    if t < 6:
        st = "unverified"
    elif t < 12:
        st = "verified"  # snaps after a deliberate beat
    else:
        st = "verified"
    # verifier badge
    rounded(d, [W//2-180, 1330, W//2+180, 1400], 12, fill="#0c2a24", outline=OK)
    text_en(d, "VERIFIER", (W//2, 1365), 22, OK, anchor="mm", bold=True)
    pin(d, VLON, VLAT, st, r=26)
    # big state label
    if st=="verified":
        text_ar(d, "موثّق", (W//2, 1460), 44, OK, anchor="mm", bold=True)
        text_en(d, "verified", (W//2, 1510), 26, OK, anchor="mm", light=True)
    else:
        text_ar(d, "غير موثّق", (W//2, 1460), 40, WARN, anchor="mm", bold=True)
        text_en(d, "unverified", (W//2, 1510), 26, WARN, anchor="mm", light=True)
    one_line(d, "Verification is restricted to authorized participants.",
                "التدقيق مقتصر على مشاركين مخوّلين.", size_en=33, size_ar=40)

# --- Scene 6: audit trail ~74..86 ---
def sc6(d, t):
    top_title(d, "AUDIT TRAIL", None)
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=16)
    pin(d, VLON, VLAT, "verified", r=24)
    indicator(d, 70, 150, True, "ONLINE")
    # audit log card appears line by line
    rows = [
        ("entry", VERIFY_FAC[:14]),
        ("action", "verified"),
        ("actor", "verifier"),
        ("reversible", "yes"),
    ]
    rounded(d, [W//2-340, 1330, W//2+340, 1470], 14, fill=PANEL, outline=LINE)
    for i,(k,v) in enumerate(rows):
        if t > 2 + i*1.6:
            y = 1355 + i*33
            text_en(d, k, (W//2-310, y), 20, MUTED, anchor="lm", light=True)
            text_en(d, v, (W//2+310, y), 20, INK, anchor="rm", bold=True)
    one_line(d, "Every verification action is recorded, auditable, and reversible.",
                "كل إجراء تدقيق مسجّل وقابل للتدقيق والعكس.", size_en=32, size_ar=39)

# --- Scene 7: closing card ~86..92 (silent) ---
def sc7(d, t):
    d.rectangle([0,0,W,H], fill=NAVY2)
    # faint map ghost
    map_base(d)
    for name,(la,lo) in DISTRICTS.items(): pin(d, lo, la, "pending", r=14)
    pin(d, VLON, VLAT, "verified", r=22)
    # dark overlay for legibility
    d.rectangle([0,0,W,H], fill=NAVY2)
    d.rectangle([0, H//2-160, W, H//2+160], fill=None)
    text_en(d, "Coordination survives the blackout.", (W//2, H//2-20), 40, INK, anchor="mm", bold=True)
    text_ar(d, "يصمد التنسيق عند انقطاع الاتصال.", (W//2, H//2+44), 34, MUTED, anchor="mm", bold=True)
    text_en(d, "Nidaa", (W//2, H//2+150), 26, TEAL_L, anchor="mm", bold=True)

SCENES = [
    (0, 12, sc1), (12, 24, sc2), (24, 36, sc3), (36, 52, sc4),
    (52, 74, sc5), (74, 86, sc6), (86, 92, sc7),
]

def render(t):
    img, d = bg()
    for (s,e,fn) in SCENES:
        if s <= t < e:
            fn(d, t-s); break
    # progress (subtle, bottom)
    d.rectangle([0, H-4, int(W*(t/TOTAL)), H-1], fill=TEAL)
    return img

# ---------- render frames ----------
tmp = tempfile.mkdtemp(prefix="nidaa_v2_")
print("rendering frames...")
nf = int(TOTAL*FPS)
for i in range(nf):
    render(i/FPS).save(os.path.join(tmp, f"f{i:05d}.png"))
print("frames:", nf)

# ---------- audio ----------
async def tts():
    script = ("When connectivity becomes unreliable, coordination becomes harder. "
              "Nidaa is built for that reality. "
              "Information can be recorded, organized, and shared even when the network is unavailable. "
              "Changes remain available locally until connectivity returns. "
              "When a connection is restored, updates synchronize automatically. "
              "Verification is restricted to authorized participants. "
              "Every verification action is recorded, auditable, and reversible. "
              "The goal is simple. "
              "Keep coordination possible when infrastructure cannot be assumed.")
    c = edge_tts.Communicate(script, "en-US-AriaNeural", rate="+0%")
    await c.save(os.path.join(tmp, "vo.mp3"))
asyncio.run(tts())
print("vo done")

# build full audio track (44.1k): ambient bed + VO at 12s + UI ticks
VO_AT = 12.0
sr = 44100
amb = ambient(TOTAL, sr)
# VO decode
import struct
def read_mp3(path):
    # use ffmpeg to dump wav pcm
    out = os.path.join(tmp, "vo.wav")
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-i", path, out],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(out,"rb") as w:
        assert w.read(4)==b"RIFF"
        w.read(4); assert w.read(4)==b"WAVE"
        while True:
            hdr=w.read(4)
            if not hdr: break
            sz=struct.unpack("<I",w.read(4))[0]
            if hdr==b"fmt ":
                fmt=struct.unpack("<HHIIHH",w.read(16)); w.read(sz-16)
            elif hdr==b"data":
                data=w.read(sz); break
            else: w.read(sz)
    a=np.frombuffer(data,dtype=np.int16).astype(np.float32)/32768.0
    return a
vo = read_mp3(os.path.join(tmp,"vo.mp3"))
vo_sr=44100
if vo_sr!=sr:
    vo=np.interp(np.arange(int(len(vo)*sr/vo_sr)), np.arange(len(vo)), vo).astype(np.float32)
vo_full = np.zeros(len(amb), dtype=np.float32)
start = int(VO_AT*sr)
if len(vo)<=len(vo_full)-start:
    vo_full[start:start+len(vo)] = vo*0.95
else:
    vo_full[start:] = vo[:len(vo_full)-start]*0.95

# UI ticks
ticks=[]
def add_tick(at, freq=660, dur=0.08, vol=0.10):
    s=tone(freq,dur,sr=sr,vol=vol,fade=0.01)
    i=int(at*sr)
    if i+len(s)<len(amb): ticks.append((i,s.astype(np.float32)/32768.0))
for at in [6.5, 9.0, 38.0, 60.0, 66.0]:
    add_tick(at)
# build tick layer
ticklay=np.zeros(len(amb),dtype=np.float32)
for i,s in ticks: ticklay[i:i+len(s)]+=s

mixf = (amb.astype(np.float32)/32768.0*0.5 + vo_full + ticklay*0.8)
mixf = np.clip(mixf,-1,1)
final = (mixf*32767).astype(np.int16)
write_wav(os.path.join(tmp,"audio.wav"), final, sr)
print("audio done")

# ---------- encode ----------
ff = imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([ff,"-y","-framerate",str(FPS),"-i",os.path.join(tmp,"f%05d.png"),
                "-i",os.path.join(tmp,"audio.wav"),
                "-c:v","libx264","-pix_fmt","yuv420p","-preset","slow","-crf","23",
                "-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",OUT],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("VIDEO:", OUT, os.path.getsize(OUT), "bytes")
shutil.rmtree(tmp, ignore_errors=True)
