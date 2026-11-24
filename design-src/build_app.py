"""Генерирует раздел App: app/index.html, app/android/index.html, app/ios/index.html.
Запуск из корня репозитория: python3 design-src/build_app.py  (затем seo_finalize.py)"""
from build_games import head, foot, esc, crumbs_ld, faq_ld, faq_html, AFF, PROMO, DOMAIN, write


RG = "Betting is for people aged 18 and over. Only bet money you can afford to lose, and use deposit limits and self-exclusion in your account if you need them."


def promo(prefix):
    return f"""          <div class="promo-card promo-card--compact">
            <div class="promo-card__offer">
              <p class="promo-card__label">New to 1xBet?</p>
              <p class="promo-card__value">Welcome bonus on your first deposit</p>
              <p class="promo-card__note">Add the promo code when you sign up. <a href="{prefix}promo-code/">Bonus terms</a></p>
            </div>
            <div class="promo-card__code">
              <p class="promo-card__label">Promo code</p>
              <div class="code-box">
                <span class="code-box__value" data-promo>{PROMO}</span>
                <button class="code-box__copy" type="button" data-copy data-copied="Copied!">Copy</button>
              </div>
            </div>
          </div>"""


def hero(prefix, crumbs, h1, lead, img, alt, w, h, cta):
    crumb_html = ''.join(
        (f'<a href="{u}">{esc(n)}</a><span aria-hidden="true">›</span>' if u else f'<span aria-current="page">{esc(n)}</span>')
        for n, u in crumbs)
    return f"""
    <section class="hero page-hero">
      <div class="container hero__grid">
        <div class="hero__text">
          <nav class="breadcrumbs" aria-label="Breadcrumbs">{crumb_html}</nav>
          <h1>{esc(h1)}</h1>
          <p class="hero__lead">{lead}</p>
{promo(prefix)}
          <div class="hero__actions">
            <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">{esc(cta)}</a>
          </div>
        </div>
        <figure class="hero__art">
          <picture>
            <source srcset="{prefix}assets/img/{img}.webp" type="image/webp">
            <img src="{prefix}assets/img/{img}.png" alt="{esc(alt)}" width="{w}" height="{h}" fetchpriority="high">
          </picture>
        </figure>
      </div>
    </section>
"""


def facts(title, rows):
    trs = "\n".join(f'              <tr><th scope="row">{esc(k)}</th><td data-label="Details">{v}</td></tr>' for k, v in rows)
    return f"""
    <section class="section" id="facts" aria-labelledby="facts-title">
      <div class="container">
        <h2 id="facts-title">{esc(title)}</h2>
        <div class="table-wrap">
          <table class="data-table data-table--kv">
            <caption class="visually-hidden">{esc(title)}</caption>
            <thead><tr><th scope="col">Question</th><th scope="col">Details</th></tr></thead>
            <tbody>
{trs}
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""


def steps_big(sec_id, title, lead, items, alt=True, after=""):
    lis = "\n".join(f"""          <li>
            <h3>{esc(t)}</h3>
            <p>{d}</p>
          </li>""" for t, d in items)
    return f"""
    <section class="section{' section--alt' if alt else ''}" id="{sec_id}" aria-labelledby="{sec_id}-title">
      <div class="container">
        <h2 id="{sec_id}-title">{esc(title)}</h2>
        <p class="section__lead">{lead}</p>
        <ol class="steps steps--big">
{lis}
        </ol>
{after}
      </div>
    </section>
"""


def cards(sec_id, title, items, lead="", alt=False, cols3=True, after=""):
    arts = "\n".join(f"""          <article class="card">
            <h3>{esc(t)}</h3>
            <p>{d}</p>
          </article>""" for t, d in items)
    lead_html = f'\n        <p class="section__lead">{lead}</p>' if lead else ""
    return f"""
    <section class="section{' section--alt' if alt else ''}" id="{sec_id}" aria-labelledby="{sec_id}-title">
      <div class="container">
        <h2 id="{sec_id}-title">{esc(title)}</h2>{lead_html}
        <div class="cards{' cards--3' if cols3 else ''}">
{arts}
        </div>
{after}
      </div>
    </section>
"""


def faq(title, items, alt=False):
    return f"""
    <section class="section{' section--alt' if alt else ''}" id="faq" aria-labelledby="faq-title">
      <div class="container container--narrow">
        <h2 id="faq-title">{esc(title)}</h2>
        <div class="faq">
{faq_html(items)}
        </div>
      </div>
    </section>
"""


def related(prefix, items, title="More app guides"):
    links = "\n".join(f"""          <a class="game-card game-card--sm" href="{u}">
            <img src="{prefix}assets/img/{img}-1x.webp" alt="" width="600" height="520" loading="lazy" decoding="async">
            <span class="game-card__body"><b>{esc(n)}</b><span>{esc(d)}</span><span class="game-card__more">Read the guide →</span></span>
          </a>""" for n, d, u, img in items)
    return f"""
    <section class="section section--alt" id="more" aria-labelledby="more-title">
      <div class="container">
        <h2 id="more-title">{esc(title)}</h2>
        <div class="game-grid game-grid--2">
{links}
        </div>
      </div>
    </section>
"""


def cta(title, btn):
    return f"""
    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-band__inner">
        <div>
          <h2 id="cta-title">{esc(title)}</h2>
          <p>Sign up in the app with promo code <span class="inline-code inline-code--dark" data-promo>{PROMO}</span>.</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">{esc(btn)}</a>
      </div>
    </section>
"""


def warn(text):
    return f'        <div class="notice notice--warn">\n          <p>{text}</p>\n        </div>'


# ---------------- HUB ----------------
def hub():
    p = "../"
    url = "/app/"
    fq = [
        ("Is the 1xBet app free?", "Yes. Downloading and installing the 1xBet app costs nothing. You only pay when you choose to make a deposit."),
        ("Is there a 1xBet app for Nigeria?", "Yes. There is an Android app and an iPhone app for Nigerian players. Get them through the apps section of the official 1xBet website."),
        ("Can I use the same account in the app and on the website?", "Yes. Your 1xBet account, balance and bets are the same on the app, the mobile site and the desktop site."),
        ("Do I need the app to bet on my phone?", "No. The 1xBet mobile site works in any phone browser. The app is faster and adds push notifications."),
        ("Can I use the promo code in the app?", f"Yes. The sign-up form in the app has a promo code field. Enter {PROMO} before you tap “Register”."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("1xBet Nigeria", "/"), ("App", url)]), faq_ld(fq, DOMAIN + url)]}
    compare = """
    <section class="section section--alt" id="compare" aria-labelledby="compare-title">
      <div class="container">
        <h2 id="compare-title">1xBet app vs mobile site</h2>
        <div class="table-wrap">
          <table class="data-table">
            <caption class="visually-hidden">1xBet app compared with the mobile site</caption>
            <thead><tr><th scope="col">Feature</th><th scope="col">1xBet app</th><th scope="col">Mobile site</th></tr></thead>
            <tbody>
              <tr><th scope="row">Installation</th><td data-label="1xBet app">Needs a download</td><td data-label="Mobile site">None — open in your browser</td></tr>
              <tr><th scope="row">Speed</th><td data-label="1xBet app">Faster, especially for live betting</td><td data-label="Mobile site">Depends on your browser and connection</td></tr>
              <tr><th scope="row">Notifications</th><td data-label="1xBet app">Push alerts for goals and bet results</td><td data-label="Mobile site">Limited</td></tr>
              <tr><th scope="row">Updates</th><td data-label="1xBet app">Install new versions</td><td data-label="Mobile site">Always up to date</td></tr>
              <tr><th scope="row">Account &amp; bonus</th><td data-label="1xBet app">Same account and welcome bonus</td><td data-label="Mobile site">Same account and welcome bonus</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
    feats = cards("features", "What you can do in the 1xBet app", [
        ("Live betting &amp; stats", "Follow NPFL, EPL and other games live with odds that update in real time."),
        ("Push notifications", "Get alerts for goals, results and settled bets without opening the app."),
        ("Booking codes", "Load a friend’s betslip or share yours in a couple of taps."),
        ("Casino &amp; crash games", "Play slots, live casino and crash games like Aviator in the same app."),
        ("Naira deposits &amp; withdrawals", "Deposit and withdraw in ₦ from the cashier inside the app."),
        ("One account everywhere", "Log in with the same details you use on the website."),
    ])
    reg = steps_big("register", "How to sign up in the 1xBet app with a promo code",
                    "Already installed the app? Here is how to create your account and claim the welcome bonus.", [
                        ("Open the app", "Tap “Registration” on the first screen."),
                        ("Choose a sign-up method", "Phone number, email or one click."),
                        ("Enter the promo code", f'Type <span class="inline-code" data-promo>{PROMO}</span> in the promo code field.'),
                        ("Pick your bonus and deposit", "Choose the sports or casino offer and make your first deposit in Naira."),
                    ], after=warn("<b>Stay safe:</b> only download the 1xBet app through the official website or the official App Store listing. Apps from Telegram groups or file-sharing sites can be modified to steal your login and card details."))
    body = (hero(p, [("1xBet Nigeria", p), ("App", None)], "1xBet App Nigeria: Download for Android & iPhone",
                 "The 1xBet app puts the full sportsbook and casino on your phone — live betting, push notifications and Naira payments. It’s free on Android and iPhone, and you can use the same account as on the website.",
                 "home-app", "Two phones with the 1xBet app: live NPFL match with odds and a casino lobby with crash games", 580, 520, "Get the 1xBet App")
            + compare + feats + reg + faq("1xBet app FAQ", fq) + cta("Get the 1xBet app", "Get the 1xBet App"))
    return head(p, "1xBet App Nigeria: Download for Android & iPhone (iOS)",
                "Download the 1xBet app in Nigeria for Android and iPhone: how to get it safely, key features, app vs mobile site and signing up with a promo code.",
                url, ld, current="app") + body + foot(p, rg=RG)


# ---------------- ANDROID ----------------
def android():
    p = "../../"
    url = "/app/android/"
    fq = [
        ("Is the 1xBet APK safe?", "Yes, when you download it through the official 1xBet website. APK files from other sites, Telegram groups or shared links can be modified and are not safe."),
        ("Is the 1xBet app on Google Play in Nigeria?", "It depends on the app version and your region. The apps section of the official site sends you either to Google Play or to a direct APK download — always use that link."),
        ("How much space does the 1xBet app need?", "The exact size and Android requirements are shown on the download page. Free up some storage before you start so the install doesn’t fail."),
        ("How do I update the 1xBet app on Android?", "Accept the update when the app asks, or update it in Google Play. If you installed an APK, download the newest version from the official site and install it over the old one."),
        ("Can I use the promo code in the Android app?", f"Yes. Enter {PROMO} in the promo code field when you register in the app."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("1xBet Nigeria", "/"), ("App", "/app/"), ("Android", url)]), faq_ld(fq, DOMAIN + url)]}
    body = (hero(p, [("1xBet Nigeria", p), ("App", "../"), ("Android", None)], "1xBet App for Android: Download & Install Guide for Nigeria",
                 "Get the 1xBet app on your Android phone in a few minutes. Download it through the official site — via Google Play or as a 1xBet APK file — install it, and log in or sign up with our promo code.",
                 "app-android", "Android phone showing the install dialog for the 1xBet app downloaded from the official site", 600, 520, "Download for Android")
            + facts("1xBet Android app at a glance", [
                ("Price", "Free"),
                ("Where to get it", "The apps section of the official 1xBet website — it links to Google Play or a direct APK download"),
                ("File type", "APK, when downloaded directly"),
                ("Requirements", "Shown on the download page — a recent Android version and some free storage"),
                ("Account", "The same account as on the website"),
                ("Updates", "In-app prompt, Google Play, or a new APK from the official site"),
            ])
            + steps_big("download", "How to do the 1xBet APK download on Android",
                        "Follow these steps on your Android phone. If the official site sends you to Google Play, just tap “Install” there and skip steps 4–5.", [
                            ("Open the official 1xBet site", "Use your phone’s browser (for example Chrome) — not a link from a group or ad."),
                            ("Go to the apps section", "Find “Mobile apps” in the site menu or at the bottom of the page."),
                            ("Choose Android", "Tap the Android download button."),
                            ("Allow the install", "If Android asks, allow your browser to install unknown apps (see below)."),
                            ("Install the app", "Open the downloaded 1xBet APK and tap “Install”."),
                            ("Log in or sign up", f'Open the app and log in, or register with promo code <span class="inline-code" data-promo>{PROMO}</span>.'),
                        ])
            + f"""
    <section class="section" id="unknown-apps" aria-labelledby="unknown-apps-title">
      <div class="container">
        <div class="two-col">
          <div>
            <h2 id="unknown-apps-title">How to allow installing the APK</h2>
            <p>Android blocks apps from outside Google Play by default. To install the 1xBet APK you allow it once for your browser, then switch it back off.</p>
            <ol class="steps">
              <li>Open <b>Settings</b> → <b>Apps</b> (or <b>Security</b>).</li>
              <li>Find <b>Special app access</b> → <b>Install unknown apps</b>.</li>
              <li>Choose the browser you used to download the file and turn on <b>Allow from this source</b>.</li>
              <li>After installing, come back and turn it off again.</li>
            </ol>
            <p class="muted">Menu names differ a little between phone brands such as Samsung, Tecno, Infinix and Xiaomi.</p>
          </div>
          <div class="side-box">
            <h3>Before you install</h3>
            <ul class="check-list">
              <li>Download only through the official 1xBet website.</li>
              <li>Make sure you have enough free storage.</li>
              <li>Delete any old 1xBet APK you got from somewhere else.</li>
              <li>Check the app’s permissions — it doesn’t need your contacts or SMS inbox.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""
            + cards("problems", "1xBet Android app not installing? Quick fixes", [
                ("“App not installed”", "Remove any older 1xBet app first, free up storage and try again with a fresh download."),
                ("“Problem parsing the package”", "The file didn’t download fully. Delete it and download it again on a stable connection."),
                ("Play Protect warning", "Android may warn about apps from outside Google Play. Only continue if the file came from the official 1xBet site."),
                ("Not enough storage", "Clear cache or delete unused apps and photos, then install again."),
                ("App closes or freezes", "Update to the latest version from the official site and restart your phone."),
                ("Can’t log in", f'Check your login details or reset your password. See the <a href="{p}login/">login guide</a>.'),
            ], alt=True)
            + faq("1xBet Android app FAQ", fq)
            + cta("Get the 1xBet app for Android", "Download for Android"))
    return head(p, "1xBet APK Download Nigeria: Android App Install Guide",
                "1xBet app for Android in Nigeria: how to download the 1xBet APK safely from the official site, allow the install, update the app and fix common install errors.",
                url, ld, current="android") + body + foot(p, rg=RG)


# ---------------- iOS ----------------
def ios():
    p = "../../"
    url = "/app/ios/"
    fq = [
        ("Is the 1xBet app available on the App Store in Nigeria?", "Yes. It is listed in the Nigerian App Store as “1xBet NG ― Betting & Casino”."),
        ("Which iPhones can run the 1xBet app?", "The App Store listing requires iOS 15.0 or later on iPhone, and iPadOS 15.0 or later on iPad."),
        ("Why can’t I find the 1xBet app in the App Store?", "Your Apple ID may be set to another country. Apps are shown by App Store region, so the Nigerian listing appears for Apple IDs set to Nigeria. You can also use the mobile site in Safari."),
        ("Do I need to install a profile to get the 1xBet iOS app?", "No. Install the app only from the App Store. Never install configuration profiles or apps from links sent in chats."),
        ("Can I use the promo code in the iPhone app?", f"Yes. Enter {PROMO} in the promo code field when you register in the app."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("1xBet Nigeria", "/"), ("App", "/app/"), ("iPhone", url)]), faq_ld(fq, DOMAIN + url)]}
    body = (hero(p, [("1xBet Nigeria", p), ("App", "../"), ("iPhone", None)], "1xBet App for iPhone (iOS): Download Guide for Nigeria",
                 "On iPhone the 1xBet app installs straight from the App Store, where it’s listed for Nigeria as “1xBet NG ― Betting &amp; Casino”. It’s free and needs iOS 15.0 or later.",
                 "app-ios", "iPhone showing the 1xBet NG app page in the App Store with the Get button and iOS 15.0 requirement", 600, 520, "Download for iPhone")
            + facts("1xBet iOS app at a glance", [
                ("Price", "Free"),
                ("Where to get it", "The App Store — “1xBet NG ― Betting &amp; Casino”"),
                ("iPhone requirement", "iOS 15.0 or later"),
                ("iPad requirement", "iPadOS 15.0 or later"),
                ("Account", "The same account as on the website"),
                ("Updates", "Through the App Store, like any other app"),
            ])
            + steps_big("download", "How to download the 1xBet app on iPhone",
                        "It takes about a minute. You don’t need to change any security settings on your iPhone.", [
                            ("Open the official 1xBet site in Safari", "Or search the App Store for “1xBet NG”."),
                            ("Go to the apps section", "Tap “Mobile apps” and choose iPhone."),
                            ("Open the App Store page", "Check that the app is “1xBet NG ― Betting &amp; Casino”."),
                            ("Tap “Get”", "Confirm with Face ID, Touch ID or your Apple ID password."),
                            ("Open the app", "Find the 1xBet icon on your home screen."),
                            ("Log in or sign up", f'Log in, or register with promo code <span class="inline-code" data-promo>{PROMO}</span>.'),
                        ])
            + f"""
    <section class="section" id="no-app" aria-labelledby="no-app-title">
      <div class="container">
        <div class="two-col">
          <div>
            <h2 id="no-app-title">Can’t install the app? Use the mobile site</h2>
            <p>If your iPhone is on an older iOS version or the app doesn’t show in your App Store region, the 1xBet mobile site works in Safari with the same account. You can even pin it like an app:</p>
            <ol class="steps">
              <li>Open the official 1xBet site in <b>Safari</b>.</li>
              <li>Tap the <b>Share</b> button.</li>
              <li>Choose <b>Add to Home Screen</b> and tap <b>Add</b>.</li>
            </ol>
          </div>
          <div class="side-box">
            <h3>Stay safe on iPhone</h3>
            <ul class="check-list">
              <li>Install the app only from the App Store.</li>
              <li>Never install configuration profiles from chat links.</li>
              <li>Check the app name and developer before tapping “Get”.</li>
              <li>Turn on two-step verification in your 1xBet account.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""
            + cards("problems", "1xBet iOS app problems and fixes", [
                ("“Requires a newer iOS”", "Update your iPhone in Settings → General → Software Update. The app needs iOS 15.0 or later."),
                ("App not in the App Store", "Your Apple ID may be set to another country. Use the mobile site in Safari instead."),
                ("Download stuck", "Check your connection and free storage, then tap the app icon to pause and resume."),
                ("App crashes", "Update the app in the App Store and restart your iPhone."),
                ("Can’t log in", f'Check your details or reset your password. See the <a href="{p}login/">login guide</a>.'),
                ("Notifications not showing", "Allow notifications for 1xBet in Settings → Notifications."),
            ], alt=True)
            + faq("1xBet iPhone app FAQ", fq)
            + cta("Get the 1xBet app for iPhone", "Download for iPhone"))
    return head(p, "1xBet App iOS Nigeria: Download for iPhone & iPad",
                "1xBet app for iPhone in Nigeria: get 1xBet NG from the App Store, iOS 15.0+ requirements, fixes if the app isn’t showing and sign-up with a promo code.",
                url, ld, current="ios") + body + foot(p, rg=RG)


if __name__ == "__main__":
    write("app/index.html", hub())
    write("app/android/index.html", android())
    write("app/ios/index.html", ios())
