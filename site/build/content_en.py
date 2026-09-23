# -*- coding: utf-8 -*-
"""Anime Breaker (Roblox) — English content (full 22-URL cluster, PRD §5).
事实规范(PRD §8/§17):每页区分 VERIFIED(官方 Roblox listing)/ REPORTED(二手来源,带日期)/
OBSERVED(当前客户端观察)/ UNVERIFIED(未核实)。未核实数值一律不写:
rank 成本、barrier HP、Avatar 倍率与掉率、武器数值、boss HP/位置/掉率、accessory 掉率与数值、
raid 门票/波次奖励、amulet 名称与数值、card pull rates、trial 奖励。
最后核实日期:2026-09-23。任何 Code/数值都以游戏内为准(PRD §7.4/§9)。
"""
import config

G = config.SITE["name"]
DEV = config.SITE["developer"]
RPX = config.SITE["cta_url"]
LC = "2026-09-23"   # last checked

PAGES = {}

# ============================================================
# 1. Homepage  (/)
# ============================================================
PAGES["index.html"] = {
    "path": "index.html", "home": True,
    "title": "Anime Breaker Roblox: Codes, Guides & Wiki",
    "meta": "Unofficial Anime Breaker Roblox wiki and guide: the official loop, working codes status, beginner and progression guides. Facts are labelled, never invented.",
    "pill": "Fan Wiki · Verified-First",
    "tagline": "The verified-first " + G + " reference for Roblox players",
    "intro": ("Unofficial fan resource — not affiliated with " + DEV + ". The official Roblox listing currently "
              "shows the title as <strong>" + G + " [🌳CLASS TREE]</strong>. Every mechanic here is labelled "
              "VERIFIED / REPORTED / OBSERVED, and numbers we cannot confirm are left out instead of guessed."),
    "cta2_label": "Start with the Beginner Guide",
    "cta2_url": "/guides/beginner-guide/",
    "stats": [("LIVE", "Playable on Roblox"), ("8", "Systems in the official loop"),
              ("4", "Supported device types"), ("3", "Guide languages")],
    "shot_alt": [G + " key art – character lineup", G + " gameplay – combat burst",
                 G + " world – night scenery", G + " gameplay – reward and upgrade screen"],
    "gallery_credit": ("Screenshots are from the official Roblox experience page and remain the property of "
                       + DEV + "; shown for reference only."),
    "sections": [
        ("h2", "What is " + G + " on Roblox?"),
        ("p", G + " is a Roblox anime-style progression experience by " + DEV + ". The official listing describes "
              "an <strong>Energy-driven loop</strong>: you gain Energy, open <strong>Cards</strong> to get "
              "<strong>Companions</strong>, fight enemies for resources, unlock <strong>Avatars</strong>, "
              "<strong>Weapons</strong> and rare items, then <strong>Rank Up</strong> and <strong>Upgrade</strong> "
              "towards <strong>Raids</strong>. The same page lists computers, phones, tablets and consoles as "
              "supported device types."),
        ("p", "This site is organised around the decision a player actually faces next: spend Energy or save it, "
              "rank up or upgrade, farm a <a href=\"/guides/secret-boss-locations/\">secret boss</a> or push "
              "<a href=\"/guides/progression/\">progression</a>. Start with the "
              "<a href=\"/guides/beginner-guide/\">beginner guide</a>, or jump to the "
              "<a href=\"/codes/\">codes</a> page if you only need live codes."),
        ("h2", "The core loop (official description)"),
        ("p", "The official listing describes the loop as a chain. This is the verified shape of it:"),
        ("ol", [
            "<strong>Gain Energy</strong> — Energy is the entry point of the loop; everything starts here. More: <a href=\"/guides/energy/\">Energy guide</a>.",
            "<strong>Open Cards for Companions</strong> — Cards are how you acquire Companions. More: <a href=\"/wiki/cards/\">Cards</a> · <a href=\"/wiki/companions/\">Companions</a>.",
            "<strong>Fight enemies for resources</strong> — combat and farming feed the economy. More: <a href=\"/wiki/resources/\">Resources</a>.",
            "<strong>Unlock Avatars, Weapons and rare items</strong> — the unlock layer of the loop. More: <a href=\"/wiki/avatars/\">Avatars</a> · <a href=\"/wiki/weapons/\">Weapons</a> · <a href=\"/wiki/accessories/\">Accessories</a>.",
            "<strong>Rank Up / Upgrade</strong> — the power step. More: <a href=\"/guides/rank-up/\">Rank Up</a> · <a href=\"/guides/upgrades/\">Upgrades</a>.",
            "<strong>Raids</strong> — the end-of-loop challenge tier. More: <a href=\"/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "Current status (" + LC + ")"),
        ("p", "The official title string currently contains <strong>CLASS TREE</strong>, which points at an active "
              "class/progression update line — see the <a href=\"/updates/\">updates hub</a> for what that means for "
              "your build. Codes are a live system, and the ones we track are timestamped on the "
              "<a href=\"/codes/\">codes page</a>."),
        ("h2", G + " at a glance"),
        ("table", {"head": ["Field", "Details"],
                   "rows": [
                       ["Official title", G + " [🌳CLASS TREE] (current official Roblox title)"],
                       ["Developer / publisher", DEV],
                       ["Platform", "Roblox — computers, phones, tablets and consoles"],
                       ["Genre", "Anime-style progression / collection experience"],
                       ["Core loop", "Energy → Cards → Companions → fight for resources → Avatars / Weapons → Rank Up / Upgrade → Raids"],
                       ["Live systems", "Codes (active), update line currently tagged CLASS TREE"],
                       ["Verification", "Every claim is labelled VERIFIED, REPORTED, OBSERVED or UNVERIFIED"],
                   ]}),
        ("note", "Play on the official experience page: <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX +
                 "</a>. Codes, costs, drop rates and balance values change between updates — this site re-checks "
                 "them and prints the date it checked."),
        ("h2", "Player journey: what to read next"),
        ("p", "The site is built as a route through the loop, not as a wall of pages. Follow it in order, or jump "
              "to the step you are stuck on:"),
        ("ul", [
            "<strong>Step 1 — Learn the loop:</strong> <a href=\"/guides/beginner-guide/\">Beginner Guide</a>",
            "<strong>Step 2 — Fix your Energy:</strong> <a href=\"/guides/energy/\">Energy</a> → <a href=\"/wiki/cards/\">Cards</a> → <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>Step 3 — Choose power:</strong> <a href=\"/guides/upgrades/\">Upgrades</a> → <a href=\"/guides/rank-up/\">Rank Up</a> → <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Step 4 — Unlock:</strong> <a href=\"/wiki/avatars/\">Avatars</a> → <a href=\"/wiki/weapons/\">Weapons</a> → <a href=\"/wiki/worlds/\">Worlds</a>",
            "<strong>Step 5 — Farm and challenge:</strong> <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a> → <a href=\"/wiki/accessories/\">Accessories</a> → <a href=\"/guides/raids/\">Raids</a> → <a href=\"/guides/trial/\">Trial</a> → <a href=\"/wiki/amulets/\">Amulets</a>",
            "<strong>No Robux?</strong> <a href=\"/guides/f2p/\">F2P guide</a> · <a href=\"/codes/\">Codes</a>",
        ]),
        ("h2", "Major systems in the wiki"),
        ("cards", [
            ("Cards", "How Cards are used and how they lead to Companions.", "/wiki/cards/"),
            ("Companions", "Acquisition, use and how they differ from Avatars.", "/wiki/companions/"),
            ("Avatars", "Unlocking, growing and farming with Avatars.", "/wiki/avatars/"),
            ("Weapons", "Acquisition and the role weapons play.", "/wiki/weapons/"),
            ("Accessories & Amulets", "Boss drops, upgrades and bottleneck gear decisions.", "/wiki/accessories/"),
            ("Resources & Worlds", "Currencies, sources and world navigation.", "/wiki/resources/"),
        ]),
        ("h2", "Why this wiki is verified-first"),
        ("p", "Roblox wikis copy each other, and version-sensitive numbers (rank costs, boss HP, drop rates, "
              "multipliers) end up frozen at launch values that no longer match the live client. This site uses "
              "four labels instead:"),
        ("ul", [
            "<strong>VERIFIED</strong> — stated by the official Roblox listing or reproducible in the current client.",
            "<strong>REPORTED</strong> — published by a dated secondary source (for example the live codes snapshot of " + LC + ").",
            "<strong>OBSERVED</strong> — seen in current-client play, still being re-tested.",
            "<strong>UNVERIFIED</strong> — claimed somewhere, confirmed nowhere. Listed so you can test it, never presented as fact.",
        ]),
        ("note", "High-risk values — rank costs and multipliers, boss HP and drop rates, Avatar multipliers, weapon "
                 "stats, accessory stats, raid ticket costs, Amulet values, card pull rates and Trial rewards — are "
                 "deliberately absent unless a current source can back them."),
        ("h2", "Jump into the wiki"),
        ("cards", [
            ("Beginner Guide", "The core loop and your first session, step by step.", "/guides/beginner-guide/"),
            ("Codes", "Working and expired codes with the date we checked.", "/codes/"),
            ("Wiki Hub", "All documented systems in one place.", "/wiki/"),
            ("Guides Hub", "Task and optimisation guides.", "/guides/"),
            ("Updates", "What changed, and what is only detected.", "/updates/"),
            ("F2P Guide", "Progress decisions without Robux.", "/guides/f2p/"),
        ]),
    ],
    "faq": [
        ("What is " + G + " on Roblox?", "An anime-style Roblox progression experience by " + DEV + ". The official listing describes an Energy-driven loop: gain Energy, open Cards for Companions, fight enemies for resources, unlock Avatars, Weapons and rare items, then Rank Up / Upgrade and take on Raids."),
        ("Is " + G + " free to play?", "It runs inside Roblox, which is free to install. Any optional Robux purchases exist inside the experience and are not required to follow the core loop described officially."),
        ("What does CLASS TREE mean in the " + G + " title?", "The official title string currently reads " + G + " [🌳CLASS TREE], which signals an active class/progression update line. This site does not invent patch details beyond what the official title and dated sources show — see the updates hub."),
        ("Where do I redeem " + G + " codes?", "Codes are redeemed inside the experience. The current list we track, with its verification date, is on the codes page."),
        ("Is there an " + G + " tier list or best units page?", "Not yet, on purpose. Tier lists freeze meta values that change every update; until a current source can back them, this site publishes decision frameworks instead — see the upgrades and progression guides."),
        ("Where should a new player start?", "The beginner guide, then Energy and Cards. Those three cover the part of the loop a first session actually touches."),
        ("Why are some numbers missing?", "Because unverified numbers are worse than no numbers. Rank costs, drop rates, multipliers, boss HP and similar values are only printed when a current source backs them."),
    ],
    "related": [("Beginner Guide", "/guides/beginner-guide/", "Start your first session"),
                ("Codes", "/codes/", "Live status with verification date"),
                ("Progression Guide", "/guides/progression/", "Where the loop gets hard")],
}

# ============================================================
# 2. Wiki hub  (/wiki/)
# ============================================================
PAGES["wiki/index.html"] = {
    "path": "wiki/index.html",
    "title": "Anime Breaker Wiki – Cards, Companions & Avatars",
    "meta": "The Anime Breaker wiki hub: Cards, Companions, Avatars, Weapons, Accessories, Amulets, Resources and Worlds, explained with verification labels.",
    "pill": "Wiki", "h1": G + " Wiki",
    "lead": ("The reference layer of the site: every documented system, what it does in the loop, and how "
             "confident we are about it."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/")],
    "sections": [
        ("p", "This hub covers the systems named in the official " + G + " description plus the gear and world "
              "layers players ask about most. Each page states what is VERIFIED, what is REPORTED and what is "
              "merely OBSERVED in the current client — and every page carries the date it was last checked."),
        ("h2", "Systems in the official core loop"),
        ("table", {"head": ["System", "Role in the loop", "Confidence"],
                   "rows": [
                       ["Energy", "Entry point: gained, spent and saved to open Cards.", "VERIFIED (official listing)"],
                       ["Cards", "The acquisition layer: open Cards for Companions.", "VERIFIED (official listing)"],
                       ["Companions", "Fight alongside you and feed the resource economy.", "VERIFIED (official listing)"],
                       ["Avatars", "Unlock layer: change what you play as.", "VERIFIED (official listing)"],
                       ["Weapons", "Unlock layer: gear that changes combat output.", "VERIFIED (official listing)"],
                       ["Rank Up", "Power step: moves your account up its rank ladder.", "VERIFIED (official listing)"],
                       ["Upgrades", "Power step: spend resources to strengthen what you own.", "VERIFIED (official listing)"],
                       ["Raids", "Challenge tier at the end of the loop.", "VERIFIED (official listing)"],
                   ]}),
        ("h2", "Gear, economy and world layers"),
        ("ul", [
            "<strong><a href=\"/wiki/accessories/\">Accessories</a></strong> — boss-sourced equipment and the decisions around it.",
            "<strong><a href=\"/wiki/amulets/\">Amulets</a></strong> — additional gear slot reported at bottleneck stages of progression.",
            "<strong><a href=\"/wiki/resources/\">Resources</a></strong> — the currencies and materials the loop consumes.",
            "<strong><a href=\"/wiki/worlds/\">Worlds</a></strong> — how the world order is used for navigation rather than for thin subpages.",
        ]),
        ("h2", "How the wiki handles unknown values"),
        ("p", "Roblox experiences rebalance in place, so a value copied from a wiki can be wrong the same week. "
              "This wiki therefore publishes mechanics and decision logic, and only prints numbers that a current "
              "source backs — the same rule the <a href=\"/wiki/avatars/\">Avatars</a> and "
              "<a href=\"/wiki/weapons/\">Weapons</a> pages follow for multipliers and stat tables."),
        ("note", "Where a page says the data is partial, that is deliberate: the system is real and documented, "
                 "while the exact numbers are held until verified. Nothing is filled in with a plausible guess."),
    ],
    "faq": [
        ("What is the " + G + " wiki?", "A player-run reference for the systems and gear in " + G + " on Roblox, with every claim labelled by how well it is sourced. Not affiliated with " + DEV + "."),
        ("Why are some " + G + " stat tables missing?", "Because the live client can change multipliers, costs and drop rates without notice. Tables appear once a current source backs the numbers."),
        ("Which system should I read first?", "Energy, then Cards, then Companions — that is the order the official loop runs in."),
    ],
    "related": [("Guides Hub", "/guides/", "Task and optimisation guides"),
                ("Beginner Guide", "/guides/beginner-guide/", "The loop in order"),
                ("Updates", "/updates/", "What changed, and when")],
}

# ============================================================
# 3. Guides hub  (/guides/)
# ============================================================
PAGES["guides/index.html"] = {
    "path": "guides/index.html",
    "title": "Anime Breaker Guides: Beginner, Energy & Raids",
    "meta": ("All " + G + " guides: beginner guide, progression, Energy, Rank Up, Upgrades, Secret Boss "
             "Locations, Raids, Trial and the F2P route."),
    "pill": "Guides", "h1": G + " Guides",
    "lead": ("Every guide answers one decision, in the order players hit it, from the official loop outward."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/")],
    "sections": [
        ("p", "Guides are written as decisions rather than descriptions: spend or save, rank or upgrade, farm "
              "here or push further. Each one states its prerequisites, the step-by-step answer, the pitfalls and "
              "how sensitive it is to the next update."),
        ("h2", "Start here"),
        ("cards", [
            ("Beginner Guide", "Core loop, first session and the mistakes to avoid.", "/guides/beginner-guide/"),
            ("Energy", "How Energy is gained, spent and stretched.", "/guides/energy/"),
            ("Progression", "The mid and late-game bottleneck map.", "/guides/progression/"),
        ]),
        ("h2", "Optimisation guides"),
        ("cards", [
            ("Rank Up", "When ranking is worth it — and what the costs really depend on.", "/guides/rank-up/"),
            ("Upgrades", "A priority framework instead of a frozen tier list.", "/guides/upgrades/"),
            ("Raids", "Access, waves, rewards and how to spend from them.", "/guides/raids/"),
            ("Trial", "The hallway-style challenge loop and its upgrade path.", "/guides/trial/"),
        ]),
        ("h2", "Task and F2P guides"),
        ("cards", [
            ("Secret Boss Locations", "How bosses are found, farmed and kept track of.", "/guides/secret-boss-locations/"),
            ("F2P Guide", "Progress decisions when you spend no Robux.", "/guides/f2p/"),
            ("Codes", "Live code status with verification dates.", "/codes/"),
        ]),
        ("note", "Guides are re-checked against the current client: values that change with balance patches are "
                 "labelled as such rather than printed as constants."),
    ],
    "faq": [
        ("Which " + G + " guide should I read first?", "The beginner guide. Then Energy and Cards, because the first session is spent almost entirely inside that part of the loop."),
        ("Do the guides use real numbers?", "Only numbers a current source backs. Costs, drop rates and multipliers that shift between updates are described as decision logic instead of frozen constants."),
        ("Is there a best-upgrades or best-weapons page?", "No. Those pages go stale within a patch. The upgrades guide instead gives a prioritisation framework you can apply to whatever your account currently has."),
    ],
    "related": [("Wiki Hub", "/wiki/", "The system reference layer"),
                ("Updates", "/updates/", "Update sensitivity"),
                ("Codes", "/codes/", "Free resources while they last")],
}

# ============================================================
# 4. Codes  (/codes/)
# ============================================================
PAGES["codes/index.html"] = {
    "path": "codes/index.html",
    "title": G + " Codes (September 2026) – Working & Expired",
    "meta": "Anime Breaker codes status as of September 2026: reported active milestone and update codes, how to redeem, and how expired codes are handled.",
    "pill": "Live", "h1": G + " Codes",
    "lead": ("A dated code page, not an evergreen one. Every code here is either reported active by a dated "
             "source or treated as expired — and every entry tells you to test it in game."),
    "breadcrumb": [("Home", "/"), ("Codes", "/codes/")],
    "sections": [
        ("p", "<strong>Last verified: " + LC + "</strong>. Codes in " + G + " are an <strong>active live system</strong> "
              "(REPORTED — secondary codes coverage dated 2026-09-22). That coverage counted roughly "
              "<strong>14 active codes</strong> at that date, including milestone and update codes. Milestone codes "
              "like these are usually tied to community goals and get retired, so treat the list below as dated, "
              "not permanent."),
        ("h2", "Reported active codes (" + LC + ")"),
        ("table", {"head": ["Code", "Status", "What the source says"],
                   "rows": [
                       ["10KCCU", "REPORTED active", "Milestone code (community count milestone) — test in game; this site does not print rewards it cannot verify."],
                       ["2MVISITS", "REPORTED active", "Milestone code (visits milestone)."],
                       ["20KFAVORITES", "REPORTED active", "Milestone code (favourites milestone)."],
                       ["NEWPORTAL", "REPORTED active", "Update-style code, reported alongside a portal update line."],
                       ["NEWSHADOW", "REPORTED active", "Update-style code, reported alongside a shadow update line."],
                   ]}),
        ("note", "Reward values are deliberately left blank: the secondary snapshot lists code strings, not "
                 "itemised rewards, and copied reward tables are exactly how code pages go wrong. Enter the code "
                 "in game and read the reward from the confirmation prompt."),
        ("h2", "Expired codes"),
        ("p", "Roblox code systems expire silently — a code that worked last week can stop working without an "
              "announcement. This page does not publish an 'expired' list it cannot verify, for the same reason it "
              "does not publish invented rewards: an unverified expiry date is misinformation. If a listed code "
              "fails, treat it as expired for your build and check the <a href=\"/updates/\">updates hub</a> for the "
              "current line."),
        ("h2", "How to redeem codes in " + G),
        ("ol", [
            "<strong>Join the official experience</strong> — open " + G + " through its official Roblox page.",
            "<strong>Find the in-game code entry</strong> — Roblox experiences place code entry in a menu, settings or a dedicated codes panel; the exact slot moves between builds, so use the current UI rather than a copied screenshot.",
            "<strong>Enter the code exactly</strong> — Roblox codes are case- and character-sensitive; copy-paste where the field allows it.",
            "<strong>Confirm and read the reward prompt</strong> — if nothing is granted, the code is expired or already redeemed on that account.",
        ]),
        ("h2", "Where new codes appear"),
        ("ul", [
            "<strong>Milestone codes</strong> — tied to community numbers (visits, favourites, concurrent players), which is why the codes above look like counters.",
            "<strong>Update codes</strong> — shipped alongside content lines, which is how NEWPORTAL and NEWSHADOW read.",
            "<strong>Re-check cadence</strong> — this page is re-dated whenever the code set is re-verified, and the maintenance rules below show what a code needs before it is listed.",
        ]),
        ("h2", "Why a code might not work"),
        ("ul", [
            "<strong>It expired</strong> — the most common cause; milestone codes are the first to go.",
            "<strong>Typo or case mismatch</strong> — re-enter character by character.",
            "<strong>Already redeemed</strong> — most Roblox code systems allow one redemption per account.",
            "<strong>Wrong game</strong> — similarly named Roblox anime titles run their own code sets; codes are not transferable between experiences.",
        ]),
        ("h2", "How this page is maintained"),
        ("ul", [
            "A code is listed only with a dated source and the status word REPORTED.",
            "Rewards are only printed once visible in the game's own confirmation prompt.",
            "The page is re-verified as a set rather than edited code-by-code, so the date at the top always matches the whole table.",
        ]),
        ("note", "If the table above and a newer source disagree, trust the newer source in game. This page exists "
                 "to be dated and honest, not to be the longest list on the internet."),
    ],
    "faq": [
        ("Are there working " + G + " codes right now?", "As of " + LC + " a dated secondary source reported about 14 active codes, including 10KCCU, 2MVISITS, 20KFAVORITES, NEWPORTAL and NEWSHADOW. Test each one in game — status changes faster than any list."),
        ("What do " + G + " codes give you?", "The dated snapshot lists code strings rather than itemised rewards, so this site does not print reward values. The in-game confirmation prompt is the authoritative answer."),
        ("How do I redeem " + G + " codes?", "Join the official experience, open the in-game code entry (usually in a menu or settings panel, which can move between builds), type the code exactly and confirm."),
        ("Why is a code that worked yesterday not working?", "Milestone codes are retired as community goals pass. An expired code and a mistyped code look the same in the UI — retype it once, then assume expired."),
        ("Do codes from other anime Roblox games work here?", "No. Code sets are per-experience; similarly named titles run their own lists."),
        ("How often is this page updated?", "Whenever the code set is re-verified. The date at the top of the page always describes the table below it."),
    ],
    "related": [("Updates", "/updates/", "Which update line the codes belong to"),
                ("F2P Guide", "/guides/f2p/", "Turn free rewards into progress"),
                ("Beginner Guide", "/guides/beginner-guide/", "What to do with your first rewards")],
}

# ============================================================
# 5. Updates  (/updates/)
# ============================================================
PAGES["updates/index.html"] = {
    "path": "updates/index.html",
    "title": "Anime Breaker Updates – CLASS TREE Status & Changes",
    "meta": "Anime Breaker updates hub: the current CLASS TREE title status, what is verified in the official listing, and what is only reported.",
    "pill": "Live", "h1": G + " Updates",
    "lead": ("A dated hub for " + G + " changes — built to stop 'a public record changed' turning into "
             "'this feature is live'."),
    "breadcrumb": [("Home", "/"), ("Updates", "/updates/")],
    "sections": [
        ("p", "Checked <strong>" + LC + "</strong>. The official listing currently renders the title as "
              "<strong>" + G + " [🌳CLASS TREE]</strong>. That tag is the strongest update signal available without "
              "inventing patch notes: it indicates an active class/progression update line in the game's own "
              "branding."),
        ("h2", "What is verified right now"),
        ("table", {"head": ["Item", "Status (" + LC + ")", "Note"],
                   "rows": [
                       ["Official title", "VERIFIED", G + " [🌳CLASS TREE] as shown on the official Roblox listing."],
                       ["Core loop", "VERIFIED", "Energy → Cards → Companions → resources → Avatars / Weapons → Rank Up / Upgrade → Raids."],
                       ["Supported devices", "VERIFIED", "Computers, phones, tablets and consoles."],
                       ["Code system", "REPORTED active", "Secondary coverage dated 2026-09-22 counted about 14 active codes. See the codes page."],
                   ]}),
        ("h2", "What this page will not do"),
        ("ul", [
            "<strong>No invented patch notes</strong> — the CLASS TREE tag does not get expanded into balance numbers or feature lists by guesswork.",
            "<strong>No frozen launch values</strong> — when a system changes, the value is re-labelled instead of quietly kept.",
            "<strong>No 'detected therefore live'</strong> — a public record or a competitor page changing is a lead, not a confirmation.",
        ]),
        ("h2", "How to read an update with this site"),
        ("ol", [
            "<strong>Check the date</strong> — every page prints the day it was last verified; anything after that date may be stale.",
            "<strong>Check the label</strong> — VERIFIED, REPORTED, OBSERVED and UNVERIFIED mean different things on purpose.",
            "<strong>Re-test in game</strong> — the live client outranks any page, including this one.",
        ]),
        ("note", "Update-driven pages to re-read after a patch: <a href=\"/codes/\">Codes</a>, "
                 "<a href=\"/guides/rank-up/\">Rank Up</a> (costs), <a href=\"/guides/upgrades/\">Upgrades</a> "
                 "(priorities), <a href=\"/guides/raids/\">Raids</a> (tickets and rewards) and "
                 "<a href=\"/wiki/weapons/\">Weapons</a> (stats)."),
    ],
    "faq": [
        ("What is the latest " + G + " update?", "As of " + LC + " the official listing carries the CLASS TREE title tag, and the code system is reported active with milestone and update codes. Both are dated on this site rather than described as permanent."),
        ("Does CLASS TREE mean a new class system?", "The tag is part of the game's official title, so an active class/progression line is the reasonable reading. This site does not publish feature lists or balance numbers that no current source backs."),
        ("How often are " + G + " updates published?", "No public schedule is part of the verified record, so this site does not promise one. Pages carry last-checked dates instead."),
        ("Why is this updates page short?", "Because length is not evidence. Only changes with a dated source are listed; the rest stay unlisted until they can be tested."),
    ],
    "related": [("Codes", "/codes/", "The most update-sensitive page on the site"),
                ("Progression Guide", "/guides/progression/", "Re-plan after a balance patch"),
                ("Rank Up", "/guides/rank-up/", "Costs change with updates")],
}

# ============================================================
# 6. Beginner Guide  (/guides/beginner-guide/)
# ============================================================
PAGES["guides/beginner-guide/index.html"] = {
    "path": "guides/beginner-guide/index.html",
    "title": "Anime Breaker Beginner Guide – How to Play & Energy",
    "meta": "How to play Anime Breaker on Roblox: the official Energy-driven loop explained, your first session, and which mistakes cost the most early progress.",
    "pill": "Guides", "h1": G + " Beginner Guide",
    "lead": ("Your first session, mapped onto the official loop: Energy in, Cards opened, Companions out, "
             "resources spent — in the right order."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Beginner Guide", "/guides/beginner-guide/")],
    "sections": [
        ("p", "The official " + G + " description gives you the loop directly: <strong>gain Energy → open Cards for "
              "Companions → fight enemies for resources → unlock Avatars, Weapons and rare items → Rank Up / "
              "Upgrade → Raids</strong>. A beginner guide is mostly about not breaking the order of that loop."),
        ("h2", "Prerequisites"),
        ("ul", [
            "<strong>Roblox installed</strong> — " + G + " runs on computers, phones, tablets and consoles.",
            "<strong>The official experience page</strong> — <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX + "</a>.",
            "<strong>A reason to read first</strong> — early resources are the scarcest thing you own; the loop punishes random spending.",
        ]),
        ("h2", "Your first session, step by step"),
        ("ol", [
            "<strong>Learn where Energy comes from</strong> — Energy is the loop's entry point. Find how your account gains it before you spend anything. <a href=\"/guides/energy/\">Energy guide</a>",
            "<strong>Open Cards deliberately</strong> — Cards are the official route to Companions. Open them as a set rather than one at a time, so you can see what your roster is short of. <a href=\"/wiki/cards/\">Cards</a>",
            "<strong>Field Companions and fight</strong> — Companions are what you take into combat in the official description; the resources they help you earn are the currency of everything later. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>Bank resources before spending</strong> — the loop's next steps (Avatars, Weapons, Rank Up, Upgrades) all draw on the same pool. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Make one progression decision, not five</strong> — pick either an upgrade or a rank push and commit; splitting early resources across everything is the standard beginner mistake. <a href=\"/guides/upgrades/\">Upgrades</a> · <a href=\"/guides/rank-up/\">Rank Up</a>",
            "<strong>Only then look at Avatars and Weapons</strong> — they are the unlock layer of the official loop and they pay off once your resource flow is stable. <a href=\"/wiki/avatars/\">Avatars</a> · <a href=\"/wiki/weapons/\">Weapons</a>",
        ]),
        ("h2", "Beginner mistakes that cost the most"),
        ("ul", [
            "<strong>Spending Energy the moment you have it</strong> — without knowing your income rate, you cannot tell a good session from a bad one.",
            "<strong>Chasing rarity before flow</strong> — a rare unlock on an account with no resource income stalls immediately.",
            "<strong>Trusting a copied number</strong> — rank costs, multipliers and drop rates change between updates; a screenshot from a month ago is a rumour.",
            "<strong>Ignoring codes</strong> — the code system is live, and free rewards early are worth more than the same rewards later. <a href=\"/codes/\">Codes</a>",
        ]),
        ("note", "Update sensitivity: the loop itself is verified from the official listing and is stable; the numbers "
                 "around it are not. If a guide elsewhere quotes exact Energy amounts, rank costs or pull rates "
                 "without a date, treat it as unverified."),
    ],
    "faq": [
        ("How do you play " + G + "?", "Follow the official loop: gain Energy, open Cards for Companions, fight enemies for resources, unlock Avatars, Weapons and rare items, then Rank Up / Upgrade and take on Raids. Supported devices are computers, phones, tablets and consoles."),
        ("What should I do first in " + G + "?", "Learn how your account gains Energy, then spend it on Cards as a set so you can see what your Companion roster lacks. Field them, farm resources, and make one progression decision instead of spreading resources across everything."),
        ("Is " + G + " pay to win?", "The verified record describes an in-experience progression loop rather than a paid one. Optional Robux purchases exist in many Roblox experiences, but this site does not publish purchase claims it cannot verify — the F2P guide covers playing without them."),
        ("How long does it take to get your first Companion?", "We do not print timings: they depend on your Energy income and the Card pool, both of which change between updates. The Cards page explains the mechanic instead."),
        ("What is the biggest beginner mistake?", "Splitting early resources across Avatars, Weapons, Upgrades and Rank Up at once. Bank first, then commit to one path — the upgrades guide shows how to choose."),
    ],
    "related": [("Energy", "/guides/energy/", "The loop's entry point"),
                ("Cards", "/wiki/cards/", "How Companions are acquired"),
                ("Upgrades", "/guides/upgrades/", "Your first real decision")],
}

# ============================================================
# 7. Progression  (/guides/progression/)
# ============================================================
PAGES["guides/progression/index.html"] = {
    "path": "guides/progression/index.html",
    "title": "Anime Breaker Progression Guide – Early to Late Game",
    "meta": ("A " + G + " progression guide built as a bottleneck map: what limits you early, mid and late, and "
             "which decision actually moves the wall."),
    "pill": "Guides", "h1": G + " Progression Guide",
    "lead": ("Not a level list — a map of what is actually stopping you at each stage, and which lever moves it."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Progression", "/guides/progression/")],
    "sections": [
        ("p", "Progression in " + G + " runs on the official loop: Energy feeds Cards, Cards produce Companions, "
              "Companions and combat produce resources, resources convert into Avatars, Weapons, Rank Up and "
              "Upgrades, and that output is tested in Raids. When progress stalls, the stall is always at one "
              "specific link — and the fix is rarely 'play more'."),
        ("h2", "Stage 1 — early: the flow bottleneck"),
        ("ul", [
            "<strong>Symptom:</strong> you are always out of Energy or out of the resource you need next.",
            "<strong>Real problem:</strong> income rate, not item rarity. A rare unlock on a slow account is still slow.",
            "<strong>Lever:</strong> check how Energy is gained and spent first. <a href=\"/guides/energy/\">Energy</a> → <a href=\"/wiki/cards/\">Cards</a>",
        ]),
        ("h2", "Stage 2 — mid: the commitment bottleneck"),
        ("ul", [
            "<strong>Symptom:</strong> several half-finished systems, nothing strong enough to push.",
            "<strong>Real problem:</strong> resources spread across Rank Up, Upgrades, Avatars and Weapons at once.",
            "<strong>Lever:</strong> pick one line and finish it. <a href=\"/guides/upgrades/\">Upgrades</a> · <a href=\"/guides/rank-up/\">Rank Up</a>",
        ]),
        ("h2", "Stage 3 — late: the ceiling bottleneck"),
        ("ul", [
            "<strong>Symptom:</strong> ordinary content is comfortable, but specific challenges are walls.",
            "<strong>Real problem:</strong> gear and rarity gaps — accessories, amulets and weapons decide the ceiling, not raw playtime.",
            "<strong>Lever:</strong> target the drop source deliberately. <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a> → <a href=\"/wiki/accessories/\">Accessories</a> → <a href=\"/wiki/amulets/\">Amulets</a> → <a href=\"/guides/raids/\">Raids</a>",
        ]),
        ("h2", "The decision rule that survives every update"),
        ("ol", [
            "<strong>Name the wall in one sentence</strong> — 'I cannot finish this challenge' or 'I run out of Energy', never 'I am stuck'.",
            "<strong>Match it to one loop link</strong> — Energy, Cards, Companions, resources, unlock, power, challenge.",
            "<strong>Spend only along that link</strong> — everything else waits. This is what keeps a mid-game account moving after a balance patch reshuffles the numbers.",
        ]),
        ("note", "Deliberately absent: numeric progression thresholds, rank costs, multiplier breakpoints and drop "
                 "rates. Those values shift between updates and the loop above does not depend on them."),
    ],
    "faq": [
        ("How do you progress fast in " + G + "?", "Fix the link that is actually blocking you. Early that is Energy income, mid it is unfinished commitments spread across too many systems, late it is gear and rarity ceilings. The loop is verified from the official listing; the numbers around it change."),
        ("What is the fastest way to get stronger in " + G + "?", "Finish one line before starting another — either a rank push or an upgrade push. Splitting resources is the most reliable way to stay weak in an update-driven Roblox experience."),
        ("Does " + G + " have a level cap?", "No verified cap is part of the official record. Rank ladders and multipliers are the kind of value that moves between builds, so this site does not print one."),
        ("When should I start doing Raids?", "When your ceiling problem is challenges rather than resources — that is the point where raid access and rewards outweigh another farming route. See the Raids guide."),
    ],
    "related": [("Rank Up", "/guides/rank-up/", "The power step"),
                ("Secret Boss Locations", "/guides/secret-boss-locations/", "Where ceilings break"),
                ("Raids", "/guides/raids/", "The challenge tier")],
}

# ============================================================
# 8. Energy  (/guides/energy/)
# ============================================================
PAGES["guides/energy/index.html"] = {
    "path": "guides/energy/index.html",
    "title": G + " Energy – How to Get, Use & Stretch Energy",
    "meta": ("Energy in " + G + ": the official loop's entry point. How it is gained, what it is spent on, and "
             "how to stop wasting it — without inventing rates or caps."),
    "pill": "Guides", "h1": G + " Energy",
    "lead": ("Energy is the first link of the official loop. This guide covers what it does, how it is spent, "
             "and how to read your own income."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Energy", "/guides/energy/")],
    "sections": [
        ("p", "The official " + G + " description opens with Energy: you <strong>gain Energy</strong>, and Energy is "
              "what lets you <strong>open Cards for Companions</strong>. Everything else in the game is downstream "
              "of that first conversion."),
        ("h2", "What Energy does"),
        ("ul", [
            "<strong>It gates the Card layer</strong> — Cards are the official route to Companions, and Energy is what you spend to open them. <a href=\"/wiki/cards/\">Cards</a>",
            "<strong>It paces your session</strong> — because it is a spend-then-wait style resource, your session quality is decided by how you spend it, not by how long you play.",
            "<strong>It converts into everything else</strong> — Companions produce the combat and farm output that becomes resources. <a href=\"/wiki/companions/\">Companions</a> · <a href=\"/wiki/resources/\">Resources</a>",
        ]),
        ("h2", "How to gain Energy"),
        ("p", "The official record establishes Energy as the loop's input; it does not publish a rate. Rather than "
              "copy a rate off a wiki, measure your own:"),
        ("ol", [
            "<strong>Record your Energy before a session</strong> — note the number and the time.",
            "<strong>Play normally for a fixed window</strong> — same content, same spending pattern.",
            "<strong>Record it again</strong> — the difference is your real income for that window, on the current build.",
            "<strong>Re-measure after a major update</strong> — income sources are exactly the kind of value updates change.",
        ]),
        ("note", "This measurement habit is the whole trick. Published Energy rates go stale within a patch cycle; "
                 "your own two-point measurement does not."),
        ("h2", "How to spend Energy well"),
        ("ul", [
            "<strong>Spend in sets, not sips</strong> — opening Cards as a batch tells you what your roster is missing before you commit. <a href=\"/wiki/cards/\">Cards</a>",
            "<strong>Do not spend to 'top up' a bad session</strong> — if a spend session produced nothing useful, the answer is the next batch, not more spend.",
            "<strong>Know what Energy does not buy</strong> — Rank Up, Upgrades, Avatars, Weapons and Raids draw on resources and progression, not Energy alone. <a href=\"/guides/rank-up/\">Rank Up</a>",
            "<strong>Track your conversion</strong> — Energy in, useful Companions or resources out. That ratio is the only progression metric worth watching early.",
        ]),
        ("h2", "Energy and the free path"),
        ("p", "On a no-Robux account, Energy pacing is your main lever: free code rewards and consistent daily "
              "sessions matter more than any single big purchase. The <a href=\"/guides/f2p/\">F2P guide</a> covers "
              "the rest of that route, and the <a href=\"/codes/\">codes page</a> tracks the free rewards we can "
              "date."),
        ("note", "We do not publish Energy caps, regeneration rates, refill costs or Card pull rates: no current "
                 "source backs them, and they change. If you need a number, measure it as above."),
    ],
    "faq": [
        ("How do you get Energy in " + G + "?", "Energy is the entry point of the official loop — you gain it, then spend it to open Cards for Companions. The official record does not publish a rate, so measure your own income over a fixed window instead of trusting a copied number."),
        ("What do you spend Energy on in " + G + "?", "Opening Cards. Cards are the official route to Companions, and Companions are what produce the combat and resource output that funds everything else."),
        ("Is Energy the same as a stamina system?", "Functionally it paces your session the way a stamina resource does, and the official description treats it as the loop's input. Exact caps, regen and refill behaviour are not published here because they are not verified."),
        ("What if I waste my Energy?", "You cannot undo a spend, but you can change the pattern: spend in sets, measure Energy in versus useful output out, and re-measure after updates instead of following a stale guide."),
    ],
    "related": [("Cards", "/wiki/cards/", "Where Energy goes"),
                ("Beginner Guide", "/guides/beginner-guide/", "The full first-session order"),
                ("F2P Guide", "/guides/f2p/", "Energy pacing without Robux")],
}

# ============================================================
# 9. Rank Up  (/guides/rank-up/)
# ============================================================
PAGES["guides/rank-up/index.html"] = {
    "path": "guides/rank-up/index.html",
    "title": G + " Rank Up – When to Rank & What It Depends On",
    "meta": "Rank Up in Anime Breaker: what the official loop includes, when a rank push is worth the resources, and why no verified cost table is published.",
    "pill": "Guides", "h1": G + " Rank Up",
    "lead": ("Ranking is one of the two power steps in the official loop. This guide is about timing it — "
             "and about being honest that its costs are version-sensitive."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Rank Up", "/guides/rank-up/")],
    "sections": [
        ("p", "The official " + G + " loop includes <strong>Rank Up</strong> as a distinct step, after you have "
              "unlocked Avatars, Weapons and rare items. That placement matters: ranking is a power step you take "
              "once your economy can support it, not a first-day goal."),
        ("h2", "What ranking is for"),
        ("ul", [
            "<strong>It is a power step, not a side system</strong> — the official loop puts it alongside upgrades, after the unlock layer.",
            "<strong>It competes for the same resources</strong> as <a href=\"/guides/upgrades/\">Upgrades</a>, <a href=\"/wiki/avatars/\">Avatars</a> and <a href=\"/wiki/weapons/\">Weapons</a> — which is why timing is the entire question.",
            "<strong>It is version-sensitive</strong> — rank ladders get rebalanced, so exact costs and multipliers are re-checked rather than memorised.",
        ]),
        ("h2", "When a rank push is worth it"),
        ("ol", [
            "<strong>Your income is stable</strong> — you can describe roughly how much resource you earn per session. <a href=\"/guides/energy/\">Energy</a>",
            "<strong>Your roster is not the wall</strong> — if fights fail because of what you own rather than what you are, gear and Companions come first. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>You can absorb the next cost tier</strong> — ranking up front-loads cost; if the next tier stalls you, you have traded a slow climb for a hard stop.",
            "<strong>You are not mid-way through an upgrade line</strong> — finish it. Abandoned half-upgrades are the classic mid-game resource sink. <a href=\"/guides/upgrades/\">Upgrades</a>",
        ]),
        ("h2", "When to wait"),
        ("ul", [
            "<strong>Right after a major update</strong> — the update line currently tagged CLASS TREE is exactly the kind of change that reshuffles class and rank value. <a href=\"/updates/\">Updates</a>",
            "<strong>When a code wave is live</strong> — free rewards change how much you need to farm. <a href=\"/codes/\">Codes</a>",
            "<strong>When your bottleneck is a challenge, not a stat</strong> — that is a gear problem; go to <a href=\"/guides/secret-boss-locations/\">boss farming</a> or <a href=\"/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "What we do not publish about ranking"),
        ("p", "Rank cost tables, per-rank multipliers, requirement values and the exact number of ranks are held "
              "back deliberately. Multiple secondary pages currently disagree on these numbers, and a disagreement "
              "is a lead, not a fact. When a current source can be backed, this page gains a dated table — until "
              "then it stays a decision guide."),
        ("note", "If you only take one thing from this page: rank when your economy can carry the next tier, not "
                 "when the button becomes available."),
    ],
    "faq": [
        ("When should you rank up in " + G + "?", "When your resource income is stable, your roster is not the thing failing, and you can absorb the next cost tier. If an upgrade or gear line is half finished, finish it first — abandoned lines are the classic mid-game sink."),
        ("How much does it cost to rank up in " + G + "?", "No verified cost table is published here. Secondary sources disagree on rank costs, and they change with updates. Treat any undated cost table as unverified."),
        ("Does ranking up make you stronger than upgrading?", "The official loop treats Rank Up and Upgrades as two power steps competing for the same resources. Which one pays off more depends on your current bottleneck, not on a universal answer."),
        ("Should I rank up right after an update?", "Usually wait. Updates — the current line is tagged CLASS TREE — are exactly when class and rank values move. Re-measure your economy and priorities after the dust settles."),
    ],
    "related": [("Upgrades", "/guides/upgrades/", "The other power step"),
                ("Progression Guide", "/guides/progression/", "Which wall to attack"),
                ("Updates", "/updates/", "Why values move")],
}

# ============================================================
# 10. Upgrades  (/guides/upgrades/)
# ============================================================
PAGES["guides/upgrades/index.html"] = {
    "path": "guides/upgrades/index.html",
    "title": G + " Upgrades – Priority Framework (Best Upgrades)",
    "meta": "Best upgrades in Anime Breaker as a prioritisation framework, not a frozen tier list: what to feed first, what to park, and why order changes.",
    "pill": "Guides", "h1": G + " Upgrades",
    "lead": ("A priority framework you can apply to your own account right now — because the 'best upgrade' in a "
             "Roblox experience is a moving target."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Upgrades", "/guides/upgrades/")],
    "sections": [
        ("p", "Upgrades are the second power step in the official " + G + " loop, sitting alongside Rank Up after "
              "the unlock layer. Players search for 'best upgrades' expecting a ranked list; the honest answer is "
              "that a list which is right this week is wrong after the next rebalance. So here is the decision "
              "logic instead."),
        ("h2", "The priority test, in order"),
        ("ol", [
            "<strong>What is failing?</strong> Name the specific content you cannot clear. An upgrade that does not change that outcome is not a priority, whatever its rarity.",
            "<strong>Which link is weakest?</strong> Output (fights and farms), survivability, or resource flow. Feed the weakest link. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>What compounds?</strong> Between two options, pick the one that makes future sessions faster — usually the one that improves your farming route rather than a single fight.",
            "<strong>What is cheapest per step?</strong> Step cost curves differ; a cheap line you can finish beats an expensive line you must abandon. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>What survives the next update?</strong> Upgrades tied to your core loop (Companions, weapons you actually use) hold value across patches better than flavour-of-the-month picks.",
        ]),
        ("h2", "What to upgrade first as a beginner"),
        ("ul", [
            "<strong>Your farming set-up</strong> — anything that raises how much resource your sessions produce. <a href=\"/guides/energy/\">Energy</a>",
            "<strong>Your main Companion line</strong> — Companions are what you take into combat in the official loop. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>One weapon you will still use later</strong> — spreading upgrades across many weapons is the most common early waste. <a href=\"/wiki/weapons/\">Weapons</a>",
        ]),
        ("h2", "What to park"),
        ("ul", [
            "<strong>Anything bought for a single event</strong> — unless that event is your current wall.",
            "<strong>A second and third weapon line</strong> — until your first can clear the content you are stuck on.",
            "<strong>Cosmetic-adjacent unlocks</strong> — they do not move the loop. <a href=\"/wiki/avatars/\">Avatars</a> are worth unlocking, but not at the cost of a stalled attack line.",
        ]),
        ("h2", "Why there is no ranked 'best upgrades' table"),
        ("p", "Because a ranked table requires per-level numbers, and no current source publishes a consistent set "
              "for this build. Secondary pages contradict each other on multipliers and upgrade costs. Publishing "
              "a confident ranking built on disagreeing sources would be inventing a fact, so this page gives you "
              "the framework and dates its own last check instead."),
        ("note", "Update sensitivity: after a balance patch, re-run the priority test from step one. Your weakest "
                 "link may have changed even if your account did not."),
    ],
    "faq": [
        ("What are the best upgrades in " + G + "?", "The ones that fix your current bottleneck: farming output first for most accounts, then one Companion line, then one weapon line. A static ranking would be wrong after the next rebalance, so this guide gives the decision order instead of a frozen list."),
        ("Should I upgrade or rank up first in " + G + "?", "Both are power steps sharing the same resources. Upgrade when your income is stable and a specific upgrade changes an outcome you care about; rank when your economy can carry the next cost tier. Finish one line before starting the other."),
        ("Is it worth upgrading many weapons?", "No, not early. One working weapon line beats three unfinished ones, and weapon values are exactly what updates change."),
        ("How often do upgrade priorities change in " + G + "?", "Whenever the game is rebalanced — the current update line is tagged CLASS TREE. Re-check after each major update rather than following an old tier list."),
    ],
    "related": [("Rank Up", "/guides/rank-up/", "Timing the other power step"),
                ("Resources", "/wiki/resources/", "What upgrades consume"),
                ("Weapons", "/wiki/weapons/", "Which line to commit to")],
}

# ============================================================
# 11. Cards  (/wiki/cards/)
# ============================================================
PAGES["wiki/cards/index.html"] = {
    "path": "wiki/cards/index.html",
    "title": G + " Cards – How Cards Unlock Companions",
    "meta": ("Cards in " + G + ": the official acquisition layer. What Cards do, how they connect to Energy and "
             "Companions, and why pull rates are not published here."),
    "pill": "Wiki", "h1": G + " Cards",
    "lead": ("Cards are the official bridge between Energy and Companions — the acquisition layer of the loop."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Cards", "/wiki/cards/")],
    "sections": [
        ("p", "In the official " + G + " description the loop reads: gain Energy, then <strong>open Cards for "
              "Companions</strong>. So Cards are not a side collectible — they are the mechanism that converts your "
              "Energy into the roster you actually fight with."),
        ("h2", "What Cards do"),
        ("table", {"head": ["Question", "Answer", "Confidence"],
                   "rows": [
                       ["What are Cards for?", "Opening them is the official way to acquire Companions.", "VERIFIED (official listing)"],
                       ["What do they cost?", "They are the spend side of the Energy step — Energy is what you gain first.", "VERIFIED (official listing)"],
                       ["How do you open them?", "Inside the experience; the UI moves between builds, so use the current interface.", "OBSERVED"],
                       ["What are the pull rates?", "Not published here — no current source backs a rate table.", "UNVERIFIED"],
                   ]}),
        ("h2", "Cards in the loop"),
        ("ol", [
            "<strong>Gain Energy</strong> — the loop's input. <a href=\"/guides/energy/\">Energy</a>",
            "<strong>Open Cards</strong> — spend Energy, and this is the only official route to new Companions.",
            "<strong>Field the Companions</strong> — what you get from Cards is what fights for you. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>Convert combat into resources</strong> — which funds every later step. <a href=\"/wiki/resources/\">Resources</a>",
        ]),
        ("h2", "How to open Cards sensibly"),
        ("ul", [
            "<strong>Batch your openings</strong> — a set of results tells you what your roster lacks; single pulls tell you almost nothing.",
            "<strong>Judge the roster, not the pull</strong> — a duplicate-heavy batch is only a problem if it does not improve your farming route.",
            "<strong>Do not chase rates you cannot see</strong> — if a site quotes exact pull percentages without a dated source, treat it as a guess.",
        ]),
        ("note", "Deliberately absent from this page: pull rates, rarity tables, card counts and odds of specific "
                 "Companions. Those numbers change with updates and disagree across secondary sources; publishing "
                 "one would freeze a value that the live client can contradict."),
    ],
    "faq": [
        ("What are Cards in " + G + "?", "The official acquisition layer of the loop. You gain Energy, open Cards, and Cards are how you get Companions to fight with."),
        ("How do you get Cards in " + G + "?", "Cards are tied to the Energy step in the official description — Energy is the loop's first resource, and opening Cards is what it is spent on."),
        ("What are the " + G + " card pull rates?", "Not published here. No current source backs a consistent rate table, and rates are exactly the value updates change. Batch your openings and judge the roster result instead."),
        ("Do duplicates matter?", "They can, but the useful test is whether a batch improved your farming route or roster coverage — not how many duplicates appeared in one pull."),
    ],
    "related": [("Companions", "/wiki/companions/", "What Cards give you"),
                ("Energy", "/guides/energy/", "The resource Cards consume"),
                ("Beginner Guide", "/guides/beginner-guide/", "Cards in your first session")],
}

# ============================================================
# 12. Companions  (/wiki/companions/)
# ============================================================
PAGES["wiki/companions/index.html"] = {
    "path": "wiki/companions/index.html",
    "title": "Anime Breaker Companions – How to Get Them",
    "meta": ("Companions in " + G + ": how the official loop produces them through Cards, how they are used in "
             "combat, and how they differ from Avatars."),
    "pill": "Wiki", "h1": G + " Companions",
    "lead": ("Companions are the official loop's combat output — what you get from Cards and what you field."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Companions", "/wiki/companions/")],
    "sections": [
        ("p", "In the official " + G + " loop you <strong>open Cards for Companions</strong>, then <strong>fight "
              "enemies for resources</strong>. Companions sit between those two steps: they are the result of your "
              "Energy spend and the thing that carries your combat and farming."),
        ("h2", "How you get Companions"),
        ("ol", [
            "<strong>Gain Energy</strong> — the loop's input. <a href=\"/guides/energy/\">Energy</a>",
            "<strong>Open Cards</strong> — Cards are the official acquisition route. <a href=\"/wiki/cards/\">Cards</a>",
            "<strong>Field what you get</strong> — Companions are usable in combat immediately in the loop description.",
            "<strong>Improve the set over time</strong> — upgrades and unlocks raise your output. <a href=\"/guides/upgrades/\">Upgrades</a>",
        ]),
        ("h2", "Companion vs Avatar"),
        ("table", {"head": ["Aspect", "Companions", "Avatars"],
                   "rows": [
                       ["Role in the loop", "Acquired via Cards, used to fight and farm.", "Listed as an unlock alongside Weapons and rare items."],
                       ["How you get them", "Opening Cards (official).", "Unlocked through progression; community sources describe additional farming routes that this site has not verified."],
                       ["What they change", "Your combat and farming output.", "What you play as, which is why players treat Avatars as a collection and identity layer as well as a power layer."],
                       ["Confidence", "VERIFIED (official listing)", "VERIFIED for the unlock; PARTIAL for the mechanics"],
                   ]}),
        ("h2", "Using Companions well"),
        ("ul", [
            "<strong>Cover your gaps</strong> — a batch of Cards usually leaves holes in your roster; fill roles you lack rather than stacking what you already have.",
            "<strong>Feed the ones you keep</strong> — upgrades spent on a Companion you will replace are the most common waste. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Match the content</strong> — farming routes and challenge fights reward different profiles; keep one farming set and one fighting set. <a href=\"/guides/progression/\">Progression</a>",
        ]),
        ("note", "Companion multipliers, tier lists and pull rates are not published here: no current source backs a "
                 "consistent set, and 'best Companion' changes with every rebalance. The "
                 "<a href=\"/wiki/avatars/\">Avatars</a> page follows the same rule."),
    ],
    "faq": [
        ("What are Companions in " + G + "?", "The units you get from opening Cards in the official loop, and what you field to fight enemies and earn resources."),
        ("How do you get Companions in " + G + "?", "Open Cards. The official description puts Cards directly in front of Companions, and Energy is what you spend to open them."),
        ("What is the difference between a Companion and an Avatar in " + G + "?", "Companions are your roster, acquired through Cards and used in combat. Avatars are an unlock in the same official loop, and function more as an identity and progression layer on top of that roster."),
        ("Which Companion is the best in " + G + "?", "No tier list is published here. 'Best' follows the current balance patch and the content you are running, so the useful question is which role your roster is missing — see the Cards page for how to read a batch."),
    ],
    "related": [("Cards", "/wiki/cards/", "Where Companions come from"),
                ("Avatars", "/wiki/avatars/", "The other unlock layer"),
                ("Upgrades", "/guides/upgrades/", "Which ones to invest in")],
}

# ============================================================
# 13. Avatars  (/wiki/avatars/)
# ============================================================
PAGES["wiki/avatars/index.html"] = {
    "path": "wiki/avatars/index.html",
    "title": G + " Avatars – Unlocking, Growing & Farming",
    "meta": "Avatars in Anime Breaker: the official unlock layer. How Avatars are unlocked and grown, what community sources report, and which values stay unpublished.",
    "pill": "Wiki", "h1": G + " Avatars",
    "lead": ("Avatars are the loop's unlock layer — what you play as, and the collection players grind hardest for."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Avatars", "/wiki/avatars/")],
    "sections": [
        ("p", "The official " + G + " loop says you <strong>unlock Avatars, Weapons and rare items</strong> once your "
              "fights are producing resources. Avatars therefore sit in the middle of the loop: not the thing you "
              "start with, and not the thing you ignore."),
        ("h2", "Unlocking Avatars"),
        ("ol", [
            "<strong>Build your resource flow first</strong> — the unlock layer is funded by combat and farming. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Play the unlock route</strong> — Avatars are earned through in-experience progression in the official description.",
            "<strong>Expect a collection, not one pick</strong> — the loop phrases Avatars in the plural, so building a set is the design intent.",
        ]),
        ("h2", "Growing and using Avatars"),
        ("ul", [
            "<strong>Treat each Avatar as its own line</strong> — investing in one fully beats spreading across several. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Keep a farming Avatar and a fighting Avatar</strong> — the roles rarely overlap perfectly. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Test before you commit</strong> — with balance changes, the Avatar that was strong last patch may not be after the next one. <a href=\"/updates/\">Updates</a>",
        ]),
        ("h2", "Community-reported farming routes"),
        ("p", "Secondary pages describe Avatar-acquisition routes that involve repeated fights against specific NPC "
              "sets, and some list <em>estimated</em> Avatar roles and maximum levels. Those are discovery leads: "
              "the estimates come from third-party coverage, they disagree with each other, and they are dated. "
              "This page does not restate them as facts."),
        ("note", "Unpublished on purpose: Avatar multipliers, exact drop or unlock odds, maximum level values and "
                 "per-Avatar rankings. Each one is both version-sensitive and currently inconsistent across "
                 "sources. <a href=\"/guides/secret-boss-locations/\">Boss hunting</a> is covered separately, "
                 "including the values we refuse to freeze there."),
    ],
    "faq": [
        ("How do you get Avatars in " + G + "?", "They are the unlock layer of the official loop: once your fights are producing resources, Avatars, Weapons and rare items become reachable through in-experience progression."),
        ("Can you level up Avatars in " + G + "?", "Avatars grow as part of the progression layer, and upgrades are one of the two power steps in the official loop. Exact per-level values are not published here because they shift between updates."),
        ("How do you farm Avatars in " + G + "?", "Community sources describe repeated NPC fights as the farming route. That is REPORTED rather than verified, and the odds quoted alongside it are estimates — so this page describes the approach, not invented numbers."),
        ("Which Avatar is the strongest in " + G + "?", "No ranking is published here. Avatar multipliers disagree across sources and move with balance patches, so the honest guide is: pick a line, finish it, and re-evaluate after an update."),
    ],
    "related": [("Companions", "/wiki/companions/", "Companion vs Avatar compared"),
                ("Energy", "/guides/energy/", "Funding the unlock layer"),
                ("Weapons", "/wiki/weapons/", "The other unlock in the loop")],
}

# ============================================================
# 14. Weapons  (/wiki/weapons/)
# ============================================================
PAGES["wiki/weapons/index.html"] = {
    "path": "wiki/weapons/index.html",
    "title": "Anime Breaker Weapons – Acquisition & Roles",
    "meta": ("Weapons in " + G + ": how the official loop unlocks them, how to pick which one to commit to, and "
             "why no stat table is published here."),
    "pill": "Wiki", "h1": G + " Weapons",
    "lead": ("Weapons are the second half of the official unlock layer — and the place where new players waste the "
             "most resources on unfinished lines."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Weapons", "/wiki/weapons/")],
    "sections": [
        ("p", "The official loop has you <strong>unlock Avatars, Weapons and rare items</strong> once combat is "
              "producing resources. Weapons are therefore gated behind the same economy as Avatars: earn first, "
              "unlock second."),
        ("h2", "How Weapons fit in"),
        ("table", {"head": ["Question", "Answer", "Confidence"],
                   "rows": [
                       ["Are Weapons in the official loop?", "Yes — named in the unlock step alongside Avatars and rare items.", "VERIFIED (official listing)"],
                       ["How do you get them?", "Through in-experience progression; community sources additionally report boss-linked routes.", "PARTIAL (official for the loop, REPORTED for boss links)"],
                       ["What do they change?", "Your combat output — which feeds the resource step.", "OBSERVED"],
                       ["Are stat tables published here?", "No. Damage, scaling and upgrade costs are version-sensitive and inconsistent across sources.", "UNVERIFIED"],
                   ]}),
        ("h2", "Choosing a weapon line"),
        ("ol", [
            "<strong>Pick one</strong> — commit to a single weapon line until it clears the content you are stuck on. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Check the source, not the screenshot</strong> — a weapon ranking without a date is a rumour; weapons get rebalanced. <a href=\"/updates/\">Updates</a>",
            "<strong>Match it to your route</strong> — a weapon that speeds up farming pays for itself faster than one that wins a single fight. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Then chase the rare drop</strong> — bosses and challenges are where the ceiling-breaking items sit. <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a> · <a href=\"/guides/raids/\">Raids</a>",
        ]),
        ("h2", "Weapons, bosses and raids"),
        ("p", "Secondary coverage ties higher-tier weapons to boss and raid content. This site keeps that as a "
              "REPORTED link rather than a fixed drop table: <a href=\"/wiki/accessories/\">Accessories</a> covers "
              "what we can say about boss drops, and <a href=\"/guides/raids/\">Raids</a> covers the challenge tier "
              "and its reward handling."),
        ("note", "Unpublished on purpose: weapon damage values, scaling curves, upgrade cost tables and tier "
                 "rankings. All four are exactly the fields that break when the client is rebalanced."),
    ],
    "faq": [
        ("How do you get Weapons in " + G + "?", "Weapons are in the official unlock layer of the loop: once your fights are producing resources, Weapons, Avatars and rare items become reachable through in-experience progression."),
        ("What is the best weapon in " + G + "?", "No ranking is published here. Weapon values move with balance patches and disagree across secondary sources, so the useful rule is to commit to one line and re-check after an update."),
        ("Are weapons dropped by bosses in " + G + "?", "Secondary sources report boss-linked weapon and gear routes. That is REPORTED, not verified, so this site describes the route without printing drop rates."),
        ("Should I upgrade weapons or Avatars first?", "Whichever fixes your current wall. If fights fail on output, upgrade your weapon line; if you cannot reach the content at all, the unlock and farming route comes first."),
    ],
    "related": [("Secret Boss Locations", "/guides/secret-boss-locations/", "Where the rare drops are"),
                ("Accessories", "/wiki/accessories/", "Boss-sourced gear"),
                ("Upgrades", "/guides/upgrades/", "Committing to one line")],
}

# ============================================================
# 15. Secret Boss Locations  (/guides/secret-boss-locations/)
# ============================================================
PAGES["guides/secret-boss-locations/index.html"] = {
    "path": "guides/secret-boss-locations/index.html",
    "title": "Anime Breaker Secret Boss Locations – How to Find",
    "meta": ("Secret bosses in " + G + ": how bosses are approached, what farming them is for, and why no HP or "
             "drop-rate numbers are frozen on this page."),
    "pill": "Guides", "h1": G + " Secret Boss Locations",
    "lead": ("A find-and-farm guide built on approach and purpose — not on frozen HP values or copied drop odds."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Secret Boss Locations", "/guides/secret-boss-locations/")],
    "sections": [
        ("p", "Boss hunting is how players break the late-game ceiling in " + G + ": the official loop sends you to "
              "fight enemies for resources and to unlock rare items, and community coverage treats secret bosses as "
              "the concentrated version of that step. The difference between a good boss route and a bad one is "
              "targeting, not luck."),
        ("h2", "What secret bosses are for"),
        ("ul", [
            "<strong>Concentrated farming</strong> — one target instead of a route, which is why late-game players spend sessions on them.",
            "<strong>Ceiling-breaking drops</strong> — the gear and rare-item layer that keeps progression moving. <a href=\"/wiki/accessories/\">Accessories</a>",
            "<strong>A gate on the challenge tier</strong> — what you farm feeds <a href=\"/guides/raids/\">Raids</a> and the <a href=\"/guides/trial/\">Trial</a> loop.",
        ]),
        ("h2", "Finding bosses: the honest method"),
        ("ol", [
            "<strong>Advance until the world opens up</strong> — boss access is progression-gated in the official loop's unlock step. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Explore the current world instead of one old map screenshot</strong> — layouts and spawn areas move between updates. <a href=\"/wiki/worlds/\">Worlds</a>",
            "<strong>Watch the update line</strong> — the current title tag CLASS TREE marks a live update line, and update lines are when boss content moves. <a href=\"/updates/\">Updates</a>",
            "<strong>Record what you find</strong> — your own dated note of where a boss appeared is worth more than a copied coordinate list.",
        ]),
        ("h2", "How to farm a boss efficiently"),
        ("ul", [
            "<strong>Bring a farming set, not a showcase set</strong> — repeat clears matter more than a single impressive win. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>Fix your route before your stats</strong> — if a clear takes too long, the bottleneck is usually the approach, not your damage.",
            "<strong>Stop when the drop stops paying</strong> — once you own the upgrade you came for, the next farm target is elsewhere.",
        ]),
        ("h2", "What this page will not publish"),
        ("p", "Boss HP values, spawn or respawn timers, exact drop percentages, and coordinate lists copied from "
              "other wikis. Secondary pages currently quote these numbers and disagree with each other — a "
              "disagreement is not a source. When values can be verified against the current client, they will be "
              "added here with a date; until then, the method above is the durable part."),
        ("note", "The same rule applies to the <a href=\"/wiki/accessories/\">Accessories</a> page, which covers "
                 "what boss drops are for rather than promising a drop table."),
    ],
    "faq": [
        ("Where are the secret bosses in " + G + "?", "Boss access is progression-gated and world layout changes between updates, so this site does not publish a frozen coordinate list. The durable method: push progression, explore the current world, watch the update line, and record what you find."),
        ("How do you farm bosses in " + G + "?", "Use a repeatable farming set rather than a showcase set, fix your approach route before your damage, and move on once the upgrade you wanted is secured."),
        ("What do bosses drop in " + G + "?", "Bosses are the reported source of gear and rare items that break the late-game ceiling, feeding the Accessories and Raids layers. Exact drop rates are deliberately not printed here."),
        ("Do boss positions change after updates?", "Assume yes. Roblox experiences rework worlds between updates, and the current title carries a CLASS TREE update tag — which is exactly when this kind of content moves."),
    ],
    "related": [("Accessories", "/wiki/accessories/", "What bosses are farmed for"),
                ("Worlds", "/wiki/worlds/", "Where you are hunting"),
                ("Raids", "/guides/raids/", "The tier after bosses")],
}

# ============================================================
# 16. Accessories  (/wiki/accessories/)
# ============================================================
PAGES["wiki/accessories/index.html"] = {
    "path": "wiki/accessories/index.html",
    "title": G + " Accessories – Boss Drops & Gear Decisions",
    "meta": ("Accessories in " + G + ": the boss-sourced gear layer, how to decide what to keep and upgrade, and "
             "why drop rates and stat values stay unpublished."),
    "pill": "Wiki", "h1": G + " Accessories",
    "lead": ("Accessories are the gear layer that comes out of boss farming — and the place late-game accounts "
             "spend their resources."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Accessories", "/wiki/accessories/")],
    "sections": [
        ("p", "The official " + G + " loop ends the unlock step with <strong>rare items</strong>, and sends you into "
              "Raids; community coverage places accessories in exactly that band, sourced from the boss fights "
              "described on the <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a> page."),
        ("h2", "Where accessories come from"),
        ("table", {"head": ["Source", "Status", "Note"],
                   "rows": [
                       ["Boss drops", "REPORTED", "Secondary coverage ties accessories to boss farming; treated as the gear band that breaks late-game ceilings."],
                       ["Rare-item unlock step", "VERIFIED (official listing)", "The official loop names rare items in the unlock layer alongside Avatars and Weapons."],
                       ["Raid rewards", "REPORTED", "Raid content is verified as the challenge tier; its specific reward contents are not published here."],
                   ]}),
        ("h2", "Deciding what to keep and upgrade"),
        ("ol", [
            "<strong>Ask what it fixes</strong> — an accessory that does not change a fight you are failing is a collector's item for now. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Prefer compounding picks</strong> — gear that speeds farming pays back across every future session.",
            "<strong>Upgrade one slot fully</strong> — spreading resources thin across accessories is the late-game version of the beginner mistake. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Re-check after updates</strong> — gear values are among the first things rebalanced. <a href=\"/updates/\">Updates</a>",
        ]),
        ("h2", "Accessories, amulets and weapons"),
        ("ul", [
            "<strong><a href=\"/wiki/amulets/\">Amulets</a></strong> — an additional gear slot reported at the same bottleneck stages, with the same rule: no invented names or values.",
            "<strong><a href=\"/wiki/weapons/\">Weapons</a></strong> — the output half of the gear layer.",
            "<strong><a href=\"/guides/raids/\">Raids</a></strong> — where the gear you built gets tested.",
        ]),
        ("note", "Unpublished on purpose: accessory drop rates, per-item stat values, upgrade cost tables and "
                 "best-in-slot lists. All four are version-sensitive and currently inconsistent across secondary "
                 "sources."),
    ],
    "faq": [
        ("What are accessories in " + G + "?", "The gear layer that sits with the rare items named in the official unlock step, and which community coverage sources from boss farming."),
        ("How do you get accessories in " + G + "?", "Reported routes are boss drops and the rare-item progression layer; raid content is verified as the challenge tier, but its specific reward contents are not published here."),
        ("Which accessory is best in " + G + "?", "No best-in-slot list is published. The working test is whether an accessory changes a fight you are currently failing — otherwise it is a collection piece for later."),
        ("Should I upgrade accessories or weapons first?", "Fix your current wall: output problems point at weapons, ceiling problems at gear. Commit to one slot at a time rather than spreading resources."),
    ],
    "related": [("Secret Boss Locations", "/guides/secret-boss-locations/", "Where drops come from"),
                ("Amulets", "/wiki/amulets/", "The next gear slot"),
                ("Raids", "/guides/raids/", "Testing what you built")],
}

# ============================================================
# 17. Raids  (/guides/raids/)
# ============================================================
PAGES["guides/raids/index.html"] = {
    "path": "guides/raids/index.html",
    "title": G + " Raids – Access, Waves, Rewards & What to Spend",
    "meta": ("Raids in " + G + ": the official loop's challenge tier. Access and wave structure, how to treat "
             "rewards, and why ticket costs stay unpublished."),
    "pill": "Guides", "h1": G + " Raids",
    "lead": ("Raids are where the loop ends — the point at which everything you farmed gets tested at once."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Raids", "/guides/raids/")],
    "sections": [
        ("p", "Raids are named explicitly in the official " + G + " loop, after the power steps. That order is the "
              "message: raids are not an entry point, they are the tier your account graduates into."),
        ("h2", "How raids fit the loop"),
        ("ol", [
            "<strong>Graduate from farming</strong> — you need a stable resource loop before raid access is meaningful. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Bring your real set</strong> — Companions, Weapons, Avatars and gear all matter here in a way ordinary farming does not. <a href=\"/wiki/companions/\">Companions</a>",
            "<strong>Read the wave structure</strong> — raid content is described as wave-based by community coverage; each wave is a checkpoint for what your account is missing. <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a>",
            "<strong>Spend rewards deliberately</strong> — what comes out of raids should feed the wall that stopped you, not the next shiny unlock. <a href=\"/wiki/accessories/\">Accessories</a>",
        ]),
        ("h2", "Access, tickets and cost handling"),
        ("p", "Community sources describe raid access being gated by progression and by a consumable-style entry "
              "cost. This site treats that as REPORTED structure and does not print ticket prices, wave counts or "
              "reward tables — those are among the most frequently rebalanced values in an update-driven Roblox "
              "experience, and the secondary sources currently disagree on them."),
        ("h2", "Planning your first raids"),
        ("ul", [
            "<strong>Fix the failing wave, not the whole raid</strong> — identify the wave that ends your run and find what it demands.",
            "<strong>Keep a farming route alongside raids</strong> — raids consume resources as well as grant them. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Do not change everything at once</strong> — one change per attempt tells you what actually worked. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Track the update line</strong> — raid tuning moves with updates. <a href=\"/updates/\">Updates</a>",
        ]),
        ("note", "Related layers: <a href=\"/wiki/amulets/\">Amulets</a> and <a href=\"/wiki/resources/\">Resources</a> "
                 "for what raids consume and return, and <a href=\"/guides/trial/\">Trial</a> for the other "
                 "challenge-style loop."),
    ],
    "faq": [
        ("How do you unlock raids in " + G + "?", "Raids sit at the end of the official loop, after your power steps. In practice that means a stable resource loop and a set that can clear challenge content before raid access becomes useful."),
        ("How many waves do " + G + " raids have?", "Community coverage describes wave-based raids, but exact wave counts are not published here — they change with updates and secondary sources disagree."),
        ("Do raids cost tickets in " + G + "?", "A consumable-style entry cost is reported. No ticket price is printed here for the same reason: it is a frequently rebalanced value."),
        ("What should I spend raid rewards on?", "The wall that stopped you. If a specific wave ended your run, feed the fix for that wave rather than the next unlock in the list."),
    ],
    "related": [("Amulets", "/wiki/amulets/", "A raid-adjacent gear slot"),
                ("Resources", "/wiki/resources/", "What raids consume"),
                ("Trial", "/guides/trial/", "The other challenge loop")],
}

# ============================================================
# 18. Trial  (/guides/trial/)
# ============================================================
PAGES["guides/trial/index.html"] = {
    "path": "guides/trial/index.html",
    "title": G + " Trial (Hallway) – Loop, Upgrades & Rewards",
    "meta": ("The " + G + " Trial / hallway challenge loop: how the run structure works, what it is for, and how "
             "to turn its rewards into progression."),
    "pill": "Guides", "h1": G + " Trial",
    "lead": ("The Trial (often called the hallway) is a repeatable challenge loop — a measurable test of what you "
             "have built."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("Trial", "/guides/trial/")],
    "sections": [
        ("p", "The Trial is covered by community sources as a hallway-style run: you push through repeated "
              "encounters and the run ends when your setup fails. That structure makes it the cleanest diagnostic "
              "in the game — the run tells you exactly which link of the loop is weakest."),
        ("h2", "How the Trial loop works"),
        ("ol", [
            "<strong>Enter and push</strong> — each encounter is a checkpoint rather than a single boss fight.",
            "<strong>Note where the run ends</strong> — the failing encounter names your bottleneck. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Upgrade the failing link only</strong> — one change, then re-run. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Convert rewards into the next push</strong> — Trial output is meant to feed progression, not sit in a menu. <a href=\"/wiki/resources/\">Resources</a>",
        ]),
        ("h2", "What the Trial is for"),
        ("ul", [
            "<strong>Diagnosing builds</strong> — a run isolates what your account lacks better than open-world farming.",
            "<strong>Repeatable upgrade funding</strong> — reported as a progression resource source, which is why it pairs with the upgrade guide.",
            "<strong>Bridging to raids</strong> — the wave-based pressure of <a href=\"/guides/raids/\">Raids</a> is easier once you can survive Trial-style stacking.",
        ]),
        ("h2", "Reported vs verified on this page"),
        ("table", {"head": ["Item", "Status"],
                   "rows": [
                       ["Trial/hallway exists as a repeatable challenge loop", "REPORTED (secondary gameplay coverage)"],
                       ["Wave/stacking run structure", "REPORTED"],
                       ["Exact reward tables and per-run costs", "Not published here — version-sensitive and inconsistent across sources"],
                       ["Official-loop placement (challenge tier alongside Raids)", "VERIFIED (official listing names Raids; the Trial is documented here as the adjacent challenge loop)"],
                   ]}),
        ("note", "As with <a href=\"/wiki/accessories/\">Accessories</a> and <a href=\"/wiki/amulets/\">Amulets</a>, "
                 "the mechanic is documented and the numbers are not. A Trial number that is right this week can be "
                 "wrong after the next update."),
    ],
    "faq": [
        ("What is the Trial in " + G + "?", "A repeatable, hallway-style challenge loop reported by community coverage. You push through stacked encounters until your setup fails, which makes it a good diagnostic for what your account is missing."),
        ("How do you get rewards from the Trial?", "Reported as a progression resource source: you push as far as your setup allows and convert the output into upgrades for the link that failed."),
        ("Is the Trial the same as raids in " + G + "?", "No. Raids are named in the official loop as the challenge tier; the Trial is a separate, reported challenge loop that shares the same wave-pressure feel and pairs well with raid preparation."),
        ("Why are Trial reward numbers missing?", "Because they are rebalanced and secondary sources disagree on them. This page documents the loop and the decision logic instead of freezing a value."),
    ],
    "related": [("Resources", "/wiki/resources/", "What Trial rewards become"),
                ("Raids", "/guides/raids/", "The tier it prepares you for"),
                ("Progression Guide", "/guides/progression/", "Reading the failing wave")],
}

# ============================================================
# 19. Amulets  (/wiki/amulets/)
# ============================================================
PAGES["wiki/amulets/index.html"] = {
    "path": "wiki/amulets/index.html",
    "title": "Anime Breaker Amulets – Acquisition & Use",
    "meta": ("Amulets in " + G + ": the reported gear slot at bottleneck stages — what it is for, how to decide "
             "on it, and why no name, stat or origin table is published."),
    "pill": "Wiki", "h1": G + " Amulets",
    "lead": ("Amulets are the gear decision players look for once ordinary upgrades stop moving the wall."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Amulets", "/wiki/amulets/")],
    "sections": [
        ("p", "Amulets appear in community coverage as an additional equipment layer that matters around the "
              "late-game bottleneck — the point where your account is comfortable in normal content but specific "
              "challenges, <a href=\"/guides/raids/\">Raids</a> and the <a href=\"/guides/trial/\">Trial</a>, keep "
              "ending runs. This page documents the decision, not a copied tier list."),
        ("h2", "When an amulet is the right answer"),
        ("ul", [
            "<strong>Your basics are done</strong> — weapons, one Companion line and a farming route are working. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>You are losing to the same wall repeatedly</strong> — a repeatable failure means a specific stat gap, not bad luck. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>An upgrade would change that outcome</strong> — if it would not, the amulet is a collection piece for now.",
        ]),
        ("h2", "How to approach amulet acquisition"),
        ("ol", [
            "<strong>Identify the requirement first</strong> — know which challenge is failing before you farm for the answer. <a href=\"/guides/secret-boss-locations/\">Secret Boss Locations</a>",
            "<strong>Farm a route, not a rumour</strong> — pick a repeatable source and time it, rather than trusting an undated odds table.",
            "<strong>Commit to one</strong> — split investment across several amulets repeats the classic mid-game mistake at a higher cost. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Re-check after updates</strong> — gear bands get retuned, and the current title carries a CLASS TREE update tag. <a href=\"/updates/\">Updates</a>",
        ]),
        ("h2", "Why this page has no amulet list"),
        ("p", "Amulet names, stat values, origins and upgrade costs are among the least consistently documented "
              "values in current secondary coverage — different sites list different items, and none of them date "
              "their tables. Under this site's rule, a disagreement is a lead rather than a fact, so the list stays "
              "unpublished until a current source can back it."),
        ("note", "The same standard applies across the gear band: <a href=\"/wiki/accessories/\">Accessories</a>, "
                 "<a href=\"/wiki/weapons/\">Weapons</a> and <a href=\"/guides/raids/\">Raids</a> all document "
                 "mechanics and decisions while leaving rebalanced numbers out."),
    ],
    "faq": [
        ("What are amulets in " + G + "?", "A reported additional gear layer that matters at the late-game bottleneck — the stage where normal content is comfortable but specific challenges keep ending your runs."),
        ("How do you get amulets in " + G + "?", "Community coverage describes boss and challenge-linked acquisition. This site treats those as reported routes and does not print drop rates or origins for specific items."),
        ("Should I farm amulets or upgrades first?", "Upgrades and your core gear first. An amulet pays off when a specific, repeatable failure has already told you what you are missing."),
        ("Why is there no amulet tier list here?", "Because current sources disagree on the items and none date their tables. Publishing one would mean freezing a value the live client can contradict."),
    ],
    "related": [("Accessories", "/wiki/accessories/", "The gear layer beside it"),
                ("Raids", "/guides/raids/", "Where it gets tested"),
                ("Resources", "/wiki/resources/", "What gear farming costs")],
}

# ============================================================
# 20. Resources  (/wiki/resources/)
# ============================================================
PAGES["wiki/resources/index.html"] = {
    "path": "wiki/resources/index.html",
    "title": "Anime Breaker Resources – Currencies & Sources",
    "meta": ("Resources in " + G + ": the economy behind the official loop — where resources come from, what they "
             "buy, and how to stop leaking them."),
    "pill": "Wiki", "h1": G + " Resources",
    "lead": ("Resources are what the whole loop converts into — and the fastest way to lose progress is to spend "
             "them on the wrong link."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Resources", "/wiki/resources/")],
    "sections": [
        ("p", "The official " + G + " loop is explicit that you <strong>fight enemies for resources</strong>. Those "
              "resources then fund the unlock layer (Avatars, Weapons, rare items) and the power steps (Rank Up, "
              "Upgrades), before the whole account is tested in Raids. Every resource question is therefore a "
              "spending-order question."),
        ("h2", "Source → use → spend"),
        ("table", {"head": ["Stage", "What happens", "Where it is covered"],
                   "rows": [
                       ["Source", "Combat and farming produce resources, powered by Energy → Cards → Companions.", "Energy · Cards · Companions"],
                       ["Use", "Resources fund unlocks and power steps: Avatars, Weapons, Rank Up, Upgrades.", "Avatars · Weapons · Rank Up · Upgrades"],
                       ["Spend test", "Does it fix the wall you are actually hitting?", "Progression"],
                       ["Ceiling", "Gear band and challenge tiers raise the ceiling: bosses, accessories, amulets, raids, trial.", "Secret Boss Locations · Accessories · Amulets · Raids · Trial"],
                   ]}),
        ("h2", "How resources leak"),
        ("ul", [
            "<strong>Parallel commitments</strong> — funding a rank push and an upgrade line at the same time is the single biggest sink in a mid-game account. <a href=\"/guides/rank-up/\">Rank Up</a>",
            "<strong>Flavour-of-the-month spending</strong> — chasing whatever a video called best without a dated source. <a href=\"/updates/\">Updates</a>",
            "<strong>Farming without a target</strong> — sessions that produce resources but no decision produce no progress.",
            "<strong>Ignoring free sources</strong> — the code system is live, and early free resources are worth more. <a href=\"/codes/\">Codes</a>",
        ]),
        ("h2", "The spending rule"),
        ("ol", [
            "<strong>Bank first</strong> — hold a buffer sized to the next decision, not to zero.",
            "<strong>One line at a time</strong> — finish what you started before opening a second front.",
            "<strong>Re-measure after updates</strong> — costs and incomes move; a rule you wrote down last month may no longer apply. <a href=\"/guides/progression/\">Progression</a>",
        ]),
        ("note", "No currency amounts, per-session yields, cost tables or exchange values are published here. Energy "
                 "income, rank costs and upgrade costs are all version-sensitive, and this page documents the "
                 "economy's shape rather than freezing its numbers."),
    ],
    "faq": [
        ("What are resources in " + G + "?", "The output of the combat and farming step in the official loop — the pool that funds Avatars, Weapons, rare items, Rank Up and Upgrades before the account is tested in Raids."),
        ("How do you get resources in " + G + "?", "By fighting enemies, as the official loop describes. In practice that means a working Energy → Cards → Companions chain and a farming route you can repeat."),
        ("What should I spend resources on first in " + G + "?", "Whatever fixes the wall you are hitting — usually farming output early and one committed upgrade or rank line later. Splitting resources across parallel lines is the most common way progress stalls."),
        ("How much of each resource do you need?", "No amounts are published here, because costs and incomes are rebalanced between updates. Bank a buffer sized to your next decision instead of to a copied number."),
    ],
    "related": [("Trial", "/guides/trial/", "A repeatable resource source"),
                ("Rank Up", "/guides/rank-up/", "A major resource sink"),
                ("F2P Guide", "/guides/f2p/", "Resource discipline with no Robux")],
}

# ============================================================
# 21. Worlds  (/wiki/worlds/)
# ============================================================
PAGES["wiki/worlds/index.html"] = {
    "path": "wiki/worlds/index.html",
    "title": G + " Worlds – World Order & Navigation",
    "meta": ("Worlds in " + G + ": how the world order works as a progression ladder, and how to navigate from "
             "each world to the systems, bosses and raids it feeds."),
    "pill": "Wiki", "h1": G + " Worlds",
    "lead": ("Worlds are the map layer of the loop — a ladder of progression stops, not a set of thin subpages."),
    "breadcrumb": [("Home", "/"), ("Wiki", "/wiki/"), ("Worlds", "/wiki/worlds/")],
    "sections": [
        ("p", "In " + G + " the world you are in tells you what your account should be doing: farm, unlock, or push a "
              "challenge. Community coverage documents multiple worlds with a broadly increasing difficulty order, "
              "and the current title carries a CLASS TREE update tag — which is the kind of change that reshuffles "
              "world content."),
        ("h2", "How to use the world order"),
        ("ol", [
            "<strong>Treat worlds as gates</strong> — if a world feels impossible, your bottleneck is one link back in the loop. <a href=\"/guides/progression/\">Progression</a>",
            "<strong>Farm in the world you can clear fastest</strong> — speed beats prestige for resource output. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Unlock forward, farm backward</strong> — push to the next world for unlocks, but keep a repeatable route in the one you clear reliably. <a href=\"/wiki/avatars/\">Avatars</a>",
            "<strong>Re-scout after updates</strong> — world layouts and boss placements move between builds. <a href=\"/updates/\">Updates</a>",
        ]),
        ("h2", "Navigation from here"),
        ("cards", [
            ("Secret Boss Locations", "How bosses are found and farmed in the current world.", "/guides/secret-boss-locations/"),
            ("Accessories", "What boss farming in later worlds is for.", "/wiki/accessories/"),
            ("Raids", "The challenge tier that tests the world you reached.", "/guides/raids/"),
            ("Trial", "The repeatable challenge loop outside the world ladder.", "/guides/trial/"),
            ("Weapons", "Unlocks that carry between worlds.", "/wiki/weapons/"),
            ("Resources", "What each world's farming produces.", "/wiki/resources/"),
        ]),
        ("note", "This page deliberately does not create one subpage per world. A page whose only difference is a "
                 "world name adds no decision value — the useful information is the order, the bottleneck and what "
                 "each world feeds, which is what is documented here. World names, caps and per-world drop tables "
                 "stay unpublished until a current source backs them."),
    ],
    "faq": [
        ("How many worlds are in " + G + "?", "Community coverage documents multiple worlds in an increasing difficulty order, and the count is the kind of thing updates change. This site does not publish a world count it cannot date."),
        ("What is the world order in " + G + "?", "The order is broadly increasing difficulty, and each world acts as a gate: if one feels impossible, the fix is usually one link back in the loop rather than more attempts."),
        ("Should I farm in the newest world I unlocked?", "Not necessarily. Fast clears produce more than slow ones, so many players unlock forward and farm backward in the world they can repeat reliably."),
        ("Why is there no per-world page for " + G + "?", "Because a page that only changes the world name adds nothing. This page documents the ladder, the bottleneck logic and the links to bosses, raids and systems."),
    ],
    "related": [("Secret Boss Locations", "/guides/secret-boss-locations/", "Bosses per world area"),
                ("Progression Guide", "/guides/progression/", "Which gate you are stuck at"),
                ("Updates", "/updates/", "World content moves with updates")],
}

# ============================================================
# 22. F2P  (/guides/f2p/)
# ============================================================
PAGES["guides/f2p/index.html"] = {
    "path": "guides/f2p/index.html",
    "title": G + " F2P Guide – Progressing Without Robux",
    "meta": "An Anime Breaker F2P guide: progress with no Robux spending, where free rewards actually help, and which habits keep a free account moving.",
    "pill": "Guides", "h1": G + " F2P Guide",
    "lead": ("Free accounts are not slower accounts — they are accounts that cannot afford a bad spending order."),
    "breadcrumb": [("Home", "/"), ("Guides", "/guides/"), ("F2P", "/guides/f2p/")],
    "sections": [
        ("p", "The official " + G + " loop is a progression loop, not a purchase loop: Energy → Cards → Companions → "
              "resources → unlocks → Rank Up / Upgrade → Raids. Nothing in that chain is described as paywalled. "
              "What a free account lacks is forgiveness for wasted resources."),
        ("h2", "The F2P rules that actually matter"),
        ("ol", [
            "<strong>Never spend without a named target</strong> — free accounts cannot brute-force a mistake. <a href=\"/wiki/resources/\">Resources</a>",
            "<strong>Take every dated free reward</strong> — the code system is live and codes are the cheapest resource injection available. <a href=\"/codes/\">Codes</a>",
            "<strong>Measure your Energy income</strong> — two-point measurement beats any copied rate. <a href=\"/guides/energy/\">Energy</a>",
            "<strong>Commit to one line</strong> — one Companion line, one weapon line, then one power step. <a href=\"/guides/upgrades/\">Upgrades</a>",
            "<strong>Farm where you clear fast</strong> — route quality is the free player's main multiplier. <a href=\"/wiki/worlds/\">Worlds</a>",
        ]),
        ("h2", "Where free accounts get stuck"),
        ("ul", [
            "<strong>Roster gaps, not currency gaps</strong> — a thin roster limits farming rate, which limits everything. <a href=\"/wiki/cards/\">Cards</a>",
            "<strong>Spread-out upgrades</strong> — the same mistake paid for at higher cost. <a href=\"/guides/rank-up/\">Rank Up</a>",
            "<strong>Chasing tier lists</strong> — undated rankings lead free accounts into expensive dead ends. <a href=\"/guides/progression/\">Progression</a>",
        ]),
        ("h2", "A realistic F2P order of operations"),
        ("ol", [
            "<strong>Session 1–3:</strong> learn Energy income, open Cards in batches, get a farming Companion set working. <a href=\"/guides/beginner-guide/\">Beginner Guide</a>",
            "<strong>Week 1:</strong> bank resources, finish one upgrade line, redeem every live code you can date.",
            "<strong>After that:</strong> unlock forward through <a href=\"/wiki/avatars/\">Avatars</a> and "
            "<a href=\"/wiki/weapons/\">Weapons</a>, farm the gear band via "
            "<a href=\"/guides/secret-boss-locations/\">bosses</a>, and only then push "
            "<a href=\"/guides/raids/\">Raids</a>.",
        ]),
        ("note", "This page makes no claims about what Robux purchases contain or cost. Roblox experiences change "
                 "their storefronts without notice, and this site does not publish unverifiable purchase details — "
                 "the F2P route above is built entirely on the verified loop."),
    ],
    "faq": [
        ("Can you play " + G + " without spending Robux?", "Yes in structure: the official loop describes progression through Energy, Cards, Companions, resources and unlocks, not through purchases. A free account mainly needs stricter resource discipline."),
        ("What should a free player do first in " + G + "?", "Measure Energy income, open Cards in batches for a working farming set, then commit to a single upgrade line while banking resources for the next decision."),
        ("Are codes worth it for F2P accounts?", "Yes — they are the cheapest resource injection available to a free account, and the codes page tracks what is reported active with the date it was checked."),
        ("Is " + G + " pay to win?", "No verified claim supports that, and this site does not publish purchase details it cannot check. The loop itself is effort-driven; the real F2P risk is wasting resources on parallel commitments."),
    ],
    "related": [("Codes", "/codes/", "Free resources, dated"),
                ("Beginner Guide", "/guides/beginner-guide/", "The first three sessions"),
                ("Energy", "/guides/energy/", "The free player's main lever")],
}

PAGE_ORDER = [
    "index.html", "wiki/index.html", "guides/index.html", "codes/index.html", "updates/index.html",
    "guides/beginner-guide/index.html", "guides/progression/index.html", "guides/energy/index.html",
    "guides/rank-up/index.html", "guides/upgrades/index.html", "guides/secret-boss-locations/index.html",
    "guides/raids/index.html", "guides/trial/index.html", "guides/f2p/index.html",
    "wiki/cards/index.html", "wiki/companions/index.html", "wiki/avatars/index.html",
    "wiki/weapons/index.html", "wiki/accessories/index.html", "wiki/amulets/index.html",
    "wiki/resources/index.html", "wiki/worlds/index.html",
]
