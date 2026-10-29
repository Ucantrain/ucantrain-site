# ucantrain.org: notes for Claude

This repo is the live website for **U Can Train**, Saturday athletic training for grades 6–12
(any sport, in season or out) run by Ethan Grams and Avery Holtzleicer at the
U Can Danz! Dance Company studio, 7928 Kerber Blvd, Chanhassen, MN 55317.
Contact: ucantrainmn@gmail.com. Instagram: @ucantrainmn (linked in the footer and in JSON-LD sameAs). This repo is **public**: never commit private business info
(insurance, finances, studio agreements, personal details). Those live in Ethan's private handoff doc.

## How the site is built and published
- `src/template.html` is the page (HTML + CSS + a little JS). `src/seo_head.html` holds the
  title, search description, Open Graph tags and JSON-LD structured data.
- `python3 src/build.py` writes `index.html` at the repo root. **Never hand-edit index.html.**
  `python3 src/build.py --artifact` also writes `build/u-can-train.html` (images embedded; git-ignored)
  for the private Claude preview artifact.
- Images live in `img/` (logo.png, ethan.jpg, avery.jpg). Icons at the root (favicon.ico,
  icon-192.png, icon-512.png, apple-touch-icon.png) come from `python3 src/make_icons.py`.
- Other root files: og-image.jpg (link-preview image), robots.txt, sitemap.xml, 404.html,
  netlify.toml (cache and security headers).
- **Netlify free plan = 300 credits/month, 15 per deploy; at 0 the site goes offline until the cycle resets
  (cycles start the 25th).** Batch changes into one push. Pushes that only touch CLAUDE.md, README.md, src/
  or .gitignore are skipped by the `ignore` rule in netlify.toml and cost nothing.
- **Deploy = push to `main`.** Netlify (project `profound-beignet-ba3575`, visitor access set to
  Public) auto-deploys within about a minute. Commit as `U Can Train <ucantrainmn@gmail.com>`.
- After a meaningful content change, bump `<lastmod>` in sitemap.xml.

## Analytics
- Google Analytics 4 under ucantrainmn@gmail.com: account "U Can Train", property/stream "ucantrain.org",
  Measurement ID G-2HJ8C1S9JG (tag at the top of src/seo_head.html, so only the live site is tracked).
  Enhanced measurement is on: outbound clicks to app.jackrabbitclass.com = Sign Up clicks.
- The flyer QR code points to https://ucantrain.org/?utm_source=flyer&utm_medium=qr so flyer scans show
  as source "flyer" in Analytics.

## Domain, DNS and search (all set up Oct 24–26, 2026)
- Domain `ucantrain.org` registered at Namecheap. Advanced DNS records:
  - A `@` → 75.2.60.5 (Netlify)
  - CNAME `www` → profound-beignet-ba3575.netlify.app.
  - TXT `@` → google-site-verification=WZRcFyclQpatzCENt90btsu34f_BPdwNm6WiveYmiyE
    (**do not delete**; it keeps Google Search Console verified)
- Google Search Console: Domain property `ucantrain.org` under ucantrainmn@gmail.com. Sitemap
  submitted, status Success; home page indexed.
- Bing Webmaster Tools: imported from Search Console; sitemap submitted, indexing requested.
- Google Business Profile "U Can Train" (category Personal trainer, Saturday 8:00 AM–1:30 PM,
  no phone, website ucantrain.org) is created but **not public until video verification** is done.
- Netlify HTTPS certificate is active.

## Content facts the site must match
- Sessions every Saturday from Nov 7, 2026: 8:00–9:30 am, 10:00–11:30 am, 12:00–1:30 pm.
  Every slot is grades 6–12 with easier and harder levels (no separate middle/high school slots).
  No Sundays. No sessions Sat Nov 14, Sat Nov 28 or Sat Dec 26 (Nov 14 added Oct 28). Max 20 athletes per session; 90 minutes.
- Pricing: $20 single session; $85 5-session pack ($17 each, use within 10 weeks).
- First-time offer (athletes new to U Can Train, not new to their sport), sign up by Fri Nov 6:
  first session $10, or 5-session pack $75.
- Coaches: Ethan Grams, "Chan JV Soccer Head Coach · Former Chan Soccer Player". Avery
  Holtzleicer, "NBA Dancer · Dance and Fitness Instructor".
- Wear athletic clothes and clean tennis shoes (no cleats; shoes worn outside are fine if clean, per Ethan Oct 28);
  bring water and a towel; arrive 5–10 minutes early; parents wait in the lobby; cancel 24+ hours
  ahead; note injuries at signup.
- Five focus areas: Mobility, Explosiveness, Strength, Balance, Injury Prevention.

## Style rules Ethan has asked for
- Always write the studio as **"U Can Danz! Dance Company"** on the website.
- Don't frame the program as "offseason" training on the site; it's for all athletes in any season.
- Title-case short labels (e.g. "Single Session", "5-Session Pack").
- Removed on purpose; don't re-add: the "Inside a 90-minute session" breakdown, a soccer-specific
  FAQ, holiday names on the calendar (small 🦃/🎄 icons on Nov 26 and Dec 25 instead), duplicate coach
  photos in the hero.

## Open items
- **Signup:** every Sign Up button (header, hero, offer band, signup section) links to the
  Jackrabbit registration page https://app.jackrabbitclass.com/regv2.asp?id=519495 (added Oct 28, 2026).
- After the Business Profile video verification: add studio and session photos to the profile.

## Before pushing, check phones
Serve the repo (`python3 -m http.server 8765`) and run `node src/check_mobile.js` (needs Playwright;
the Saira Condensed and Archivo fonts installed locally give accurate wrapping). Widths 360/390/430/768
should report no `wide` elements and no `broken` words.
