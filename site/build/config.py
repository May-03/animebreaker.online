# -*- coding: utf-8 -*-
"""Anime Breaker (Roblox) — 站点配置(基于第五套模板)。
语言:English + Português (BR) + Español — 按 Roblox 全球玩家大盘(US / BR / MX)选择,不含中文。
品牌色:实测官方 Roblox 体验页 5 张 key art/截图(2026-09-23, universeId 10675117523)
        → 火焰橙红(战斗主视觉)+ 深蓝夜空(场景)+ 暖沙金(稀有物品高光)。
事实规范(PRD §8/§17):所有内容分级 VERIFIED / OBSERVED / COMMUNITY REPORT / UNVERIFIED;
未核实数值(rank 成本、boss HP、掉率、武器数值、Avatar 倍率、pull rates、raid 门票)一律不写。
"""

# ============================================================
# ★ 1. 站点基本信息
# ============================================================
SITE = {
    "name": "Anime Breaker",           # 官方 Roblox 标题:Anime Breaker [🌳CLASS TREE](2026-09-23 核实)
    "slug": "anime-breaker",
    "developer": "HF x Anime Breaker", # 官方 Roblox 体验页开发者/发布者
    "domain": "animebreaker.online",   # 正式域名(本地预览时被 --domain 覆盖)
    "ga_id": "",                       # GA4 Measurement ID(上线部署时后补,留空则不输出 gtag)
    "cta_url": "https://www.roblox.com/games/109928390521457/",  # 官方 Roblox 体验页(已核实存在)
}

# ============================================================
# ★ 2. 语言:English + Português (Brasil) + Español
#    (Roblox 最活跃玩家地区语言:US / Brazil / Mexico;删除语言 = 从 LANG_ORDER 删 key + 删 content import)
# ============================================================
LANGS = {
    "en": {"dir": "", "lang": "en", "hreflang": "en", "name": "English", "short": "EN"},
    "pt": {"dir": "pt/", "lang": "pt-BR", "hreflang": "pt-BR", "name": "Português (Brasil)", "short": "PT"},
    "es": {"dir": "es/", "lang": "es", "hreflang": "es", "name": "Español", "short": "ES"},
}
LANG_ORDER = ["en", "pt", "es"]

HERO_TITLE = {
    "en": "Anime Breaker Roblox Wiki & Guide",
    "pt": "Anime Breaker Roblox Wiki e Guia",
    "es": "Anime Breaker Roblox Wiki y Guía",
}

# ============================================================
# ★ 3. 导航(每语言 3 栏下拉 + 移动分组 + 页脚)
#    与 content_*.py 的 22 个页面 path 一一对应(PRD §5 全量矩阵,无 HOLD 页)。
# ============================================================
RPX = SITE["cta_url"]

NAV = {
    "en": {
        "home": ("Home", "/"),
        "cols": [
            ("Start Here", [
                ("Beginner Guide", "The core loop and first steps", "/guides/beginner-guide/"),
                ("Guides", "All system and optimization guides", "/guides/"),
                ("Wiki", "The full system reference hub", "/wiki/"),
                ("Codes", "Working and expired code status", "/codes/"),
            ]),
            ("Game Systems", [
                ("Cards", "How Cards unlock Companions", "/wiki/cards/"),
                ("Companions", "Fight alongside your Companions", "/wiki/companions/"),
                ("Avatars", "Avatar rarity, growth and farming", "/wiki/avatars/"),
                ("Weapons", "Weapon acquisition and roles", "/wiki/weapons/"),
                ("Worlds", "World order and navigation", "/wiki/worlds/"),
            ]),
            ("Progress & Live", [
                ("Energy", "Gain, use and save Energy", "/guides/energy/"),
                ("Rank Up", "When to rank and upgrade", "/guides/rank-up/"),
                ("Upgrades", "Upgrade priority decisions", "/guides/upgrades/"),
                ("Raids", "Raid access, waves and rewards", "/guides/raids/"),
                ("Updates", "Verified update hub", "/updates/"),
            ]),
        ],
        "cta": ("Play on Roblox", RPX),
        "footer_cols": [
            ("Start Here", [("Beginner Guide", "/guides/beginner-guide/"), ("Guides", "/guides/"), ("Codes", "/codes/"), ("Updates", "/updates/")]),
            ("Wiki", [("Cards", "/wiki/cards/"), ("Companions", "/wiki/companions/"), ("Avatars", "/wiki/avatars/"), ("Weapons", "/wiki/weapons/"), ("Worlds", "/wiki/worlds/")]),
            ("Progress", [("Energy", "/guides/energy/"), ("Rank Up", "/guides/rank-up/"), ("Upgrades", "/guides/upgrades/"), ("Secret Boss Locations", "/guides/secret-boss-locations/"), ("Raids", "/guides/raids/")]),
            ("Gear & More", [("Accessories", "/wiki/accessories/"), ("Amulets", "/wiki/amulets/"), ("Resources", "/wiki/resources/"), ("Trial", "/guides/trial/"), ("F2P", "/guides/f2p/")]),
        ],
        "footer_site": [("Home", "/"), ("Wiki", "/wiki/"), ("Guides", "/guides/"), ("Codes", "/codes/"), ("Updates", "/updates/")],
    },
    "pt": {
        "home": ("Início", "/pt/"),
        "cols": [
            ("Comece aqui", [
                ("Guia para Iniciantes", "O ciclo principal e primeiros passos", "/pt/guides/beginner-guide/"),
                ("Guias", "Todos os guias de sistemas e otimização", "/pt/guides/"),
                ("Wiki", "O hub de referência de sistemas", "/pt/wiki/"),
                ("Códigos", "Status de códigos ativos e expirados", "/pt/codes/"),
            ]),
            ("Sistemas do Jogo", [
                ("Cartas", "Como as Cartas desbloqueiam Companions", "/pt/wiki/cards/"),
                ("Companions", "Lute ao lado dos seus Companions", "/pt/wiki/companions/"),
                ("Avatares", "Raridade, crescimento e farm de Avatares", "/pt/wiki/avatars/"),
                ("Armas", "Obtenção e função das Armas", "/pt/wiki/weapons/"),
                ("Mundos", "Ordem dos mundos e navegação", "/pt/wiki/worlds/"),
            ]),
            ("Progresso & Novidades", [
                ("Energia", "Ganhe, use e economize Energia", "/pt/guides/energy/"),
                ("Subir de Rank", "Quando rankear e melhorar", "/pt/guides/rank-up/"),
                ("Melhorias", "Decisões de prioridade de melhorias", "/pt/guides/upgrades/"),
                ("Raids", "Acesso, ondas e recompensas de Raids", "/pt/guides/raids/"),
                ("Atualizações", "Hub de atualizações verificado", "/pt/updates/"),
            ]),
        ],
        "cta": ("Jogar no Roblox", RPX),
        "footer_cols": [
            ("Comece aqui", [("Guia para Iniciantes", "/pt/guides/beginner-guide/"), ("Guias", "/pt/guides/"), ("Códigos", "/pt/codes/"), ("Atualizações", "/pt/updates/")]),
            ("Wiki", [("Cartas", "/pt/wiki/cards/"), ("Companions", "/pt/wiki/companions/"), ("Avatares", "/pt/wiki/avatars/"), ("Armas", "/pt/wiki/weapons/"), ("Mundos", "/pt/wiki/worlds/")]),
            ("Progresso", [("Energia", "/pt/guides/energy/"), ("Subir de Rank", "/pt/guides/rank-up/"), ("Melhorias", "/pt/guides/upgrades/"), ("Locais dos Bosses Secretos", "/pt/guides/secret-boss-locations/"), ("Raids", "/pt/guides/raids/")]),
            ("Equipamento & Mais", [("Acessórios", "/pt/wiki/accessories/"), ("Amuletos", "/pt/wiki/amulets/"), ("Recursos", "/pt/wiki/resources/"), ("Trial", "/pt/guides/trial/"), ("F2P", "/pt/guides/f2p/")]),
        ],
        "footer_site": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Guias", "/pt/guides/"), ("Códigos", "/pt/codes/"), ("Atualizações", "/pt/updates/")],
    },
    "es": {
        "home": ("Inicio", "/es/"),
        "cols": [
            ("Empieza aquí", [
                ("Guía para Principiantes", "El bucle principal y primeros pasos", "/es/guides/beginner-guide/"),
                ("Guías", "Todas las guías de sistemas y optimización", "/es/guides/"),
                ("Wiki", "El hub de referencia de sistemas", "/es/wiki/"),
                ("Códigos", "Estado de códigos activos y expirados", "/es/codes/"),
            ]),
            ("Sistemas del Juego", [
                ("Cartas", "Cómo las Cartas desbloquean Companions", "/es/wiki/cards/"),
                ("Companions", "Lucha junto a tus Companions", "/es/wiki/companions/"),
                ("Avatares", "Rareza, crecimiento y farmeo de Avatares", "/es/wiki/avatars/"),
                ("Armas", "Obtención y función de las Armas", "/es/wiki/weapons/"),
                ("Mundos", "Orden de los mundos y navegación", "/es/wiki/worlds/"),
            ]),
            ("Progreso y Novedades", [
                ("Energía", "Gana, usa y ahorra Energía", "/es/guides/energy/"),
                ("Subir de Rango", "Cuándo rankear y mejorar", "/es/guides/rank-up/"),
                ("Mejoras", "Decisiones de prioridad de mejoras", "/es/guides/upgrades/"),
                ("Raids", "Acceso, oleadas y recompensas de Raids", "/es/guides/raids/"),
                ("Actualizaciones", "Hub de actualizaciones verificado", "/es/updates/"),
            ]),
        ],
        "cta": ("Jugar en Roblox", RPX),
        "footer_cols": [
            ("Empieza aquí", [("Guía para Principiantes", "/es/guides/beginner-guide/"), ("Guías", "/es/guides/"), ("Códigos", "/es/codes/"), ("Actualizaciones", "/es/updates/")]),
            ("Wiki", [("Cartas", "/es/wiki/cards/"), ("Companions", "/es/wiki/companions/"), ("Avatares", "/es/wiki/avatars/"), ("Armas", "/es/wiki/weapons/"), ("Mundos", "/es/wiki/worlds/")]),
            ("Progreso", [("Energía", "/es/guides/energy/"), ("Subir de Rango", "/es/guides/rank-up/"), ("Mejoras", "/es/guides/upgrades/"), ("Ubicaciones de Jefes Secretos", "/es/guides/secret-boss-locations/"), ("Raids", "/es/guides/raids/")]),
            ("Equipo y Más", [("Accesorios", "/es/wiki/accessories/"), ("Amuletos", "/es/wiki/amulets/"), ("Recursos", "/es/wiki/resources/"), ("Trial", "/es/guides/trial/"), ("F2P", "/es/guides/f2p/")]),
        ],
        "footer_site": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Guías", "/es/guides/"), ("Códigos", "/es/codes/"), ("Actualizaciones", "/es/updates/")],
    },
}

# ============================================================
# ★ 4. 品牌(实测官方 Roblox 截图取色)
#   官方 key art 主视觉(火焰橙红 #a84818 hsl(20,75%,38%) / #a83000 hsl(17,100%,33%))+
#   场景夜空蓝(#183048/#306078)+ 稀有物品暖沙金(#f0d890)。见 README「★ 品牌色怎么定」。
# ============================================================
BRAND = {
    "color-brand": "#b8461c",        # 品牌主色:火焰橙红 hsl(18,75%,41%)
    "color-brand-strong": "#e57a2e", # 渐变亮端:灼热橙 hsl(24,78%,54%)
    "color-brand-ink": "#2b0f02",    # 按钮文字:深炭棕(压在橙红上)
    "color-accent": "#3f8fb4",       # 强调色:魔法夜空蓝 hsl(200,48%,48%)
    "color-accent-soft": "#6bb3d4",  # 浅夜空蓝 hsl(200,56%,63%)
}

# logo(内联 SVG 48×48:夜空蓝底 + 火焰,呼应官方视觉;favicon.svg/.ico 同步替换)
LOGO_SVG = ('<svg class="logo-mark" viewBox="0 0 48 48" width="36" height="36" role="img" aria-label="'
            + SITE["name"] +
            '"><rect x="2" y="2" width="44" height="44" rx="13" fill="#0e1620" stroke="#2c4056" stroke-width="1.5"></rect>'
            '<path d="M24 10 C28.5 15.5 33 20 33 27 C33 33.2 29 37 24 39 C19 37 15 33.2 15 27 C15 20 19.5 15.5 24 10Z" fill="#b8461c"></path>'
            '<path d="M24 17 C26.5 21 29.5 24.5 29.5 29 C29.5 32.8 27.2 35 24 36.2 C20.8 35 18.5 32.8 18.5 29 C18.5 24.5 21.5 21 24 17Z" fill="#e57a2e"></path>'
            '<circle cx="29.5" cy="22" r="1.3" fill="#f0d890"></circle><circle cx="19" cy="31" r="1" fill="#f0d890" opacity="0.8"></circle>'
            '<path d="M24 14 v4 M12 24 h4 M32 24 h4 M24 30 v4" stroke="#3f8fb4" stroke-width="1" opacity="0.55"></path></svg>')