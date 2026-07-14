#!/usr/bin/env python3
"""
Build the Nidaa 90-second partner demo video WITHOUT a camera or recordings.

Approach: render faithful UI-replica frames in the app's exact theme (read from
globals.css), populated with REAL seed data from the repo, animate the offline
survival + verification workflow, narrate with edge-tts (Arabic + English),
and encode with the bundled imageio-ffmpeg binary.

Output: pilot/demo-video.mp4  (~90s, 1080x1920 portrait, Arabic-RTL first)

Faithful to repo theme:
  --teal #0f766e  --teal-dark #0b5750  --bg #f3f4f6  --card #fff
  --need #b91c1c  --offer #15803d  --amber #b45309  --muted #6b7280
"""
import json, os, subprocess, math, asyncio, tempfile, shutil
from PIL import Image, ImageDraw, ImageFont
import edge_tts

ROOT = r"C:\Users\theab\nidaa"
OUT = os.path.join(ROOT, "pilot", "demo-video.mp4")
W, H = 1080, 1920
FPS = 30

# ---- palette (from globals.css) ----
TEAL="#0f766e"; TEAL_D="#0b5750"; BG="#f3f4f6"; CARD="#ffffff"
NEED="#b91c1c"; OFFER="#15803d"; AMBER="#b45309"; MUTED="#6b7280"
TEXT="#111827"; RED_BG="#fee2e2"; GREEN_BG="#d1fae5"; YEL_BG="#fef3c7"; GREY_BG="#f3f4f6"

FONT_DIR = r"C:\Windows\Fonts"
def font(path, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, path), size)
F_AR = "segoeui.ttf"          # Arabic (Segoe UI has Arabic glyphs; GARABD tofu'd in PIL)
F_AR_B = "segoeuib.ttf"       # Arabic bold (Segoe UI Bold)
F_EN = "segoeui.ttf"           # Latin
F_EN_B = "segoeuib.ttf"        # Latin bold

def rtl(s): return s  # strings already in visual order; PIL draws RTL naturally for Arabic

def txt(d, s, pos, fnt, fill, anchor="la", maxw=None):
    if maxw and d.textlength(s, font=fnt) > maxw:
        # shrink-to-fit preserving the Arabic (no truncation)
        size = fnt.size
        f2 = ImageFont.truetype(fnt.path, max(14, int(size * maxw / d.textlength(s, font=fnt))))
        d.text(pos, s, font=f2, fill=fill, anchor=anchor)
    else:
        d.text(pos, s, font=fnt, fill=fill, anchor=anchor)

# ---- real seed data (from data/db.json in repo) ----
with open(os.path.join(ROOT, "data", "db.json"), encoding="utf-8") as fh:
    db = json.load(fh)
entries = db["entries"]

def find(cat, verified=None, author=None):
    for e in entries:
        if e.get("category")==cat and (verified is None or e.get("verified")==verified) and (author is None or e.get("authorRole")==author):
            return e
    return entries[0]

MED_OFFER = find("medical", True)            # verified offer (pharmacy/clinic)
FOOD_NEED = find("food", False)              # unverified need
WATER_NEED = find("water", True)             # verified need
SHELTER_OFFER = find("shelter", True)

# pick a created entry to become the user's offline post
USER_POST = {
    "type":"need","category":"medical",
    "titleAr":"حالة طبية عاجلة — تحتاج أدوية ربو","titleEn":"Urgent medical case — needs asthma medication",
    "city":"خان يونس","region":"gza",
}
TARGET_ID = MED_OFFER["id"]  # verifier will mark this verified

# ---- frame helpers ----
def base():
    img = Image.new("RGB", (W,H), BG)
    d = ImageDraw.Draw(img)
    return img, d

def header(d, title_ar, title_en, status=None):
    d.rectangle([0,0,W,150], fill=TEAL)
    d.text((40,46), title_ar, font=font(F_AR_B,46), fill="#ffffff", anchor="la")
    d.text((40,108), title_en, font=font(F_EN,22), fill="#d1fae5", anchor="la")
    if status:
        # status pill top-right
        col = {"online":GREEN_BG,"offline":RED_BG,"pending":YEL_BG}[status[0]]
        tcol = {"online":"#065f46","offline":"#991b1b","pending":"#92400e"}[status[0]]
        w = 40 + len(status[1])*15
        d.rounded_rectangle([W-40-w-28,46,W-40,108], radius=16, fill=col)
        d.text((W-40-14,77), status[1], font=font(F_EN_B,26), fill=tcol, anchor="ra")

def statusbar(d, items):
    y=170
    x=40
    for kind,label in items:
        col = {"online":GREEN_BG,"offline":RED_BG,"pending":YEL_BG}[kind]
        tcol= {"online":"#065f46","offline":"#991b1b","pending":"#92400e"}[kind]
        tw = 40 + len(label)*15
        d.rounded_rectangle([x,y,x+tw+40,y+54], radius=27, fill=col)
        d.text((x+20,y+27), label, font=font(F_EN_B,24), fill=tcol, anchor="lm")
        x += tw+60

def card(d, x, y, w, e, verified=None, local=False):
    ch=300
    d.rounded_rectangle([x,y,x+w,y+ch], radius=18, fill=CARD, outline="#e5e7eb", width=2)
    # type tag
    is_need = e["type"]=="need"
    tcol = NEED if is_need else OFFER
    tb = RED_BG if is_need else GREEN_BG
    tt = f'{("حاجة" if is_need else "عرض")} · {e["category"].upper()}'
    d.rounded_rectangle([x+24,y+24,x+24+150,y+24+44], radius=10, fill=tb)
    d.text((x+99,y+46), tt, font=font(F_AR_B,22), fill=tcol, anchor="mm")
    # title ar
    txt(d, e["titleAr"], (x+24,y+96), font(F_AR_B,30), TEXT, anchor="la", maxw=w-48)
    # city / region
    d.text((x+24,y+150), f'📍 {e.get("city") or "—"}  ·  {e.get("region","—")}', font=font(F_EN,22), fill=MUTED, anchor="la")
    d.text((x+24,y+190), f'role: {e.get("authorRole")}', font=font(F_EN,20), fill=MUTED, anchor="la")
    # verified tag
    if verified is True:
        d.rounded_rectangle([x+w-200,y+24,x+w-24,y+24+44], radius=10, fill=GREEN_BG)
        d.text((x+w-112,y+46), "✓ موثّق", font=font(F_AR_B,22), fill="#065f46", anchor="mm")
    elif verified is False:
        d.rounded_rectangle([x+w-210,y+24,x+w-24,y+24+44], radius=10, fill=GREY_BG)
        d.text((x+w-117,y+46), "غير موثّق", font=font(F_AR_B,22), fill=MUTED, anchor="mm")
    if local:
        d.rounded_rectangle([x+24,y+232,x+24+230,y+232+46], radius=10, fill=YEL_BG)
        d.text((x+139,y+255), "محفوظ محلياً", font=font(F_AR_B,22), fill="#92400e", anchor="mm")

def caption(d, line_ar, line_en):
    d.rectangle([0,H-150,W,H], fill=TEAL_D)
    txt(d, line_ar, (W//2, H-104), font(F_AR_B,34), "#ffffff", anchor="mm", maxw=W-60)
    d.text((W//2, H-52), line_en, font=font(F_EN,22), fill="#a7f3d0", anchor="mm")

def progress_bar(d, t):  # t in 0..1 white-on-teal bottom strip
    d.rectangle([0,H-8,W, H-2], fill="#0b5750")
    d.rectangle([0,H-8, int(W*t), H-2], fill="#5eead4")

# ---- timing: 90s @30fps = 2700 frames. Build scene list with durations ----
# scenes: (start_s, end_s, render_fn) ; we render each at 30fps
def scene_online(d, t):
    header(d, "نداء", "Nidaa — community coordination board", ("online","Online"))
    statusbar(d, [("online","Online"),("pending","Synced")])
    card(d, 40, 250, W-80, MED_OFFER, verified=True)
    card(d, 40, 580, W-80, WATER_NEED, verified=True)
    card(d, 40, 910, W-80, FOOD_NEED, verified=False)
    caption(d, "اللوحة تعمل الآن وعبر الإنترنت", "The board, online — real verified facilities")

def scene_offline_post(d, t):
    header(d, "نداء", "Nidaa — offline-first", ("offline","Offline"))
    statusbar(d, [("offline","No internet"),("pending","Saved locally")])
    card(d, 40, 250, W-80, MED_OFFER, verified=True)
    # the new post being composed (highlight)
    card(d, 40, 580, W-80, USER_POST, verified=False, local=True)
    caption(d, "أنشئ طلباً بدون اتصال — يُحفظ على الجهاز", "Create a need offline — saved on device")

def scene_offline_browse(d, t):
    header(d, "نداء", "Nidaa — usable while offline", ("offline","Offline"))
    statusbar(d, [("offline","No internet"),("pending","Saved locally")])
    card(d, 40, 250, W-80, USER_POST, verified=False, local=True)
    card(d, 40, 580, W-80, WATER_NEED, verified=True)
    card(d, 40, 910, W-80, MED_OFFER, verified=True)
    caption(d, "تصفّح واقرأ كل ما حُفظ — بلا إنترنت", "Browse & read saved entries with no connection")

def scene_sync(d, t):
    header(d, "نداء", "Nidaa — reconnect & sync", ("online","Back online"))
    statusbar(d, [("online","Syncing"),("pending","Uploading")])
    card(d, 40, 250, W-80, MED_OFFER, verified=True)
    card(d, 40, 580, W-80, USER_POST, verified=False)  # now synced (no local badge)
    card(d, 40, 910, W-80, WATER_NEED, verified=True)
    caption(d, "عاد الاتصال — رُفع المنشور بلا فقدان", "Connection returns — post uploads, zero data loss")

def scene_verify(d, t):
    header(d, "نداء", "Nidaa — trusted verification", ("online","Online"))
    statusbar(d, [("online","Verifier"),("pending","Audited")])
    card(d, 40, 250, W-80, MED_OFFER, verified=True)
    card(d, 40, 580, W-80, USER_POST, verified=True)  # verifier confirmed
    card(d, 40, 910, W-80, WATER_NEED, verified=True)
    caption(d, "موثّق من جهة موثوقة — قابل للتدقيق والعكس", "Verified by a trusted actor — auditable & reversible")

SCENES = [
    (0, 10, scene_online),
    (10, 30, scene_offline_post),
    (30, 50, scene_offline_browse),
    (50, 70, scene_sync),
    (70, 90, scene_verify),
]

def render_frame(t):
    img, d = base()
    for (s,e,fn) in SCENES:
        if s <= t < e:
            fn(d, t-s)
            break
    progress_bar(d, t/90.0)
    return img

# ---- 1) render all frames to temp dir ----
tmp = tempfile.mkdtemp(prefix="nidaa_frames_")
print("rendering frames...")
nframes = 90*FPS
for i in range(nframes):
    t = i/FPS
    img = render_frame(t)
    img.save(os.path.join(tmp, f"f{i:05d}.png"))
print("frames done:", nframes)

# ---- 2) TTS narration (edge-tts, Arabic + English) ----
async def make_tts():
    # Arabic narration
    ar_text = ("ندا، لوحة تنسيق مجتمعي تعمل حتى بدون إنترنت. شاهد: ننشئ طلباً طبياً "
               "بلا اتصال فيُحفظ على الجهاز. نتصفح كل المنشورات دون إنترنت. "
               "عند عودة الاتصال يُرفع المنشور بلا فقدان. جهة موثوقة توثّقه — قابل للتدقيق والعكس. "
               "ندا تبقى قابلة للاستخدام حتّى عندما ينقطع الاتصال.")
    en_text = ("Nidaa is a coordination board that works even offline. Watch: we create a medical "
               "need with no connection — it is saved on the device. We browse all entries without "
               "internet. When the connection returns, the post uploads with zero data loss. A trusted "
               "verifier confirms it — auditable and reversible. Nidaa stays usable even when connectivity doesn't.")
    acomm = edge_tts.Communicate(ar_text, "ar-EG-SalmaNeural")
    await acomm.save(os.path.join(tmp, "ar.mp3"))
    ecomm = edge_tts.Communicate(en_text, "en-US-AriaNeural")
    await ecomm.save(os.path.join(tmp, "en.mp3"))
asyncio.run(make_tts())
print("tts done")

# ---- 3) encode with bundled ffmpeg: frames + mixed audio (ar then en) ----
ff = shutil.which("ffmpeg") or None
if not ff:
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
print("ffmpeg:", ff)

# concat ar then en audio with 1s silence gap
silence = os.path.join(tmp, "sil.mp3")
subprocess.run([ff, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "1", silence],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
combined = os.path.join(tmp, "nar.mp3")
# ffmpeg concat via list
with open(os.path.join(tmp,"list.txt"),"w") as l:
    l.write(f"file '{os.path.join(tmp,'ar.mp3').replace(chr(92),'/')}'\n")
    l.write(f"file '{silence.replace(chr(92),'/')}'\n")
    l.write(f"file '{os.path.join(tmp,'en.mp3').replace(chr(92),'/')}'\n")
subprocess.run([ff, "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp,"list.txt"),
                "-c", "copy", combined], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# normalize audio length to ~90s (pad/trim) and mux
final_audio = os.path.join(tmp, "nar_padded.mp3")
subprocess.run([ff, "-y", "-i", combined, "-af", "apad", "-t", "90", final_audio],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([ff, "-y", "-framerate", str(FPS), "-i", os.path.join(tmp,"f%05d.png"),
                "-i", final_audio,
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
                "-shortest", "-movflags", "+faststart", OUT],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("video written:", OUT, os.path.getsize(OUT), "bytes")
shutil.rmtree(tmp, ignore_errors=True)
