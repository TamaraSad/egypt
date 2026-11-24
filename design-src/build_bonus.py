"""Генерирует раздел бонусов: bonus/index.html.
Запуск из папки design-src: python3 build_bonus.py  (затем seo_finalize.py из корня)"""
from build_games import head, foot, crumbs_ld, faq_ld, DOMAIN, write
from build_app import hero, steps_big, cards, faq, AFF, PROMO

RG = "Bonuses are for people aged 18 and over. A bonus never guarantees winnings — only bet money you can afford to lose, and use deposit limits and self-exclusion in your account if you need them."


def page():
    p = "../"
    url = "/bonus/"
    fq = [
        ("What is the 1xBet welcome bonus in Nigeria?", "New customers can choose a sports or casino welcome bonus at sign-up. The sports bonus is added to your first deposit; the casino offer is usually a package over several deposits. The current amounts are shown on the sign-up form."),
        ("How do I get a 1xBet bonus?", f"Register, choose the bonus you want, add promo code {PROMO} and make a qualifying first deposit. Regular promotions for existing players are in the “Promo” section of your account."),
        ("How do I withdraw my 1xBet bonus?", "First complete the wagering requirement within the time limit — for the sports bonus that’s usually accumulators with 3+ selections at odds of 1.40 or higher. When it’s done, the bonus becomes withdrawable cash."),
        ("Can I get more than one welcome bonus?", "No. The welcome bonus is one per person, household, device and payment method. Duplicate accounts can lose their bonuses."),
        ("What is a 1xBet free bet?", "A free bet lets you place a bet without using your own money. If it wins, you usually get the winnings without the free bet stake. Free bets have their own terms and expiry date."),
        ("Are there 1xBet bonuses without a deposit?", "Welcome bonuses need a qualifying deposit. Some promotions for existing players, such as promo code store rewards, can give free bets or spins without a new deposit."),
    ]
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("1xBet Nigeria", "/"), ("Bonus", url)]), faq_ld(fq, DOMAIN + url)]}

    overview = """
    <section class="section" id="types" aria-labelledby="types-title">
      <div class="container">
        <h2 id="types-title">1xBet bonus types at a glance</h2>
        <div class="table-wrap">
          <table class="data-table">
            <caption class="visually-hidden">Main 1xBet bonuses in Nigeria</caption>
            <thead><tr><th scope="col">Bonus</th><th scope="col">Who it’s for</th><th scope="col">How you get it</th></tr></thead>
            <tbody>
              <tr><th scope="row">Sports welcome bonus</th><td data-label="Who it’s for">New customers</td><td data-label="How you get it">Choose it at sign-up and make a qualifying first deposit</td></tr>
              <tr><th scope="row">Casino welcome package</th><td data-label="Who it’s for">New customers</td><td data-label="How you get it">Choose it at sign-up; usually paid over several deposits</td></tr>
              <tr><th scope="row">Free bets</th><td data-label="Who it’s for">Existing players</td><td data-label="How you get it">Promotions, special events and the promo code store</td></tr>
              <tr><th scope="row">Accumulator of the Day</th><td data-label="Who it’s for">All players</td><td data-label="How you get it">Add the daily accumulator to your betslip</td></tr>
              <tr><th scope="row">Promo code store</th><td data-label="Who it’s for">Active players</td><td data-label="How you get it">Exchange bonus points from your bets for rewards</td></tr>
              <tr><th scope="row">Cashback &amp; VIP</th><td data-label="Who it’s for">Regular players</td><td data-label="How you get it">Part of your stakes back, depending on your level</td></tr>
            </tbody>
          </table>
        </div>
        <p class="muted">Promotions change regularly. Check the “Promo” section of your 1xBet account for what’s live right now.</p>
      </div>
    </section>
"""

    welcome = f"""
    <section class="section section--alt" id="welcome" aria-labelledby="welcome-title">
      <div class="container">
        <h2 id="welcome-title">1xBet welcome bonus Nigeria: sports or casino</h2>
        <p class="section__lead">You can take only one welcome offer, so choose the one that matches how you’ll actually play. Both are activated with promo code <span class="inline-code" data-promo>{PROMO}</span>.</p>
        <div class="two-col">
          <div class="side-box">
            <h3>Sports welcome bonus</h3>
            <ul class="check-list">
              <li>1xBet first deposit bonus added to your first qualifying deposit.</li>
              <li>Wagered on accumulators — usually 3+ selections at odds of 1.40 or higher.</li>
              <li>Usually 30 days to complete wagering.</li>
              <li>Best for football and other sports bettors.</li>
            </ul>
          </div>
          <div class="side-box">
            <h3>1xBet casino bonus (welcome package)</h3>
            <ul class="check-list">
              <li>Usually spread over your first few deposits, often with free spins.</li>
              <li>Wagered as a multiple of the bonus on eligible casino games.</li>
              <li>Some games count less or not at all towards wagering.</li>
              <li>Best for slots, live casino and crash games.</li>
            </ul>
          </div>
        </div>
        <a class="btn btn--primary" href="{AFF}" target="_blank" rel="sponsored noopener">Claim the Welcome Bonus</a>
        <a class="link-more" href="{p}promo-code/">How to use the promo code, with a wagering example →</a>
      </div>
    </section>
"""

    promos = cards("promotions", "1xBet promotions for existing players", [
        ("1xBet free bet", "Free bets from promotions and special events — check the stake, minimum odds and expiry before using one."),
        ("1xBet Accumulator of the Day", "A ready-made accumulator picked by 1xBet, often with boosted odds."),
        ("1xBet promo code store", "Earn bonus points from your bets and swap them for promo codes such as free bets or free spins."),
        ("1xBet cashback & VIP", "Regular players can get part of their stakes back, with better terms at higher levels."),
        ("Tournaments & prize draws", "Leaderboards and draws around big football events and casino games."),
        ("Event specials", "Extra offers around AFCON, the Premier League and other major competitions."),
    ], lead="After the welcome bonus, 1xBet runs regular offers. They change often, so treat this list as a guide and check your account for the current ones.")

    withdraw = steps_big("withdraw", "How to Withdraw 1xBet Bonus Money",
                         "Bonus money can’t be withdrawn straight away. Here’s how it turns into cash you can take out.", [
                             ("Check the terms", "Open the bonus in your account to see the wagering multiple, eligible bets and time limit."),
                             ("Place qualifying bets", "For the sports bonus: accumulators with 3+ selections at odds of 1.40 or higher."),
                             ("Track your progress", "Your account shows how much you’ve wagered and how much is left."),
                             ("Finish before it expires", "Unfinished wagering is cancelled when the time limit runs out."),
                             ("Verify your account", "Upload a valid ID — it’s needed before your first withdrawal."),
                             ("Withdraw in Naira", "Once wagering is done, the bonus winnings become withdrawable cash."),
                         ])

    rules = cards("rules", "1xBet bonus terms and rules to know", [
        ("One bonus per person", "Only one welcome bonus per person, household, device and payment method."),
        ("Minimum deposit", "Deposits below the minimum for the offer don’t get the bonus."),
        ("Payment methods", "Some deposit methods may not qualify for bonuses — check the terms before paying."),
        ("Withdrawing early", "Withdrawing before wagering is finished can cancel the bonus and its winnings."),
        ("Bet restrictions", "Single bets, low odds and some markets don’t count towards wagering."),
        ("Terms can change", "The terms shown in your account on the day you claim are the ones that apply."),
    ], alt=True, after='        <div class="notice notice--warn">\n          <p><b>Beware of fake bonuses:</b> 1xBet bonuses are only claimed in your account or on the sign-up form. Never pay anyone or share your login to “activate” a bonus.</p>\n        </div>')

    body = (hero(p, [("1xBet Nigeria", p), ("Bonus", None)], "1xBet Bonus Nigeria: Welcome Offers, Free Bets & Cashback",
                 f"Every 1xBet bonus available to Nigerian players in one place: the sports and casino welcome offers for new customers, plus free bets, Accumulator of the Day, the promo code store and cashback. Claim the welcome bonus with promo code <span class=\"inline-code inline-code--dark\" data-promo>{PROMO}</span>.",
                 "bonus-wallet", "Phone showing a 1xBet sports welcome bonus with wagering progress, a free bet ticket and cashback", 600, 520, "Claim Your Bonus")
            + overview + welcome + promos + withdraw + rules
            + faq("1xBet bonus FAQ", fq)
            + f"""
    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-band__inner">
        <div>
          <h2 id="cta-title">Get your 1xBet welcome bonus</h2>
          <p>Sign up with promo code <span class="inline-code inline-code--dark" data-promo>{PROMO}</span> and make your first deposit.</p>
        </div>
        <a class="btn btn--primary btn--lg" href="{AFF}" target="_blank" rel="sponsored noopener">Claim Your Bonus</a>
      </div>
    </section>
""")
    return head(p, "1xBet Bonus Nigeria: Welcome Bonus, Free Bets & Cashback",
                "All 1xBet bonuses in Nigeria: sports and casino welcome offers, free bets, Accumulator of the Day, promo code store, cashback and how to withdraw a bonus.",
                url, ld, current="bonus") + body + foot(p, rg=RG)


if __name__ == "__main__":
    write("bonus/index.html", page())
