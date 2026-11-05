import sys, os, json, subprocess
SPEC = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and sys.argv[1].endswith(".json") else {}
if not os.path.exists("ses.mp3"):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "60", "-q:a", "9", "ses.mp3"])
import sys, os, math, re, subprocess
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
DUR = 60
FD = "/usr/share/fonts/opentype/inter/"
BG = (13, 10, 20); FG = (255, 255, 255); MUTED = (170, 160, 190)
PINK = (255, 46, 136); YEL = (255, 214, 10); MINT = (46, 230, 197); RED = (255, 59, 59)
CARD = (27, 21, 40); BORDER = (60, 50, 85); DARK = (13, 10, 20)
SLEEVE = (236, 96, 82); SLEEVE_D = (196, 62, 60); SKIN = (246, 195, 160)

@lru_cache(None)
def font(w, s):
    return ImageFont.truetype(FD + (f"InterDisplay-{w}.otf" if w in ("Black", "ExtraBold") else f"Inter-{w}.otf"), s)
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def inout(x): x = clamp(x); return x * x * (3 - 2 * x)
def back(x):
    x = clamp(x); c = 1.9
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def mix(a, b, t): t = clamp(t); return tuple(int(x + (y - x) * t) for x, y in zip(a, b))
def lerp(a, b, t): return a + (b - a) * t

# ---------------- audio analysis ----------------
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", "ses.mp3", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
X = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
HOP = 160
ENV = np.sqrt(np.convolve(X ** 2, np.ones(400) / 400, "same"))[::HOP]
ENV_S = np.convolve(ENV, np.hanning(9) / np.hanning(9).sum(), "same")
PK = []
for i in range(2, len(ENV_S) - 2):
    if ENV_S[i] >= ENV_S[i - 1] and ENV_S[i] > ENV_S[i + 1] and ENV_S[i] > 0.02:
        if PK and (i - PK[-1]) * HOP / 16000 < 0.08:
            if ENV_S[i] > ENV_S[PK[-1]]: PK[-1] = i
            continue
        PK.append(i)
PK = [i * HOP / 16000 for i in PK]
EMAX = np.percentile(ENV_S, 97)
def energy(t):
    i = int(t * 100)
    if i < 0 or i >= len(ENV_S): return 0.0
    return float(ENV_S[i] / EMAX) if EMAX > 0 else 0.0

# ---------------- drawing helpers ----------------
@lru_cache(None)
def base(acc):
    s = 4
    sm = Image.new("RGB", (W // s, H // s), BG); d = ImageDraw.Draw(sm)
    d.ellipse((40, 120, 230, 330), fill=mix(BG, acc, 0.32))
    d.ellipse((-60, -40, 120, 140), fill=mix(BG, (90, 40, 140), 0.6))
    sm = sm.filter(ImageFilter.GaussianBlur(48))
    im = sm.resize((W, H), Image.BICUBIC).convert("RGBA"); d = ImageDraw.Draw(im)
    for y in range(30, H, 60):
        for x in range(30, W, 60):
            d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(32, 26, 48))
    return im

@lru_cache(None)
def tsprite(txt, w, size, color, glow=None, stroke=0):
    f = font(w, size); l, t, r, b = f.getbbox(txt, stroke_width=stroke)
    pad = 60 if glow else 8
    im = Image.new("RGBA", (r - l + pad * 2, b - t + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad - l, pad - t), txt, font=f, fill=color + (255,), stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    if glow:
        m = im.getchannel("A").filter(ImageFilter.GaussianBlur(22)).point(lambda v: min(255, int(v * 1.5)))
        g = Image.new("RGBA", im.size, glow + (0,)); g.putalpha(m); im = Image.alpha_composite(g, im)
    return im

def paste(img, spr, cx, cy, scale=1.0, alpha=1.0, rot=0):
    if alpha <= 0.01 or scale <= 0.01: return
    if rot: spr = spr.rotate(rot, Image.BICUBIC, expand=True)
    if abs(scale - 1) > 0.005: spr = spr.resize((max(1, int(spr.width * scale)), max(1, int(spr.height * scale))), Image.BILINEAR)
    if alpha < 0.999: spr = spr.copy(); spr.putalpha(spr.getchannel("A").point(lambda v: int(v * alpha)))
    img.alpha_composite(spr, (int(cx - spr.width / 2), int(cy - spr.height / 2)))

def text(img, s, w, size, col, cx, cy, scale=1.0, alpha=1.0, glow=None, rot=0, stroke=0):
    paste(img, tsprite(s, w, size, col, glow, stroke), cx, cy, scale, alpha, rot)

@lru_cache(None)
def pill(s, size, fg, bgc, padx=34, h=None):
    f = font("Black", size); tw = f.getlength(s); h = h or int(size * 2.0)
    im = Image.new("RGBA", (int(tw + padx * 2) + 8, h + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, im.width - 4, h + 4), h // 2 if h < 120 else 28, fill=bgc + (255,))
    d.text((im.width / 2, h / 2 + 4), s, font=f, fill=fg + (255,), anchor="mm"); return im

@lru_cache(None)
def glow_dot(col, r):
    im = Image.new("RGBA", (r * 4, r * 4), col + (0,)); m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).ellipse((r * 1.3, r * 1.3, r * 2.7, r * 2.7), fill=255)
    im.putalpha(m.filter(ImageFilter.GaussianBlur(r * 0.5))); return im

def check(d, cx, cy, r, col=MINT):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col); k = r / 24
    d.line([(cx - 11 * k, cy + k), (cx - 3 * k, cy + 9 * k), (cx + 12 * k, cy - 8 * k)], fill=DARK, width=max(3, int(6 * k)), joint="curve")

# ---------------- talking avatar ----------------
AV = {n: Image.open(f"av_{n}.png").convert("RGBA") for n in ["back", "body"] + [f"head_m{m}_e{e}" for m in range(3) for e in (0, 1)]}
SH_L, SH_R = (400, 905), (680, 905)
POSES = {  # (elbow, hand, fingers) for left / right arm in canvas coords
    "rest":  (((345, 1160), (330, 1385), 0), ((735, 1160), (750, 1385), 0)),
    "wave":  (((345, 1160), (330, 1385), 0), ((800, 820), (835, 640), 0)),
    "shock": (((300, 820), (395, 640), 0), ((780, 820), (685, 640), 0)),
    "point": (((345, 1160), (330, 1385), 0), ((815, 880), (930, 760), 1)),
    "c1":    (((345, 1160), (330, 1385), 0), ((770, 900), (720, 740), 1)),
    "c2":    (((345, 1160), (330, 1385), 0), ((770, 900), (720, 740), 2)),
    "c3":    (((345, 1160), (330, 1385), 0), ((770, 900), (720, 740), 3)),
    "open":  (((300, 960), (210, 860), 0), ((780, 960), (870, 860), 0)),
    "whisper": (((345, 1160), (330, 1385), 0), ((700, 860), (610, 700), 0)),
}
def arm_state(t):
    prev, cur, tc = "rest", "rest", 0
    for tk, p in PK_POSE:
        if t >= tk: prev, cur, tc = cur, p, tk
    a = inout((t - tc) / 0.28)
    out = []
    for side in range(2):
        (e0, h0, f0), (e1, h1, f1) = POSES[prev][side], POSES[cur][side]
        e = (lerp(e0[0], e1[0], a), lerp(e0[1], e1[1], a)); h = (lerp(h0[0], h1[0], a), lerp(h0[1], h1[1], a))
        if cur == "wave" and side == 1 and a > 0.9: h = (h[0] + 22 * math.sin(t * 11), h[1] + 6 * math.cos(t * 11))
        out.append((e, h, f1 if a > 0.6 else f0))
    return out

def draw_arm(d, sh, e, h, fingers):
    for col, wd in ((SLEEVE_D, 74), (SLEEVE, 62)):
        d.line([sh, e], fill=col, width=wd); d.line([e, h], fill=col, width=wd - 4)
        r = wd / 2; d.ellipse((e[0] - r, e[1] - r, e[0] + r, e[1] + r), fill=col)
    r = 36
    for k in range(fingers):
        fx = h[0] - 18 + k * 18; d.line([(fx, h[1] - 10), (fx, h[1] - 70)], fill=(214, 150, 118), width=22); d.line([(fx, h[1] - 10), (fx, h[1] - 66)], fill=SKIN, width=16)
    d.ellipse((h[0] - r - 3, h[1] - r - 3, h[0] + r + 3, h[1] + r + 3), fill=(214, 150, 118))
    d.ellipse((h[0] - r, h[1] - r, h[0] + r, h[1] + r), fill=SKIN)

BLINKS = [x * 0.1 for x in range(0, 700, 1) if (x % 33 == 7)]
def avatar_layer(t, tilt_extra=0.0):
    en = energy(t)
    m = 0 if en < 0.18 else (1 if en < 0.5 else 2)
    eyes = 0 if any(b <= t < b + 0.12 for b in BLINKS) else 1
    canvas = Image.new("RGBA", (1080, 1400), (0, 0, 0, 0))
    tilt = 3 * math.sin(t * 1.7) + tilt_extra + 2.0 * en * math.sin(t * 9)
    bob = -8 * en
    headgrp = Image.new("RGBA", (1080, 1400), (0, 0, 0, 0))
    headgrp.alpha_composite(AV["back"])
    canvas.alpha_composite(headgrp.rotate(tilt, Image.BICUBIC, center=(540, 760), translate=(0, bob)))
    canvas.alpha_composite(AV["body"])
    canvas.alpha_composite(AV[f"head_m{m}_e{eyes}"].rotate(tilt, Image.BICUBIC, center=(540, 760), translate=(0, bob)))
    d = ImageDraw.Draw(canvas)
    (el, hl, fl), (er, hr, fr) = arm_state(t)
    draw_arm(d, SH_L, el, hl, fl); draw_arm(d, SH_R, er, hr, fr)
    return canvas

# ---------------- story engine: spec.json -> 1080x1920 story mp4 ----------------
ACC = {"pembe": PINK, "sari": YEL, "nane": MINT, "kirmizi": RED}
BEATS = SPEC.get("beats", []); T0 = []; _t = 0.0
for b in BEATS: T0.append(_t); _t += float(b.get("d", 2.5))
DUR = _t
PK_POSE = [(0, "rest")] + [(T0[i], b.get("pose", "rest")) for i, b in enumerate(BEATS)]
def put_avatar(img, t, sc=0.62, top=1150):
    lay = avatar_layer(t, 0).resize((int(1080 * sc), int(1400 * sc)), Image.BILINEAR)
    img.alpha_composite(lay, (int(540 - lay.width / 2), int(top + 12 * math.sin(t * 2.2))))
def glitch(img, s, cy, size, col, k, T):
    if k <= 0.02: return
    for dx, c in ((-6, PINK), (6, MINT)):
        if k < 1 or int(T * 12) % 9 == 0: text(img, s, "Black", size, c, 540 + dx * (1.5 - k), cy, 1.0, 0.6 * k)
    text(img, s, "Black", size, col, 540, cy, lerp(1.25, 1, ease(k)), clamp(k), glow=col)
def fit(s, w, size, maxw=980):
    while size > 30 and font(w, size).getlength(s) > maxw: size -= 4
    return size
# icons: film eq pad robot shop chart check question money plane
def ic(d, name, cx, cy, s, col, T):
    if name == "film":
        d.rounded_rectangle((cx-120*s, cy-85*s, cx+120*s, cy+85*s), int(20*s), outline=col, width=int(10*s)); d.polygon([(cx-30*s, cy-45*s), (cx-30*s, cy+45*s), (cx+45*s, cy)], fill=col)
    elif name == "eq":
        for j in range(7):
            h = (40 + 70 * abs(math.sin(T * 6 + j * 1.3))) * s; x = cx - 150*s + j*50*s; d.rounded_rectangle((x, cy+80*s-h*1.4, x+32*s, cy+80*s), int(10*s), fill=col)
    elif name == "pad":
        d.rounded_rectangle((cx-140*s, cy-70*s, cx+140*s, cy+70*s), int(70*s), fill=col); d.rectangle((cx-95*s, cy-10*s, cx-45*s, cy+10*s), fill=BG); d.rectangle((cx-80*s, cy-25*s, cx-60*s, cy+25*s), fill=BG)
        for ox, oy in ((65, -18), (95, 12)): d.ellipse((cx+(ox-14)*s, cy+(oy-14)*s, cx+(ox+14)*s, cy+(oy+14)*s), fill=BG)
    elif name == "robot":
        d.rounded_rectangle((cx-100*s, cy-70*s, cx+100*s, cy+80*s), int(34*s), outline=col, width=int(10*s)); d.ellipse((cx-55*s, cy-20*s, cx-20*s, cy+15*s), fill=col); d.ellipse((cx+20*s, cy-20*s, cx+55*s, cy+15*s), fill=col)
        d.line((cx, cy-70*s, cx, cy-110*s), fill=col, width=int(9*s)); d.ellipse((cx-16*s, cy-135*s, cx+16*s, cy-103*s), fill=col)
    elif name == "shop":
        d.rectangle((cx-110*s, cy-10*s, cx+110*s, cy+100*s), outline=col, width=int(10*s))
        for j in range(4): x = cx-120*s+j*60*s; d.pieslice((x, cy-70*s, x+60*s, cy-10*s), 0, 180, fill=col if j % 2 == 0 else PINK)
        d.rectangle((cx-25*s, cy+30*s, cx+25*s, cy+100*s), fill=col)
    elif name == "chart":
        for j, h in enumerate((60, 100, 80, 150)): d.rounded_rectangle((cx-120*s+j*65*s, cy+90*s-h*s*min(1, T % 3 + .3), cx-75*s+j*65*s, cy+90*s), int(8*s), fill=col)
    elif name == "check":
        d.ellipse((cx-100*s, cy-100*s, cx+100*s, cy+100*s), fill=col); d.line((cx-50*s, cy, cx-12*s, cy+40*s, cx+55*s, cy-40*s), fill=BG, width=int(22*s), joint="curve")
    elif name == "question":
        d.ellipse((cx-100*s, cy-100*s, cx+100*s, cy+100*s), outline=col, width=int(12*s)); d.text((cx, cy+6*s), "?", font=font("Black", int(150*s)), fill=col, anchor="mm")
    elif name == "money":
        d.ellipse((cx-100*s, cy-100*s, cx+100*s, cy+100*s), fill=col); d.text((cx, cy+6*s), "$", font=font("Black", int(140*s)), fill=BG, anchor="mm")
    elif name == "plane":
        d.polygon([(cx-110*s, cy), (cx+110*s, cy-85*s), (cx+50*s, cy+85*s), (cx, cy+18*s)], fill=col); d.polygon([(cx, cy+18*s), (cx+110*s, cy-85*s), (cx+12*s, cy+72*s)], fill=mix(col, BG, 0.3))
def beat(img, T, b, t0, t1):
    k = back((T - t0) / 0.35) * (1 - ease((T - (t1 - 0.22)) / 0.22) if T > t1 - 0.22 else 1)
    col = ACC.get(b.get("color", "pembe"), PINK); ty = b["type"]
    if ty == "hook":
        s = b["big"]; glitch(img, s, 620, fit(s, "Black", 170), FG, (T - t0 - 0.05) / 0.3 * (k if T > t1 - 0.22 else 1), T)
        if b.get("sub"): text(img, b["sub"], "Bold", fit(b["sub"], "Bold", 54), MUTED, 540, 790, back((T - t0 - 0.4) / 0.35) * clamp(k))
    elif ty == "big":
        y = 520
        for j, ln in enumerate(b["lines"]):
            c = ACC.get(ln.get("color"), FG); sz = fit(ln["t"], "Black", ln.get("size", 110))
            text(img, ln["t"], "Black", sz, c, 540, y, back((T - t0 - j * 0.3) / 0.35) * clamp(k) if T > t1 - 0.22 else back((T - t0 - j * 0.3) / 0.35), glow=c if c != FG else None); y += sz * 1.3
    elif ty == "card":
        card = Image.new("RGBA", (860, 720), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle((4, 4, 856, 716), 50, fill=CARD + (255,), outline=col + (255,), width=8); ic(d, b.get("icon", "check"), 430, 230, 1.3, col, T)
        d.text((430, 470), b["l1"], font=font("Black", fit(b["l1"], "Black", 80, 780)), fill=FG, anchor="mm"); d.text((430, 585), b["l2"], font=font("Black", fit(b["l2"], "Black", 96, 780)), fill=col, anchor="mm")
        paste(img, card, 540, 760, lerp(0.7, 1, clamp(k)), clamp(k), rot=b.get("rot", -3))
    elif ty == "question":
        d = ImageDraw.Draw(img); ic(d, "question", 540, 470, 0.7 * clamp(k), col, T) if k > 0.1 else None
        y = 650
        for ln in b["lines"]:
            sz = fit(ln, "Black", 88); text(img, ln, "Black", sz, FG, 540, y, back((T - t0 - 0.2) / 0.35)); y += sz * 1.25
        if b.get("hint"): paste(img, pill(b["hint"], 34, DARK, col), 540, y + 30, back((T - t0 - 0.6) / 0.35), rot=-2)
    elif ty == "cta":
        d = ImageDraw.Draw(img); ic(d, b.get("icon", "plane"), 540, 500 - 15 * math.sin(T * 3), 0.9 * clamp(k), col, T) if k > 0.1 else None
        s = b["big"]; text(img, s, "Black", fit(s, "Black", 96), FG, 540, 700, k)
        if b.get("pill"): paste(img, pill(b["pill"], 46, DARK, col), 540, 860, back((T - t0 - 0.4) / 0.35), rot=-3)
def frame(T):
    i = max(j for j in range(len(BEATS)) if T0[j] <= T) if BEATS else 0
    b = BEATS[i]; t1 = T0[i] + float(b.get("d", 2.5))
    img = base(ACC.get(b.get("color", "pembe"), PINK)).copy()
    paste(img, pill(SPEC.get("tag", "OTOPİLOT AI"), 34, DARK, YEL), 540, 300, back(T / 0.3), rot=-2)
    beat(img, T, b, T0[i], t1)
    if SPEC.get("avatar", True) and b["type"] != "question": put_avatar(img, T)
    elif b["type"] == "question": put_avatar(img, T, 0.45, 1430)
    if T < 0.2: img = Image.blend(Image.new("RGBA", (W, H), BG + (255,)), img, T / 0.2)
    if T > DUR - 0.3: img = Image.blend(img, Image.new("RGBA", (W, H), BG + (255,)), clamp((T - (DUR - 0.3)) / 0.3))
    for pt in T0:
        if pt <= T < pt + 0.2:
            s = 1 + 0.05 * (1 - (T - pt) / 0.2); big = img.resize((int(W * s), int(H * s)), Image.BILINEAR)
            img = big.crop(((big.width - W) // 2, (big.height - H) // 2, (big.width - W) // 2 + W, (big.height - H) // 2 + H))
    return img
def music(path):
    sr = 44100; n = int(DUR * sr); t = np.arange(n) / sr; buf = np.zeros(n, np.float32); beat_ = 0.5; rng = np.random.default_rng(3)
    def add(t0, sig, v):
        i = int(t0 * sr); j = min(n, i + len(sig)); buf[i:j] += v * sig[: j - i]
    def env(d, a=0.005, r=8): tt = np.arange(int(d * sr)) / sr; return np.minimum(tt / a, 1) * np.exp(-r * tt), tt
    chords = [(220.0, 261.6, 329.6), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7), (164.8, 196.0, 246.9)]
    for b in range(int(DUR / beat_)):
        tb = b * beat_; ch = chords[(b // 4) % 4]
        e, tt = env(0.35, 0.002, 14); add(tb, np.sin(2 * np.pi * (55 + 90 * np.exp(-30 * tt)) * tt) * e, 0.9)
        e, tt = env(0.05, 0.001, 60); add(tb + beat_ / 2, rng.standard_normal(len(tt)) * e, 0.12)
        for k in range(4):
            e, tt = env(beat_ / 4, 0.003, 10); f = ch[k % 3] * 2; add(tb + k * beat_ / 4, (np.sign(np.sin(2 * np.pi * f * tt)) * 0.3 + np.sin(2 * np.pi * f * tt)) * e, 0.08)
        e, tt = env(beat_, 0.01, 3); add(tb, np.sin(2 * np.pi * ch[0] / 2 * tt) * e, 0.35)
    for tp in T0[1:]:
        m = int(0.4 * sr); nz = np.convolve(rng.standard_normal(m), np.ones(40) / 40, "same") * np.sin(np.linspace(0, np.pi, m)) ** 2 * 2; add(tp - 0.2, nz, 0.4)
    buf *= np.minimum(1, (DUR - t) / 0.6)
    (np.clip(buf / max(1e-6, np.abs(buf).max() / 0.9), -1, 1) * 32767).astype(np.int16).tofile(path)
def render(out):
    mid = round(DUR * FPS / 2) / FPS
    def part(a, b, f):
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", f], stdin=subprocess.PIPE)
        for fi in range(round(a * FPS), round(b * FPS)): p.stdin.write(frame(fi / FPS).convert("RGB").tobytes())
        p.stdin.close(); p.wait()
    pid = os.fork()
    if pid == 0: part(0, mid, "_a.mp4"); os._exit(0)
    part(mid, DUR, "_b.mp4"); os.waitpid(pid, 0)
    open("_l.txt", "w").write("file _a.mp4\nfile _b.mp4\n"); music("_m.raw")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-f", "s16le", "-ar", "44100", "-ac", "1", "-i", "_m.raw",
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], check=True)
if __name__ == "__main__":
    mode = sys.argv[2] if len(sys.argv) > 2 else "render"
    if mode == "preview":
        ims = [frame(T0[i] + float(b.get("d", 2.5)) * 0.6).convert("RGB").resize((270, 480)) for i, b in enumerate(BEATS)]
        sh = Image.new("RGB", (270 * len(ims), 480)); [sh.paste(im, (k * 270, 0)) for k, im in enumerate(ims)]; sh.save(sys.argv[3] if len(sys.argv) > 3 else "preview.png")
    else: render(sys.argv[3] if len(sys.argv) > 3 else "story.mp4")
