import json, re

def load(fn):
    txt = open(fn, encoding='utf-8').read()
    eq = txt.index('=', txt.index('=')+1)
    prefix = txt[:eq+1]
    body = txt[eq+1:].rstrip()
    if body.endswith(';'):
        body = body[:-1]
    return prefix, json.loads(body)

def save(fn, prefix, data):
    body = json.dumps(data, indent=2, ensure_ascii=False)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(prefix + body + ';\n')

# --- updates.js ---
prefix, upd = load('data/updates.js')
new_updates = [
    {
        "date": "2026-07-17",
        "competitorId": "origin",
        "category": "campaign",
        "headline": "Origin's homepage hero switches from single-origin feature to a broader 'A Summer Shared' hosting campaign",
        "detail": "The homepage top banner now reads 'A Summer Shared — Seasonal hosting, elevated with exceptional coffee', replacing the Kibira Hill Honey, Burundi single-origin feature that held the hero slot on 15-16 Jul. The weekly single-origin release may still be purchasable elsewhere on the site; only the homepage hero placement has changed. This reads as a seasonal lifestyle push (dinner parties, hosting) rather than a coffee-specific launch — 'Resolute' remains the featured flagship espresso blend alongside it.",
        "bridgeResponse": "A lifestyle hosting angle plays well for Origin's retail/gift audience but has no bearing on wholesale or equipment accounts. Bridge's positioning stays anchored in the operational case — published pricing, full-stack service, named enterprise references.",
        "source": "https://www.origincoffee.co.uk/",
        "severity": "info"
    },
    {
        "date": "2026-07-17",
        "competitorId": "liquidline",
        "category": "pricing",
        "headline": "Schaerer Coffee Soul 12 lease price drops back to £94.50/week — fourth movement in six weeks",
        "detail": "Confirmed live on the product page: lease price is back to £94.50/week, down £3.00 from the £97.50/week logged on 16 Jul. This is the same figure seen on 11 Jun, meaning the price has now moved 97.50 → 94.50 → 97.50 → 94.50 across four checks since 10 Jun. The pattern points to frequent or dynamic lease-price review rather than a one-off promotion; no discount messaging or offer banner accompanies the change.",
        "bridgeResponse": "Worth flagging internally: a prospect quoted Liquidline's Schaerer lease on different days could see a genuinely different number. Bridge's published pricing removes that ambiguity — one number, holds until we change it.",
        "source": "https://www.liquidline.co.uk/commercial-coffee-machines/bean-to-cup/schaerer-coffee-soul-12-fresh-milk/",
        "severity": "watch"
    }
]
upd['updates'] = new_updates + upd['updates']
save('data/updates.js', prefix, upd)
print('updates.js: added', len(new_updates), '-> total', len(upd['updates']))

# --- promotions.js ---
prefix, promo = load('data/promotions.js')
new_promos = [
    {
        "competitorId": "origin",
        "type": "content",
        "name": "'A Summer Shared' hosting campaign",
        "detail": "New homepage hero campaign framing coffee around seasonal hosting/entertaining, displacing the Kibira Hill Honey single-origin feature from the top banner slot. 'Resolute' espresso blend remains the top featured product alongside it.",
        "source": "https://www.origincoffee.co.uk/",
        "spotted": "2026-07-17",
        "counter": "A retail lifestyle campaign with no wholesale or equipment angle. Bridge's shop-window story stays operational: published pricing and full-stack service."
    }
]
promo['items'] = new_promos + promo['items']
promo['lastUpdated'] = "2026-07-17"
save('data/promotions.js', prefix, promo)
print('promotions.js: added', len(new_promos), '-> total', len(promo['items']))

# --- pricing.js ---
prefix, price = load('data/pricing.js')
new_snapshot = {
    "date": "2026-07-17",
    "entries": [
        {
            "competitorId": "liquidline",
            "item": "Schaerer Coffee Soul 12 lease",
            "price": "£94.50 / week",
            "change": "-£3.00/wk vs 16 Jul (£97.50); fourth movement in six weeks (97.50 -> 94.50 -> 97.50 -> 94.50 since 10 Jun) — consistent with frequently reviewed or dynamic lease pricing rather than a promotion"
        }
    ]
}
price['snapshots'].append(new_snapshot)
save('data/pricing.js', prefix, price)
print('pricing.js: added snapshot -> total', len(price['snapshots']))

# --- competitors.js ---
prefix, comp = load('data/competitors.js')
comp['lastUpdated'] = "2026-07-17"
save('data/competitors.js', prefix, comp)
print('competitors.js: lastUpdated bumped to 2026-07-17')
