"""Рендерит HTML-макеты из design-src/ в assets/img/*.png и *.webp (2x, прозрачный фон).
Запуск: python3 design-src/render_mocks.py [имя ...]   (без аргументов — все)"""
import os, re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOCKS = {  # исходник -> имя картинки
    'mock-hero.html': 'home-hero', 'mock-promo.html': 'home-promo',
    'mock-app.html': 'home-app', 'mock-login.html': 'home-login',
    'signup-mockup.html': 'signup-mockup',
}
want = sys.argv[1:] or list(MOCKS)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get('CHROME', '/usr/bin/google-chrome'))
    for src in want:
        path = os.path.join(ROOT, 'design-src', src)
        if not os.path.exists(path): continue
        css = open(path, encoding='utf-8').read()
        w = int(re.search(r'body \{[^}]*width: (\d+)px', css).group(1)); h = int(re.search(r'body \{[^}]*height: (\d+)px', css).group(1))
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
        pg.goto('file://' + path); pg.wait_for_timeout(300)
        out = os.path.join(ROOT, 'assets', 'img', MOCKS[src])
        pg.screenshot(path=out + '.png', omit_background=True); pg.close()
        Image.open(out + '.png').save(out + '.webp', 'WEBP', quality=86, method=6)
        print(src, '->', MOCKS[src], f'{w*2}x{h*2}', os.path.getsize(out + '.webp') // 1024, 'KB webp')
    b.close()
