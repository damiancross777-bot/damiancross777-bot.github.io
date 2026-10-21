#!/usr/bin/env python3
"""Builds the Phoneporium.AU static site. Run: python3 build.py (writes the HTML pages in place)."""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "phoneporium.au@gmail.com"
UPDATED = "21 October 2026"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700;800&display=swap" rel="stylesheet">')


def page(path, title, desc, body, nav=""):
    up = "/" if path == "404" else "../" * (path.count("/") + 1 if path else 0)
    def cur(n):
        return ' aria-current="page"' if n == nav else ""
    html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{up}assets/favicon-64.png">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body class="{'home' if not path else ''}">
<header class="site-head"><div class="wrap">
  <a class="brand" href="{up or './'}"><span class="brand-mark" aria-hidden="true">P</span>Phoneporium.AU</a>
  <nav class="site-nav" aria-label="Main">
    <a href="{up}gridrova/"{cur('gridrova')}>GridRova</a>
    <a href="{up}gridrova/support/"{cur('support')}>Support</a>
    <a href="{up}gridrova/privacy/"{cur('privacy')}>Privacy</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <p>Phoneporium.AU, an independent game developer in Australia. Contact <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <nav aria-label="Footer">
    <a href="{up}gridrova/privacy/">Privacy policy</a>
    <a href="{up}gridrova/delete-data/">Delete your data</a>
    <a href="{up}gridrova/support/">Support</a>
  </nav>
</div></footer>
</body>
</html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    if path == "404":
        out = ROOT / "404.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


# ---- Hero board: drawn like the GridRova store art (white board, navy letters, sage trace) ----------
BOARD = ["QBEAW", "YULDN", "HOIAK", "SVBER", "APFMT"]
assert "".join(BOARD[i][i] for i in range(5)) == "QUIET"
C, PAD = 80, 20
parts = [f'<rect x="4" y="4" width="{5*C+2*PAD-8}" height="{5*C+2*PAD-8}" rx="28" class="b-face"/>']
for i in range(1, 5):
    parts.append(f'<line x1="{PAD+i*C}" y1="{PAD+8}" x2="{PAD+i*C}" y2="{PAD+5*C-8}" class="b-rule"/>')
    parts.append(f'<line x1="{PAD+8}" y1="{PAD+i*C}" x2="{PAD+5*C-8}" y2="{PAD+i*C}" class="b-rule"/>')
c0, c4 = PAD + C / 2, PAD + 4 * C + C / 2
parts.append(f'<line x1="{c0}" y1="{c0}" x2="{c4}" y2="{c4}" class="b-trace" pathLength="1"/>')
for r, row in enumerate(BOARD):
    for c, ch in enumerate(row):
        parts.append(f'<text x="{PAD+c*C+C/2}" y="{PAD+r*C+C/2}" class="b-letter">{ch}</text>')
board = (f'<svg class="board" viewBox="0 0 {5*C+2*PAD} {5*C+2*PAD}" role="img" '
         f'aria-label="A word-search board with the word QUIET traced diagonally">' + "".join(parts) + "</svg>")

page("", "Phoneporium.AU", "Phoneporium.AU makes calm, family-friendly mobile word games in Australia. Home of GridRova.", f"""
<section class="hero scenic"><div class="wrap">
  <div class="hero-copy">
    <h1>Small games for quiet minutes.</h1>
    <p>Phoneporium.AU is an independent studio in Australia making calm, family-friendly puzzle games for Android.</p>
    <p>Our first game, GridRova, is a scenic word search with 300 levels.</p>
  </div>
  {board}
</div></section>
<section class="section"><div class="wrap">
  <h2>GridRova</h2>
  <a class="feature-link" href="gridrova/"><img class="feature-art" src="assets/gridrova-feature.jpg" alt="GridRova beside a sage-highlighted BLOOM word grid, with a sunlit mountain valley and river behind it." width="1024" height="500"></a>
  <div class="game solo">
    <div>
      <p>Trace hidden words across 300 levels and 30 scenic stops, from easy first grids to longer words in every direction. Play untimed, try a daily puzzle or take on a time challenge.</p>
      <p class="status">Coming soon to Google Play</p>
      <p><a href="gridrova/">More about GridRova</a></p>
    </div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <h2>Help and policies</h2>
  <div class="links">
    <a href="gridrova/support/"><strong>Support</strong><span>Questions, problems and how to reach us.</span></a>
    <a href="gridrova/privacy/"><strong>Privacy policy</strong><span>What GridRova stores, and why.</span></a>
    <a href="gridrova/delete-data/"><strong>Delete your data</strong><span>Remove your online rankings data.</span></a>
  </div>
</div></section>
""")

page("gridrova", "GridRova by Phoneporium.AU", "GridRova is a scenic word-search game with 300 levels, daily puzzles and optional time challenges.", f"""
<section class="feature"><div class="wrap">
  <img class="feature-art" src="../assets/gridrova-feature.jpg" alt="GridRova beside a sage-highlighted BLOOM word grid, with a sunlit mountain valley and river behind it." width="1024" height="500">
</div></section>
<section class="intro"><div class="wrap">
  <img class="intro-icon" src="../assets/gridrova-icon-256.png" alt="" width="112" height="112">
  <div>
    <h1>GridRova</h1>
    <p class="lede">Spot hidden words and explore 300 levels of scenic word-search puzzles.</p>
    <p>That lovely moment when a hidden word suddenly comes into focus: one last letter, a quick trace, and there it is. GridRova turns that small discovery into a scenic word-search journey.</p>
    <p class="status">Coming soon to Google Play</p>
  </div>
</div></section>
<section class="shots-band" aria-label="Screens from GridRova"><ul class="shots"><li><img src="../assets/shots/gridrova-01.jpg" alt="A welcoming five-by-five word-search board in The Firefly Wilds, with GOAT, FROG and OWL to find." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-02.jpg" alt="An underwater word-search board with CORGI highlighted vertically and MINK horizontally; LARK and SEAL remain." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-03.jpg" alt="The journey shows forest and underwater scenic stops, completed levels and the next available puzzle." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-04.jpg" alt="The scenic album shows The Firefly Wilds and The Sapphire Sanctuary collected, with later postcards still locked." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-05.jpg" alt="The help panel offers a free nudge, a coin-priced trace and one free rescue per puzzle." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-06.jpg" alt="The daily Colors puzzle has VIOLET highlighted backwards across a row and RUSSET vertically in a scenic sky setting." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-07.jpg" alt="An optional timed Animals puzzle shows a countdown and solved-word highlights for CUCKOO and FALCON." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-08.jpg" alt="Settings offer separate sound options, reduced motion, high contrast and tap-first-and-last-letter selection." width="540" height="960" loading="lazy"></li></ul></section>
<section class="section"><div class="wrap">
  <h2>What's inside</h2>
  <ul class="facts">
    <li>300 levels</li><li>30 scenic stops</li><li>Postcards to collect</li><li>Daily puzzles from level 10</li>
    <li>Time challenges from level 20</li><li>Plays offline</li><li>No purchases</li>
  </ul>
  <p style="max-width:62ch">Start with simple puzzles, then explore larger grids, longer words and more directions. Themes from animals and food to space and ocean life keep each chapter fresh. Stuck? Use a recharging nudge, or spend in-game coins on hints. Coins are earned by playing and can't be bought.</p>
  <p style="max-width:62ch">GridRova is free and shows ads. Players under 13, and anyone who prefers not to give their age, only see child-safe ads. Optional online rankings use a random name, never an email address.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="links">
    <a href="support/"><strong>Support</strong><span>Get help with GridRova.</span></a>
    <a href="privacy/"><strong>Privacy policy</strong><span>What GridRova stores, and why.</span></a>
    <a href="delete-data/"><strong>Delete your data</strong><span>Remove your online rankings data.</span></a>
  </div>
</div></section>
""", nav="gridrova")

page("gridrova/privacy", "GridRova privacy policy", "How GridRova by Phoneporium.AU handles information, including ads, the age question and online rankings.", f"""
<article class="doc"><div class="wrap">
<h1>GridRova privacy policy</h1>
<p class="meta">Last updated {UPDATED}. Applies to GridRova version 1.0 for Android.</p>

<div class="summary">
<h2>The short version</h2>
<ul>
<li>GridRova has no sign-up. We never ask for your name, email, phone number, contacts, photos or location.</li>
<li>Your game progress stays on your phone.</li>
<li>When the game first opens it asks what year you were born. Only an age group is kept, on your phone, to choose which kind of ads you can see.</li>
<li>Players under 13, and anyone who chooses "Prefer not to say", only get child-safe, non-personalised ads.</li>
<li>Online rankings use a random player name and an anonymous ID. You can delete that data from the game at any time.</li>
<li>We don't sell your information, and GridRova has no in-app purchases and no analytics.</li>
</ul>
</div>

<h2>Who we are</h2>
<p>GridRova is made by Phoneporium.AU, an independent game developer in Australia. We are responsible for the information described in this policy. You can contact us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Information kept on your phone</h2>
<p>GridRova saves the following on your device so you can carry on where you left off: level progress, puzzle in progress, coins, postcards, settings (sound, music, grid lines) and your age group. This information isn't sent to us. It is removed if you uninstall the game or clear its storage.</p>

<h2>The age question</h2>
<p>The first time you open GridRova, it asks "What year were you born?" with nothing preselected, and a "Prefer not to say" option. The game works out an age group (under 13, 13 to 17, or 18 and over) and stores only that group and when it was chosen. The birth year itself is not stored or sent anywhere.</p>
<p>The age group is used only to set up ads (see below). You can switch to child-safe ads at any time in Settings. To protect younger players, the game won't switch from child-safe ads back to normal ads.</p>

<h2>Advertising</h2>
<p>GridRova is free and shows ads from Google AdMob. Ads are not shown until the age question has been answered.</p>
<table>
<thead><tr><th scope="col">Age group</th><th scope="col">What happens</th></tr></thead>
<tbody>
<tr><td>Under 13, or "Prefer not to say"</td><td>Ad requests are marked as child-directed and under the age of consent. Only non-personalised ads rated G are requested. Formats that can't meet child-safe rules are switched off.</td></tr>
<tr><td>13 to 17</td><td>Ad requests are marked as under the age of consent. Only non-personalised ads rated PG are requested.</td></tr>
<tr><td>18 and over</td><td>Google's consent message is shown where the law requires it. With your consent, ads may be personalised; otherwise they are non-personalised. Ads are rated PG or lower.</td></tr>
</tbody>
</table>
<p>To show and measure ads, Google may collect information such as your IP address, device and app information and ad interactions, and the device advertising ID. For child-directed and under-age requests, Google limits how this information is used and doesn't use it to personalise ads. Google handles this information under its own policy: <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its services</a>. You can reset or delete your advertising ID in your phone's settings.</p>

<h2>Online rankings</h2>
<p>GridRova has optional daily rankings and a Champions list for players who finish all 300 levels. When you first take part, the game creates an anonymous player ID using Google Firebase Authentication. No email address or account is involved. The ID is stored securely on your phone.</p>
<p>Our server then keeps:</p>
<ul>
<li>your anonymous player ID and a randomly generated player name (for example, a word pairing), which you didn't choose and which doesn't identify you</li>
<li>start and finish times of ranked puzzles, your result and rank</li>
<li>which levels have been recorded online, for the Champions list</li>
<li>any in-game coin prizes awarded for a daily podium place (coins have no cash value)</li>
</ul>
<p>Your random player name, rank and time are shown publicly on the rankings. Our server runs on Google Cloud in Australia (Sydney region). Google keeps basic request logs, which include IP addresses, for security and troubleshooting; these are kept for about 30 days.</p>
<p>Version 1.0 has no account linking and no cloud save. Your game progress is not uploaded.</p>

<h2>What we don't do</h2>
<ul>
<li>We don't sell or rent personal information.</li>
<li>We don't use analytics or tracking tools of our own.</li>
<li>The game doesn't request location, contacts, camera, microphone, photos or file storage permissions.</li>
<li>There are no in-app purchases or chat features.</li>
</ul>

<h2>Children</h2>
<p>GridRova is designed to be suitable for all ages, including children. We don't ask children for personal information. Players under 13, and anyone whose age is unknown, get child-safe ad settings as described above. Online rankings use only a random name and an anonymous ID. A parent or guardian can delete a child's online data at any time from the game or by emailing us.</p>

<h2>How long we keep information</h2>
<ul>
<li>On your phone: until you uninstall the game or clear its data.</li>
<li>Online rankings data: while you keep playing. You can delete it whenever you like.</li>
<li>Final daily results: kept so past podiums stay correct. If you delete your data, your place stays but your name is replaced with "Deleted player".</li>
<li>Server request logs: about 30 days.</li>
</ul>

<h2>Deleting your data</h2>
<p>In GridRova, open Settings and choose "Delete my online data". This removes your anonymous ID and everything our server holds about you, straight away. Your progress on your phone isn't affected. You can also <a href="../delete-data/">ask us by email</a>.</p>

<h2>Your rights</h2>
<p>You can ask us what information we hold about you, ask us to correct it or delete it, or ask a question about this policy by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>. Because we don't collect names or email addresses through the game, we may ask you for the player name shown in the game so we can find your data. We aim to reply within 30 days.</p>
<p>We follow the Australian Privacy Principles. If you are not happy with our response, you can contact the <a href="https://www.oaic.gov.au/privacy/privacy-complaints">Office of the Australian Information Commissioner</a>. If you live elsewhere, you may also have rights under your local law, such as the GDPR in Europe and the UK.</p>

<h2>Information sent overseas</h2>
<p>Ad requests are handled by Google, which may process information in other countries, including the United States. Our rankings server is hosted in Australia.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we'll update this page and the date at the top. If the change is significant, such as adding accounts or cloud save, we'll also say so in the game before it takes effect.</p>
</div></article>
""", nav="privacy")

page("gridrova/support", "GridRova support", "Get help with GridRova by Phoneporium.AU.", f"""
<article class="doc"><div class="wrap">
<h1>GridRova support</h1>
<p class="meta">Email <a href="mailto:{EMAIL}?subject=GridRova%20support">{EMAIL}</a>. We usually reply within a few working days.</p>
<p>When you write, it helps to include your phone model, the Android version and the level number, plus a screenshot if something looks wrong.</p>

<h2>Common questions</h2>
<h3>Will I lose my progress if I change phones?</h3>
<p>Progress is saved on your phone. Version 1.0 doesn't include cloud save, so progress doesn't move to a new phone, and uninstalling the game removes it.</p>
<h3>Does GridRova work offline?</h3>
<p>Yes. The journey and daily puzzles work without internet. Ads and online rankings need a connection.</p>
<h3>Can I buy coins?</h3>
<p>No. GridRova has no purchases. You earn coins by playing, and your first Rescue in each puzzle is free.</p>
<h3>Why did the game ask for my birth year?</h3>
<p>So it can choose suitable ads. Only an age group is kept, on your phone. If you'd rather not say, choose "Prefer not to say" and you'll get child-safe ads. See the <a href="../privacy/">privacy policy</a> for details.</p>
<h3>How do I switch to child-safe ads?</h3>
<p>Open Settings and choose "Use child-safe ads".</p>
<h3>Where does my ranking name come from?</h3>
<p>It's generated at random so that nobody's real name appears on the rankings.</p>
<h3>How do I delete my online data?</h3>
<p>Open Settings and choose "Delete my online data". More options are on the <a href="../delete-data/">delete your data</a> page.</p>
</div></article>
""", nav="support")

page("gridrova/delete-data", "Delete your GridRova data", "How to delete the online data GridRova by Phoneporium.AU holds about you.", f"""
<article class="doc"><div class="wrap">
<h1>Delete your GridRova data</h1>
<p class="meta">GridRova by Phoneporium.AU. Last updated {UPDATED}.</p>
<p>GridRova doesn't use accounts or email addresses. If you've taken part in online rankings, our server holds an anonymous player ID, a random player name and your ranking results. You can delete all of it.</p>

<h2>Delete it in the game</h2>
<ol class="steps">
<li>Open GridRova and go to Settings.</li>
<li>Choose "Delete my online data" and confirm.</li>
<li>Your anonymous ID, player name, ranking results, Champions record and any coin prize records are removed from our server straight away.</li>
</ol>

<h2>Ask us by email</h2>
<p>If you no longer have the game installed, email <a href="mailto:{EMAIL}?subject=GridRova%20data%20deletion">{EMAIL}</a> with the subject "GridRova data deletion" and, if you can, your player name as shown in the game. We'll confirm when it's done, within 30 days.</p>

<h2>What is deleted, and what is kept</h2>
<ul>
<li>Deleted: your anonymous player ID, player name, ranked attempts and results, Champions record and coin prize records.</li>
<li>Kept: past daily final results keep your place so other players' ranks stay correct, but your name is replaced with "Deleted player". We also keep a record of the anonymous ID and when it was deleted, so a prize can't be paid to a deleted player.</li>
<li>Server request logs held by Google Cloud are removed automatically after about 30 days.</li>
</ul>
<p>Progress saved on your phone isn't affected. To remove it, uninstall GridRova or clear its storage in Android Settings.</p>
</div></article>
""")

page("404", "Page not found | Phoneporium.AU", "This page doesn't exist.", f"""
<article class="doc"><div class="wrap">
<h1>That page isn't here</h1>
<p>The link may be out of date. Try the <a href="/">home page</a>, <a href="/gridrova/support/">GridRova support</a> or the <a href="/gridrova/privacy/">privacy policy</a>.</p>
</div></article>
""")
print("built")
