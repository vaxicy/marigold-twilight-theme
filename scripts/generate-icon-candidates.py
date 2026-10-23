"""Marigold Twilight Theme - icon candidates.

Code-drawn marks, a light/dark contact sheet and an inline strip.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

DEEP = (82, 45, 96, 255)          # #522D60
PLUM = (128, 66, 110, 255)        # #80426E
ORANGE = (242, 166, 123, 255)     # #F2A67B
BUTTER = (255, 211, 139, 255)     # #FFD38B
PALE = (255, 236, 205, 255)
WHITE = (255, 255, 255, 255)

LIGHT_BG = (248, 242, 240, 255)
DARK_BG = (38, 24, 44, 255)
LIGHT_INK = (62, 36, 50, 255)
DARK_INK = (245, 226, 210, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def petal(cx, cy, ang, length, width, n=64):
    """An ellipse whose inner end sits on the centre point."""
    pts = []
    ca, sa = math.cos(ang), math.sin(ang)
    for i in range(n):
        t = 2 * math.pi * i / n
        x = length * 0.5 + length * 0.5 * math.cos(t)
        y = width * 0.5 * math.sin(t)
        pts.append((cx + x * ca - y * sa, cy + x * sa + y * ca))
    return pts


def rounded(draw, box, radius, fill):
    draw.rounded_rectangle([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                           radius=wd(radius), fill=fill)


# ---------------------------------------------------------------- candidates

def cand_bloom():
    img = canvas()
    d = ImageDraw.Draw(img)
    cx, cy = 512, 512

    for i in range(10):
        ang = 2 * math.pi * i / 10
        poly(d, petal(cx, cy, ang, 250, 86), PLUM)
    for i in range(8):
        ang = 2 * math.pi * i / 8 + math.pi / 8
        poly(d, petal(cx, cy, ang, 186, 70), DEEP)
    disc(d, (cx, cy), 118, ORANGE)
    disc(d, (cx, cy), 62, BUTTER)

    return finish(img)


def cand_petal_ring():
    img = canvas()
    d = ImageDraw.Draw(img)
    cx, cy = 512, 512

    for i in range(8):
        ang = 2 * math.pi * i / 8 - math.pi / 2
        colour = ORANGE if i % 2 == 0 else PLUM
        poly(d, petal(cx, cy, ang, 300, 96), colour)

    disc(d, (cx, cy), 146, DEEP)
    disc(d, (cx, cy), 96, BUTTER)

    return finish(img)


def cand_sunset_dip():
    img = canvas()
    d = ImageDraw.Draw(img)

    # sun sinking behind the horizon
    d.pieslice([scr((292, 400)), scr((732, 840))], 180, 360, fill=ORANGE)
    d.line([scr((186, 620)), scr((838, 620))], fill=DEEP, width=wd(30))
    for y, w in ((682, 250), (722, 158)):
        d.line([scr((512 - w, y)), scr((512 + w, y))], fill=BUTTER, width=wd(20))
    for y in (252, 304):
        d.line([scr((332, y)), scr((692, y))], fill=PLUM, width=wd(14))

    return finish(img)


def cand_stem():
    img = canvas()
    d = ImageDraw.Draw(img)
    cx, cy = 566, 360

    for i in range(8):
        ang = 2 * math.pi * i / 8
        poly(d, petal(cx, cy, ang, 178, 72), PLUM)
    disc(d, (cx, cy), 108, ORANGE)
    disc(d, (cx, cy), 54, BUTTER)

    stem = [(cx - 10, cy + 90), (470, 640), (420, 856)]
    d.line([scr(p) for p in stem], fill=DEEP, width=wd(30), joint="curve")

    poly(d, petal(432, 606, math.radians(196), 150, 64), PLUM)
    poly(d, petal(452, 712, math.radians(-24), 132, 58), PLUM)

    return finish(img)


def cand_lantern():
    img = canvas()
    d = ImageDraw.Draw(img)

    # glow
    disc(d, (512, 560), 300, (255, 211, 139, 60))
    disc(d, (512, 560), 214, (255, 211, 139, 90))

    rounded(d, (346, 372, 678, 762), 40, DEEP)
    disc(d, (512, 566), 128, ORANGE)
    disc(d, (512, 566), 72, BUTTER)
    # roof + handle
    poly(d, [(312, 372), (712, 372), (512, 250)], PLUM)
    d.arc([scr((436, 176)), scr((588, 288))], 200, 340, fill=PLUM, width=wd(26))
    # base
    rounded(d, (326, 762, 698, 812), 20, PLUM)

    return finish(img)


def cand_bloom_pair():
    img = canvas()
    d = ImageDraw.Draw(img)

    def flower(cx, cy, n_out, r_out, w_out, n_in, r_in, w_in):
        for i in range(n_out):
            poly(d, petal(cx, cy, 2 * math.pi * i / n_out, r_out, w_out), PLUM)
        for i in range(n_in):
            poly(d, petal(cx, cy, 2 * math.pi * i / n_in + math.pi / n_in, r_in, w_in), DEEP)
        disc(d, (cx, cy), r_in * 0.56, ORANGE)
        disc(d, (cx, cy), r_in * 0.28, BUTTER)

    flower(400, 424, 10, 226, 76, 8, 168, 62)
    flower(706, 664, 8, 148, 58, 6, 108, 46)

    return finish(img)


CANDIDATES = [
    ("01", "bloom", cand_bloom),
    ("02", "petal-ring", cand_petal_ring),
    ("03", "sunset-dip", cand_sunset_dip),
    ("04", "stem", cand_stem),
    ("05", "lantern", cand_lantern),
    ("06", "bloom-pair", cand_bloom_pair),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "MARIGOLD TWILIGHT THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
