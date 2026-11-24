"""Оптимизация ассетов. Запуск из корня репозитория: python3 design-src/build_assets.py
- макеты: name.webp (2x), name-1x.webp (1x), name.png (1x, 256 цветов) — запасной вариант;
- логотип: PNG 256 цветов;
- CSS/JS: style.min.css, main.min.js, game-scenes.min.js (консервативная минификация).
Исходники макетов (2x PNG) берутся из design-src/out/, куда их кладёт render_mocks.py."""
import os
import re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
OUT = os.path.join(ROOT, "design-src", "out")
MOCKS = ["home-hero", "home-promo", "home-app", "home-login", "signup-mockup", "app-android", "app-ios"]


def kb(path):
    return os.path.getsize(path) // 1024


def images():
    for name in MOCKS:
        src = os.path.join(OUT, name + "@2x.png")
        if not os.path.exists(src):  # первый запуск: исходник — текущий PNG 2x
            os.makedirs(OUT, exist_ok=True)
            os.replace(os.path.join(IMG, name + ".png"), src)
        im = Image.open(src).convert("RGBA")
        im.save(os.path.join(IMG, name + ".webp"), "WEBP", quality=80, method=6)
        half = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
        half.save(os.path.join(IMG, name + "-1x.webp"), "WEBP", quality=82, method=6)
        half.quantize(256, method=Image.Quantize.FASTOCTREE).save(os.path.join(IMG, name + ".png"), optimize=True)
        print(f"{name}: 2x {kb(os.path.join(IMG, name + '.webp'))} KB, 1x {kb(os.path.join(IMG, name + '-1x.webp'))} KB, png {kb(os.path.join(IMG, name + '.png'))} KB")
    logo = os.path.join(IMG, "1xbet-logo.png")
    src = os.path.join(OUT, "1xbet-logo@4x.png")
    if not os.path.exists(src):
        os.replace(logo, src)
    Image.open(src).convert("RGBA").quantize(256, method=Image.Quantize.FASTOCTREE).save(logo, optimize=True)
    print("logo", kb(logo), "KB")


def min_css(s):
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([{};,>])\s*", r"\1", s)
    s = re.sub(r":\s+", ":", s)  # безопасно: в стилях нет селекторов с пробелом после «:»
    s = s.replace(";}", "}")
    return s.strip()


def min_js(s):
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)          # блочные комментарии (в строках их нет)
    out = []
    for line in s.splitlines():
        t = line.strip()
        if not t or t.startswith("//"):
            continue
        out.append(t)
    return "\n".join(out) + "\n"


def code():
    pairs = [("assets/css/style.css", "assets/css/style.min.css", min_css),
             ("assets/js/main.js", "assets/js/main.min.js", min_js),
             ("assets/js/game-scenes.js", "assets/js/game-scenes.min.js", min_js)]
    for src, dst, fn in pairs:
        with open(os.path.join(ROOT, src), encoding="utf-8") as f:
            data = fn(f.read())
        with open(os.path.join(ROOT, dst), "w", encoding="utf-8") as f:
            f.write(data)
        print(f"{dst}: {os.path.getsize(os.path.join(ROOT, src)) // 1024} KB -> {os.path.getsize(os.path.join(ROOT, dst)) // 1024} KB")


if __name__ == "__main__":
    images()
    code()
