"""Финальная SEO-обработка всех HTML-страниц (идемпотентно).
Запуск из корня репозитория ПОСЛЕ build_games.py и build_assets.py:
    python3 design-src/seo_finalize.py
Делает: минифицированные CSS/JS, og:image (размеры, alt) и twitter:image,
schema.org WebSite + Organization + WebPage/Article (BreadcrumbList, FAQPage, ItemList сохраняются),
адаптивные srcset для картинок-макетов."""
import html
import json
import os
import re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://example.com"
HOME = DOMAIN + "/"
DATE = "2026-11-24"
SITE = "1xBet Nigeria Guide"
PAGES = ["index.html", "registration/index.html", "promo-code/index.html", "games/index.html",
         "games/aviator/index.html", "games/chicken-road/index.html", "games/tower-rush/index.html"]
HERO_SIZES = "(max-width: 600px) 90vw, (max-width: 1000px) 460px, 560px"
FIG_SIZES = "(max-width: 600px) 320px, (max-width: 1000px) 400px, 420px"


def dims(name):
    im = Image.open(os.path.join(ROOT, "assets", "img", name + ".webp"))
    return im.width, im.width // 2


def process(path):
    full = os.path.join(ROOT, path)
    s = open(full, encoding="utf-8").read()

    # 1. минифицированные ассеты
    s = re.sub(r'assets/css/style\.css"', 'assets/css/style.min.css"', s)
    s = re.sub(r'assets/js/main\.js"', 'assets/js/main.min.js"', s)
    s = re.sub(r'assets/js/game-scenes\.js"', 'assets/js/game-scenes.min.js"', s)

    # 2. og:image + twitter
    if 'property="og:image:width"' not in s:
        s = re.sub(r'(<meta property="og:image" content="[^"]+">)',
                   r'\1\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n'
                   r'  <meta property="og:image:alt" content="1xBet Nigeria guide: sign up, promo code and welcome bonus">', s, count=1)
    if 'name="twitter:image"' not in s:
        s = s.replace('<meta name="twitter:card" content="summary_large_image">',
                      '<meta name="twitter:card" content="summary_large_image">\n'
                      f'  <meta name="twitter:image" content="{DOMAIN}/assets/img/og-cover.jpg">')

    # 3. адаптивные картинки
    def pic(m):
        prefix, name = m.group(1), m.group(2)
        w2, w1 = dims(name)
        hero = name in ("home-hero", "signup-mockup") or (name == "home-promo" and path.startswith("promo-code"))
        sizes = HERO_SIZES if hero else FIG_SIZES
        return (f'<source type="image/webp" srcset="{prefix}assets/img/{name}-1x.webp {w1}w, '
                f'{prefix}assets/img/{name}.webp {w2}w" sizes="{sizes}">')
    s = re.sub(r'<source (?:type="image/webp" )?srcset="((?:\.\./)*)assets/img/([a-z-]+?)(?:-1x)?\.webp[^"]*"[^>]*>', pic, s)

    # 4. schema.org
    title = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1))
    desc = html.unescape(re.search(r'<meta name="description" content="(.*?)"', s).group(1))
    canon = re.search(r'<link rel="canonical" href="(.*?)"', s).group(1)
    h1 = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1))).strip()
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
    data = json.loads(m.group(2))
    graph = data.get("@graph", [data])
    keep = [g for g in graph if g.get("@type") in ("BreadcrumbList", "FAQPage", "ItemList")]
    org = {"@type": "Organization", "@id": HOME + "#org", "name": SITE, "url": HOME,
           "logo": {"@type": "ImageObject", "url": DOMAIN + "/favicon.svg"}}
    website = {"@type": "WebSite", "@id": HOME + "#website", "url": HOME, "name": SITE,
               "inLanguage": "en-NG", "publisher": {"@id": HOME + "#org"}}
    image = {"@type": "ImageObject", "url": DOMAIN + "/assets/img/og-cover.jpg", "width": 1200, "height": 630}
    if path == "index.html":
        page = {"@type": "WebPage", "@id": canon + "#webpage", "url": canon, "name": title, "description": desc,
                "inLanguage": "en-NG", "isPartOf": {"@id": HOME + "#website"}, "primaryImageOfPage": image,
                "datePublished": DATE, "dateModified": DATE}
    else:
        page = {"@type": "Article", "@id": canon + "#article", "headline": h1, "name": title, "description": desc,
                "url": canon, "mainEntityOfPage": canon, "inLanguage": "en-NG", "image": image,
                "datePublished": DATE, "dateModified": DATE,
                "author": {"@id": HOME + "#org"}, "publisher": {"@id": HOME + "#org"},
                "isPartOf": {"@id": HOME + "#website"}}
    new = {"@context": "https://schema.org", "@graph": [website, org, page] + keep}
    s = s[:m.start(2)] + "\n" + json.dumps(new, ensure_ascii=False, indent=2) + "\n  " + s[m.end(2):]

    open(full, "w", encoding="utf-8").write(s)
    print("ok", path, [g["@type"] for g in new["@graph"]])


if __name__ == "__main__":
    for p in PAGES:
        process(p)
