#!/usr/bin/env python3
"""Builds the Phoneporium.AU static site. Run: python3 build.py (writes the HTML pages in place)."""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "phoneporium.au@gmail.com"
UPDATED = "22 October 2026"
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
<link rel="stylesheet" href="{up}assets/site.css?v=4">
</head>
<body class="{'home' if not path else ''}">
<header class="site-head"><div class="wrap">
  <a class="brand" href="{up or './'}"><span class="brand-mark" aria-hidden="true">P</span>Phoneporium.AU</a>
  <nav class="site-nav" aria-label="Main">
    <a href="{up}gridrova/"{cur('gridrova')}>GridRova</a>
    <a href="{up}gridrova-leaderboard/">Rankings</a>
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
    <a href="{up}gridrova-leaderboard/">Daily rankings</a>
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

page("", "Phoneporium.AU", "Phoneporium.AU makes calm mobile word games in Australia. Home of GridRova.", f"""
<section class="hero scenic"><div class="wrap">
  <div class="hero-copy">
    <h1>Small games for quiet minutes.</h1>
    <p>Phoneporium.AU is an independent studio in Australia making calm puzzle games for Android.</p>
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
      <p><a href="gridrova/">More about GridRova</a> · <a href="gridrova-leaderboard/">Daily rankings</a></p>
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
<section class="shots-band" aria-label="Screens from GridRova"><div class="wrap"><ul class="shots"><li><img src="../assets/shots/gridrova-01.jpg" alt="A welcoming five-by-five word-search board in The Firefly Wilds, with GOAT, FROG and OWL to find." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-02.jpg" alt="An underwater word-search board with CORGI highlighted vertically and MINK horizontally; LARK and SEAL remain." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-03.jpg" alt="The journey shows forest and underwater scenic stops, completed levels and the next available puzzle." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-04.jpg" alt="The scenic album shows The Firefly Wilds and The Sapphire Sanctuary collected, with later postcards still locked." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-05.jpg" alt="The help panel offers a free nudge, a coin-priced trace and one free rescue per puzzle." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-06.jpg" alt="The daily Colors puzzle has VIOLET highlighted backwards across a row and RUSSET vertically in a scenic sky setting." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-07.jpg" alt="An optional timed Animals puzzle shows a countdown and solved-word highlights for CUCKOO and FALCON." width="540" height="960" loading="lazy"></li><li><img src="../assets/shots/gridrova-08.jpg" alt="Settings offer separate sound options, reduced motion, high contrast and tap-first-and-last-letter selection." width="540" height="960" loading="lazy"></li></ul></div></section>
<section class="section"><div class="wrap">
  <h2>What's inside</h2>
  <ul class="facts">
    <li>300 levels</li><li>30 scenic stops</li><li>Postcards to collect</li><li>Daily puzzles from level 10</li>
    <li>Time challenges from level 20</li><li>Plays offline</li><li>No purchases</li>
  </ul>
  <p style="max-width:62ch">Start with simple puzzles, then explore larger grids, longer words and more directions. Themes from animals and food to space and ocean life keep each chapter fresh. Stuck? Use a recharging nudge, or spend in-game coins on hints. Coins are earned by playing and can't be bought.</p>
  <p style="max-width:62ch">GridRova is free, shows ads and is intended for players aged 13 and older. Optional online rankings use an anonymous account with a random player name, never an email address.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="links">
    <a href="../gridrova-leaderboard/"><strong>Daily rankings</strong><span>Today's podium and past results.</span></a>
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
<li>You don't enter a username, password or email to play, and we never ask for your name, phone number, contacts, photos or location.</li>
<li>Your game progress, coins and medals are saved on your phone.</li>
<li>When the game first opens it asks what year you were born. Only an age group is kept, on your phone, to choose suitable ad settings.</li>
<li>Players under 13, and anyone who chooses "Prefer not to say", get Google's most protective ad settings: non-personalised ads rated G.</li>
<li>If you choose to play online rankings, an anonymous player account is created for you. You can delete it, and its online data, from the game at any time.</li>
<li>We don't sell your information. GridRova has no in-app purchases and no separate analytics tool of our own.</li>
</ul>
</div>

<h2>Who we are</h2>
<p>GridRova is made by Phoneporium.AU, an independent game developer in Australia. We are responsible for the information described in this policy. You can contact us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Who GridRova is for</h2>
<p>GridRova is intended for players aged 13 and older. It isn't designed for or directed at children. The game still asks every player's birth year, and younger or unknown-age players get the more protective ad settings described below. A parent or guardian can contact us about a child's online data at any time.</p>

<h2>Information kept on your phone</h2>
<p>GridRova saves the following on your device so you can carry on where you left off: level progress, any puzzle in progress, coins, medals, postcards, settings (sound, music, grid lines) and your age group. This information isn't sent to us. It is removed if you uninstall the game or clear its storage. A backup file you choose to export is yours to keep or delete.</p>

<h2>The age question</h2>
<p>The first time you open GridRova, it asks "What year were you born?" with nothing preselected, and a "Prefer not to say" option. The birth year is used only on your phone, at that moment, to work out an age group (under 13, 13 to 17, or 18 and over). Only the age group and when it was chosen are saved, on your phone. The birth year itself is not stored or sent anywhere.</p>
<p>The age group is used only to set up ads (see below). You can switch to child-safe ads at any time in Settings. The game won't switch from child-safe ads back to normal ads.</p>

<h2>Advertising</h2>
<p>GridRova is free and shows ads from Google AdMob. Ads are not requested until the age question has been answered.</p>
<table>
<thead><tr><th scope="col">Age group</th><th scope="col">What the game asks Google for</th></tr></thead>
<tbody>
<tr><td>Under 13, or "Prefer not to say"</td><td>Ad requests are marked as child-directed and under the age of consent, and ask for non-personalised ads rated G.</td></tr>
<tr><td>13 to 17</td><td>Ad requests are marked as under the age of consent and ask for non-personalised ads rated PG.</td></tr>
<tr><td>18 and over</td><td>Google's consent message is shown where the law requires it. With your consent, ads may be personalised; otherwise they are non-personalised. Ads are rated PG or lower.</td></tr>
</tbody>
</table>
<p>To show and measure ads and prevent fraud, Google AdMob processes information such as your IP address (which can indicate approximate location), device and app information, ad interactions, app performance diagnostics and device identifiers such as the advertising ID. For child-directed and under-age requests, Google limits how this information is used. Google handles this information under its own policy: <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its services</a>. You can reset or delete your advertising ID in your phone's settings.</p>

<h2>Online rankings</h2>
<p>Online rankings are optional. If you choose to play them, Google Firebase Authentication creates an anonymous player account for you. There is no username, password or email, and the account's sign-in key is stored securely on your phone. We use the account's identifier to link your ranked results and any in-game prize records to you.</p>
<p>For each ranked puzzle you play, our server keeps:</p>
<ul>
<li>your anonymous player ID and a randomly generated player name, which you didn't choose and which doesn't identify you</li>
<li>when you started and finished, the word paths you submitted, your time, your result and your rank</li>
<li>receipts for any in-game coin prizes awarded for a daily podium place (coins have no cash value)</li>
</ul>
<p>Your random player name, rank and time are shown publicly on the <a href="../../gridrova-leaderboard/">daily rankings</a>. Our server runs on Google Cloud in Australia (Sydney region). Google keeps request logs, which include IP addresses, for security and troubleshooting.</p>
<p>Version 1.0 has no account linking, email sign-in or cloud save. Because the anonymous account's key lives only on your phone, it can't be moved to or recovered on another phone, and your game progress is never uploaded.</p>

<h2>What we don't do</h2>
<ul>
<li>We don't sell or rent personal information.</li>
<li>We don't include a separate analytics tool of our own. Google AdMob processes ad interactions and diagnostics to serve and measure ads, as described above.</li>
<li>The game doesn't request location, contacts, camera, microphone, photos or file storage permissions.</li>
<li>There are no in-app purchases or chat features.</li>
</ul>

<h2>How long we keep information</h2>
<ul>
<li>On your phone: until you uninstall the game or clear its data.</li>
<li>Online rankings data: until you delete it.</li>
<li>Published final daily results: kept so past podiums stay correct. If you delete your data, your place stays but your name is replaced with "Deleted player".</li>
<li>Deletion marker: a record of your anonymous ID and when it was deleted, kept for 30 days so a prize can't be paid to a deleted account, then removed automatically.</li>
<li>Server request logs (which include IP addresses): deleted automatically after 30 days.</li>
<li>Google Cloud's administrative audit records for our server (for example, that an account was deleted): kept by Google for 400 days. This period is set by Google and can't be shortened.</li>
</ul>

<h2>Deleting your data</h2>
<p>In GridRova, open Settings and choose "Delete my online data". This removes your anonymous player account and its ranking, attempt and prize records straight away. Published final standings keep your place with the name "Deleted player", and a short-lived deletion marker is kept as described above. Game progress, coins and medals on your phone aren't affected. Deleting online data doesn't erase records Google AdMob handles under its own policy, or backup files you exported. If you no longer have the game, see <a href="../delete-data/">delete your data</a>.</p>

<h2>Your rights</h2>
<p>You can ask us what information we hold about you, or ask us to correct or delete it, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>. We'll reply within 7 days. Because we don't collect names or email addresses through the game, we'll ask for the player name shown in the game so we can find your data.</p>
<p>We follow the Australian Privacy Principles. If you are not happy with our response, you can contact the <a href="https://www.oaic.gov.au/privacy/privacy-complaints">Office of the Australian Information Commissioner</a>. If you live elsewhere, you may also have rights under your local law, such as the GDPR in Europe and the UK.</p>

<h2>Information sent overseas</h2>
<p>Ad requests are handled by Google, which may process information in other countries, including the United States. Our rankings server is hosted in Australia.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we'll update this page and the date at the top. If the change is significant, such as adding email sign-in or cloud save, we'll also say so in the game before it takes effect.</p>
</div></article>
""", nav="privacy")

page("gridrova/support", "GridRova support", "Get help with GridRova by Phoneporium.AU.", f"""
<article class="doc"><div class="wrap">
<h1>GridRova support</h1>
<p class="meta">Email <a href="mailto:{EMAIL}?subject=GridRova%20support">{EMAIL}</a>. We reply within 7 days.</p>
<p>When you write, it helps to include your phone model, the Android version and the level number, plus a screenshot if something looks wrong.</p>

<h2>Common questions</h2>
<h3>Will I lose my progress if I change phones?</h3>
<p>Progress is saved on your phone. Version 1.0 doesn't include cloud save or account recovery, so progress and your online rankings account don't move to a new phone, and uninstalling the game removes them.</p>
<h3>Does GridRova work offline?</h3>
<p>Yes. The journey and daily puzzles work without internet. Ads and online rankings need a connection.</p>
<h3>Can I buy coins?</h3>
<p>No. GridRova has no purchases. You earn coins by playing, and your first Rescue in each puzzle is free.</p>
<h3>Why did the game ask for my birth year?</h3>
<p>So it can choose suitable ads. Only an age group is kept, on your phone. If you'd rather not say, choose "Prefer not to say" and you'll get child-safe ads. See the <a href="../privacy/">privacy policy</a> for details.</p>
<h3>How do I switch to child-safe ads?</h3>
<p>Open Settings and choose "Use child-safe ads".</p>
<h3>Where does my ranking name come from?</h3>
<p>It's generated at random when you first play online rankings, so nobody's real name appears on the rankings.</p>
<h3>How do I delete my online data?</h3>
<p>Open Settings and choose "Delete my online data". More options are on the <a href="../delete-data/">delete your data</a> page.</p>
</div></article>
""", nav="support")

page("gridrova/delete-data", "Delete your GridRova data", "How to delete the online data GridRova by Phoneporium.AU holds about you.", f"""
<article class="doc"><div class="wrap">
<h1>Delete your GridRova data</h1>
<p class="meta">GridRova by Phoneporium.AU. Last updated {UPDATED}.</p>
<p>You don't enter a username, password or email to play GridRova. If you played online rankings, the game created an anonymous player account for you, and our server holds its ID, a random player name, your ranked results and any prize records. You can delete the account and that data.</p>

<h2>Delete it in the game</h2>
<ol class="steps">
<li>Open GridRova and go to Settings.</li>
<li>Choose "Delete my online data" and confirm.</li>
<li>Your anonymous account, player name, ranked attempts and results, and coin prize records are removed from our server straight away, and the account can no longer sign in.</li>
</ol>

<h2>Ask us by email</h2>
<p>If you no longer have the game, email <a href="mailto:{EMAIL}?subject=GridRova%20data%20deletion">{EMAIL}</a> with the subject "GridRova data deletion" and your player name exactly as it appeared in the game. We'll reply within 7 days.</p>
<p>There's no password or email linked to an anonymous account, so we can't check who owns it. To protect current players, we delete by email only when exactly one account has that player name and it hasn't been used for at least 30 days. If it's been used more recently, please delete it from Settings on the phone that has the game. We never ask for passwords or payment details.</p>

<h2>What is deleted, and what is kept</h2>
<ul>
<li>Deleted: your anonymous account and its sign-in, player name, ranked attempts and results, and coin prize records.</li>
<li>Kept: published final daily results keep your place so other players' ranks stay correct, with your name replaced by "Deleted player". A record of the deleted account ID and deletion time is kept for 30 days so a prize can't be paid to a deleted account, then removed automatically.</li>
<li>Server request logs held by Google Cloud are deleted automatically after 30 days. Google Cloud's administrative audit records, such as the fact that an account was deleted, are kept by Google for 400 days.</li>
<li>Records Google AdMob handles under its own policy aren't covered by this deletion. You can reset or delete your advertising ID in your phone's settings.</li>
</ul>
<p>Progress, coins and medals saved on your phone aren't affected. To remove them, uninstall GridRova or clear its storage in Android Settings.</p>
</div></article>
""")

page("404", "Page not found | Phoneporium.AU", "This page doesn't exist.", f"""
<article class="doc"><div class="wrap">
<h1>That page isn't here</h1>
<p>The link may be out of date. Try the <a href="/">home page</a>, <a href="/gridrova/support/">GridRova support</a> or the <a href="/gridrova/privacy/">privacy policy</a>.</p>
</div></article>
""")
print("built")
