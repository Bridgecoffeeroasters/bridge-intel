import json

def load(fname, key):
    content = open(fname, encoding='utf-8').read()
    marker = f'window.BCR.{key}='
    idx = content.index(marker) + len(marker)
    data = content[idx:].rstrip()
    if data.endswith(';'):
        data = data[:-1]
    return json.loads(data)

def save(fname, key, obj):
    body = json.dumps(obj, indent=1, ensure_ascii=True)
    content = 'window.BCR=window.BCR||{};window.BCR.' + key + '=' + body + ';\n'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

TODAY = "2026-09-17"

# ---------- updates.js ----------
upd = load('updates.js', 'upd')

new_updates = [
 {
  "date": TODAY,
  "competitorId": "clifton",
  "category": "launch",
  "headline": "Clifton marks 25 years with a £21 flagship Pink Bourbon",
  "detail": "New single-origin release (Finca Cultivares, Huila, Pink Bourbon, anaerobic natural) launched to mark the roaster's 25th anniversary, priced above the existing Unparalleled Series ceiling (£15.00–£20.75/120g) and marketed on the anniversary story rather than a transparency stat. Product page shows an active add-to-cart and quantity selector, so reads as live stock despite a generic \"Sale Sold out\" template label.",
  "bridgeResponse": "A useful contrast: Clifton is 25 years old and building a campaign around it. Bridge has been roasting in Cardiff since 1985 — 41 years — and that heritage isn't currently doing any work in our own marketing. Worth a look for the shareholder narrative or a customer-facing story.",
  "source": "https://cliftoncoffee.co.uk/products/25th-anniversary-coffee-colombia",
  "severity": "watch"
 },
 {
  "date": TODAY,
  "competitorId": "ucc",
  "category": "campaign",
  "headline": "Dr Coffee M12 Plus stays out of stock; its own spec sheet now disagrees with itself",
  "detail": "The flagship product page still shows out of stock at £2,999.99 with no buy-now route, only a callback form. A separate 'Dr Coffee Callback' landing page lists the same machine at different dimensions (41 x 60 x 65cm) to the product page's own spec (W63 x D50 x H58cm) — extending the pattern of contradictory detail on UCC's single headline hardware campaign.",
  "bridgeResponse": "Their flagship machine push is now weeks into being unbuyable with conflicting specs published under their own name. Worth flagging to the sales team as a live objection-handling point when a UCC prospect mentions the M12 Plus.",
  "source": "https://www.ucc-coffee-direct.co.uk/products/dr-coffee-m12-plus-automatic-coffee-machine",
  "severity": "watch"
 },
 {
  "date": TODAY,
  "competitorId": "liquidline",
  "category": "campaign",
  "headline": "Liquidline breaks seven weeks of marketing silence with a customer-story hero",
  "detail": "Homepage refreshed 15 September (first change since 28 July) with new hero creative, 'What Does Your Coffee Say About Your Business?', built around a Schaerer Soul 12 installation at a customer site. Pricing pages for the K2 and Soul 12 are unchanged, so this reads as a marketing relaunch rather than a commercial change — worth watching for follow-through in journal posts or social activity.",
  "bridgeResponse": "If Liquidline is coming back to life after a quiet summer, expect more customer-story content built around their own installs. Our own case studies — Salesforce Tower, Four Seasons, Cambridge colleges — do the same job and are worth keeping current.",
  "source": "https://www.liquidline.co.uk/",
  "severity": "watch"
 },
 {
  "date": TODAY,
  "competitorId": "union",
  "category": "pricing",
  "headline": "Union's SEPTEMBER20 discount passes a week with still no end date",
  "detail": "The 20% sitewide code (first spotted 8 September) is still the homepage hero nine days on, with no end date published anywhere on the site. Combined with no autumn blend appearing to replace Summer Blend, an open-ended sitewide discount now reads more like a price reset than a calendar promotion.",
  "bridgeResponse": "A discount with no exit plan tends to become the new price. Bridge doesn't discount its published wholesale pricing, which is the point of publishing it — worth keeping in view for anyone benchmarking us against Union on bean cost.",
  "source": "https://unionroasted.com/",
  "severity": "watch"
 },
 {
  "date": TODAY,
  "competitorId": "ucc",
  "category": "strategy",
  "headline": "Ueshima House Blend and Fuji Mountain restock after the supply gap",
  "detail": "Both lines, sold out as of the last pass (9–10 September), now show in stock on their product pages. The wider pattern of rotating stock-outs across Ueshima, Grand Café and Lyons formats logged over recent weeks appears to be easing on these two SKUs specifically; the Grand Café temporary-packaging constraint from the plant works was not confirmed resolved.",
  "bridgeResponse": "Removes a talking point rather than creating a new risk. Availability is still the more useful contrast to draw — Bridge roasts to a fixed weekly schedule in Cardiff.",
  "source": "https://www.ucc-coffee-direct.co.uk/products/ueshima-house-blend-coffee-bags-bulk-150-x-7g",
  "severity": "info"
 },
 {
  "date": TODAY,
  "competitorId": "ucc",
  "category": "content",
  "headline": "UCC adds a matcha syrup banner to the shop homepage",
  "detail": "Ueshima Matcha Syrup (1L) now has its own promotional tile on the UCC Coffee Direct homepage alongside the Dr Coffee, Lyons and Ueshima banners — a new product placement; price not confirmed on the page.",
  "bridgeResponse": "Matcha is showing up across several competitors' shop windows this year. Worth a standing item on the NPD radar rather than a one-off reaction to UCC specifically.",
  "source": "https://www.ucc-coffee-direct.co.uk/products/ueshima-matcha-syrup-1l-bottle",
  "severity": "info"
 },
]

upd['updates'] = new_updates + upd['updates']
save('updates.js', 'upd', upd)
print("updates.js: added", len(new_updates), "-> total", len(upd['updates']))

# ---------- promotions.js ----------
promo = load('promotions.js', 'promo')

new_promo_items = [
 {
  "competitorId": "clifton",
  "type": "coffee",
  "name": "25th Anniversary Coffee - Colombia",
  "detail": "Pink Bourbon, Finca Cultivares, Huila — anaerobic natural, launched to mark Clifton's 25th anniversary",
  "price": "£21.00 / 110g",
  "image": "https://cliftoncoffee.co.uk/cdn/shop/files/25.png?v=1789648526",
  "source": "https://cliftoncoffee.co.uk/products/25th-anniversary-coffee-colombia",
  "spotted": TODAY,
  "counter": "Clifton is marking 25 years; Bridge has been roasting in Cardiff since 1985 — a longer story we don't currently use."
 },
 {
  "competitorId": "ucc",
  "type": "content",
  "name": "Ueshima Matcha Syrup 1L Bottle",
  "detail": "New promotional tile on the UCC Coffee Direct shop homepage, alongside Dr Coffee, Lyons and Ueshima banners",
  "price": "Not stated on the page",
  "source": "https://www.ucc-coffee-direct.co.uk/products/ueshima-matcha-syrup-1l-bottle",
  "spotted": TODAY
 },
]

promo['items'] = new_promo_items + promo['items']
promo['lastUpdated'] = TODAY
save('promotions.js', 'promo', promo)
print("promotions.js: added", len(new_promo_items), "-> total", len(promo['items']))

# ---------- competitors.js ----------
comp = load('competitors.js', 'comp')
comp['lastUpdated'] = TODAY

focus_adds = {
 "liquidline": "Homepage refreshed 15 September after seven weeks of silence, with a new hero built around a Schaerer Soul 12 customer story ('Moor Park') — first content change since 28 July (17 Sep)",
 "ucc": "Ueshima House Blend and Fuji Mountain bags restocked; Dr Coffee M12 Plus remains out of stock with a new spec-sheet contradiction (63x50x58cm on the product page vs 41x60x65cm on the callback page); new Ueshima Matcha Syrup banner added to the shop homepage (17 Sep)",
 "union": "SEPTEMBER20 sitewide discount now nine days old with still no end date and no autumn blend launched — reads increasingly like a price reset rather than a calendar promotion (17 Sep)",
 "clifton": "New 25th Anniversary Coffee - Colombia (£21/110g, Pink Bourbon) launched above the existing Unparalleled Series ceiling, marking the roaster's 25th year (17 Sep)",
}

for c in comp['competitors']:
    cid = c.get('id')
    if cid in focus_adds:
        c.setdefault('currentFocus', []).insert(0, focus_adds[cid])

save('competitors.js', 'comp', comp)
print("competitors.js: lastUpdated ->", comp['lastUpdated'])
