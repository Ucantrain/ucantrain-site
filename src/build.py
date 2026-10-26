#!/usr/bin/env python3
"""Build the live site from src/.

    python3 src/build.py              -> writes index.html at the repo root (what Netlify publishes)
    python3 src/build.py --artifact   -> also writes build/u-can-train.html with images embedded
                                         (only needed for the private Claude preview artifact)

Edit src/template.html (page) and src/seo_head.html (search/share tags), then run this.
Never hand-edit index.html: the next build overwrites it.
"""
import base64, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(ROOT, *p)
t = open(R('src', 'template.html')).read()
IMAGES = {'{{LOGO}}': 'logo.png', '{{ETHAN}}': 'ethan.jpg', '{{AVERY}}': 'avery.jpg'}

def data_uri(f):
    m = 'image/png' if f.endswith('.png') else 'image/jpeg'
    return 'data:%s;base64,%s' % (m, base64.b64encode(open(R('img', f), 'rb').read()).decode())

# Hosted page: images as real files under /img/
page = t
for ph, f in IMAGES.items():
    page = page.replace(ph, '/img/' + f)
i = page.index('</style>') + len('</style>')
head = page[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '') \
               .replace('<title>U Can Train</title>\n', open(R('src', 'seo_head.html')).read())
# drop the template's short preview description; seo_head.html carries the real one
head = '\n'.join(l for l in head.split('\n')
                 if not l.startswith('<meta name="description" content="Saturday athletic training for grades 6–12, any sport'))
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<link rel="icon" href="/favicon.ico" sizes="48x48">\n'
        '<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<meta name="theme-color" content="#45147A">\n' + head +
        '\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)} '
        'body{margin:0} img{max-width:100%} [hidden]{display:none!important}</style>\n</head>\n<body>\n'
        + page[i:] + '\n</body>\n</html>\n')
open(R('index.html'), 'w').write(html)
print('wrote index.html (%d bytes)' % len(html))

if '--artifact' in sys.argv:
    a = t
    for ph, f in IMAGES.items():
        a = a.replace(ph, data_uri(f))
    os.makedirs(R('build'), exist_ok=True)
    open(R('build', 'u-can-train.html'), 'w').write(a)
    print('wrote build/u-can-train.html')
