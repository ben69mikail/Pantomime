#!/usr/bin/env python3
"""Konvertiert Quell-Fotos -> WebP (optimiert) und macht das Logo transparent.
Quelle: assets/img-src/  Ziel: assets/img/
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img-src"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

MAX_W = 1600          # Fotos auf max. 1600px Breite begrenzen
QUALITY = 80

def clean_name(p: Path) -> str:
    n = p.stem.lower()
    for a, b in [(" ", "-"), ("_", "-"), ("ä", "ae"), ("ö", "oe"), ("ü", "ue")]:
        n = n.replace(a, b)
    while "--" in n:
        n = n.replace("--", "-")
    return n

def to_webp(p: Path):
    img = Image.open(p).convert("RGB")
    if img.width > MAX_W:
        h = round(img.height * MAX_W / img.width)
        img = img.resize((MAX_W, h), Image.LANCZOS)
    dst = OUT / (clean_name(p) + ".webp")
    img.save(dst, "WEBP", quality=QUALITY, method=6)
    return dst, img.size

def logo_transparent(p: Path, out_name: str):
    """Rand-Weiss per Flood-Fill von den Ecken entfernen, Innen-Weiss (Mime-Gesicht) bleibt."""
    img = Image.open(p).convert("RGBA")
    w, h = img.size
    # Flood-Fill auf einer Kopie zum Erkennen der zusammenhaengenden Randflaeche
    mask = img.copy()
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1),
             (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]
    fill = (255, 0, 255, 0)  # Marker
    for s in seeds:
        try:
            ImageDraw.floodfill(mask, s, fill, thresh=40)
        except Exception:
            pass
    px_m = mask.load()
    px = img.load()
    for y in range(h):
        for x in range(w):
            if px_m[x, y] == fill:
                px[x, y] = (255, 255, 255, 0)
    # auf Inhalt zuschneiden
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    img.save(OUT / out_name, "WEBP", quality=92, method=6, lossless=False)
    # zusaetzlich PNG fuer Favicon-Quelle
    img.save(OUT / out_name.replace(".webp", ".png"), "PNG")
    return img.size

def make_og(src_webp_name: str):
    """1200x630 OG-Bild aus einem Hero-Foto (zentriert gecroppt)."""
    src = OUT / src_webp_name
    img = Image.open(src).convert("RGB")
    tw, th = 1200, 630
    scale = max(tw / img.width, th / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = (img.width - tw) // 2
    top = (img.height - th) // 3   # leicht nach oben -> Gesicht im Bild
    img = img.crop((left, top, left + tw, top + th))
    img.save(OUT / "og-pantomime.jpg", "JPEG", quality=86)
    img.save(OUT / "og-pantomime.webp", "WEBP", quality=82, method=6)

photos = [p for p in SRC.iterdir()
          if p.suffix.lower() in (".jpg", ".jpeg", ".png") and not p.stem.upper().startswith("LOGO")]
for p in sorted(photos):
    dst, size = to_webp(p)
    print(f"  {p.name:46s} -> {dst.name:42s} {size[0]}x{size[1]}")

print("Logo transparent:")
print("  haupt:", logo_transparent(SRC / "LOGO-Pantomime.png", "logo.webp"))
print("  wide :", logo_transparent(SRC / "LOGO-Pantomime-wide.png", "logo-wide.webp"))

make_og("cropped-pantomime-11.webp")
print("OG-Bild erzeugt.")
print("Fertig. Dateien in:", OUT)
