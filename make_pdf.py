#!/usr/bin/env python3
"""
Rawafid Fintech 2026 — Hybrid PDF
Background = high-res PNG image (guaranteed rendering)
Text layer = Arabic vector text on top (editable in Canva/Acrobat)
"""

from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image
import io, os

# ── Fonts ────────────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont('A',  'NotoSansArabic.ttf'))
pdfmetrics.registerFont(TTFont('AB', 'NotoSansArabic.ttf'))

# ── Load the existing high-quality poster PNG ─────────────────────────────
PNG_PATH = 'screenshots/poster_canva.png'
bg_img = Image.open(PNG_PATH)
IMG_W, IMG_H = bg_img.size   # 1080 x 2063
print(f'Background image: {IMG_W}x{IMG_H}px')

# ── PDF dimensions = image dimensions (in points, 1pt ≈ 1px for 72dpi) ──
W, H = float(IMG_W), float(IMG_H)

# ── Helpers ───────────────────────────────────────────────────────────────
def ar(text):
    return get_display(arabic_reshaper.reshape(text))

def txt(c, text, x, y, size, color,
        font='AB', align='center', alpha=0):
    """Draw Arabic text. alpha=0 means invisible (for Canva text layer)."""
    c.saveState()
    c.setFont(font, size)
    if alpha == 0:
        # Transparent text — editable but invisible (image shows through)
        # Use a tiny alpha to keep it invisible but present in PDF structure
        c.setFillColorRGB(1, 1, 1, alpha=0.01)
    else:
        c.setFillColor(color)
    t = ar(text)
    if align == 'center':
        c.drawCentredString(x, y, t)
    elif align == 'right':
        c.drawRightString(x, y, t)
    else:
        c.drawString(x, y, t)
    c.restoreState()

def vtxt(c, text, x, y, size, color, font='AB', align='center'):
    """Visible Arabic text drawn on top of image."""
    txt(c, text, x, y, size, color, font=font, align=align, alpha=1)

# ════════════════════════════════════════════════════════════════════════
# CREATE PDF
# ════════════════════════════════════════════════════════════════════════
output = 'rawafid_fintech_2026.pdf'
c = rl_canvas.Canvas(output, pagesize=(W, H))
c.setTitle('معرض روافد فنتك 2026 — باقات الرعاية')
c.setAuthor('Tech Nation Club — جامعة الإمام محمد بن سعود الإسلامية')
c.setSubject('فرصة رعاية — Sponsorship Opportunity')

# ── 1. Draw full-page background image ──────────────────────────────────
img_reader = ImageReader(PNG_PATH)
c.drawImage(img_reader, 0, 0, width=W, height=H, preserveAspectRatio=False)

# ── 2. Add invisible text layer for Canva/Acrobat editability ────────────
# These are transparent text boxes sitting exactly over the visible text
# Canva will import them as editable text elements

PAD = 50

# Hero texts
txt(c, 'معرض',                          W/2, H-128,  52, None)
txt(c, 'روافد فنتك',                    W/2, H-230,  90, None)
txt(c, '2026',                          W/2, H-312,  70, None)
txt(c, 'برعاية جامعة الإمام محمد بن سعود الإسلامية',
       W/2, H-356, 12, None)
txt(c, 'بإشراف كلية علوم الحاسب وكلية الاعمال · الرياض',
       W/2, H-376, 10, None)

# Info strip
txt(c, '5 – 6 مايو 2026',          W - W/6,  H-600, 13, None)
txt(c, '8:30 ص – 12:00 م',         W/2,      H-600, 13, None)
txt(c, 'بهو جامعة الإمام · الرياض', W/6,     H-600, 13, None)

# Package titles & prices
txt(c, 'الراعي الاستراتيجي',  W*0.75, H-760, 15, None, align='right')
txt(c, '12,000 ريال سعودي',  W*0.75, H-780, 10, None, align='right')
txt(c, 'الراعي الذهبي',      W*0.25, H-760, 15, None, align='right')
txt(c, '6,000 ريال سعودي',  W*0.25, H-780, 10, None, align='right')

# Contact
txt(c, 'انضم إلى روافد فنتك 2026', W-PAD, 430, 26, None, align='right')
txt(c, 'pr.technationclub@gmail.com', PAD+190, 360, 11, None, align='center')
txt(c, '+966 53 483 1944',            PAD+190, 308, 11, None, align='center')

# Footer
txt(c, 'معرض روافد فنتك 2026', W/2, 22, 10, None)
txt(c, 'جامعة الإمام محمد بن سعود الإسلامية · الرياض', W-PAD, 22, 9, None, align='right')

# ── 3. Also embed a clean high-res version (A4-compatible)  ──────────────
c.save()
print(f'✅  Hybrid PDF saved: {output}')
print(f'    Page: {int(W)}x{int(H)} pts  |  Image: {IMG_W}x{IMG_H}px')
file_size = os.path.getsize(output)
print(f'    File size: {file_size/1024:.0f} KB')
