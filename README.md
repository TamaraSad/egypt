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

## Размещение
Любой статический хостинг (GitHub Pages, Netlify, Cloudflare Pages). HTTPS, минификация CSS/JS при сборке.
