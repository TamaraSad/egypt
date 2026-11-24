# 1xBet Nigeria — landing page

Static landing page (HTML/CSS/JS), English, for Nigerian users.

## Structure
```
index.html                    landing page
assets/css/style.css          styles
assets/js/main.js             menu, FAQ, promo code + copy button
assets/img/*.svg              illustrations
seo/keywords-nigeria.csv      semantic core: cluster, keyword, intent, priority, target page
favicon.svg, robots.txt, sitemap.xml
```

## Где что менять
- **Промокод** — одна строка в `assets/js/main.js` (`PROMO_CODE`). В HTML он тоже прописан как запасной вариант для браузеров без JS.
- **Партнёрская ссылка** — во всех кнопках с `rel="sponsored"` в `index.html` (поиск по `reffpa.com`).
- **Логотип 1xBet** — `assets/img/1xbet-logo.png` (шапка и подвал). Исходник был маленьким (100×23 px), увеличен ×4. Лучше заменить на официальный SVG/PNG из промо-материалов партнёрской программы.
- **Домен** — заменить `https://example.com` в `index.html`, `robots.txt`, `sitemap.xml`.
- **OG-картинка** — `assets/img/og-cover.jpg` (1200×630).

## Перед запуском
- Проверить, что промокод работает для нигерийских аккаунтов, и сверить условия бонуса на 1xbet.ng.
- Проверить, что партнёрская ссылка ведёт нигерийских пользователей на лицензированный 1xbet.ng.
- Рекламу ставок в Нигерии регулирует ARCON (Advertising Regulatory Council of Nigeria) — уточнить требования к партнёрским материалам.

## Сборка (после любых правок)
```
python3 design-src/render_mocks.py      # только если меняли макеты design-src/mock-*.html
python3 design-src/build_games.py       # только если меняли тексты игр
cd design-src && python3 build_app.py && python3 build_login.py && cd ..   # разделы App и Login
python3 design-src/build_assets.py      # WebP 1x/2x, PNG-заглушки, логотип, *.min.css / *.min.js
python3 design-src/seo_finalize.py      # schema.org, og/twitter, srcset, подключение .min-файлов
```
Правки стилей и скриптов делаются в `style.css`, `main.js`, `game-scenes.js`; сайт подключает их `.min`-версии.

## SEO
- У каждой страницы свои title (≤ 60 символов), description (120–160), canonical, Open Graph и Twitter Card.
- schema.org: WebSite + Organization на всех страницах, WebPage на главной, Article на внутренних,
  BreadcrumbList, FAQPage (совпадает с видимым FAQ), ItemList в разделе Games.
- `sitemap.xml` (11 URL) и `robots.txt`. Перед запуском замените `https://example.com` на домен во всех файлах.

## Размещение
Любой статический хостинг (GitHub Pages, Netlify, Cloudflare Pages). HTTPS, минификация CSS/JS при сборке.
