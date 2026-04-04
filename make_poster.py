from PIL import Image, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import ImageFont
import os

# ─── Canvas ──────────────────────────────────────────
W, H = 1080, 1920
img = Image.new("RGB", (W, H), (11, 31, 19))
draw = ImageDraw.Draw(img, "RGBA")

# ─── Background image ────────────────────────────────
try:
    bg = Image.open("poster_bg.webp").convert("RGB")
    bg = bg.resize((W, H), Image.LANCZOS)
    # Apply dark green overlay
    overlay = Image.new("RGB", (W, H), (11, 31, 19))
    img = Image.blend(bg, overlay, alpha=0.82)
    draw = ImageDraw.Draw(img, "RGBA")
except Exception as e:
    print(f"BG: {e}")

# ─── Fonts ───────────────────────────────────────────
def font(size):
    try:
        return ImageFont.truetype("NotoSansArabic.ttf", size)
    except:
        return ImageFont.load_default()

def ar(text):
    try:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except:
        return text

# ─── Colors ──────────────────────────────────────────
GREEN   = (61, 170, 134)
GREEN_L = (82, 201, 159)
WHITE   = (255, 255, 255)
DIM     = (160, 160, 160)
MUTED   = (110, 110, 110)
GOLD    = (244, 194, 80)
BLUE_L  = (126, 200, 227)
GRAY_L  = (152, 168, 184)
SURFACE = (255, 255, 255, 20)
SURFACE2= (255, 255, 255, 12)
BORDER  = (255, 255, 255, 45)

pad = 44

def rr(x1, y1, x2, y2, r=14, fill=None, outline=None, w=1):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill, outline=outline, width=w)

def c_text(text, y, fnt, fill=WHITE, cx=W//2):
    bb = draw.textbbox((0,0), text, font=fnt)
    tw = bb[2]-bb[0]
    draw.text((cx - tw//2, y), text, font=fnt, fill=fill)

def r_text(text, x, y, fnt, fill=WHITE):
    draw.text((x, y), text, font=fnt, fill=fill, anchor="ra")

def l_text(text, x, y, fnt, fill=WHITE):
    draw.text((x, y), text, font=fnt, fill=fill)

# ══════════════════════════════════════════════════════
# TOP BAR
# ══════════════════════════════════════════════════════
draw.line([(0, 90), (W, 90)], fill=(61, 170, 134, 55), width=1)

# Brand (right side)
f28 = font(28)
b1 = ar("معرض "); b2 = ar("روافد فنتك")
bw1 = draw.textbbox((0,0), b1, font=f28)[2]
bw2 = draw.textbbox((0,0), b2, font=f28)[2]
x0 = W - pad - bw1 - bw2
draw.text((x0, 26), b1, font=f28, fill=WHITE)
draw.text((x0+bw1, 26), b2, font=f28, fill=GREEN_L)

# Pill (left side)
f18 = font(18)
pill = ar("فرصة رعاية · 2026")
pb = draw.textbbox((0,0), pill, font=f18)
pw = pb[2]-pb[0]; ph = pb[3]-pb[1]
rr(pad, 20, pad+pw+28, 20+ph+16, r=100, fill=(61,170,134,30), outline=(61,170,134,90))
draw.text((pad+14, 28), pill, font=f18, fill=GREEN_L)

# ══════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════
y = 116

# Badge
f19 = font(19)
badge = ar("ملخص الرعاية والمشاركة")
bb = draw.textbbox((0,0), badge, font=f19)
bw = bb[2]-bb[0]; bh = bb[3]-bb[1]
bx = W//2 - bw//2 - 18
rr(bx, y, bx+bw+36, y+bh+18, r=100, fill=(61,170,134,22), outline=(61,170,134,75))
draw.text((bx+18, y+9), badge, font=f19, fill=GREEN_L)
y += bh + 46

# Line 1: "معرض"
f90 = font(96)
t1 = ar("معرض")
t1b = draw.textbbox((0,0), t1, font=f90)
c_text(t1, y, f90, fill=WHITE)
y += t1b[3]-t1b[1] + 2

# Line 2: "روافد فنتك 2026"
f82 = font(86)
t2 = ar("روافد فنتك 2026")
t2b = draw.textbbox((0,0), t2, font=f82)
c_text(t2, y, f82, fill=GREEN_L)
y += t2b[3]-t2b[1] + 28

# Subtitle
f26 = font(26); f22 = font(22)
sub1 = ar("برعاية جامعة الإمام محمد بن سعود الإسلامية")
sub2 = ar("بإشراف كلية علوم الحاسب وكلية الاعمال")
c_text(sub1, y, f26, fill=(215,215,215))
y += 36
c_text(sub2, y, f22, fill=MUTED)
y += 50

# ══════════════════════════════════════════════════════
# INFO STRIP — 4 cards
# ══════════════════════════════════════════════════════
cw = (W - pad*2 - 12*3) // 4
ch = 100
f_lbl = font(16); f_val = font(24)
info = [
    ("التاريخ",  "5-6 مايو 2026",        GREEN),
    ("الوقت",    "8:30 ص - 12:00 م",     GREEN),
    ("الموقع",   "بهو جامعة الإمام",      GREEN),
    ("الحضور",   "+3000 طالب وطالبة",    GREEN),
]
for i, (lbl, val, col) in enumerate(info):
    x1 = pad + i*(cw+12)
    y1 = y; x2 = x1+cw; y2 = y1+ch
    rr(x1, y1, x2, y2, r=12, fill=(255,255,255,14), outline=(col[0],col[1],col[2],50))
    # top accent
    draw.rounded_rectangle([x1, y1, x2, y1+3], radius=2, fill=(*col,180))
    # label
    lbl_r = ar(lbl)
    lb = draw.textbbox((0,0), lbl_r, font=f_lbl)
    draw.text((x2-12, y1+12), lbl_r, font=f_lbl, fill=DIM, anchor="ra")
    # value
    val_r = ar(val)
    vb = draw.textbbox((0,0), val_r, font=f_val)
    draw.text((x2-12, y1+38), val_r, font=f_val, fill=WHITE, anchor="ra")

y += ch + 50

# ══════════════════════════════════════════════════════
# DIVIDER
# ══════════════════════════════════════════════════════
def divider(y, label):
    f = font(20)
    lr = ar(label)
    lb = draw.textbbox((0,0), lr, font=f)
    lw = lb[2]-lb[0]; lh = lb[3]-lb[1]
    cx = W//2
    draw.text((cx-lw//2, y), lr, font=f, fill=GREEN)
    mid_y = y + lh//2 + 1
    draw.line([(pad, mid_y), (cx-lw//2-14, mid_y)], fill=(61,170,134,70), width=1)
    draw.line([(cx+lw//2+14, mid_y), (W-pad, mid_y)], fill=(61,170,134,70), width=1)
    return y + lh + 30

# ══════════════════════════════════════════════════════
# PACKAGES
# ══════════════════════════════════════════════════════
y = divider(y, "باقات الرعاية")

pkgs = [
    ("الراعي الاستراتيجي", "12,000 ريال",   BLUE_L,  "أعلى مستوى ظهور\nوأولوية المسرح"),
    ("الراعي الذهبي",      "6,000 ريال",    GOLD,    "حضور بارز + بوث\n+ تغطية إعلامية"),
    ("شركاء النجاح",       "عيني",          GRAY_L,  "هدايا أو خدمات\nمقابل ذكر رسمي"),
    ("المشاركون",          "بوث مستقل",     GREEN,   "بوثك الخاص\nأو بوث مجهز بالكامل"),
]
pkw = (W - pad*2 - 10*3) // 4
pkh = 175
f_nm = font(22); f_pr = font(34); f_pk = font(18)

for i, (name, price, col, perk) in enumerate(pkgs):
    x1 = pad + i*(pkw+10)
    y1 = y; x2 = x1+pkw; y2 = y1+pkh
    rr(x1, y1, x2, y2, r=14, fill=(col[0],col[1],col[2],18), outline=(col[0],col[1],col[2],65))
    # accent bar top
    draw.rounded_rectangle([x1, y1, x2, y1+4], radius=3, fill=col)
    # name
    nm_r = ar(name)
    nbb = draw.textbbox((0,0), nm_r, font=f_nm)
    draw.text((x2-14, y1+16), nm_r, font=f_nm, fill=WHITE, anchor="ra")
    # price
    pr_r = ar(price)
    draw.text((x2-14, y1+50), pr_r, font=f_pr, fill=col, anchor="ra")
    # perk lines
    for j, line in enumerate(perk.split("\n")):
        pk_r = ar(line)
        draw.text((x2-14, y1+102+j*26), pk_r, font=f_pk, fill=DIM, anchor="ra")

y += pkh + 50

# ══════════════════════════════════════════════════════
# ORGS
# ══════════════════════════════════════════════════════
y = divider(y, "أبرز المشاركين المتوقعين")

orgs = [
    ("البنك المركزي SAMA", (0,112,60)),
    ("فنتك السعودية",      (0,122,83)),
    ("SDAIA",              (27,79,154)),
    ("وزارة الاستثمار",    (0,104,55)),
    ("الأكاديمية المالية", (30,58,95)),
    ("STC Bank",           (106,31,122)),
    ("بنك الإنماء",        (0,75,141)),
    ("بنك الرياض",         (0,48,135)),
    ("تمارا",              (212,82,26)),
    ("Tabby",              (15,155,142)),
    ("EY",                 (200,160,0)),
    ("PwC",                (210,40,20)),
]
f_org = font(21)
badge_h = 42; gap_x = 10
x_cur = W - pad
y_cur = y

for (name, col) in orgs:
    nr = ar(name)
    nb = draw.textbbox((0,0), nr, font=f_org)
    nw = nb[2]-nb[0]
    bw = nw + 28
    if x_cur - bw < pad:
        x_cur = W - pad
        y_cur += badge_h + gap_x
    x1 = x_cur - bw
    x2 = x_cur
    rr(x1, y_cur, x2, y_cur+badge_h, r=8,
       fill=(col[0],col[1],col[2],30),
       outline=(col[0],col[1],col[2],100))
    draw.text((x2-14, y_cur+9), nr, font=f_org, fill=WHITE, anchor="ra")
    x_cur = x1 - gap_x

y = y_cur + badge_h + 50

# ══════════════════════════════════════════════════════
# BENEFITS
# ══════════════════════════════════════════════════════
y = divider(y, "أبرز مزايا الرعاية")

benefits = [
    "إعلان في كل منشور قبل وخلال وبعد الفعالية",
    "حضور على المسرح أمام آلاف الحضور",
    "وصول لأكثر من 3000 طالب وطالبة",
    "تغطية مصورة احترافية لجناحك",
    "درع تكريمي رسمي في حفل الختام",
    "تقرير إحصائي لقياس العائد بعد الفعالية",
]
f_ben = font(22)
b_w = (W - pad*2 - 14) // 2
b_h = 66
nums = ["01", "02", "03", "04", "05", "06"]

for i, txt in enumerate(benefits):
    col = i % 2
    row = i // 2
    x1 = (W - pad - b_w) if col == 0 else pad
    y1 = y + row*(b_h+10)
    x2 = x1+b_w; y2 = y1+b_h
    rr(x1, y1, x2, y2, r=12, fill=(61,170,134,18), outline=(61,170,134,50))
    # number badge
    nm = nums[i]
    f_num = font(16)
    nb = draw.textbbox((0,0), nm, font=f_num)
    nw = nb[2]-nb[0]
    draw.rounded_rectangle([x1+10, y1+(b_h-30)//2, x1+10+nw+14, y1+(b_h+30)//2], radius=6, fill=GREEN)
    draw.text((x1+17, y1+(b_h-30)//2+5), nm, font=f_num, fill=WHITE)
    # text
    txt_r = ar(txt)
    draw.text((x2-14, y1+(b_h-22)//2+2), txt_r, font=f_ben, fill=(215,215,215), anchor="ra")

y += 3*(b_h+10) + 50

# ══════════════════════════════════════════════════════
# CONTACT BAR
# ══════════════════════════════════════════════════════
bar_y = H - 170
bar_h = 110
rr(pad, bar_y, W-pad, bar_y+bar_h, r=18,
   fill=(61,170,134,28), outline=(61,170,134,90), w=2)

# CTA (right)
f_cta = font(34)
cta = ar("تواصل معنا وانضم الآن")
r_text(cta, W-pad-18, bar_y+22, f_cta, fill=WHITE)

# Email + Phone (left)
f_ct = font(21)
email_str = "pr.technationclub@gmail.com"
phone_str = "+966 53 483 1944"
# email row
eb = draw.textbbox((0,0), email_str, font=f_ct)
ew = eb[2]-eb[0]; eh = eb[3]-eb[1]
rr(pad+14, bar_y+14, pad+14+ew+26, bar_y+14+eh+18, r=8, fill=(255,255,255,18))
draw.text((pad+27, bar_y+23), email_str, font=f_ct, fill=(210,210,210))
# phone row
pb = draw.textbbox((0,0), phone_str, font=f_ct)
pw2 = pb[2]-pb[0]; ph2 = pb[3]-pb[1]
rr(pad+14, bar_y+56, pad+14+pw2+26, bar_y+56+ph2+18, r=8, fill=(255,255,255,18))
draw.text((pad+27, bar_y+65), phone_str, font=f_ct, fill=(210,210,210))

# ══════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════
f_ft = font(18)
foot = ar("معرض روافد فنتك 2026  ·  جامعة الإمام محمد بن سعود الإسلامية  ·  الرياض")
c_text(foot, H-46, f_ft, fill=(90,90,90))

# ─── Save ────────────────────────────────────────────
os.makedirs("screenshots", exist_ok=True)
out = "screenshots/poster_rawafid_2026.jpg"
img.save(out, "JPEG", quality=96)
print(f"Saved: {out}  ({W}x{H})")
