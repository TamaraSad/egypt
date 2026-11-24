"""Генерирует раздел Games: games/index.html и страницы игр.
Запуск из корня репозитория:  python3 design-src/build_games.py
Тексты игр — в словаре GAMES ниже. Промокод подставляется скриптом main.js в [data-promo].
"""
import html
import json
import os

DOMAIN = "https://example.com"
AFF = "https://reffpa.com/L?tag=d_3686639m_1599c_&amp;site=3686639&amp;ad=1599&amp;r=registration"
PROMO = "EGYPTONEX20"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def esc(s):
    return html.escape(s, quote=True)


def head(prefix, title, desc, canonical, ld, current="games"):
    cur = lambda k: ' aria-current="page"' if k == current else ""
    return f"""<!DOCTYPE html>
<html lang="en-NG" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- ЗАМЕНИТЕ https://example.com на реальный домен во всех местах -->
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{DOMAIN}{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0b1d36">

  <meta property="og:type" content="article">
  <meta property="og:locale" content="en_NG">
  <meta property="og:site_name" content="1xBet Nigeria Guide">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{DOMAIN}{canonical}">
  <meta property="og:image" content="{DOMAIN}/assets/img/og-cover.jpg">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="{prefix}assets/css/style.css">

  <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
    <symbol id="flag-ng" viewBox="0 0 900 600">
      <rect width="900" height="600" fill="#ffffff"/>
      <rect width="300" height="600" fill="#008751"/>
      <rect x="600" width="300" height="600" fill="#008751"/>
    </symbol>
  </svg>


  <header class="site-header" id="top">
    <div class="container site-header__inner">
      <a class="site-logo" href="{prefix}" aria-label="1xBet Nigeria guide — home">
        <img src="{prefix}assets/img/1xbet-logo.png" alt="1xBet" width="122" height="28">
      </a>

      <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>

      <nav class="site-nav" id="site-nav" aria-label="Main menu">
        <ul>
          <li><a href="{prefix}">Home</a></li>
          <li><a href="{prefix}registration/">Sign Up</a></li>
          <li><a href="{prefix}promo-code/"{cur("promo")}>Promo Code</a></li>
          <li><a href="{prefix}bonus/"{cur("bonus")}>Bonus</a></li>
          <li class="has-sub"><a href="{prefix}app/"{cur("app")}>App</a><button class="sub-toggle" type="button" aria-expanded="false" aria-label="Show app pages"><span aria-hidden="true">▾</span></button><ul class="sub-menu"><li><a href="{prefix}app/android/"{cur("android")}>Android</a></li><li><a href="{prefix}app/ios/"{cur("ios")}>iPhone</a></li></ul></li>
          <li><a href="{prefix}login/"{cur("login")}>Login</a></li>
          <li class="has-sub"><a href="{prefix}games/"{cur("games")}>Games</a><button class="sub-toggle" type="button" aria-expanded="false" aria-label="Show game pages"><span aria-hidden="true">▾</span></button><ul class="sub-menu"><li><a href="{prefix}games/aviator/"{cur("aviator")}>Aviator</a></li><li><a href="{prefix}games/chicken-road/"{cur("chicken-road")}>Chicken Road</a></li><li><a href="{prefix}games/tower-rush/"{cur("tower-rush")}>Tower Rush</a></li></ul></li>
        </ul>
      </nav>

      <a class="btn btn--primary btn--sm header-cta" href="{AFF}" target="_blank" rel="sponsored noopener">Sign Up</a>
    </div>
  </header>

  <main id="main">
"""


def foot(prefix, scenes=False, rg=None):
    scene_js = f'\n  <script src="{prefix}assets/js/game-scenes.js" defer></script>' if scenes else ""
    return f"""
    <section class="section legal" id="legal" aria-labelledby="legal-title">
      <div class="container">
        <h2 id="legal-title">{"Bet responsibly" if rg else "Play responsibly"}</h2>
        <div class="legal__grid">
          <div class="legal__item">
            <h3><span class="age-badge">18+</span> Adults only</h3>
            <p>{rg or "Casino games are for people aged 18 and over. Results are random — only play with money you can afford to lose, and use deposit limits and self-exclusion in your account if you need them."}</p>
          </div>
        </div>
        <p class="disclaimer"><b>Disclaimer:</b> This is an independent guide and is not operated by 1xBet{"" if rg else " or the game providers"}. We may earn a commission when you sign up through links on this page. Trademarks belong to their owners.{" Offers, features and terms can change — always check the official 1xBet site." if rg else " Game availability, limits and RTP can differ by casino — check the game’s info panel before you play."}</p>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container site-footer__inner">
      <div class="site-footer__brand">
        <span class="brand-logo">
          <img src="{prefix}assets/img/1xbet-logo.png" alt="1xBet" width="139" height="32">
        </span>
        <span class="footer-divider" aria-hidden="true"></span>
        <span class="footer-country">
          <svg class="flag flag--sm" role="img" aria-label="Flag of Nigeria"><use href="#flag-ng"/></svg>
          <span>Nigeria</span>
        </span>
      </div>
      <nav aria-label="Site links">
        <ul>
          <li><a href="{prefix}">Home</a></li>
          <li><a href="{prefix}bonus/">Bonus</a></li>
          <li><a href="{prefix}app/">App</a></li>
          <li><a href="{prefix}games/">Games</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy/">Privacy Policy</a></li>
          <li><a href="/terms/">Terms of Use</a></li>
          <li><a href="/responsible-gambling/">Responsible Gambling</a></li>
        </ul>
      </nav>
      <p class="site-footer__copy"><span class="age-badge">18+</span> © <span id="year">2026</span> Independent 1xBet Nigeria guide. Affiliate links. T&amp;Cs apply.</p>
    </div>
  </footer>

  <a class="to-top" href="#top" aria-label="Back to top">↑</a>

  <script src="{prefix}assets/js/main.js" defer></script>{scene_js}
</body>
</html>
"""


def promo_card():
    return f"""          <div class="promo-card promo-card--compact">
            <div class="promo-card__offer">
              <p class="promo-card__label">New to 1xBet?</p>
              <p class="promo-card__value">Casino welcome bonus</p>
              <p class="promo-card__note">Choose the casino offer at sign-up. Terms apply.</p>
            </div>
            <div class="promo-card__code">
              <p class="promo-card__label">Promo code</p>
              <div class="code-box">
                <span class="code-box__value" data-promo>{PROMO}</span>
                <button class="code-box__copy" type="button" data-copy data-copied="Copied!">Copy</button>
              </div>
            </div>
          </div>"""


GAMES = {
    "aviator": {
        "name": "Aviator",
        "img": "game-aviator.svg",
        "img_alt": "Crash game screen with a plane climbing on a rising curve, a 2.47x multiplier and two bet panels",
        "title": "Aviator on 1xBet Nigeria: How to Play, Rules, RTP & Tips",
        "desc": "How to play Aviator on 1xBet Nigeria: rules, 97% RTP, double bet, auto cash-out, provably fair results and safe play tips. 18+.",
        "h1": "Aviator on 1xBet Nigeria: How to Play the Crash Game",
        "lead": "Aviator is the crash game Nigerian players talk about most. A plane takes off, the multiplier climbs from 1.00x, and you decide when to cash out — before the plane flies away.",
        "short": "The original crash game: a plane takes off, the multiplier climbs, and you cash out before it flies away.",
        "facts": [
            ("Provider", "Spribe"),
            ("Released", "2019"),
            ("Game type", "Crash game"),
            ("RTP", "97% (theoretical, long-term)"),
            ("Bets per round", "Up to two, each with its own cash-out"),
            ("Key features", "Auto bet, auto cash-out, live bets, provably fair"),
        ],
        "chips": [("Spribe", ""), ("RTP 97%", ""), ("Crash", "")],
        "how": [
            "Place one or two bets during the short countdown before take-off.",
            "The plane takes off and the multiplier grows from 1.00x.",
            "Cash out at any moment: your win is your stake × the multiplier at that moment.",
            "If the plane flies away before you cash out, that bet is lost.",
            "The crash point of each round is random, and you can verify it with the provably fair check.",
        ],
        "features": [
            ("Double bet", "Run two bets in the same round — for example, one with an early auto cash-out and one you cash out by hand."),
            ("Auto cash-out", "Set a target multiplier before the round. If the plane reaches it, the bet is cashed out for you."),
            ("Live bets & stats", "See other players’ bets and cash-outs in real time, plus the history of recent rounds."),
            ("Provably fair", "Each round’s result can be checked with cryptographic seeds, so it can’t be changed after the bet."),
        ],
        "search": "Aviator",
        "scam": "“Aviator predictor” apps, bots and Telegram “signals” are scams. The crash point is random and can’t be predicted — sellers make money from you, not from the game.",
        "faq": [
            ("Can I play Aviator on 1xBet Nigeria?", "Aviator is one of the most popular games in the 1xBet casino. Log in, open the casino and search for “Aviator”. Availability can change, so check the lobby."),
            ("What is the RTP of Aviator?", "Aviator has a theoretical RTP of 97%. It is a long-term average over millions of rounds, not what you will get in one session."),
            ("Do Aviator predictors work?", "No. Results are random and provably fair. Any app or channel that promises to predict the next multiplier is trying to take your money."),
            ("Can I play Aviator on my phone?", "Yes. Aviator runs in the 1xBet app and on the mobile site, on Android and iPhone."),
            ("Can I use the welcome bonus on Aviator?", "It depends on the terms of the casino welcome offer. Some games count less or not at all towards wagering — check the bonus terms before you play."),
        ],
    },
    "chicken-road": {
        "name": "Chicken Road",
        "img": "game-chicken-road.svg",
        "img_alt": "Chicken crossing a road with multiplier markers on each lane and cars driving by",
        "title": "Chicken Road on 1xBet Nigeria: How to Play, Levels & RTP",
        "desc": "How to play Chicken Road on 1xBet Nigeria: game rules, 4 difficulty levels, up to 98% RTP, when to cash out and safe play tips. 18+.",
        "h1": "Chicken Road on 1xBet Nigeria: How to Play and Pick a Difficulty",
        "lead": "Chicken Road is a quick casino game where you help a chicken cross a busy road. Every lane it survives raises the multiplier — cash out whenever you like, or risk one more step.",
        "short": "Guide a chicken across a busy road. Every safe lane raises the multiplier — cash out or risk one more step.",
        "facts": [
            ("Provider", "InOut Games"),
            ("Game type", "Step-by-step multiplier game"),
            ("RTP", "Up to 98% (theoretical, long-term)"),
            ("Difficulty levels", "Easy, Medium, Hard, Hardcore"),
            ("Main decision", "When to stop and cash out"),
            ("Round length", "A few seconds to a minute"),
        ],
        "chips": [("InOut Games", ""), ("RTP up to 98%", ""), ("4 levels", "")],
        "how": [
            "Choose your stake and a difficulty level.",
            "Tap to move the chicken forward one lane at a time.",
            "Each lane it crosses safely raises the multiplier.",
            "Cash out at any point to take stake × the current multiplier.",
            "If the chicken gets hit, the round ends and the stake is lost.",
        ],
        "features": [
            ("Easy", "More lanes and smaller steps up the multiplier. The calmest way to learn the game."),
            ("Medium", "Bigger jumps per lane with a higher chance of the round ending."),
            ("Hard", "Fewer safe steps, faster-growing multipliers."),
            ("Hardcore", "The biggest multipliers and the highest risk on every single step."),
        ],
        "features_title": "Difficulty levels",
        "search": "Chicken Road",
        "scam": "Chicken Road “hacks”, “signals” and bots don’t work. Each step is random — nobody can tell you which lane is safe.",
        "faq": [
            ("Can I play Chicken Road on 1xBet Nigeria?", "Search for “Chicken Road” in the 1xBet casino lobby after you log in. Game lists can change, so check what’s available in your account."),
            ("Is Chicken Road skill or luck?", "Luck. Whether the chicken survives a lane is random. Your only decision is when to cash out."),
            ("Which difficulty level is best?", "None of them gives you better long-term odds. Higher levels just make wins bigger and rarer, so pick the one that fits your budget."),
            ("What is the RTP of Chicken Road?", "The provider lists an RTP of up to 98%. It is a long-term average, and the exact figure can depend on the casino’s settings."),
            ("Can I play Chicken Road on my phone?", "Yes. It is built for mobile and runs in the 1xBet app and on the mobile site."),
        ],
    },
    "tower-rush": {
        "name": "Tower Rush",
        "img": "game-tower-rush.svg",
        "img_alt": "Crane stacking floors on a tower with an x3.20 multiplier and a cash-out button",
        "title": "Tower Rush on 1xBet Nigeria: How to Play, Rules & RTP",
        "desc": "How to play Tower Rush on 1xBet Nigeria: how the tower-building crash game works, its RTP, when to cash out and safe play tips. 18+.",
        "h1": "Tower Rush on 1xBet Nigeria: How to Play the Tower-Building Game",
        "lead": "In Tower Rush a crane stacks floor after floor on a tower, and every new floor pushes the multiplier higher. Cash out while the tower stands — if it collapses first, the round is lost.",
        "short": "A crane stacks floor after floor. Each floor raises the multiplier — cash out before the tower falls.",
        "facts": [
            ("Provider", "Galaxsys"),
            ("Game type", "Crash-style tower game"),
            ("RTP", "Around 97% (can vary by casino settings)"),
            ("Main decision", "When to cash out"),
            ("Round length", "A few seconds"),
            ("Devices", "Desktop, Android and iPhone"),
        ],
        "chips": [("Galaxsys", ""), ("RTP ~97%", ""), ("Crash", "")],
        "how": [
            "Set your stake before the round starts.",
            "The crane starts stacking floors on the tower.",
            "Every new floor raises the multiplier.",
            "Cash out at any moment to take stake × the current multiplier.",
            "If the tower collapses before you cash out, the stake is lost.",
        ],
        "features": [
            ("Simple to follow", "One tower, one multiplier, one button — easy to learn in a couple of rounds."),
            ("Fast rounds", "Rounds last seconds, so set a budget before you start and stick to it."),
            ("Cash-out control", "You choose the moment to stop. Earlier cash-outs win more often but pay less."),
            ("Game info panel", "Check the panel inside the game for the exact RTP, limits and rules at your casino."),
        ],
        "search": "Tower Rush",
        "scam": "Tower Rush “predictors” and paid signals are scams. When the tower collapses is random and can’t be forecast.",
        "faq": [
            ("Can I play Tower Rush on 1xBet Nigeria?", "Search for “Tower Rush” in the 1xBet casino lobby after you log in. Game lists change, so check what’s available in your account."),
            ("Who makes Tower Rush?", "Tower Rush is made by Galaxsys, a casino game studio known for fast crash-style games."),
            ("What is the RTP of Tower Rush?", "Listings show an RTP of around 97%, but casinos can use different settings. The info panel inside the game shows the exact figure."),
            ("Is there a strategy that always wins?", "No. The collapse point is random. Cash-out timing changes how often you win and how much, not the house edge."),
            ("Can I play Tower Rush on my phone?", "Yes. It runs in the 1xBet app and on the mobile site."),
        ],
    },
}
ORDER = ["aviator", "chicken-road", "tower-rush"]


def faq_ld(items, page_id):
    return {"@type": "FAQPage", "@id": page_id + "#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(items)]}


def faq_html(items):
    return "\n".join(f"""          <details>
            <summary>{esc(q)}</summary>
            <p>{esc(a)}</p>
          </details>""" for q, a in items)


def game_page(slug):
    g = GAMES[slug]
    prefix = "../../"
    url = f"/games/{slug}/"
    ld = {"@context": "https://schema.org", "@graph": [
        crumbs_ld([("1xBet Nigeria", "/"), ("Games", "/games/"), (g["name"], url)]),
        faq_ld(g["faq"], DOMAIN + url)]}
    facts = "\n".join(f'              <tr><th scope="row">{esc(k)}</th><td data-label="Details">{esc(v)}</td></tr>' for k, v in g["facts"])
    how = "\n".join(f"            <li>{esc(s)}</li>" for s in g["how"])
    feats = "\n".join(f"""          <article class="card">
            <h3>{esc(t)}</h3>
            <p>{esc(d)}</p>
          </article>""" for t, d in g["features"])
    others = "\n".join(f"""          <a class="game-card game-card--sm" href="../{o}/">
            <img src="{prefix}assets/img/{GAMES[o]['img']}" alt="" width="560" height="420" loading="lazy" decoding="async">
            <span class="game-card__body"><b>{esc(GAMES[o]['name'])}</b><span>{esc(GAMES[o]['short'])}</span></span>
          </a>""" for o in ORDER if o != slug)
    name = esc(g["name"])
    body = f"""
    <section class="hero page-hero">
      <div class="container hero__grid">
        <div class="hero__text">
          <nav class="breadcrumbs" aria-label="Breadcrumbs">
            <a href="{prefix}">1xBet Nigeria</a><span aria-hidden="true">›</span><a href="../">Games</a><span aria-hidden="true">›</span><span aria-current="page">{name}</span>
          </nav>
          <h1>{esc(g['h1'])}</h1>
          <p class="hero__lead">{esc(g['lead'])}</p>
{promo_card()}
          <div class="hero__actions">
            <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">Play {name} on 1xBet</a>
          </div>
        </div>
        <figure class="hero__art">
          <div class="game-screen">
            <img class="game-fallback" src="{prefix}assets/img/{g['img']}" alt="{esc(g['img_alt'])}" width="560" height="420" fetchpriority="high">
            <canvas class="game-canvas" data-scene="{slug}" width="560" height="420" role="img" aria-label="Animated preview of a {name} round"></canvas>
          </div>
        </figure>
      </div>
    </section>

    <section class="section" id="facts" aria-labelledby="facts-title">
      <div class="container">
        <h2 id="facts-title">{name} at a glance</h2>
        <div class="table-wrap">
          <table class="data-table data-table--kv">
            <caption class="visually-hidden">{name} key facts</caption>
            <thead><tr><th scope="col">Feature</th><th scope="col">Details</th></tr></thead>
            <tbody>
{facts}
            </tbody>
          </table>
        </div>
        <p class="muted">RTP is a theoretical long-term figure. It doesn’t tell you what will happen in a single round or session.</p>
      </div>
    </section>

    <section class="section section--alt" id="how" aria-labelledby="how-title">
      <div class="container">
        <div class="two-col">
          <div>
            <h2 id="how-title">How {name} works</h2>
            <ol class="steps">
{how}
            </ol>
          </div>
          <div class="side-box">
            <h2 class="h3">How to play {name} on 1xBet</h2>
            <ol class="steps">
              <li>Sign up on 1xBet with promo code <span class="inline-code" data-promo>{PROMO}</span>.</li>
              <li>Make a deposit in Naira.</li>
              <li>Open the casino and search for “{esc(g['search'])}”.</li>
              <li>Set your stake and play a few low-stake rounds first.</li>
            </ol>
            <a class="btn btn--primary" href="{AFF}" target="_blank" rel="sponsored noopener">Play {name}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="features" aria-labelledby="features-title">
      <div class="container">
        <h2 id="features-title">{esc(g.get('features_title', name + ' features'))}</h2>
        <div class="cards">
{feats}
        </div>
      </div>
    </section>

    <section class="section section--alt" id="smart" aria-labelledby="smart-title">
      <div class="container">
        <h2 id="smart-title">Play {name} with a plan</h2>
        <div class="two-col">
          <ul class="check-list">
            <li>Decide your budget for the session before you start, and stop when it’s gone.</li>
            <li>Keep stakes small — rounds are fast and add up quickly.</li>
            <li>Don’t chase losses with bigger bets.</li>
            <li>Cash-out timing changes how often you win and how much, not the long-term odds.</li>
          </ul>
          <div class="notice notice--warn">
            <p><b>Watch out:</b> {esc(g['scam'])}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="faq" aria-labelledby="faq-title">
      <div class="container container--narrow">
        <h2 id="faq-title">{name} FAQ</h2>
        <div class="faq">
{faq_html(g['faq'])}
        </div>
      </div>
    </section>


    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-band__inner">
        <div>
          <h2 id="cta-title">Try {name} on 1xBet</h2>
          <p>Sign up with promo code <span class="inline-code inline-code--dark" data-promo>{PROMO}</span> and pick the casino welcome offer.</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">Play {name} on 1xBet</a>
      </div>
    </section>
"""
    return head(prefix, g["title"], g["desc"], url, ld, current=slug) + body + foot(prefix, scenes=True)


def hub_page():
    prefix = "../"
    url = "/games/"
    hub_faq = [
        ("Which 1xBet games are most popular in Nigeria?", "Crash and instant games like Aviator, Chicken Road and Tower Rush are among the most played, alongside slots and live casino."),
        ("Are these games fair?", "They use random number generators, and games like Aviator offer a provably fair check. Results can’t be predicted or influenced."),
        ("Can I try the games for free?", "Some casinos offer demo modes for these games. Check the game in the 1xBet lobby — if a demo is available, you’ll see a “Demo” option."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [
        crumbs_ld([("1xBet Nigeria", "/"), ("Games", url)]),
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": GAMES[s]["name"], "url": f"{DOMAIN}/games/{s}/"} for i, s in enumerate(ORDER)]},
        faq_ld(hub_faq, DOMAIN + url)]}
    cards = "\n".join(f"""          <a class="game-card" href="{s}/">
            <img src="{prefix}assets/img/{GAMES[s]['img']}" alt="{esc(GAMES[s]['img_alt'])}" width="560" height="420" {'fetchpriority="high"' if i == 0 else 'loading="lazy" decoding="async"'}>
            <span class="game-card__body">
              <b>{esc(GAMES[s]['name'])}</b>
              <span>{esc(GAMES[s]['short'])}</span>
              <span class="chips">{''.join(f'<em>{esc(c)}</em>' for c, _ in GAMES[s]['chips'])}</span>
              <span class="game-card__more">How to play {esc(GAMES[s]['name'])} →</span>
            </span>
          </a>""" for i, s in enumerate(ORDER))
    body = f"""
    <section class="hero page-hero page-hero--slim">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumbs">
          <a href="{prefix}">1xBet Nigeria</a><span aria-hidden="true">›</span><span aria-current="page">Games</span>
        </nav>
        <h1>1xBet Games Nigeria: Aviator, Chicken Road &amp; Tower Rush</h1>
        <p class="hero__lead">Fast casino games are some of the most played on 1xBet in Nigeria. Here’s how Aviator, Chicken Road and Tower Rush compare — pick a game from the Games menu for the full guide.</p>
      </div>
    </section>


    <section class="section section--alt" id="compare" aria-labelledby="compare-title">
      <div class="container">
        <h2 id="compare-title">Compare the games</h2>
        <div class="table-wrap">
          <table class="data-table">
            <caption class="visually-hidden">Aviator, Chicken Road and Tower Rush compared</caption>
            <thead><tr><th scope="col">Game</th><th scope="col">Provider</th><th scope="col">How a round works</th><th scope="col">RTP</th></tr></thead>
            <tbody>
              <tr><th scope="row">Aviator</th><td data-label="Provider">Spribe</td><td data-label="How a round works">Plane takes off, cash out before it flies away</td><td data-label="RTP">97%</td></tr>
              <tr><th scope="row">Chicken Road</th><td data-label="Provider">InOut Games</td><td data-label="How a round works">Move lane by lane, cash out before the chicken is hit</td><td data-label="RTP">Up to 98%</td></tr>
              <tr><th scope="row">Tower Rush</th><td data-label="Provider">Galaxsys</td><td data-label="How a round works">Floors stack up, cash out before the tower falls</td><td data-label="RTP">~97%</td></tr>
            </tbody>
          </table>
        </div>
        <p class="muted">RTP figures are theoretical long-term averages and can differ by casino settings.</p>
      </div>
    </section>

    <section class="section" id="faq" aria-labelledby="faq-title">
      <div class="container container--narrow">
        <h2 id="faq-title">1xBet games FAQ</h2>
        <div class="faq">
{faq_html(hub_faq)}
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-band__inner">
        <div>
          <h2 id="cta-title">Play on 1xBet</h2>
          <p>Sign up with promo code <span class="inline-code inline-code--dark" data-promo>{PROMO}</span> and pick the casino welcome offer.</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">Sign Up on 1xBet</a>
      </div>
    </section>
"""
    return head(prefix, "1xBet Games Nigeria: Aviator, Chicken Road & Tower Rush", "Guides to popular 1xBet casino games in Nigeria: Aviator, Chicken Road and Tower Rush — rules, RTP, tips and how to play each one. 18+.", url, ld) + body + foot(prefix)


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


if __name__ == "__main__":
    write("games/index.html", hub_page())
    for s in ORDER:
        write(f"games/{s}/index.html", game_page(s))
