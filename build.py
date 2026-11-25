#!/usr/bin/env python3
"""Build The Home Pilates Edit static site into this directory."""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "images"
DATA = ROOT / "data"
POSTS = ROOT / "posts"
ASSETS = ROOT / "assets"

SITE_NAME = "The Home Pilates Edit"
SITE_URL = "https://matt0315.github.io/home-pilates-edit"
PRICE_DATE = "25 November 2026"
PRICE_ZONE = "Australia/Perth"

# --- Products / posts -------------------------------------------------------

PRODUCTS = [
    {
        "id": "zanzer-grip-socks",
        "group": "Grip socks",
        "title": "A $14 four-pack of reformer grip socks, if you’re just starting",
        "card": "ZANZER grip socks",
        "meta": "Amazon AU · from $14.44 for a 4-pack",
        "price": 14.44,
        "price_was": 16.99,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the 4-pack option we opened (ASIN B0D3DT4YXK). Other pack sizes and colours on the same listing were cheaper or dearer on the Women’s Yoga Socks bestsellers list the same day, so check the option you actually want. Typical price shown on the page was $16.99.",
        "url": "https://www.amazon.com.au/dp/B0D3DT4YXK",
        "network": "amazon",
        "retailer": "Amazon AU",
        "image": "zanzer-grip-socks.jpg",
        "image_kind": "AI-generated illustration",
        "alt": "AI-generated illustration of cream ankle grip socks on a dark mat in a sunlit room. Not a photo of the exact ZANZER pair, and not a customer review.",
        "cta": "View on Amazon AU",
    },
    {
        "id": "all-fenix-grip-socks",
        "group": "Grip socks",
        "title": "All Fenix pilates grip socks: the $17 Australian pair",
        "card": "All Fenix grip socks",
        "meta": "allfenix.com · $17, was $24.99",
        "price": 17,
        "price_was": 24.99,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the black pair. The page showed $17, marked down from $24.99, during All Fenix’s Black Friday sale period (29 October to 30 November 2026). Sale items in that window are listed as final sale unless faulty. Standard AU shipping was $11.15, free over $150.",
        "url": "https://allfenix.com/products/pilates-grip-socks-black",
        "network": "commission-factory",
        "retailer": "All Fenix",
        "image": "all-fenix-grip-socks.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a simple black ankle sock with dotted grip on the sole, on a warm paper background. Not a brand photo.",
        "cta": "View at All Fenix",
    },
    {
        "id": "moveactive-crew-socks",
        "group": "Grip socks",
        "title": "MoveActive’s black crew grip socks, the studio staple",
        "card": "MoveActive crew grip socks",
        "meta": "moveactive.com.au · $22.95",
        "price": 22.95,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for Crew Grip Socks in black. Free standard shipping on orders over $65. Delivery to WA was listed as 7–10 business days standard, 3–5 days express.",
        "url": "https://moveactive.com.au/products/crew-non-slip-grip-socks-black",
        "network": "awin",
        "retailer": "MoveActive",
        "image": "moveactive-crew-socks.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a black crew sock with a dotted grip sole, on a sage-tinted paper background. Not a brand photo.",
        "cta": "View at MoveActive",
    },
    {
        "id": "wildbody-seafree-leggings",
        "group": "Clothing",
        "title": "WildBody’s organic cotton leggings, made for actual work",
        "card": "WildBody SeaFree leggings",
        "meta": "wildbody.com.au · $139",
        "price": 139,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the SeaFree Organic Cotton Leggings in Cacao: $139 AUD. Free standard shipping over $189 AUD.",
        "url": "https://www.wildbody.com.au/products/seafree-leggings",
        "network": "commission-factory",
        "retailer": "WildBody",
        "image": "wildbody-seafree-leggings.jpg",
        "image_kind": "AI-generated illustration",
        "alt": "AI-generated illustration of a person in brown high-waisted leggings and a white crop top, taking a mirror photo. Approximate likeness only — the real SeaFree leggings are listed with no front seam, which this image does not show accurately. Not a customer review.",
        "cta": "View at WildBody",
    },
    {
        "id": "lululemon-align-crop",
        "group": "Clothing",
        "title": "lululemon Align No Line crop, on sale at $89",
        "card": "lululemon Align crop",
        "meta": "lululemon AU · $89, was $129",
        "price": 89,
        "price_was": 129,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the Align No Line High-Rise Crop 21\": $89, regularly $129. The page said the style is not eligible for change-of-mind returns, and that shipping is free with a lululemon account.",
        "url": "https://www.lululemon.com.au/en-au/p/lululemon-align-no-line-high-rise-crop-21/hff1a0vntw",
        "network": "lululemon",
        "retailer": "lululemon AU",
        "image": "lululemon-align-crop.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of cropped high-waisted leggings in a deep forest green, on a cream background. Not a brand photo and not a product shot of the Align pant.",
        "cta": "View at lululemon AU",
    },
    {
        "id": "spopal-pilates-kit",
        "group": "Kits and props",
        "title": "The $30 Spopal pilates kit, and what a budget set is actually for",
        "card": "Spopal 22-piece kit",
        "meta": "Amazon AU · $29.99",
        "price": 29.99,
        "price_was": 39.99,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the 22-piece Spopal Home Pilates Ring Set (ASIN B0GXKHCJX1): $29.99, shown with 25% off. It was listed as in stock, shipped from Amazon and sold by YoujihuiDirect. It also sat at #1 on Amazon AU’s Pilates Sets bestsellers list that day.",
        "url": "https://www.amazon.com.au/dp/B0GXKHCJX1",
        "network": "amazon",
        "retailer": "Amazon AU",
        "image": "spopal-pilates-kit.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a pilates ring, small ball, loop bands and a pair of socks arranged on a warm pink-sand background. Generic props, not a photo of the Spopal kit.",
        "cta": "View on Amazon AU",
    },
    {
        "id": "larfafa-pilates-kit",
        "group": "Kits and props",
        "title": "LarFaFa’s pilates kit: more reviews, slower delivery",
        "card": "LarFaFa pilates kit",
        "meta": "Amazon AU · $38.35",
        "price": 38.35,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the LarFaFa Pilates Kit listing (ASIN B0FTFMN9QN): $38.35. A bestsellers list the same day still showed $35.99. The page said it is usually dispatched in 2–3 days, with delivery estimated 14–17 December, from a third-party seller rather than Amazon itself.",
        "url": "https://www.amazon.com.au/dp/B0FTFMN9QN",
        "network": "amazon",
        "retailer": "Amazon AU",
        "image": "larfafa-pilates-kit.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a pilates ring, ball and folded resistance bands on a muted blush background. Generic props, not a photo of the LarFaFa kit.",
        "cta": "View on Amazon AU",
    },
    {
        "id": "moveactive-pilates-ring",
        "group": "Kits and props",
        "title": "A $45 pilates ring from MoveActive",
        "card": "MoveActive pilates ring",
        "meta": "moveactive.com.au · $45",
        "price": 45,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the Pilates Ring in black: $45 AUD. Listed as 37 cm (14.5 in) across, with a fibreglass inner ring, EVA foam and TPR handles. Free shipping over $65.",
        "url": "https://moveactive.com.au/products/new-pilates-ring-black",
        "network": "awin",
        "retailer": "MoveActive",
        "image": "moveactive-pilates-ring.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a black pilates ring with padded handles on a sage paper background. Not a brand photo.",
        "cta": "View at MoveActive",
    },
    {
        "id": "moveactive-resistance-band",
        "group": "Kits and props",
        "title": "MoveActive’s medium loop band, for legs and side-lying work",
        "card": "MoveActive medium band",
        "meta": "moveactive.com.au · $28",
        "price": 28,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the Medium Resistance Band in black: $28 AUD. Listed dimensions are 32 cm × 8 cm. Free shipping over $65.",
        "url": "https://moveactive.com.au/products/medium-resistance-band-black",
        "network": "awin",
        "retailer": "MoveActive",
        "image": "moveactive-resistance-band.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a short black fabric loop resistance band on a sand background. Not a brand photo.",
        "cta": "View at MoveActive",
    },
    {
        "id": "moveactive-reformer-mat",
        "group": "Mats",
        "title": "A washable mat for the reformer carriage, not the floor",
        "card": "MoveActive reformer mat",
        "meta": "moveactive.com.au · $79",
        "price": 79,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the Microfibre Reformer Mat in Ivory: $79 AUD. Listed size is 94 × 56 cm, plus a 27 × 19 cm neck section, at 2 mm thick. Free shipping over $65.",
        "url": "https://moveactive.com.au/products/microfibre-reformer-mat-ivory",
        "network": "awin",
        "retailer": "MoveActive",
        "image": "moveactive-reformer-mat.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a slim ivory reformer carriage mat with a narrower head section, on a warm wood-toned background. Not a brand photo.",
        "cta": "View at MoveActive",
    },
    {
        "id": "manduka-cloud-mat",
        "group": "Mats",
        "title": "Manduka’s 12 mm Cloud mat for floor pilates at home",
        "card": "Manduka Cloud pilates mat",
        "meta": "manduka.com.au · $229.95",
        "price": 229.95,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) on manduka.com.au: $229.95 AUD for the CLOUD Pilates Mat 12 mm. The site advertised free shipping on orders from $200.",
        "url": "https://manduka.com.au/products/cloud-pilates-mat-12mm",
        "network": "direct",
        "retailer": "Manduka Australia",
        "image": "manduka-cloud-mat.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a thick, dark floor pilates mat unrolled on pale timber. Not a brand photo and not the Manduka logo.",
        "cta": "View at Manduka Australia",
    },
    {
        "id": "lifespan-contour-folding",
        "group": "Reformers",
        "title": "Lifespan’s folding wooden reformer, currently $1,399",
        "card": "Lifespan Contour Folding",
        "meta": "lifespanfitness.com.au · $1,399, was $2,399",
        "price": 1399,
        "price_was": 2399,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the Contour Folding Wooden Pilates Reformer Machine in beige (LFRF-CONTFLD2B): $1,399, with an RRP of $2,399. The page marked it in stock. This is a bulky item; check current delivery quotes for your address, especially in WA.",
        "url": "https://www.lifespanfitness.com.au/products/contour-folding-wooden-pilates-reformer-machine-beige",
        "network": "direct",
        "retailer": "Lifespan Fitness",
        "image": "lifespan-contour-folding.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a folding wooden pilates reformer in a simple home space, seen from the side. Generic machine, not a brand photo.",
        "cta": "View at Lifespan Fitness",
    },
    {
        "id": "your-reformer-folding",
        "group": "Reformers",
        "title": "Your Reformer’s folding machine, the $2,495 home option",
        "card": "Your Reformer YR Original Folding",
        "meta": "yourreformer.com.au · $2,495, was $2,995",
        "price": 2495,
        "price_was": 2995,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) for the YR Original Folding: $2,495, regularly $2,995. The product page we opened also indicated the sale item may be sold out, so confirm stock before you plan around that price.",
        "url": "https://yourreformer.com.au/products/pilates-reformer-machine-foldable",
        "network": "impact",
        "retailer": "Your Reformer",
        "image": "your-reformer-folding.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a maple-framed folding pilates reformer in a bright apartment. Generic machine, not a brand photo.",
        "cta": "View at Your Reformer",
    },
    {
        "id": "technogym-reform",
        "group": "Reformers",
        "title": "Technogym Reform at $18,550: who that price is actually for",
        "card": "Technogym Reform",
        "meta": "technogym.com · $18,550 including delivery",
        "price": 18550,
        "price_was": None,
        "price_note": "Price as seen on 25 November 2026 (Australia/Perth) on Technogym’s Australian site: $18,550, listed as inclusive of delivery and professional installation. The page also said delivery is typically scheduled within two weeks of order confirmation.",
        "url": "https://www.technogym.com/en-AU/product/technogym-reform_MSAA-SLS.html",
        "network": "commission-factory",
        "retailer": "Technogym Australia",
        "image": "technogym-reform.jpg",
        "image_kind": "Original illustration",
        "alt": "Original illustration of a contemporary, sculptural pilates reformer in a minimal sand-coloured room. Generic machine, not a Technogym product photo and with no logo.",
        "cta": "View at Technogym Australia",
    },
]


def money(value: float) -> str:
    if float(value).is_integer():
        return f"${int(value):,}"
    return f"${value:,.2f}"


# --- Illustrations ----------------------------------------------------------

def _font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _noise(im: Image.Image, amount: int = 14, seed: int = 1) -> Image.Image:
    rng = random.Random(seed)
    px = im.load()
    w, h = im.size
    for _ in range(w * h // 9):
        x, y = rng.randrange(w), rng.randrange(h)
        r, g, b = px[x, y][:3]
        d = rng.randint(-amount, amount)
        px[x, y] = (max(0, min(255, r + d)), max(0, min(255, g + d)), max(0, min(255, b + d)))
    return im


def _vignette(im: Image.Image, strength: float = 0.28) -> Image.Image:
    w, h = im.size
    overlay = Image.new("RGB", (w, h), (20, 16, 12))
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((-int(w * 0.15), -int(h * 0.2), int(w * 1.15), int(h * 1.2)), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(120))
    inv = ImageEnhance.Brightness(mask).enhance(0)
    # Use inverted blur as darkness at edges
    edge = Image.eval(mask, lambda v: int((255 - v) * strength))
    return Image.composite(overlay, im, edge)


def _paper(size, colour, seed):
    im = Image.new("RGB", size, colour)
    # soft radial light
    light = Image.new("RGB", size, (255, 250, 242))
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    w, h = size
    d.ellipse((int(w * 0.15), int(h * -0.1), int(w * 0.9), int(h * 0.75)), fill=180)
    mask = mask.filter(ImageFilter.GaussianBlur(90))
    im = Image.composite(light, im, mask)
    im = _noise(im, 10, seed)
    return _vignette(im, 0.18)


def _label(im: Image.Image, text: str):
    d = ImageDraw.Draw(im)
    font = _font(22)
    d.text((48, im.size[1] - 58), text, font=font, fill=(90, 84, 76))
    return im


def _save(im: Image.Image, name: str):
    im = im.filter(ImageFilter.SMOOTH)
    path = IMAGES / name
    im.save(path, "JPEG", quality=88, optimize=True)
    return path


def illus_socks(name, bg, sock, grip, cuff_h=0.22):
    im = _paper((1600, 1000), bg, hash(name) % 9999)
    d = ImageDraw.Draw(im)
    # two socks, slightly angled
    def sock_at(cx, cy, rot_hint=0):
        w, h = 230, 520
        x0, y0 = cx - w // 2, cy - h // 2
        d.rounded_rectangle((x0, y0, x0 + w, y0 + h), 110, fill=sock)
        # cuff
        d.rounded_rectangle((x0, y0, x0 + w, y0 + int(h * cuff_h)), 40, fill=tuple(max(0, c - 18) for c in sock))
        # sole grips
        sole_y = y0 + int(h * 0.55)
        for i in range(6):
            for j in range(3):
                gx = x0 + 50 + i * 24
                gy = sole_y + j * 36
                d.ellipse((gx, gy, gx + 14, gy + 14), fill=grip)

    sock_at(680, 500)
    sock_at(980, 520)
    return _save(_label(im, "Original illustration"), name)


def illus_kit(name, bg, ring, ball, band):
    im = _paper((1600, 1000), bg, hash(name) % 9999)
    d = ImageDraw.Draw(im)
    # ring
    cx, cy, r = 620, 500, 260
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=ring, width=42)
    d.ellipse((cx - r + 36, cy - r + 36, cx + r - 36, cy + r - 36), outline=tuple(min(255, c + 30) for c in ring), width=8)
    # handles
    d.rounded_rectangle((cx - 70, cy - r - 28, cx + 70, cy - r + 50), 20, fill=ring)
    d.rounded_rectangle((cx - 70, cy + r - 50, cx + 70, cy + r + 28), 20, fill=ring)
    # ball
    d.ellipse((1040, 420, 1280, 660), fill=ball)
    d.ellipse((1080, 450, 1180, 530), fill=tuple(min(255, c + 25) for c in ball))
    # bands
    d.rounded_rectangle((1040, 700, 1360, 760), 24, fill=band)
    d.rounded_rectangle((1080, 780, 1320, 830), 20, fill=tuple(max(0, c - 20) for c in band))
    return _save(_label(im, "Original illustration"), name)


def illus_ring(name):
    im = _paper((1600, 1000), (214, 222, 214), 11)
    d = ImageDraw.Draw(im)
    cx, cy, r = 800, 500, 300
    col = (28, 28, 28)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=48)
    d.rounded_rectangle((cx - 80, cy - r - 30, cx + 80, cy - r + 55), 22, fill=(50, 50, 50))
    d.rounded_rectangle((cx - 80, cy + r - 55, cx + 80, cy + r + 30), 22, fill=(50, 50, 50))
    return _save(_label(im, "Original illustration"), name)


def illus_band(name):
    im = _paper((1600, 1000), (232, 220, 204), 12)
    d = ImageDraw.Draw(im)
    # loop band perspective-ish flattened oval
    d.ellipse((430, 360, 1170, 680), outline=(28, 28, 28), width=64)
    d.ellipse((490, 410, 1110, 630), outline=(60, 60, 60), width=6)
    return _save(_label(im, "Original illustration"), name)


def illus_reformer_mat(name):
    im = _paper((1600, 1000), (210, 186, 160), 13)
    d = ImageDraw.Draw(im)
    # wood-ish floor already in bg; ivory mat with neck
    ivory = (245, 238, 226)
    shadow = (170, 150, 128)
    d.rounded_rectangle((360, 430, 1320, 820), 18, fill=shadow)
    d.rounded_rectangle((340, 390, 1300, 780), 18, fill=ivory)
    d.rounded_rectangle((700, 250, 940, 420), 16, fill=ivory)
    return _save(_label(im, "Original illustration"), name)


def illus_floor_mat(name):
    im = _paper((1600, 1000), (228, 222, 212), 14)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((420, 260, 1280, 860), 12, fill=(40, 44, 48))
    d.rounded_rectangle((440, 280, 1260, 840), 10, fill=(34, 38, 42))
    # thick edge to suggest 12mm
    d.rectangle((420, 820, 1280, 860), fill=(22, 24, 26))
    return _save(_label(im, "Original illustration"), name)


def illus_leggings(name):
    im = _paper((1600, 1000), (232, 226, 214), 15)
    d = ImageDraw.Draw(im)
    green = (46, 72, 56)
    # stylised cropped leggings, no body, no logo
    # waist
    d.rounded_rectangle((620, 160, 980, 280), 40, fill=green)
    # legs cropped mid-calf
    d.rounded_rectangle((640, 250, 800, 860), 80, fill=green)
    d.rounded_rectangle((800, 250, 960, 860), 80, fill=tuple(max(0, c - 8) for c in green))
    return _save(_label(im, "Original illustration"), name)


def illus_reformer(name, bg, wood, carriage, seed):
    im = _paper((1600, 1000), bg, seed)
    d = ImageDraw.Draw(im)
    # side-on reformer
    x, y, L, H = 220, 430, 1160, 160
    # legs
    d.rectangle((x + 40, y + H, x + 90, y + H + 140), fill=wood)
    d.rectangle((x + L - 90, y + H, x + L - 40, y + H + 140), fill=wood)
    # frame rails
    d.rounded_rectangle((x, y, x + L, y + H), 20, fill=wood)
    d.rounded_rectangle((x + 18, y + 18, x + L - 18, y + H - 18), 14, fill=tuple(min(255, c + 20) for c in wood))
    # carriage
    d.rounded_rectangle((x + 280, y + 8, x + 720, y + H - 8), 16, fill=carriage)
    # footbar
    d.rounded_rectangle((x + L - 160, y - 90, x + L - 40, y + 20), 12, fill=wood)
    # springs suggestion
    for i in range(4):
        sy = y + 50 + i * 18
        d.line((x + 80, sy, x + 280, sy), fill=(120, 80, 70), width=3)
    return _save(_label(im, "Original illustration"), name)


def crop_portrait_to_hero(src: Path, dest_name: str, focus_y: float):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target_ratio = 1600 / 1000
    # cover crop
    if w / h > target_ratio:
        nw = int(h * target_ratio)
        left = (w - nw) // 2
        box = (left, 0, left + nw, h)
    else:
        nh = int(w / target_ratio)
        top = int((h - nh) * focus_y)
        top = max(0, min(h - nh, top))
        box = (0, top, w, top + nh)
    out = im.crop(box).resize((1600, 1000), Image.Resampling.LANCZOS)
    # small caption bar so the AI label is in the file as well as on the page
    d = ImageDraw.Draw(out)
    d.rectangle((0, 940, 1600, 1000), fill=(28, 26, 23))
    d.text((36, 954), "AI-generated illustration — not a customer photo or review", font=_font(22), fill=(230, 224, 214))
    out.save(IMAGES / dest_name, "JPEG", quality=88, optimize=True)


def build_images():
    IMAGES.mkdir(exist_ok=True)
    pack = Path("/workspace/tts/packs/2026-11-25")
    crop_portrait_to_hero(pack / "01-zanzer-grip-socks/still.jpg", "zanzer-grip-socks.jpg", focus_y=0.72)
    crop_portrait_to_hero(pack / "02-wildbody-seafree-leggings/still.jpg", "wildbody-seafree-leggings.jpg", focus_y=0.42)
    illus_socks("all-fenix-grip-socks.jpg", (230, 224, 214), (28, 28, 30), (210, 210, 210))
    illus_socks("moveactive-crew-socks.jpg", (216, 222, 214), (20, 20, 20), (80, 80, 80), cuff_h=0.32)
    illus_leggings("lululemon-align-crop.jpg")
    illus_kit("spopal-pilates-kit.jpg", (236, 214, 210), (190, 90, 110), (232, 160, 168), (120, 70, 80))
    illus_kit("larfafa-pilates-kit.jpg", (236, 220, 214), (80, 70, 70), (220, 170, 160), (90, 80, 78))
    illus_ring("moveactive-pilates-ring.jpg")
    illus_band("moveactive-resistance-band.jpg")
    illus_reformer_mat("moveactive-reformer-mat.jpg")
    illus_floor_mat("manduka-cloud-mat.jpg")
    illus_reformer("lifespan-contour-folding.jpg", (228, 220, 206), (168, 136, 96), (232, 224, 210), 21)
    illus_reformer("your-reformer-folding.jpg", (236, 228, 214), (188, 154, 108), (92, 72, 62), 22)
    illus_reformer("technogym-reform.jpg", (226, 222, 214), (190, 186, 178), (236, 232, 226), 23)
    # favicon
    icon = Image.new("RGB", (256, 256), (60, 81, 68))
    d = ImageDraw.Draw(icon)
    d.rounded_rectangle((40, 108, 216, 148), 20, fill=(247, 242, 234))
    # small coil
    d.arc((96, 72, 160, 136), 200, 160, fill=(247, 242, 234), width=10)
    icon.save(ASSETS / "favicon.png", "PNG")


# Bodies are written in a second module below for length.
from post_bodies import BODIES  # type: ignore  # noqa: E402


def rel(depth: int, path: str) -> str:
    return ("../" * depth) + path


def page_shell(title: str, depth: int, current: str, main: str, description: str) -> str:
    css = rel(depth, "css/styles.css")
    links = rel(depth, "data/links.json")
    js = rel(depth, "js/links.js")
    home = rel(depth, "index.html")
    about = rel(depth, "about.html")
    disclose = rel(depth, "disclose.html")
    contact = rel(depth, "contact.html")
    fav = rel(depth, "assets/favicon.png")
    if current == "home":
        canon = SITE_URL + "/"
    elif current.startswith("posts/"):
        canon = f"{SITE_URL}/{current}"
    elif current in {"about", "disclose", "contact", "404"}:
        canon = f"{SITE_URL}/{current}.html"
    else:
        canon = f"{SITE_URL}/{current}"
    def nav_cur(label, key):
        href = {"home": home, "about": about, "disclose": disclose, "contact": contact}[key]
        here = current.startswith("posts/") and key == "home" and False
        ac = ' aria-current="page"' if current == key or current == f"{key}.html" else ""
        return f'<a href="{href}"{ac}>{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canon}">
  <link rel="icon" href="{fav}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,560&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="wordmark" href="{home}">{SITE_NAME}<small>Australia</small></a>
      <nav class="nav" aria-label="Primary">
        {nav_cur("Home", "home")}
        {nav_cur("About", "about")}
        {nav_cur("Disclosures", "disclose")}
        {nav_cur("Contact", "contact")}
      </nav>
    </div>
  </header>
  <main id="main">
{main}
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-nav">
        <a href="{home}">Home</a>
        <a href="{about}">About</a>
        <a href="{disclose}">Affiliate &amp; AI disclosure</a>
        <a href="{contact}">Contact</a>
      </div>
      <p>Some links may earn us a commission, at no extra cost to you. Some images are AI-generated illustrations, not real customer photos or reviews. See the <a href="{disclose}">disclosure page</a>.</p>
      <p>© 2026 {SITE_NAME}. Independent notes, not a pilates studio and not the retailer of these products.</p>
    </div>
  </footer>
  <script src="{js}" data-links="{links}" defer></script>
</body>
</html>
"""


def build_links_json():
    products = {}
    for p in PRODUCTS:
        products[p["id"]] = {
            "name": p["card"],
            "url": p["url"],
            "trackedUrl": "",
            "network": p["network"],
            "retailer": p["retailer"],
            "priceAud": p["price"],
            "priceWasAud": p["price_was"],
            "priceChecked": "2026-11-25",
            "priceTimezone": PRICE_ZONE,
        }
    data = {
        "updated": "2026-11-25",
        "notes": "Put an Amazon Associates AU tracking ID in tags.amazon. For Commission Factory, Awin, Impact or other networks, paste the full tracked deep link into products[id].trackedUrl. links.js will swap every data-product-link on the site. Leave trackedUrl empty to use the untagged url field.",
        "tags": {
            "amazon": ""
        },
        "products": products,
    }
    DATA.mkdir(exist_ok=True)
    (DATA / "links.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def home_page() -> str:
    featured_ids = [
        "all-fenix-grip-socks",
        "wildbody-seafree-leggings",
        "your-reformer-folding",
    ]
    by_id = {p["id"]: p for p in PRODUCTS}
    cards = []
    for pid in featured_ids:
        p = by_id[pid]
        href = f"posts/{p['id']}.html"
        cards.append(
            f"""        <a class="card" href="{href}">
          <img src="images/{p['image']}" alt="{p['alt']}">
          <div class="card-body">
            <h3>{p['card']}</h3>
            <p>{p['meta']}</p>
            <p class="caption">{p['image_kind']}</p>
          </div>
        </a>"""
        )

    groups = []
    current = None
    items = []
    for p in PRODUCTS:
        if p["group"] != current:
            if items:
                groups.append(f'      <p class="group-label">{current}</p>\n      <div class="bio-list">\n' + "\n".join(items) + "\n      </div>")
            current = p["group"]
            items = []
        items.append(
            f"""        <a class="bio-btn" href="posts/{p['id']}.html">
          <span><strong>{p['card']}</strong><span class="meta">{p['retailer']}</span></span>
          <span class="price">{money(p['price'])}</span>
        </a>"""
        )
    if items:
        groups.append(f'      <p class="group-label">{current}</p>\n      <div class="bio-list">\n' + "\n".join(items) + "\n      </div>")

    main = f"""    <div class="narrow">
      <section class="hero">
        <h1>Pilates and home-exercise gear you can actually buy in Australia.</h1>
        <p class="lede">Short, original notes on grip socks, mats, props and reformers: what they cost today, who they suit, and the catches worth reading before you click.</p>
        <ul class="chips">
          <li class="chip">Independent notes</li>
          <li class="chip">Prices checked {PRICE_DATE}</li>
          <li class="chip">AU retailers</li>
        </ul>
      </section>
      <p class="notice">Some links may earn a commission. Some images are AI-generated illustrations, not customer photos or reviews. We have not wear-tested every item. <a href="disclose.html">Read the full disclosure</a>.</p>
    </div>
    <div class="wrap section">
      <h2>Latest picks</h2>
      <div class="card-grid">
{chr(10).join(cards)}
      </div>
    </div>
    <div class="narrow section">
      <h2>All product notes</h2>
{chr(10).join(groups)}
    </div>
"""
    return page_shell(
        f"{SITE_NAME} — pilates and home-exercise notes, Australia",
        0,
        "home",
        main,
        "Original notes on pilates and home-exercise products you can buy in Australia, with current prices and honest caveats.",
    )


def post_page(p: dict) -> str:
    body = BODIES[p["id"]]
    was = f'<span class="was">{money(p["price_was"])}</span>' if p["price_was"] is not None else ""
    main = f"""    <article class="narrow prose" style="padding-top:1.6rem">
      <p class="post-kicker">{p['group']}</p>
      <h1>{p['title']}</h1>
      <figure class="post-hero">
        <img src="../images/{p['image']}" alt="{p['alt']}">
        <figcaption class="caption">{p['image_kind']}. Not a brand photo and not a real customer review.</figcaption>
      </figure>
      <div class="price-block">
        <div><span class="now">{money(p['price'])} AUD</span>{was}</div>
        <p>{p['price_note']}</p>
      </div>
{body}
      <div class="cta-row">
        <a class="btn" data-product-link="{p['id']}" href="{p['url']}" rel="nofollow sponsored noopener" target="_blank">{p['cta']}</a>
        <a class="btn btn-ghost" href="../index.html">All picks</a>
      </div>
      <p class="caption">This is a product note based on the retailer’s listing and the price we saw on {PRICE_DATE}. It is not a personal review, medical advice, or a claim that we have used the item in a studio.</p>
    </article>
"""
    desc = f"{p['card']} — {p['meta']}. Original product note from {SITE_NAME}."
    return page_shell(f"{p['title']} — {SITE_NAME}", 1, f"posts/{p['id']}.html", main, desc.replace('"', "&quot;"))


ABOUT = f"""    <article class="narrow prose" style="padding-top:1.8rem">
      <h1>About {SITE_NAME}</h1>
      <p>This is a small Australian site with original notes on pilates and home-exercise products you can buy here: grip socks, clothing, mats, props and reformers.</p>
      <p>The aim is practical. We look at the current price, what is actually in the box, shipping and return catches, and who an item seems to suit. We would rather say “we have not used this ourselves” than write a pretend studio review.</p>
      <p>We are not a pilates studio, not a physiotherapist, and not the seller of these products. Nothing here is medical advice. If you are returning from injury, talk to a qualified practitioner before you buy a machine or change the way you train.</p>
      <p>Some photographs on the site are AI-generated illustrations, and they are labelled as such. They are not photos of us wearing the exact product, and they are not customer reviews. Where an illustration may differ from the real item, we say so on the page.</p>
      <p>We are applying to Australian affiliate programs so that, if you buy through a link, the site can earn a commission at no extra cost to you. Until those applications are approved, the buttons go to ordinary product pages with no tracking tag. There is a full explanation on the <a href="disclose.html">Affiliate &amp; AI disclosure</a> page.</p>
      <p>Prices are checked in Australia/Perth and dated on each note. Retailers change them, often during sales, so always confirm the figure on the product page before you order.</p>
    </article>
"""

DISCLOSE = f"""    <article class="narrow prose" style="padding-top:1.8rem">
      <h1>Affiliate and AI disclosure</h1>
      <h2>Affiliate links</h2>
      <p>Some links on this site may be affiliate links. That means {SITE_NAME} may earn a commission if you click through and buy, at no extra cost to you. It does not change the price you pay.</p>
      <p>We expect to use, once accepted: Amazon Associates AU, Commission Factory, Awin and Impact, plus any direct programs a brand already runs in Australia. Until an application is approved and a tracking ID is added, links on this site are ordinary, untagged product URLs.</p>
      <p>We do not accept payment from a brand for a favourable write-up, and we do not pretend to have used a product we have only seen on a listing. When we have not worn, used or independently tested an item, the note says so.</p>
      <h2>AI-generated imagery and video</h2>
      <p>Some images on this site are AI-generated illustrations. Each of those images is labelled. They are created to show a type of product in a simple setting. They are not photographs of the exact retail item, not photos of a real customer, and not reviews.</p>
      <p>If we later share short videos on TikTok that use AI-generated imagery, those clips should also be labelled with TikTok’s AI-generated content setting, and should not be presented as real customer reviews.</p>
      <p>AI illustrations can get details wrong. On the WildBody SeaFree note, for example, the illustration shows a front seam; the retailer’s listing describes a no-front-seam design. Always treat the product page as the source of truth for colour, cut and features.</p>
      <h2>Prices and availability</h2>
      <p>Prices are in Australian dollars and dated, with the timezone Australia/Perth. Stock, delivery dates, sale periods and return rules change. Confirm everything on the retailer’s page before you buy, especially on higher-priced reformers and on sale items marked as final sale.</p>
      <h2>How we keep links in one place</h2>
      <p>Every product URL lives in a single file, <code>data/links.json</code>. When a tracking tag or network deep link is added there, the buttons on the site pick it up automatically. You do not need to edit each post.</p>
    </article>
"""

CONTACT = f"""    <article class="narrow prose" style="padding-top:1.8rem">
      <h1>Contact</h1>
      <p>The simplest way to reach us is to DM the {SITE_NAME} TikTok account once that account is live. We will add the handle here as soon as it is ready. We do not publish a personal phone number.</p>
      <p>For questions about an order, a return, a delivery or a faulty item, contact the retailer you bought from. We do not sell or ship these products ourselves.</p>
      <p>If you represent a brand or an affiliate network and need to review this site, the disclosure page and the product notes are the best place to start.</p>
    </article>
"""


def write_html():
    POSTS.mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(home_page(), encoding="utf-8")
    (ROOT / "about.html").write_text(
        page_shell(f"About — {SITE_NAME}", 0, "about", ABOUT, f"What {SITE_NAME} is, and how the notes are written."),
        encoding="utf-8",
    )
    (ROOT / "disclose.html").write_text(
        page_shell(f"Affiliate and AI disclosure — {SITE_NAME}", 0, "disclose", DISCLOSE, "How affiliate links and AI-generated illustrations are used on this site."),
        encoding="utf-8",
    )
    (ROOT / "contact.html").write_text(
        page_shell(f"Contact — {SITE_NAME}", 0, "contact", CONTACT, f"How to contact {SITE_NAME}."),
        encoding="utf-8",
    )
    for p in PRODUCTS:
        (POSTS / f"{p['id']}.html").write_text(post_page(p), encoding="utf-8")

    # 404
    main_404 = """    <article class="narrow prose" style="padding-top:2rem">
      <h1>Page not found</h1>
      <p>That address is not on this site. Head back to the <a href="index.html">home page</a> for the latest picks.</p>
    </article>
"""
    (ROOT / "404.html").write_text(page_shell(f"Page not found — {SITE_NAME}", 0, "404", main_404, "Page not found."), encoding="utf-8")


def write_meta():
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    urls = [
        f"{SITE_URL}/",
        f"{SITE_URL}/about.html",
        f"{SITE_URL}/disclose.html",
        f"{SITE_URL}/contact.html",
    ] + [f"{SITE_URL}/posts/{p['id']}.html" for p in PRODUCTS]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>2026-11-25</lastmod></url>")
    sm.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (ASSETS / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#3c5144"/><rect x="10" y="28" width="44" height="8" rx="4" fill="#f7f2ea"/><path d="M24 20c8-10 16 0 16 8" fill="none" stroke="#f7f2ea" stroke-width="4" stroke-linecap="round"/></svg>\n',
        encoding="utf-8",
    )


README = f"""# {SITE_NAME}

Public link-in-bio and product-note site for an Australian pilates / home-exercise TikTok account.

Live URL (GitHub Pages): {SITE_URL}/

## Affiliate links

All product URLs live in **`data/links.json`**. Pages ship with untagged retailer URLs. A small script, `js/links.js`, rewrites every `data-product-link` button from that file.

To add tracking later:

1. Amazon Associates AU: put the tracking ID in `tags.amazon`. Amazon product URLs will gain `?tag=YOURID`.
2. Commission Factory, Awin, Impact or a direct program: paste the full tracked deep link into `products[ID].trackedUrl`. That value wins over the untagged `url`.

Do not edit the buttons on each post unless you also update `links.json`.

## Editing content

Source is static HTML/CSS in this folder (not `dist/` or `build/`). The same files are kept at `/workspace/tts/site/` on the working machine.

Prices on each note are dated {PRICE_DATE} ({PRICE_ZONE}). Update the note and the matching `priceAud` / `priceChecked` fields when you re-check a listing.

## Images

Two images (`zanzer-grip-socks.jpg`, `wildbody-seafree-leggings.jpg`) are AI-generated illustrations made for this project. The rest are original illustrations. None are brand photos or customer photos. Do not hotlink retailer imagery.

## Deploy

GitHub Pages, `main` branch, site root, with `.nojekyll`. No custom domain is attached.
"""


def word_counts():
    import re
    print("Word counts (post bodies only):")
    for p in PRODUCTS:
        text = re.sub(r"<[^>]+>", " ", BODIES[p["id"]])
        n = len(re.findall(r"[A-Za-z0-9’']+", text))
        flag = "OK" if 250 <= n <= 500 else "OUT OF RANGE"
        print(f"  {n:4d}  {flag}  {p['id']}")


def main():
    build_images()
    build_links_json()
    write_html()
    write_meta()
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    word_counts()
    print("Built", ROOT)


if __name__ == "__main__":
    main()
