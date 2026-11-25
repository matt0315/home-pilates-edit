# The Home Pilates Edit

Public link-in-bio and product-note site for an Australian pilates / home-exercise TikTok account.

Live URL (GitHub Pages): https://matt0315.github.io/home-pilates-edit/

## Affiliate links

All product URLs live in **`data/links.json`**. Pages ship with untagged retailer URLs. A small script, `js/links.js`, rewrites every `data-product-link` button from that file.

To add tracking later:

1. Amazon Associates AU: put the tracking ID in `tags.amazon`. Amazon product URLs will gain `?tag=YOURID`.
2. Commission Factory, Awin, Impact or a direct program: paste the full tracked deep link into `products[ID].trackedUrl`. That value wins over the untagged `url`.

Do not edit the buttons on each post unless you also update `links.json`.

## Editing content

Source is static HTML/CSS in this folder (not `dist/` or `build/`). The same files are kept at `/workspace/tts/site/` on the working machine.

Prices on each note are dated 25 November 2026 (Australia/Perth). Update the note and the matching `priceAud` / `priceChecked` fields when you re-check a listing.

## Images

Two images (`zanzer-grip-socks.jpg`, `wildbody-seafree-leggings.jpg`) are AI-generated illustrations made for this project. The rest are original illustrations. None are brand photos or customer photos. Do not hotlink retailer imagery.

## Deploy

GitHub Pages, `main` branch, site root, with `.nojekyll`. No custom domain is attached.
