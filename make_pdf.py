#!/usr/bin/env python3
"""
Generate high-quality editable PDF poster for Rawafid Fintech 2026
Uses ReportLab with NotoSansArabic font + arabic-reshaper + bidi
"""

from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line
import arabic_reshaper
from bidi.algorithm import get_display
import math

# ── Register fonts ──────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont('NotoArabic',      'NotoSansArabic.ttf'))
pdfmetrics.registerFont(TTFont('NotoArabicBold',  'NotoSansArabic.ttf'))

# ── Page size: matches poster (pts) ─────────────────────────────────────
W, H = 1080, 2063

# ── Color palette ────────────────────────────────────────────────────────
C_BG        = HexColor('#060F09')
C_BG2       = HexColor('#071410')
C_BG3       = HexColor('#0A1C10')
C_GREEN     = HexColor('#3DAA86')
C_GREEN2    = HexColor('#52c99f')
C_GOLD      = HexColor('#D4A84B')
C_GOLD2     = HexColor('#B8913A')
C_GOLD3     = HexColor('#9A7020')
C_TEAL      = HexColor('#0D7D6C')
C_TEAL2     = HexColor('#1A9E8A')
C_DARK_GRN  = HexColor('#1B6B52')
C_DARK_GRN2 = HexColor('#175E42')
C_STRIP     = HexColor('#0A2016')
C_WHITE     = HexColor('#FFFFFF')
C_WHITE_DIM = HexColor('#C8C8C8')
C_CARD_BG   = HexColor('#FFFFFF')
C_TEXT_DARK = HexColor('#0D2218')
C_MUTED     = HexColor('#888888')
C_BORDER    = HexColor('#1F3A2A')

def ar(text):
    """Reshape + bidi Arabic text for proper rendering."""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

def draw_rounded_rect(c, x, y, w, h, radius=12, fill_color=None, stroke_color=None, stroke_width=0):
    """Draw a rounded rectangle."""
    c.saveState()
    if fill_color:
        c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_width)
    else:
        c.setLineWidth(0)
    c.roundRect(x, y, w, h, radius, fill=1 if fill_color else 0, stroke=1 if stroke_color else 0)
    c.restoreState()

def draw_rect(c, x, y, w, h, color, alpha=1.0):
    c.saveState()
    c.setFillColor(color, alpha=alpha)
    c.setLineWidth(0)
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.restoreState()

def ar_text(c, text, x, y, font_size, color=C_WHITE, font='NotoArabic', align='center'):
    """Draw Arabic text at position (x,y = baseline)."""
    c.saveState()
    c.setFont(font, font_size)
    c.setFillColor(color)
    t = ar(text)
    if align == 'center':
        c.drawCentredString(x, y, t)
    elif align == 'right':
        c.drawString(x - c.stringWidth(t, font, font_size), y, t)
    elif align == 'left':
        c.drawString(x, y, t)
    c.restoreState()

def text_w(c, text, font, size):
    shaped = ar(text)
    return c.stringWidth(shaped, font, size)

# ══════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ══════════════════════════════════════════════════════════════════════════
output_path = 'rawafid_fintech_2026.pdf'
c = rl_canvas.Canvas(output_path, pagesize=(W, H))
c.setTitle('معرض روافد فنتك 2026 — باقات الرعاية')
c.setAuthor('Tech Nation Club — جامعة الإمام')

# ═══ FULL BACKGROUND ════════════════════════════════════════════════════
draw_rect(c, 0, 0, W, H, C_BG)


# ════════════════════════════════════════════════════════════════════════
# SECTION 1: HERO  (y: H-520 → H)  = 1543 → 2063
# ════════════════════════════════════════════════════════════════════════
HERO_TOP = H        # 2063
HERO_H   = 530
HERO_BOT = H - HERO_H  # 1533

# Hero gradient layers (simulated with transparent rects)
draw_rect(c, 0, HERO_BOT, W, HERO_H, C_BG3)
# radial highlight center – approximate with ellipses
c.saveState()
c.setFillColor(HexColor('#1B6B52'), alpha=0.25)
c.ellipse(W*0.15-150, HERO_BOT+HERO_H*0.1, W*0.85+150, HERO_BOT+HERO_H*0.9, fill=1, stroke=0)
c.restoreState()

# Decorative rings
for (cx, cy, r, alpha) in [
    (W-120, HERO_BOT+HERO_H-80, 240, 0.13),
    (W-120, HERO_BOT+HERO_H-80, 165, 0.09),
    (W-120, HERO_BOT+HERO_H-80, 85,  0.16),
    (100,   HERO_BOT+120,       140, 0.10),
]:
    c.saveState()
    c.setStrokeColor(C_GREEN, alpha=alpha)
    c.setLineWidth(1.5)
    c.setFillColor(C_BG, alpha=0)
    c.circle(cx, cy, r, fill=0, stroke=1)
    c.restoreState()

# ── Badge pill ──────────────────────────────────────────────────────────
badge_text = ar('فرصة رعاية حصرية · 2026')
bw = c.stringWidth(badge_text, 'NotoArabic', 9.5) + 40
bx = W/2 - bw/2
by = HERO_BOT + HERO_H - 65
draw_rounded_rect(c, bx, by, bw, 24, radius=12,
                  fill_color=HexColor('#0D2818'),
                  stroke_color=HexColor('#3DAA86'), stroke_width=1)
# dot
c.saveState()
c.setFillColor(C_GREEN2)
c.circle(bx + bw - 18, by + 12, 3.5, fill=1, stroke=0)
c.restoreState()
c.saveState()
c.setFont('NotoArabic', 9.5)
c.setFillColor(C_GREEN2)
c.drawCentredString(W/2, by + 7, badge_text)
c.restoreState()

# ── Main title ───────────────────────────────────────────────────────────
# "معرض"
c.saveState()
c.setFont('NotoArabicBold', 52)
c.setFillColor(HexColor('#E8E8E8'))
c.drawCentredString(W/2, HERO_BOT + HERO_H - 128, ar('معرض'))
c.restoreState()

# "روافد فنتك" — big gradient (simulated: layered in green)
c.saveState()
c.setFont('NotoArabicBold', 88)
c.setFillColor(C_GREEN2)
c.drawCentredString(W/2, HERO_BOT + HERO_H - 230, ar('روافد فنتك'))
c.restoreState()

# "2026" ghost
c.saveState()
c.setFont('NotoArabicBold', 72)
c.setFillColor(HexColor('#FFFFFF'), alpha=0.10)
c.drawCentredString(W/2, HERO_BOT + HERO_H - 312, '2026')
c.restoreState()

# ── Subtitle ────────────────────────────────────────────────────────────
c.saveState()
c.setFont('NotoArabicBold', 11.5)
c.setFillColor(HexColor('#DDDDDD'))
c.drawCentredString(W/2, HERO_BOT + HERO_H - 356, ar('برعاية جامعة الإمام محمد بن سعود الإسلامية'))
c.restoreState()
c.saveState()
c.setFont('NotoArabic', 10)
c.setFillColor(HexColor('#808080'))
c.drawCentredString(W/2, HERO_BOT + HERO_H - 376, ar('بإشراف كلية علوم الحاسب وكلية الاعمال · الرياض'))
c.restoreState()

# ── Stat chips ───────────────────────────────────────────────────────────
stats = [
    ('يومان',  'تواجد كامل',    HexColor('#0A2A18'), HexColor('#3DAA86')),
    ('+20',    'جهة مشاركة',    HexColor('#0A2018'), HexColor('#D4A84B')),
    ('+3000',  'طالب وطالبة',   HexColor('#0A1820'), HexColor('#5B8DD9')),
    ('5–6',    'مايو 2026',     HexColor('#0A2A18'), HexColor('#3DAA86')),
]
chip_w, chip_h = 200, 62
chips_total = len(stats) * chip_w + (len(stats)-1) * 12
cx_start = (W - chips_total) / 2
sy = HERO_BOT + 42

for i, (num, lbl, bg, accent) in enumerate(stats):
    cx = cx_start + i * (chip_w + 12)
    draw_rounded_rect(c, cx, sy, chip_w, chip_h, radius=10,
                      fill_color=HexColor('#0F1F14'),
                      stroke_color=HexColor('#1F3A2A'), stroke_width=1)
    # accent left bar
    draw_rounded_rect(c, cx, sy, 4, chip_h, radius=2, fill_color=accent)
    # number
    c.saveState()
    c.setFont('NotoArabicBold', 20)
    c.setFillColor(C_WHITE)
    c.drawCentredString(cx + chip_w/2 + 8, sy + chip_h - 26, ar(num))
    c.restoreState()
    # label
    c.saveState()
    c.setFont('NotoArabic', 9)
    c.setFillColor(HexColor('#7A9A8A'))
    c.drawCentredString(cx + chip_w/2 + 8, sy + 10, ar(lbl))
    c.restoreState()

# ── Diagonal divider ─────────────────────────────────────────────────────
c.saveState()
c.setFillColor(C_BG)
p = c.beginPath()
p.moveTo(0, HERO_BOT)
p.lineTo(W, HERO_BOT + 30)
p.lineTo(W, HERO_BOT)
p.close()
c.drawPath(p, fill=1, stroke=0)
c.restoreState()


# ════════════════════════════════════════════════════════════════════════
# SECTION 2: INFO STRIP  y: 1460 → 1533
# ════════════════════════════════════════════════════════════════════════
STRIP_TOP = HERO_BOT
STRIP_H   = 72
STRIP_BOT = STRIP_TOP - STRIP_H

draw_rect(c, 0, STRIP_BOT, W, STRIP_H, HexColor('#0A1C10'))
# top/bottom lines
c.saveState()
c.setStrokeColor(C_GREEN, alpha=0.2); c.setLineWidth(0.8)
c.line(0, STRIP_TOP, W, STRIP_TOP)
c.line(0, STRIP_BOT, W, STRIP_BOT)
c.restoreState()

strip_items = [
    ('📅', '5 – 6 مايو 2026', 'التاريخ'),
    ('🕐', '8:30 ص – 12:00 م', 'الوقت'),
    ('📍', 'بهو جامعة الإمام · الرياض', 'الموقع'),
]
col_w = W // 3
for i, (ic, val, lbl) in enumerate(strip_items):
    cx = W - (i + 0.5) * col_w  # RTL
    # divider
    if i < 2:
        c.saveState()
        c.setStrokeColor(HexColor('#FFFFFF'), alpha=0.07); c.setLineWidth(0.8)
        c.line(W - (i+1)*col_w, STRIP_BOT+10, W - (i+1)*col_w, STRIP_TOP-10)
        c.restoreState()
    # label
    c.saveState()
    c.setFont('NotoArabic', 8)
    c.setFillColor(HexColor('#5A7A6A'))
    c.drawCentredString(cx, STRIP_BOT + STRIP_H - 20, ar(lbl))
    c.restoreState()
    # value
    c.saveState()
    c.setFont('NotoArabicBold', 12.5)
    c.setFillColor(C_WHITE)
    c.drawCentredString(cx, STRIP_BOT + 18, ar(val))
    c.restoreState()


# ════════════════════════════════════════════════════════════════════════
# SECTION 3: PACKAGES  y: 810 → 1460
# ════════════════════════════════════════════════════════════════════════
PKG_TOP = STRIP_BOT
PKG_H   = 650
PKG_BOT = PKG_TOP - PKG_H

draw_rect(c, 0, PKG_BOT, W, PKG_H, C_BG2)

# Section header
c.saveState()
c.setFont('NotoArabic', 8.5)
c.setFillColor(C_GREEN2)
c.drawRightString(W-50, PKG_TOP - 32, ar('باقات الرعاية'))
c.restoreState()
# Line before label
c.saveState()
c.setStrokeColor(C_GREEN2); c.setLineWidth(1.5)
c.line(W-50-c.stringWidth(ar('باقات الرعاية'),'NotoArabic',8.5)-14, PKG_TOP-27,
       W-50-c.stringWidth(ar('باقات الرعاية'),'NotoArabic',8.5)-28, PKG_TOP-27)
c.restoreState()

# Title
c.saveState()
c.setFont('NotoArabicBold', 26)
c.setFillColor(C_WHITE)
c.drawRightString(W-50, PKG_TOP - 62, ar('اختر مستوى مشاركتك'))
c.restoreState()
# "مستوى مشاركتك" accent color overdrawn
accent_t = ar('مستوى مشاركتك')
aw = c.stringWidth(accent_t, 'NotoArabicBold', 26)
c.saveState()
c.setFont('NotoArabicBold', 26)
c.setFillColor(C_GREEN2)
c.drawString(W-50-aw, PKG_TOP - 62, accent_t)
c.restoreState()
# "اختر" in white
rem_t = ar('اختر ')
rw = c.stringWidth(rem_t, 'NotoArabicBold', 26)
c.saveState()
c.setFont('NotoArabicBold', 26)
c.setFillColor(C_WHITE)
c.drawString(W-50-aw-rw, PKG_TOP - 62, rem_t)
c.restoreState()

# ── Package cards ────────────────────────────────────────────────────────
CARD_W  = 490
CARD_H  = 520
CARD_Y  = PKG_BOT + 18
CARD_GAP = 14
LEFT_X  = 50
RIGHT_X = 50 + CARD_W + CARD_GAP

cards = [
    {
        'title': 'الراعي الاستراتيجي',
        'type':  'Strategic Sponsor',
        'price': '12,000', 'tag': 'EXCLUSIVE',
        'hdr': HexColor('#C4912A'), 'hdr2': HexColor('#D4A84B'),
        'chk': HexColor('#C4912A'),
        'footer_bg': HexColor('#FFFCF2'),
        'footer_color': HexColor('#8A5C0A'),
        'items': [
            ('لقب الراعي الاستراتيجي في كل إعلان', None),
            ('جناح رئيسي بأفضل موقع قرب المسرح', None),
            ('كلمة افتتاحية + Branding على المسرح', None),
            ('رعاية جلسة رئيسية باسمك + Panel', None),
            ('Roll-up + فيديو مقابلة رسمية', 'تقرير إحصائي تفصيلي بعد المعرض'),
            ('درع فاخر على المسرح + دعوات VIP', None),
        ],
        'footer': 'أعلى مستوى تأثير وحضور في أكبر معرض فنتك أكاديمي بالرياض',
        'x': RIGHT_X,
    },
    {
        'title': 'الراعي الذهبي',
        'type':  'Gold Sponsor',
        'price': '6,000', 'tag': 'LIMITED',
        'hdr': HexColor('#9A7020'), 'hdr2': HexColor('#B8913A'),
        'chk': HexColor('#9A7020'),
        'footer_bg': HexColor('#FDFAF0'),
        'footer_color': HexColor('#7A5810'),
        'items': [
            ('لقب الراعي الذهبي في كل إعلان ومنشور', None),
            ('جناح بموقع استراتيجي متميز', None),
            ('المشاركة في الأركان الخمسة + الجلسات', None),
            ('شعار في جميع المواد التسويقية والكتيّب', None),
            ('توزيع مواد دعائية في حقائب الحضور', None),
            ('درع تكريمي + ملخص إحصائي + دعوات VIP', None),
        ],
        'footer': 'حضور إعلامي ثابت وتفاعل مباشر مع أكثر من 3000 طالب',
        'x': LEFT_X,
    },
    {
        'title': 'شركاء النجاح',
        'type':  'In-Kind Partners',
        'price': 'عيني', 'tag': 'OPEN',
        'hdr': HexColor('#0A6B5C'), 'hdr2': HexColor('#0D7D6C'),
        'chk': HexColor('#0D7D6C'),
        'footer_bg': HexColor('#EDFAF7'),
        'footer_color': HexColor('#0A5245'),
        'items': [
            ('شريك أكاديمي', 'شهادات المشاركين + بوث + ذكر في الافتتاح'),
            ('شريك مطبوعات', 'شعار على مطبوعات المعرض + بانر + الدعوات'),
            ('شريك تكنولوجي', 'منصة أو نظام مقابل ذكر رسمي + شاشات'),
            ('شريك النجاح', 'هدايا داخل كيس الهدية + شكر في الختام'),
        ],
        'footer': 'ذكر رسمي وشارة "شريك معتمد" مقابل دعمك العيني',
        'x': RIGHT_X,
        'half_height': True,
    },
    {
        'title': 'المشاركون في المعرض',
        'type':  'Exhibitors',
        'price': 'بوث', 'tag': 'OPEN',
        'hdr': HexColor('#175E42'), 'hdr2': HexColor('#1B6B52'),
        'chk': HexColor('#1B6B52'),
        'footer_bg': HexColor('#EEF9F5'),
        'footer_color': HexColor('#103D2A'),
        'items': [
            ('البوث الخاص — أحضر هويتك البصرية', 'مساحة + كهرباء + إنترنت + دعم لوجستي'),
            ('البوث المقدّم — مجهز بالكامل', 'بوث احترافي + شاشة 55" + أثاث'),
            ('لوحات وإشارات في خريطة المعرض', None),
            ('ذكر رسمي في جميع المواد الإعلامية', None),
        ],
        'footer': 'كلا الخيارين يشملان الدعم اللوجستي الكامل طوال اليومين',
        'x': LEFT_X,
        'half_height': True,
    },
]

# Two-row layout: top row has 2 tall cards, bottom row has 2 shorter cards
TOP_CARD_H   = 310
BOT_CARD_H   = 225
TOP_CARD_Y   = CARD_Y + BOT_CARD_H + 12
BOT_CARD_Y   = CARD_Y

def draw_package_card(c, card, x, y, cw, ch):
    HDR_H = 85
    r = 12
    # White card body
    draw_rounded_rect(c, x, y, cw, ch, radius=r, fill_color=C_CARD_BG)
    # Colored header (clip to top round corners)
    c.saveState()
    p = c.beginPath()
    p.moveTo(x+r, y+ch)
    p.arcTo(x, y+ch-r, x+r*2, y+ch, 90, 90)
    p.lineTo(x, y+ch-HDR_H)
    p.lineTo(x+cw, y+ch-HDR_H)
    p.lineTo(x+cw, y+ch-r)
    p.arcTo(x+cw-r*2, y+ch-r, x+cw, y+ch, 0, 90)
    p.close()
    c.clipPath(p, fill=0)
    # header gradient (simulated with two rects)
    draw_rect(c, x, y+ch-HDR_H, cw, HDR_H, card['hdr'])
    draw_rect(c, x, y+ch-HDR_H, cw//2, HDR_H, card['hdr2'], alpha=0.6)
    # decorative circle in header
    c.setFillColor(HexColor('#FFFFFF'), alpha=0.07)
    c.circle(x + cw - 20, y+ch - HDR_H//2 + 30, 60, fill=1, stroke=0)
    c.restoreState()

    # Type label (en)
    c.saveState()
    c.setFont('NotoArabic', 7.5)
    c.setFillColor(HexColor('#FFFFFFB0'))
    c.drawRightString(x + cw - 18, y+ch-18, card['type'])
    c.restoreState()

    # Title (ar)
    c.saveState()
    c.setFont('NotoArabicBold', 15)
    c.setFillColor(C_WHITE)
    c.drawRightString(x + cw - 18, y+ch-38, ar(card['title']))
    c.restoreState()

    # Price box
    price_w, price_h = 76, 58
    px = x + 14
    py = y + ch - HDR_H + (HDR_H - price_h)//2
    draw_rounded_rect(c, px, py, price_w, price_h, radius=10,
                      fill_color=HexColor('#FFFFFF26'),
                      stroke_color=HexColor('#FFFFFF4D'), stroke_width=1)
    c.saveState()
    c.setFont('NotoArabicBold', 17 if len(card['price']) > 3 else 20)
    c.setFillColor(C_WHITE)
    c.drawCentredString(px + price_w/2, py + price_h - 24, ar(card['price']))
    c.restoreState()
    c.saveState()
    c.setFont('NotoArabic', 6.5)
    c.setFillColor(HexColor('#FFFFFFB0'))
    c.drawCentredString(px + price_w/2, py + price_h - 36, ar('ريال سعودي') if card['price'][0].isdigit() else '')
    c.restoreState()
    c.saveState()
    c.setFont('NotoArabic', 6)
    c.setFillColor(HexColor('#FFFFFF80'))
    c.drawCentredString(px + price_w/2, py + 8, card['tag'])
    c.restoreState()

    # Body items
    footer_h = 36
    body_y_top = y + ch - HDR_H - 2
    body_y_bot = y + footer_h + 2
    body_h = body_y_top - body_y_bot
    items = card['items']
    item_h = body_h / len(items)

    for j, (main, sub) in enumerate(items):
        iy = body_y_top - (j + 0.5) * item_h
        # divider
        if j > 0:
            c.saveState()
            c.setStrokeColor(HexColor('#00000010')); c.setLineWidth(0.6)
            c.line(x+10, body_y_top - j*item_h, x+cw-10, body_y_top - j*item_h)
            c.restoreState()
        # checkmark circle
        chk_x = x + 18
        chk_y = iy + (3 if sub else 0)
        c.saveState()
        c.setFillColor(card['chk'])
        c.circle(chk_x, chk_y, 7, fill=1, stroke=0)
        c.setFont('NotoArabic', 7)
        c.setFillColor(C_WHITE)
        c.drawCentredString(chk_x, chk_y - 3, '✓')
        c.restoreState()
        # main text
        c.saveState()
        c.setFont('NotoArabicBold', 9.5)
        c.setFillColor(C_TEXT_DARK)
        c.drawRightString(x + cw - 16, iy + (5 if sub else -3), ar(main))
        c.restoreState()
        # sub text
        if sub:
            c.saveState()
            c.setFont('NotoArabic', 7.5)
            c.setFillColor(HexColor('#444444'))
            c.drawRightString(x + cw - 16, iy - 8, ar(sub))
            c.restoreState()

    # Footer band
    c.saveState()
    p2 = c.beginPath()
    p2.moveTo(x, y+footer_h)
    p2.lineTo(x+cw, y+footer_h)
    p2.lineTo(x+cw, y+r)
    p2.arcTo(x+cw-r*2, y, x+cw, y+r*2, 0, -90)
    p2.lineTo(x+r, y)
    p2.arcTo(x, y, x+r*2, y+r*2, 270, -90)
    p2.close()
    c.clipPath(p2, fill=0)
    c.setFillColor(card['footer_bg'])
    c.rect(x, y, cw, footer_h, fill=1, stroke=0)
    c.restoreState()
    c.saveState()
    c.setFont('NotoArabic', 8)
    c.setFillColor(card['footer_color'])
    c.drawCentredString(x + cw/2, y + 12, ar(card['footer']))
    c.restoreState()

# Draw top two cards (tall)
draw_package_card(c, cards[0], RIGHT_X, TOP_CARD_Y, CARD_W, TOP_CARD_H)
draw_package_card(c, cards[1], LEFT_X,  TOP_CARD_Y, CARD_W, TOP_CARD_H)
# Draw bottom two cards (shorter)
draw_package_card(c, cards[2], RIGHT_X, BOT_CARD_Y, CARD_W, BOT_CARD_H)
draw_package_card(c, cards[3], LEFT_X,  BOT_CARD_Y, CARD_W, BOT_CARD_H)


# ════════════════════════════════════════════════════════════════════════
# SECTION 4: ORGS  y: 600 → 810
# ════════════════════════════════════════════════════════════════════════
ORG_TOP = PKG_BOT
ORG_H   = 210
ORG_BOT = ORG_TOP - ORG_H

draw_rect(c, 0, ORG_BOT, W, ORG_H, HexColor('#071914'))
c.saveState()
c.setStrokeColor(C_GREEN, alpha=0.1); c.setLineWidth(0.8)
c.line(0, ORG_TOP, W, ORG_TOP)
c.restoreState()

# Label
c.saveState()
c.setFont('NotoArabic', 8.5)
c.setFillColor(C_GREEN2)
c.drawRightString(W-50, ORG_TOP - 28, ar('أبرز المشاركين المتوقعين'))
c.restoreState()

# Org chips
orgs = [
    ('البنك المركزي السعودي', 'SAMA',   '#3DAA86', '#0A2A1A'),
    ('SDAIA',                 'هيئة البيانات', '#5B8DD9', '#0A1A2A'),
    ('فنتك السعودية',         'Fintech Saudi', '#3DAA86', '#0A2A1A'),
    ('وزارة الاستثمار',       'Ministry of Investment', '#5B8DD9', '#0A1A2A'),
    ('الأكاديمية المالية',    'Financial Academy', '#7AAEDD', '#0A1820'),
    ('STC Bank',              'مصرف رقمي', '#A865D4', '#1A0A2A'),
    ('بنك الإنماء',           'Alinma Bank', '#5B8DD9', '#0A1A2A'),
    ('بنك الرياض',            'Riyad Bank',  '#5B8DD9', '#0A1A2A'),
    ('SIDF',                  'صندوق التنمية', '#5B8DD9', '#0A1A2A'),
    ('تمارا',                 'Tamara·BNPL', '#E8884E', '#2A1A0A'),
    ('Tabby',                 'BNPL',        '#3DAAA0', '#0A2A28'),
    ('EY',                    'Ernst & Young','#EAC326', '#2A2000'),
    ('PwC',                   'PricewaterhouseCoopers','#E87870','#2A0A0A'),
    ('Urpay',                 'محفظة رقمية', '#A865D4', '#1A0A2A'),
]

# Layout chips in rows
chip_font_size = 9.5
padding_x, padding_y = 12, 5
gap_x, gap_y = 8, 7
row_h = 32
start_x = W - 50
start_y = ORG_TOP - 52
cur_x = start_x
cur_y = start_y

for name, en, color_hex, bg_hex in orgs:
    ar_name = ar(name)
    nw = c.stringWidth(ar_name, 'NotoArabicBold', chip_font_size)
    ew = c.stringWidth(en, 'NotoArabic', 7) if en != name else 0
    chip_content_w = max(nw, ew) + padding_x * 2 + 16  # +16 for dot
    if cur_x - chip_content_w < 50:
        cur_x = start_x
        cur_y -= row_h + gap_y

    cx = cur_x - chip_content_w
    cy = cur_y

    # Chip background
    draw_rounded_rect(c, cx, cy, chip_content_w, row_h, radius=9,
                      fill_color=HexColor(bg_hex),
                      stroke_color=HexColor(color_hex + '44'), stroke_width=1.2)
    # Color dot
    c.saveState()
    c.setFillColor(HexColor(color_hex))
    c.circle(cx + chip_content_w - 14, cy + row_h/2, 4, fill=1, stroke=0)
    c.restoreState()
    # Name
    c.saveState()
    c.setFont('NotoArabicBold', chip_font_size)
    c.setFillColor(HexColor(color_hex))
    c.drawRightString(cx + chip_content_w - 22, cy + row_h/2 + 1, ar_name)
    c.restoreState()

    cur_x -= chip_content_w + gap_x


# ════════════════════════════════════════════════════════════════════════
# SECTION 5: CONTACT BAR  y: 90 → 600
# ════════════════════════════════════════════════════════════════════════
CBAR_TOP = ORG_BOT
CBAR_H   = 190
CBAR_BOT = CBAR_TOP - CBAR_H

draw_rect(c, 0, CBAR_BOT, W, CBAR_H, HexColor('#0A2016'))
c.saveState()
c.setFillColor(HexColor('#1B6B52'), alpha=0.18)
c.ellipse(W-50, CBAR_BOT+CBAR_H+80, W+200, CBAR_BOT-80, fill=1, stroke=0)
c.restoreState()
c.saveState()
c.setStrokeColor(C_GREEN, alpha=0.25); c.setLineWidth(1)
c.line(0, CBAR_TOP, W, CBAR_TOP)
c.restoreState()

# CTA text
c.saveState()
c.setFont('NotoArabic', 9)
c.setFillColor(HexColor('#5A7A6A'))
c.drawRightString(W-50, CBAR_BOT + CBAR_H - 36, ar('تواصل مع الفريق الآن'))
c.restoreState()

c.saveState()
c.setFont('NotoArabicBold', 26)
c.setFillColor(C_WHITE)
c.drawRightString(W-50, CBAR_BOT + CBAR_H - 68, ar('انضم إلى'))
c.restoreState()

c.saveState()
c.setFont('NotoArabicBold', 26)
c.setFillColor(C_GREEN2)
c.drawRightString(W-50, CBAR_BOT + CBAR_H - 100, ar('روافد فنتك 2026'))
c.restoreState()

# Contact boxes
contacts = [
    ('📧', 'pr.technationclub@gmail.com'),
    ('📱', '+966 53 483 1944'),
]
ci_w, ci_h = 370, 42
ci_x = 50
for i, (ic, val) in enumerate(contacts):
    ci_y = CBAR_BOT + CBAR_H - 65 - i * (ci_h + 10)
    draw_rounded_rect(c, ci_x, ci_y, ci_w, ci_h, radius=10,
                      fill_color=HexColor('#FFFFFF10'),
                      stroke_color=HexColor('#FFFFFF22'), stroke_width=1)
    # Icon box
    draw_rounded_rect(c, ci_x+8, ci_y+7, 28, 28, radius=7,
                      fill_color=C_DARK_GRN)
    c.saveState()
    c.setFont('NotoArabic', 10)
    c.setFillColor(C_WHITE)
    c.drawCentredString(ci_x+22, ci_y+16, ic)
    c.restoreState()
    # Value
    c.saveState()
    c.setFont('NotoArabicBold', 10.5)
    c.setFillColor(C_WHITE)
    c.drawString(ci_x+44, ci_y+15, val)
    c.restoreState()


# ════════════════════════════════════════════════════════════════════════
# FOOTER  y: 0 → 90
# ════════════════════════════════════════════════════════════════════════
FOOT_H = CBAR_BOT
draw_rect(c, 0, 0, W, FOOT_H, HexColor('#040C06'))
c.saveState()
c.setStrokeColor(C_GREEN, alpha=0.07); c.setLineWidth(0.6)
c.line(0, FOOT_H, W, FOOT_H)
c.restoreState()

foot_items = [
    (50,   'NotoArabic',     9, HexColor('#383838'), 'جميع الحقوق محفوظة © 2026', 'left'),
    (W/2,  'NotoArabicBold', 9.5, C_GREEN2, 'معرض روافد فنتك 2026', 'center'),
    (W-50, 'NotoArabic',     9, HexColor('#383838'), 'جامعة الإمام محمد بن سعود الإسلامية · الرياض', 'right'),
]
for fx, ff, fs, fc, ft, fa in foot_items:
    c.saveState()
    c.setFont(ff, fs)
    c.setFillColor(fc)
    if fa == 'center':
        c.drawCentredString(fx, FOOT_H/2 - 4, ar(ft))
    elif fa == 'right':
        c.drawRightString(fx, FOOT_H/2 - 4, ar(ft))
    else:
        c.drawString(fx, FOOT_H/2 - 4, ft)
    c.restoreState()


# ── Save ──────────────────────────────────────────────────────────────────
c.save()
print(f'✅ PDF saved: {output_path}  ({W}×{H} pts)')
