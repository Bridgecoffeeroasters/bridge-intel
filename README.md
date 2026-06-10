# Bridge market intelligence

Internal competitive intelligence tool for the Bridge Coffee Roasters sales and marketing teams. Static site — no build step, no server. Works deployed or opened directly from a folder.

## Structure

- `index.html` — the whole app (views, styling, password gate)
- `data/competitors.js` — profiles, battlecards, objection handling, our position
- `data/updates.js` — the dated intelligence feed
- `data/pricing.js` — Bridge published baseline + dated competitor price snapshots
- `data/digests.js` — weekly Monday digests

Each data file is JSON wrapped in one line of JavaScript, e.g. `window.BCR=window.BCR||{};window.BCR.upd={...};` — this lets the page load without a server. Daily automated updates only ever touch the `data/*.js` files.

## Deploying (GitHub Pages)

1. Create a repository (e.g. `bridge-intel`) and push these files to `main`
2. Repository settings → Pages → Source: deploy from branch → `main` / root
3. The site appears at `https://<account>.github.io/bridge-intel/` within a couple of minutes

Note: free GitHub Pages requires a public repository, so the password gate deters casual visitors but the repo contents are technically public. All data is public-domain competitor information. For a private repo, deploy the same files on Netlify free tier instead.

## Changing the password

The gate compares a SHA-256 hash in `index.html` (`PW_HASH`). Compute the hash of the new password and replace the constant:

    python3 -c "import hashlib; print(hashlib.sha256('newpassword'.encode()).hexdigest())"

## Data conventions (for automated updates)

**Append-only policy: nothing is ever deleted.** New feed entries and shop-window items are added with today's date; items no longer being promoted get an `ended: "YYYY-MM-DD"` field (they move to the archive toggle in the UI). History stays on the site permanently.

- `promotions`: shop-window items — `competitorId`, `type` (machine | coffee | offer | social | content), `name`, `detail`, `price`, `image` (og:image URL from the competitor's own page, optional), `source`, `spotted` (YYYY-MM-DD), `counter` (the Bridge counter, optional), `ended` (optional — set instead of deleting)
- `updates`: `date` (YYYY-MM-DD), `competitorId`, `category` (launch | hiring | strategy | campaign | event | acquisition | award | pricing | content | social | ads), `headline`, `detail`, `bridgeResponse` (what we say or do about it — always in Bridge voice), `source` (URL), `severity` (threat | watch | info)
- `pricing`: append a new object to `snapshots` only when a visible price changes; set `change` to e.g. "+£0.50 vs 10 Jun" or "baseline"
- `digests`: one entry per week, `weekEnding` is the Friday date
- Keep `lastUpdated` in the competitors file current
- Voice: British English, sentence case, calm and evidence-led. State, don't sell. No hype, no emoji. Be honest about where competitors win.
