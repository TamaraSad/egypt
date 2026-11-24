# 1xBet Nigeria — landing page

Static landing page (HTML/CSS/JS), English, for Nigerian users.

## Structure
```
index.html                    landing page (English)
pcm/index.html                Nigerian Pidgin version
assets/css/style.css          styles
assets/js/main.js             menu, FAQ, promo code + copy button
assets/img/*.svg              illustrations
seo/keywords-nigeria.csv      semantic core: cluster, keyword, intent, priority, target page
favicon.svg, robots.txt, sitemap.xml
```

## Языковые версии
- `/` — английский (`lang="en-NG"`), `/pcm/` — нигерийский пиджин (`lang="pcm"`).
- Переключатель EN / Pidgin — в шапке обеих страниц.
- hreflang между версиями не прописан: Google принимает только двухбуквенные коды ISO 639-1, а у пиджина есть только трёхбуквенный `pcm`. Обе страницы есть в sitemap.xml и связаны переключателем.
- Правки текста делаются в обоих файлах.

## Где что менять
- **Промокод** — одна строка в `assets/js/main.js` (`PROMO_CODE`). В HTML он тоже прописан как запасной вариант для браузеров без JS.
- **Партнёрская ссылка** — во всех кнопках с `rel="sponsored"` в `index.html` (поиск по `reffpa.com`).
- **Логотип 1xBet** — положите официальный файл в `assets/img/1xbet-logo.svg`; пока его нет, выводится текст «1xBet».
- **Домен** — заменить `https://example.com` в `index.html`, `robots.txt`, `sitemap.xml`.
- **OG-картинка** — `assets/img/og-cover.jpg` (1200×630).

## Перед запуском
- Проверить, что промокод работает для нигерийских аккаунтов, и сверить условия бонуса на 1xbet.ng.
- Проверить, что партнёрская ссылка ведёт нигерийских пользователей на лицензированный 1xbet.ng.
- Рекламу ставок в Нигерии регулирует ARCON (Advertising Regulatory Council of Nigeria) — уточнить требования к партнёрским материалам.

## Размещение
Любой статический хостинг (GitHub Pages, Netlify, Cloudflare Pages). HTTPS, минификация CSS/JS при сборке.
