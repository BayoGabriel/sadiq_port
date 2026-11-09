"""Generates branded placeholder images so the site renders complete until real
screenshots/photos are dropped in with the same filenames."""
import os
from PIL import Image, ImageDraw, ImageFont

INK = "#241d1a"; CREAM = "#f2ead9"
FONT = "fonts/SimplonMonoTrial-Regular.otf"
FONT_B = "fonts/SimplonMonoTrial-Bold.otf"

PROJECTS = {
    "boldswitch": ("#0b3d91", "BOLDSWITCH"),
    "boldswitch-business": ("#7c2d12", "BOLDSWITCH BUSINESS"),
    "lodapoint": ("#14532d", "LODAPOINT"),
    "bravoo": ("#4c1d95", "BRAVOO"),
}

CASE_KEYS = {
    "boldswitch": ["hero","card","dashboard","send","success","onboarding","tiers","facepay","snap","system","screens","receipt"],
    "boldswitch-business": ["hero","dashboard","link","qr","onboarding","status","collect","team","web","history","screens","store"],
    "lodapoint": ["hero","rider","driver","transporter","request","vehicle","track","schedule","fleet","web","screens","store"],
    "bravoo": ["hero","web","home","send","onboarding","verify","transfer","card","support","system","screens","site"],
}
WORK_THUMBS = ["boldswitch-card","boldswitch-hero","boldswitch-business-hero","boldswitch-business-dash",
               "lodapoint-hero","lodapoint-driver","bravoo-hero","bravoo-web"]
INDEX_TILES = ["boldswitch-1","boldswitch-2","boldswitch-3","boldswitch-4",
               "bsb-1","bsb-2","bsb-3","bsb-4",
               "loda-1","loda-2","loda-3","loda-4",
               "bravoo-1","bravoo-2","bravoo-3","bravoo-4"]
TILE_PROJECT = {"bsb": "boldswitch-business", "loda": "lodapoint"}

def font(sz, bold=False):
    try:
        return ImageFont.truetype(FONT_B if bold else FONT, sz)
    except Exception:
        return ImageFont.load_default()

def make(path, w, h, bg, title, sub):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)
    # subtle vignette band
    d.rectangle([0, int(h*0.55), w, h], fill=tuple(max(0, c-14) for c in Image.new("RGB",(1,1),bg).getpixel((0,0))))
    t, s = font(int(h*0.055), True), font(int(h*0.032))
    for txt, f, y, col in ((title, t, 0.62, CREAM), (sub, s, 0.72, CREAM), ("REPLACE WITH REAL IMAGE", s, 0.80, "#ffffff55")):
        bbox = d.textbbox((0,0), txt, font=f)
        d.text(((w-(bbox[2]-bbox[0]))/2, h*y), txt, font=f, fill=col)
    img.save(path, "JPEG", quality=88)

def slug_of(name): return TILE_PROJECT.get(name.split("-")[0], name.split("-")[0])

for slug, keys in CASE_KEYS.items():
    col, label = PROJECTS[slug]
    for k in keys:
        make(f"case/{slug}/{k}.jpg", 1400, 1000, col, label, k.replace("-", " ").upper())

for name in WORK_THUMBS:
    slug = name.rsplit("-",1)[0]
    col, label = PROJECTS[slug]
    make(f"work/{name}.jpg", 1200, 800, col, label, name.split("-")[-1].upper())

for name in INDEX_TILES:
    slug = slug_of(name)
    col, label = PROJECTS[slug]
    make(f"index/{name}.jpg", 900, 700, col, label, name.upper())

for slug in PROJECTS:
    col, label = PROJECTS[slug]
    make(f"share/{slug}.jpg", 1200, 630, col, f"{label} — Sadiq Abdulazeez", "product design case study")

make("share.jpg", 1200, 630, "#5e1a17", "SADIQ ABDULAZEEZ", "LEAD PRODUCT DESIGNER — ABUJA")
make("about/sadiq.jpg", 1000, 1250, "#241d1a", "SADIQ ABDULAZEEZ", "REPLACE WITH YOUR PHOTO")

# favicon pngs + logo svg
for path, sz in [("images/favicon-32.png", 64), ("images/apple-touch-icon.png", 360)]:
    img = Image.new("RGB", (sz, sz), "#5e1a17")
    d = ImageDraw.Draw(img)
    f = font(int(sz*0.62), True)
    bbox = d.textbbox((0,0), "S", font=f)
    d.text(((sz-(bbox[2]-bbox[0]))/2, (sz-(bbox[3]-bbox[1]))/2 - bbox[1]), "S", font=f, fill=CREAM)
    img.save(path)

open("logo-sadiq.svg", "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">'
    '<rect width="120" height="120" rx="60" fill="#241d1a"/>'
    '<text x="60" y="84" font-family="Georgia, \'Times New Roman\', serif" font-style="italic" '
    'font-size="72" fill="#f2ead9" text-anchor="middle">S&#8217;</text></svg>')
open("images/favicon.svg", "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">'
    '<rect width="120" height="120" rx="26" fill="#5e1a17"/>'
    '<text x="60" y="86" font-family="Georgia, \'Times New Roman\', serif" font-style="italic" '
    'font-size="76" fill="#f2ead9" text-anchor="middle">S</text></svg>')

print("placeholders generated")
