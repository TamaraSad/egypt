"""Генерирует страницу входа: login/index.html.
Запуск из папки design-src: python3 build_login.py  (затем seo_finalize.py из корня)"""
from build_games import head, foot, crumbs_ld, faq_ld, DOMAIN, write
from build_app import hero, facts, steps_big, cards, faq, warn, AFF, PROMO


RG = "Betting is for people aged 18 and over. Only bet money you can afford to lose, and use deposit limits and self-exclusion in your account if you need them."


def page():
    p = "../"
    url = "/login/"
    fq = [
        ("How do I log in to 1xBet Nigeria?", "Tap “Log in” at the top of the official 1xBet site or on the first screen of the app, enter your account ID, phone number or email and your password, then tap “Log in”."),
        ("Can I log in to 1xBet with my phone number?", "Yes. Choose the phone option, enter your Nigerian number with +234 and your password. 1xBet may also send an SMS code to confirm it’s you."),
        ("I forgot my 1xBet password. What should I do?", "Tap “Forgot password?” on the login form and reset it by SMS or email. You need access to the phone number or email linked to your account."),
        ("Why can’t I log in to 1xBet?", "The most common reasons are a wrong password, the wrong login method selected, a typo in the phone number or a fake site. Check the address, reset your password, and contact support from the official site if your account is blocked."),
        ("Is it safe to log in to 1xBet from links in WhatsApp or Telegram?", "No. Fake sites copy the 1xBet login page to steal accounts. Type the address yourself or use the official app."),
        ("Can I use the same login in the app and on the website?", "Yes. Your 1xBet login details work on the app, the mobile site and the desktop site."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("1xBet Nigeria", "/"), ("Login", url)]), faq_ld(fq, DOMAIN + url)]}

    methods = cards("methods", "3 ways to sign in to 1xBet", [
        ("Account ID + password", "Your 1xBet account number from registration — handy if you signed up with one click."),
        ("Phone number + password", "1xBet login with phone number: enter your +234 number and password. An SMS code may be requested."),
        ("Email + password", "Use the email you registered with. Good if you don’t want to depend on SMS."),
    ], lead="Pick the tab that matches how you registered. Using the wrong tab is the most common reason a correct password “doesn’t work”.")

    app_and_reset = f"""
    <section class="section" id="app-login" aria-labelledby="app-login-title">
      <div class="container">
        <div class="two-col">
          <div>
            <h2 id="app-login-title">1xBet login in the app</h2>
            <ol class="steps">
              <li>Open the 1xBet app — see the <a href="{p}app/">app guide</a> if you don’t have it yet.</li>
              <li>Tap <b>Log in</b> on the first screen.</li>
              <li>Choose ID, phone or email and enter your password.</li>
              <li>Tick <b>Remember me</b> on your own phone only.</li>
            </ol>
          </div>
          <div class="side-box">
            <h3 id="forgot">1xBet forgot password: how to reset it</h3>
            <ol class="steps">
              <li>Tap <b>Forgot password?</b> on the login form.</li>
              <li>Choose SMS or email and enter your phone number or email.</li>
              <li>Enter the code you receive.</li>
              <li>Create a new password you don’t use anywhere else.</li>
            </ol>
          </div>
        </div>
      </div>
    </section>
"""

    security = f"""
    <section class="section" id="security" aria-labelledby="security-title">
      <div class="container">
        <h2 id="security-title">Keep your 1xBet account safe</h2>
        <div class="two-col">
          <ul class="check-list">
            <li><b>Turn on two-step verification</b> in your account settings — a code is needed at every login.</li>
            <li><b>Use a unique password</b> that you don’t use for email or social media.</li>
            <li><b>Never share SMS codes</b> — 1xBet support will never ask for them.</li>
            <li><b>Log out on shared devices</b> and don’t tick “Remember me” there.</li>
            <li><b>Check your login history</b> in the account settings from time to time.</li>
          </ul>
          <div class="notice notice--warn">
            <p><b>Watch out for fake login pages:</b> scammers copy the 1xBet sign-in page and share it in WhatsApp groups, Telegram and ads. Always check the address in your browser before typing your password, or use the official app.</p>
          </div>
        </div>
      </div>
    </section>
"""

    body = (hero(p, [("1xBet Nigeria", p), ("Login", None)], "1xBet Login Nigeria: How to Sign In to Your Account",
                 "Here’s how to do your 1xBet login (also known as 1xBet NG login) on the website and in the app, sign in with your phone number, reset a forgotten password and fix the most common login problems.",
                 "home-login", "1xBet login form in a browser with a padlock, Nigerian phone number and password, plus two-step verification and an SMS code", 600, 460, "New? Sign Up on 1xBet")
            + facts("1xBet sign in at a glance", [
                ("Where to log in", "“Log in” button at the top of the official 1xBet site, or the first screen of the app"),
                ("Login options", "Account ID, phone number (+234) or email — plus your password"),
                ("Forgot password", "Reset it by SMS or email from the login form"),
                ("Extra security", "Two-step verification and SMS codes"),
                ("One account", "The same login works on the app, mobile site and desktop"),
            ])
            + steps_big("steps", "How to log in to 1xBet on the website",
                        "Takes less than a minute on your phone or computer.", [
                            ("Open the official 1xBet site", "Type the address yourself or use a saved bookmark — not a link from a chat or ad."),
                            ("Tap “Log in”", "You’ll find it at the top right of the page."),
                            ("Choose how to sign in", "ID, phone number or email — the one you registered with."),
                            ("Enter your password", "Use the eye icon to check it for typos."),
                            ("Confirm if asked", "Enter the SMS or authenticator code if two-step verification is on."),
                        ])
            + methods
            + app_and_reset
            + cards("problems", "1xBet login problems and how to fix them", [
                ("Wrong password", "Check the login tab, Caps Lock and the +234 prefix. Still failing? Reset the password."),
                ("SMS code not arriving", "Check your signal and the number, wait a minute and request a new code, or reset by email."),
                ("Account blocked", "Too many wrong attempts or a security check. Contact support from the official site — not through social media."),
                ("Site not opening", "Check your internet connection and the address, clear the browser cache, or use the official app."),
                ("Logged out all the time", "Allow cookies for the site, keep the app updated and don’t use private browsing."),
                ("Verification requested", "1xBet may ask you to confirm your identity. Upload a clear photo of a valid ID from your account settings."),
            ], alt=True)
            + security
            + faq("1xBet login FAQ", fq, alt=True)
            + f"""
    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-band__inner">
        <div>
          <h2 id="cta-title">Don’t have a 1xBet account yet?</h2>
          <p>Sign up in two minutes with promo code <span class="inline-code inline-code--dark" data-promo>{PROMO}</span>.</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">Sign Up on 1xBet</a>
      </div>
    </section>
""")
    return head(p, "1xBet Login Nigeria: Sign In, Phone Login & Password Reset",
                "1xBet login Nigeria guide: how to sign in on the site and app, log in with your phone number, reset a forgotten password and fix common login problems.",
                url, ld, current="login") + body + foot(p, rg=RG)


if __name__ == "__main__":
    write("login/index.html", page())
