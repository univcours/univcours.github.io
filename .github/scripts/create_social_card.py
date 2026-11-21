#!/usr/bin/env python3
"""Generate the public, non-sensitive Open Graph image for UnivCours S5."""
from pathlib import Path
from math import exp, sin
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
OUT = Path("econometrie-s5-2026/share-preview.jpg")
OUT.parent.mkdir(parents=True, exist_ok=True)

# Dark navy background with subtle teal/cobalt light accents.
img = Image.new("RGB", (W, H))
pix = img.load()
for y in range(H):
    for x in range(W):
        t = y / H
        base = [6 + 2 * t, 18 + 8 * t, 32 + 11 * t]
        glow1 = exp(-(((x - 960) / 420) ** 2 + ((y - 40) / 290) ** 2) * 1.8)
        glow2 = exp(-(((x - 70) / 350) ** 2 + ((y - 530) / 230) ** 2) * 1.7)
        pix[x, y] = tuple(max(0, min(255, int(c))) for c in (
            base[0] + 5 * glow1 + 0 * glow2,
            base[1] + 33 * glow1 + 35 * glow2,
            base[2] + 45 * glow1 + 35 * glow2,
        ))
img = img.convert("RGBA")
a = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(a)

def face(size, bold=False):
    files = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    file = files[0 if bold else 1]
    return ImageFont.truetype(file, size)

WHITE = (246, 250, 254, 255)
MUTED = (175, 207, 219, 255)
TEAL = (75, 232, 215, 255)
CYAN = (61, 198, 230, 255)
GOLD = (232, 190, 118, 255)

# Horizontal grid and peripheral orbital shapes.
for xx in range(600, 1190, 48):
    d.line((xx, 80, xx, 500), fill=(85, 177, 195, 18), width=1)
for yy in range(100, 500, 48):
    d.line((600, yy, 1180, yy), fill=(85, 177, 195, 16), width=1)
for radius in range(200, 330, 60):
    d.ellipse((865-radius, 205-radius, 865+radius, 205+radius), outline=(60, 181, 209, 18), width=2)

# Logo: geometric open book.
d.rounded_rectangle((58, 41, 103, 92), radius=10, fill=(19, 67, 77, 255), outline=(75, 232, 215, 255), width=2)
d.line([(68, 60), (80, 64), (80, 78), (68, 74), (68, 60)], fill=WHITE, width=3, joint="curve")
d.line([(80, 64), (93, 60), (93, 74), (80, 78)], fill=WHITE, width=3, joint="curve")
d.text((117, 36), "UNIV", font=face(44, True), fill=WHITE)
d.text((252, 36), "COURS", font=face(44, True), fill=TEAL)
d.rounded_rectangle((950, 48, 1139, 95), radius=23, fill=(13, 66, 73, 215), outline=(70, 222, 210, 145), width=2)
d.text((979, 58), "SEMESTRE 5", font=face(19, True), fill=(198, 254, 245, 255))

d.text((61, 121), "BIBLIOTHÈQUE DE COURS EN LIGNE", font=face(19, True), fill=TEAL)

# Large readable headline, underline, and content subtitle.
d.text((58, 159), "ÉCONOMÉTRIE S5", font=face(61, True), fill=WHITE, stroke_width=0)
d.rounded_rectangle((62, 239, 490, 246), radius=3, fill=TEAL)
d.text((62, 266), "Cours · TD · Exercices · Documents", font=face(24, False), fill=MUTED)
d.text((63, 305), "Ouvrez chaque document directement sur le site", font=face(18, False), fill=(180, 217, 228, 255))

# Two prominent statistic cards.
for x, label, count, ww in [(61, "FICHIERS", "39", 225), (300, "MATIÈRES", "11", 234)]:
    d.rounded_rectangle((x, 368, x + ww, 469), radius=18, fill=(13, 54, 70, 225), outline=(65, 151, 172, 255), width=2)
    d.text((x + 22, 373), count, font=face(50, True), fill=TEAL)
    d.text((x + 109, 414), label, font=face(16, True), fill=WHITE)

# Chart illustration on the right.
d.rounded_rectangle((705, 153, 1129, 431), radius=22, fill=(13, 38, 56, 210), outline=(61, 116, 148, 165), width=2)
d.text((733, 174), "Économie & statistiques", font=face(18, True), fill=MUTED)
left, bottom, right, top = 748, 370, 1093, 232
d.line((left, top, left, bottom, right, bottom), fill=(155, 204, 213, 190), width=3)
for k in range(1, 6):
    x = left + k * 51
    y = bottom - k * 21
    d.ellipse((x - 4, y - 4, x + 4, y + 4), fill=TEAL)
    d.ellipse((x + 9, y + 12, x + 17, y + 20), fill=CYAN)
for i in range(0, 320, 4):
    x1 = left + i
    y1 = bottom - int(17 + i * .35)
    x2 = min(right, x1 + 5)
    y2 = bottom - int(17 + min(320, i + 5) * .35)
    d.line((x1, y1, x2, y2), fill=(226, 249, 251, 255), width=3)
d.text((764, 394), "Régression · Probabilités · Analyse", font=face(14, False), fill=(177, 206, 219, 255))

# Bottom WhatsApp source banner — truthful provenance, no private group info.
d.rounded_rectangle((58, 492, 1142, 584), radius=22, fill=(12, 53, 63, 250), outline=(74, 228, 208, 210), width=3)
d.ellipse((78, 511, 136, 568), fill=(34, 192, 114, 255))
d.text((93, 515), "✓", font=face(34, True), fill=WHITE)
d.text((154, 506), "Ressources et liens directs issus", font=face(26, True), fill=WHITE)
d.text((154, 541), "du groupe WhatsApp des étudiants", font=face(26, True), fill=TEAL)
d.text((61, 598), "UNIVCOURS · FICHIERS CLASSÉS PAR MATIÈRE", font=face(13, True), fill=(139, 182, 197, 255))

img = Image.alpha_composite(img, a).convert("RGB")
img.save(OUT, "JPEG", quality=87, optimize=True, subsampling=0)
assert img.size == (1200, 630)
print(f"CREATED {OUT} 1200x630 {OUT.stat().st_size} bytes")
