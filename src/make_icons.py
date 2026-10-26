#!/usr/bin/env python3
"""Regenerate the square site icons (favicon.ico, icon-192/512.png, apple-touch-icon.png) from img/logo.png.
White logo on brand purple #45147A. Run from anywhere: python3 src/make_icons.py"""
import os
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo = Image.open(os.path.join(ROOT, 'img', 'logo.png')).convert('RGBA')
logo = logo.crop(logo.getbbox())
white = Image.new('RGBA', logo.size, (255, 255, 255, 255)); white.putalpha(logo.split()[3])
def make(n):
    bg = Image.new('RGBA', (n, n), (0x45, 0x14, 0x7A, 255))
    w = int(n * 0.74); h = int(w * logo.size[1] / logo.size[0])
    bg.alpha_composite(white.resize((w, h), Image.LANCZOS), ((n - w) // 2, (n - h) // 2))
    return bg
big = make(512)
big.save(os.path.join(ROOT, 'icon-512.png'))
make(192).save(os.path.join(ROOT, 'icon-192.png'))
make(180).convert('RGB').save(os.path.join(ROOT, 'apple-touch-icon.png'))
big.save(os.path.join(ROOT, 'favicon.ico'), sizes=[(48, 48), (32, 32), (16, 16)])
print('icons written')
