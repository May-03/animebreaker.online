# -*- coding: utf-8 -*-
"""Anime Breaker (Roblox) — contenido en Español. Estructura idéntica a content_en.py
(mismos 22 paths, mismos H2, mismas FAQ por página). Términos de sistema como en el juego
(Companions, Avatars, Weapons, Raids, Trial); términos generales localizados.
Regla factual (PRD §8/§17): VERIFIED / REPORTED / OBSERVED / UNVERIFIED. Ningún valor no verificado se publica.
Última verificación: 2026-09-23.
"""
import config

G = config.SITE["name"]
DEV = config.SITE["developer"]
RPX = config.SITE["cta_url"]
LC = "2026-09-23"

PAGES = {}

# ---------- 1. Home ----------
PAGES["index.html"] = {
    "path": "index.html", "home": True,
    "title": "Anime Breaker Roblox: Códigos, Guías y Wiki",
    "meta": "Wiki y guía no oficial de Anime Breaker en Roblox: el bucle oficial, estado de códigos, guías para principiantes. Datos etiquetados, nunca inventados.",
    "pill": "Wiki de Fans · Verificación Primero",
    "tagline": "La referencia de " + G + " que separa dato verificado de rumor",
    "intro": ("Recurso de fans, no afiliado a " + DEV + ". El título oficial en Roblox aparece hoy como "
              "<strong>" + G + " [🌳CLASS TREE]</strong>. Cada mecánica lleva una etiqueta "
              "VERIFIED / REPORTED / OBSERVED, y los números que no podemos confirmar se omiten en lugar de "
              "inventarse."),
    "cta2_label": "Empezar por la Guía para Principiantes",
    "cta2_url": "/es/guides/beginner-guide/",
    "stats": [("ACTIVO", "Jugable en Roblox"), ("8", "Sistemas del bucle oficial"),
              ("4", "Tipos de dispositivo"), ("3", "Idiomas de guía")],
    "shot_alt": ["Arte oficial de " + G + " – personajes", G + " gameplay – combate",
                 G + " escenario – mundo nocturno", G + " gameplay – recompensas y mejoras"],
    "gallery_credit": ("Las imágenes provienen de la página oficial de Roblox y siguen siendo propiedad de " + DEV +
                       "; se muestran solo como referencia."),
    "sections": [
        ("h2", "¿Qué es " + G + " en Roblox?"),
        ("p", G + " es una experiencia de progresión con estética de anime en Roblox, creada por " + DEV + ". La "
              "página oficial describe un <strong>bucle impulsado por Energía</strong>: ganas Energía, abres "
              "<strong>Cartas</strong> para conseguir <strong>Companions</strong>, luchas contra enemigos por "
              "recursos, desbloqueas <strong>Avatares</strong>, <strong>Armas</strong> y objetos raros, y luego subes "
              "de <strong>Rango</strong> y haces <strong>Mejoras</strong> hasta las <strong>Raids</strong>. Esa misma "
              "página lista ordenadores, teléfonos, tablets y consolas como dispositivos compatibles."),
        ("p", "Este sitio se organiza alrededor de la siguiente decisión real del jugador: gastar o guardar Energía, "
              "subir de rango o mejorar, farmear un <a href=\"/es/guides/secret-boss-locations/\">jefe secreto</a> o "
              "empujar la <a href=\"/es/guides/progression/\">progresión</a>. Empieza por la "
              "<a href=\"/es/guides/beginner-guide/\">guía para principiantes</a>, o salta a los "
              "<a href=\"/es/codes/\">códigos</a> si solo los necesitas."),
        ("h2", "El bucle principal (descripción oficial)"),
        ("p", "La descripción oficial presenta el bucle como una cadena. Esta es su forma verificada:"),
        ("ol", [
            "<strong>Gana Energía</strong> — la Energía es la entrada del bucle; todo empieza aquí. Más: <a href=\"/es/guides/energy/\">guía de Energía</a>.",
            "<strong>Abre Cartas para conseguir Companions</strong> — es la vía oficial de adquisición. Más: <a href=\"/es/wiki/cards/\">Cartas</a> · <a href=\"/es/wiki/companions/\">Companions</a>.",
            "<strong>Lucha contra enemigos por recursos</strong> — el combate y el farmeo alimentan la economía. Más: <a href=\"/es/wiki/resources/\">Recursos</a>.",
            "<strong>Desbloquea Avatares, Armas y objetos raros</strong> — la capa de desbloqueo. Más: <a href=\"/es/wiki/avatars/\">Avatares</a> · <a href=\"/es/wiki/weapons/\">Armas</a> · <a href=\"/es/wiki/accessories/\">Accesorios</a>.",
            "<strong>Rank Up / Mejoras</strong> — el paso de poder. Más: <a href=\"/es/guides/rank-up/\">Rank Up</a> · <a href=\"/es/guides/upgrades/\">Mejoras</a>.",
            "<strong>Raids</strong> — el nivel de desafío al final del bucle. Más: <a href=\"/es/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "Estado actual (" + LC + ")"),
        ("p", "El título oficial contiene actualmente <strong>CLASS TREE</strong>, lo que apunta a una línea de "
              "actualización de clases/progresión activa — mira el <a href=\"/es/updates/\">hub de actualizaciones</a>. "
              "Los códigos son un sistema activo, y los que seguimos quedan fechados en la "
              "<a href=\"/es/codes/\">página de códigos</a>."),
        ("h2", G + " de un vistazo"),
        ("table", {"head": ["Campo", "Detalles"],
                   "rows": [
                       ["Título oficial", G + " [🌳CLASS TREE] (página de Roblox, revisado el " + LC + ")"],
                       ["Desarrollador / editor", DEV],
                       ["Plataforma", "Roblox — ordenadores, teléfonos, tablets y consolas"],
                       ["Género", "Experiencia de progresión y colección con estética de anime"],
                       ["Bucle principal", "Energía → Cartas → Companions → combate por recursos → Avatares / Armas → Rank Up / Mejoras → Raids"],
                       ["Sistemas activos", "Códigos (activos), línea de actualización marcada CLASS TREE"],
                       ["Verificación", "Cada afirmación se etiqueta VERIFIED, REPORTED, OBSERVED o UNVERIFIED"],
                   ]}),
        ("note", "Juega en la página oficial: <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX + "</a>. Códigos, "
                 "costes, tasas de drop y valores de balance cambian entre actualizaciones — este sitio los revisa y "
                 "muestra la fecha de la comprobación."),
        ("h2", "Recorrido del jugador: qué leer después"),
        ("p", "El sitio es una ruta por el bucle, no un montón de páginas. Sigue el orden o salta al paso donde estás "
              "atascado:"),
        ("ul", [
            "<strong>Paso 1 — Entiende el bucle:</strong> <a href=\"/es/guides/beginner-guide/\">Guía para Principiantes</a>",
            "<strong>Paso 2 — Resuelve tu Energía:</strong> <a href=\"/es/guides/energy/\">Energía</a> → <a href=\"/es/wiki/cards/\">Cartas</a> → <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Paso 3 — Elige poder:</strong> <a href=\"/es/guides/upgrades/\">Mejoras</a> → <a href=\"/es/guides/rank-up/\">Rank Up</a> → <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Paso 4 — Desbloquea:</strong> <a href=\"/es/wiki/avatars/\">Avatares</a> → <a href=\"/es/wiki/weapons/\">Armas</a> → <a href=\"/es/wiki/worlds/\">Mundos</a>",
            "<strong>Paso 5 — Farmea y desafía:</strong> <a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a> → <a href=\"/es/wiki/accessories/\">Accesorios</a> → <a href=\"/es/guides/raids/\">Raids</a> → <a href=\"/es/guides/trial/\">Trial</a> → <a href=\"/es/wiki/amulets/\">Amuletos</a>",
            "<strong>¿Sin Robux?</strong> <a href=\"/es/guides/f2p/\">Guía F2P</a> · <a href=\"/es/codes/\">Códigos</a>",
        ]),
        ("h2", "Sistemas principales de la wiki"),
        ("cards", [
            ("Cartas", "Cómo funcionan las Cartas y llevan a los Companions.", "/es/wiki/cards/"),
            ("Companions", "Obtención, uso y diferencia con los Avatares.", "/es/wiki/companions/"),
            ("Avatares", "Desbloqueo, crecimiento y farmeo de Avatares.", "/es/wiki/avatars/"),
            ("Armas", "Obtención y el papel de las armas.", "/es/wiki/weapons/"),
            ("Accesorios y Amuletos", "Drops de jefe y decisiones de equipo.", "/es/wiki/accessories/"),
            ("Recursos y Mundos", "Monedas, fuentes y navegación entre mundos.", "/es/wiki/resources/"),
        ]),
        ("h2", "Por qué esta wiki verifica primero"),
        ("p", "Las wikis de Roblox se copian entre sí, y los números sensibles a la versión (costes de rango, HP de "
              "jefe, tasas de drop, multiplicadores) acaban congelados en valores de lanzamiento que ya no coinciden "
              "con el cliente actual. Este sitio usa cuatro etiquetas:"),
        ("ul", [
            "<strong>VERIFIED</strong> — afirmado por la página oficial de Roblox o reproducible en el cliente actual.",
            "<strong>REPORTED</strong> — publicado por una fuente secundaria fechada (por ejemplo el snapshot de códigos del " + LC + ").",
            "<strong>OBSERVED</strong> — visto en juego en la build actual, aún en recomprobación.",
            "<strong>UNVERIFIED</strong> — afirmado en algún sitio, confirmado en ninguno. Queda listado para que lo pruebes, nunca como hecho.",
        ]),
        ("note", "Valores de alto riesgo — costes y multiplicadores de rango, HP y tasas de drop de jefes, "
                 "multiplicadores de Avatar, estadísticas de armas, estadísticas de accesorios, coste de ticket de "
                 "raid, valores de Amuleto, tasas de pull de cartas y recompensas del Trial — quedan deliberadamente "
                 "fuera sin una fuente actual."),
        ("h2", "Entra en la wiki"),
        ("cards", [
            ("Guía para Principiantes", "El bucle y tu primera sesión, paso a paso.", "/es/guides/beginner-guide/"),
            ("Códigos", "Códigos activos y expirados con la fecha de revisión.", "/es/codes/"),
            ("Hub de la Wiki", "Todos los sistemas documentados en un sitio.", "/es/wiki/"),
            ("Hub de Guías", "Guías de tareas y optimización.", "/es/guides/"),
            ("Actualizaciones", "Qué cambió y qué solo se ha detectado.", "/es/updates/"),
            ("Guía F2P", "Decisiones de progreso sin Robux.", "/es/guides/f2p/"),
        ]),
    ],
    "faq": [
        ("¿Qué es " + G + " en Roblox?", "Una experiencia de progresión con estética de anime en Roblox, de " + DEV + ". La página oficial describe un bucle impulsado por Energía: gana Energía, abre Cartas para conseguir Companions, lucha por recursos, desbloquea Avatares, Armas y objetos raros, sube de Rank y haz Mejoras hasta las Raids."),
        ("¿" + G + " es gratis?", "Corre dentro de Roblox, que es gratis de instalar. Las compras opcionales con Robux existen dentro de la experiencia y no son necesarias para seguir el bucle descrito oficialmente."),
        ("¿Qué significa CLASS TREE en el título de " + G + "?", "El título oficial aparece hoy como " + G + " [🌳CLASS TREE], lo que señala una línea activa de actualización de clases/progresión. Este sitio no inventa detalles de parche más allá de lo que muestran el título y las fuentes fechadas."),
        ("¿Dónde canjeo códigos de " + G + "?", "Los códigos se canjean dentro de la experiencia. La lista actual que seguimos, con su fecha de verificación, está en la página de códigos."),
        ("¿Hay tier list o página de mejores unidades en " + G + "?", "Todavía no, a propósito. Las tier lists congelan valores que cambian en cada actualización; mientras una fuente actual no lo respalde, publicamos marcos de decisión — mira las guías de Mejoras y Progresión."),
        ("¿Por dónde debería empezar un jugador nuevo?", "Por la guía para principiantes, luego Energía y Cartas. Esas tres cubren la parte del bucle que usa la primera sesión."),
        ("¿Por qué faltan algunos números?", "Porque un número no verificado es peor que ningún número. Costes de rango, tasas de drop, multiplicadores y HP de jefes solo aparecen cuando una fuente actual los respalda."),
    ],
    "related": [("Guía para Principiantes", "/es/guides/beginner-guide/", "Empieza tu primera sesión"),
                ("Códigos", "/es/codes/", "Estado en vivo con fecha de verificación"),
                ("Guía de Progresión", "/es/guides/progression/", "Dónde se pone difícil el bucle")],
}

# ---------- 2. Wiki hub ----------
PAGES["wiki/index.html"] = {
    "path": "wiki/index.html",
    "title": "Anime Breaker Wiki – Cartas, Companions y Avatares",
    "meta": "Hub de la wiki de Anime Breaker: Cartas, Companions, Avatares, Armas, Accesorios, Amuletos, Recursos y Mundos, con etiquetas de verificación.",
    "pill": "Wiki", "h1": G + " Wiki",
    "lead": ("La capa de referencia del sitio: cada sistema documentado, qué hace en el bucle y cuánta confianza "
             "tenemos."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/")],
    "sections": [
        ("p", "Este hub cubre los sistemas nombrados en la descripción oficial de " + G + " más las capas de equipo y "
              "de mundos que más se preguntan. Cada página indica lo que es VERIFIED, lo que es REPORTED y lo que "
              "solo es OBSERVED en el cliente actual — y cada página lleva la fecha de su última revisión."),
        ("h2", "Sistemas del bucle oficial"),
        ("table", {"head": ["Sistema", "Papel en el bucle", "Confianza"],
                   "rows": [
                       ["Energía", "Entrada: se gana, se gasta y se guarda para abrir Cartas.", "VERIFIED (página oficial)"],
                       ["Cartas", "Capa de adquisición: abrir Cartas por Companions.", "VERIFIED (página oficial)"],
                       ["Companions", "Luchan contigo y alimentan la economía de recursos.", "VERIFIED (página oficial)"],
                       ["Avatares", "Capa de desbloqueo: cambia con qué juegas.", "VERIFIED (página oficial)"],
                       ["Armas", "Capa de desbloqueo: cambian tu daño en combate.", "VERIFIED (página oficial)"],
                       ["Rank Up", "Paso de poder: sube tu cuenta en su escalera de rango.", "VERIFIED (página oficial)"],
                       ["Mejoras", "Paso de poder: gastar recursos para reforzar lo que tienes.", "VERIFIED (página oficial)"],
                       ["Raids", "Nivel de desafío al final del bucle.", "VERIFIED (página oficial)"],
                   ]}),
        ("h2", "Capas de equipo, economía y mundos"),
        ("ul", [
            "<strong><a href=\"/es/wiki/accessories/\">Accesorios</a></strong> — equipo que sale de los jefes y las decisiones alrededor.",
            "<strong><a href=\"/es/wiki/amulets/\">Amuletos</a></strong> — ranura adicional reportada en la fase de cuello de botella.",
            "<strong><a href=\"/es/wiki/resources/\">Recursos</a></strong> — las monedas y materiales que consume el bucle.",
            "<strong><a href=\"/es/wiki/worlds/\">Mundos</a></strong> — el orden de mundos usado para navegar, sin subpáginas vacías.",
        ]),
        ("h2", "Cómo trata la wiki los valores desconocidos"),
        ("p", "Las experiencias de Roblox se rebalancean en caliente, así que un valor copiado de una wiki puede "
              "estar mal la misma semana. Por eso publicamos mecánicas y lógica de decisión, y solo imprimimos "
              "números que una fuente actual respalda — la misma regla de las páginas de "
              "<a href=\"/es/wiki/avatars/\">Avatares</a> y <a href=\"/es/wiki/weapons/\">Armas</a> con "
              "multiplicadores y tablas de estadísticas."),
        ("note", "Cuando una página dice que los datos son parciales, es intencional: el sistema es real y está "
                 "documentado, y los números exactos quedan retenidos hasta verificarse. Nada se rellena con una "
                 "suposición plausible."),
    ],
    "faq": [
        ("¿Qué es la wiki de " + G + "?", "Una referencia hecha por jugadores para los sistemas y el equipo de " + G + " en Roblox, con cada afirmación etiquetada según su nivel de fuente. No afiliada a " + DEV + "."),
        ("¿Por qué faltan tablas de estadísticas de " + G + "?", "Porque el cliente puede cambiar multiplicadores, costes y tasas sin aviso. Las tablas aparecen cuando una fuente actual respalda los números."),
        ("¿Qué sistema debería leer primero?", "Energía, luego Cartas, luego Companions — es el orden en que corre el bucle oficial."),
    ],
    "related": [("Hub de Guías", "/es/guides/", "Guías de tareas y optimización"),
                ("Guía para Principiantes", "/es/guides/beginner-guide/", "El bucle en orden"),
                ("Actualizaciones", "/es/updates/", "Qué cambió y cuándo")],
}

# ---------- 3. Guides hub ----------
PAGES["guides/index.html"] = {
    "path": "guides/index.html",
    "title": "Anime Breaker Guías: Principiante, Energía y Raids",
    "meta": ("Todas las guías de " + G + ": principiantes, progresión, Energía, Rank Up, Mejoras, Jefes Secretos, "
             "Raids, Trial y la ruta F2P."),
    "pill": "Guías", "h1": G + " Guías",
    "lead": ("Cada guía responde a una decisión, en el orden en que el jugador la encuentra, desde el bucle oficial "
             "hacia fuera."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/")],
    "sections": [
        ("p", "Las guías están escritas como decisiones y no como descripciones: gastar o guardar, subir de rango o "
              "mejorar, farmear aquí o avanzar. Cada una indica sus requisitos, el paso a paso, los errores comunes "
              "y cuánto depende de la próxima actualización."),
        ("h2", "Empieza aquí"),
        ("cards", [
            ("Guía para Principiantes", "Bucle, primera sesión y errores a evitar.", "/es/guides/beginner-guide/"),
            ("Energía", "Cómo se gana, se gasta y se estira la Energía.", "/es/guides/energy/"),
            ("Progresión", "El mapa de cuellos de botella de medio y fin de juego.", "/es/guides/progression/"),
        ]),
        ("h2", "Guías de optimización"),
        ("cards", [
            ("Rank Up", "Cuándo merece la pena subir de rango — y de qué depende el coste.", "/es/guides/rank-up/"),
            ("Mejoras", "Un marco de prioridades en lugar de una tier list congelada.", "/es/guides/upgrades/"),
            ("Raids", "Acceso, oleadas, recompensas y en qué gastarlas.", "/es/guides/raids/"),
            ("Trial", "El bucle de desafío tipo pasillo y su ruta de mejoras.", "/es/guides/trial/"),
        ]),
        ("h2", "Guías de tarea y F2P"),
        ("cards", [
            ("Jefes Secretos", "Cómo se encuentran, farmean y registran los jefes.", "/es/guides/secret-boss-locations/"),
            ("Guía F2P", "Decisiones de progreso sin gastar Robux.", "/es/guides/f2p/"),
            ("Códigos", "Estado de códigos con fecha de verificación.", "/es/codes/"),
        ]),
        ("note", "Las guías se recomprueban en el cliente actual: los valores que cambian con el balance quedan "
                 "etiquetados en vez de imprimirse como constantes."),
    ],
    "faq": [
        ("¿Qué guía de " + G + " debería leer primero?", "La guía para principiantes. Después Energía y Cartas, porque la primera sesión transcurre casi entera en esa parte del bucle."),
        ("¿Las guías usan números reales?", "Solo números que respalde una fuente actual. Costes, tasas de drop y multiplicadores que cambian entre actualizaciones aparecen como lógica de decisión, no como constante congelada."),
        ("¿Hay página de mejores mejoras o mejores armas?", "No. Esas páginas caducan en un parche. La guía de Mejoras ofrece un marco de priorización aplicable a lo que tu cuenta tiene hoy."),
    ],
    "related": [("Hub de la Wiki", "/es/wiki/", "La capa de referencia"),
                ("Actualizaciones", "/es/updates/", "Sensibilidad a las actualizaciones"),
                ("Códigos", "/es/codes/", "Recursos gratis mientras duren")],
}

# ---------- 4. Codes ----------
PAGES["codes/index.html"] = {
    "path": "codes/index.html",
    "title": "Anime Breaker Códigos – Activos y Expirados",
    "meta": "Estado de los códigos de Anime Breaker en septiembre de 2026: códigos de hito y de actualización reportados activos, cómo canjear y tratar expirados.",
    "pill": "En vivo", "h1": G + " Códigos",
    "lead": ("Una página fechada, no eterna. Cada código aquí está reportado activo por una fuente fechada o "
             "tratado como expirado — y todos te piden probarlo en el juego."),
    "breadcrumb": [("Inicio", "/es/"), ("Códigos", "/es/codes/")],
    "sections": [
        ("p", "<strong>Última verificación: " + LC + "</strong>. Los códigos de " + G + " son un "
              "<strong>sistema activo</strong> (REPORTED — cobertura secundaria de códigos fechada el 2026-09-22). "
              "Esa cobertura contaba unos <strong>14 códigos activos</strong> en esa fecha, incluidos códigos de hito "
              "y de actualización. Los códigos de hito suelen retirarse cuando se alcanza la meta de la comunidad, "
              "así que trata la lista como fechada, no permanente."),
        ("h2", "Códigos reportados activos (" + LC + ")"),
        ("table", {"head": ["Código", "Estado", "Qué dice la fuente"],
                   "rows": [
                       ["10KCCU", "REPORTED activo", "Código de hito (hito de comunidad) — pruébalo en el juego; este sitio no imprime recompensas que no puede verificar."],
                       ["2MVISITS", "REPORTED activo", "Código de hito (meta de visitas)."],
                       ["20KFAVORITES", "REPORTED activo", "Código de hito (meta de favoritos)."],
                       ["NEWPORTAL", "REPORTED activo", "Código de actualización, reportado junto a una línea de portal."],
                       ["NEWSHADOW", "REPORTED activo", "Código de actualización, reportado junto a una línea de shadow."],
                   ]}),
        ("note", "Los valores de recompensa quedan en blanco a propósito: el snapshot secundario lista cadenas de "
                 "código, no recompensas detalladas, y las tablas copiadas son justo como se equivocan las páginas "
                 "de códigos. Escribe el código en el juego y lee la recompensa en la confirmación."),
        ("h2", "Códigos expirados"),
        ("p", "Los sistemas de códigos de Roblox expiran en silencio — un código que funcionaba la semana pasada "
              "puede dejar de funcionar sin anuncio. Esta página no publica una lista de expirados que no puede "
              "verificar, por la misma razón por la que no publica recompensas inventadas: una fecha de expiración no "
              "verificada es desinformación. Si un código listado falla, trátalo como expirado para tu build y mira "
              "el <a href=\"/es/updates/\">hub de actualizaciones</a>."),
        ("h2", "Cómo canjear códigos en " + G),
        ("ol", [
            "<strong>Entra en la experiencia oficial</strong> — abre " + G + " desde su página oficial de Roblox.",
            "<strong>Busca la entrada de código</strong> — las experiencias de Roblox colocan el canje en un menú, en ajustes o en un panel propio; el sitio cambia entre builds, así que usa la interfaz actual.",
            "<strong>Escribe el código exacto</strong> — los códigos de Roblox distinguen mayúsculas y caracteres; usa copiar y pegar cuando el campo lo permita.",
            "<strong>Confirma y lee la recompensa</strong> — si no se entrega nada, el código expiró o ya se canjeó en esa cuenta.",
        ]),
        ("h2", "Dónde aparecen los códigos nuevos"),
        ("ul", [
            "<strong>Códigos de hito</strong> — ligados a números de la comunidad (visitas, favoritos, jugadores simultáneos), por eso los de arriba parecen contadores.",
            "<strong>Códigos de actualización</strong> — salen junto a líneas de contenido, que es como se leen NEWPORTAL y NEWSHADOW.",
            "<strong>Ritmo de revisión</strong> — la página se refecha cada vez que se reverifica el conjunto, y las reglas de abajo muestran qué necesita un código para entrar.",
        ]),
        ("h2", "Por qué un código puede no funcionar"),
        ("ul", [
            "<strong>Expiró</strong> — la causa más común; los códigos de hito son los primeros en caer.",
            "<strong>Error de escritura</strong> — vuelve a escribirlo carácter a carácter.",
            "<strong>Ya canjeado</strong> — la mayoría de sistemas permite un canje por cuenta.",
            "<strong>Juego equivocado</strong> — títulos de anime con nombres parecidos tienen sus propios códigos; no son transferibles.",
        ]),
        ("h2", "Cómo se mantiene esta página"),
        ("ul", [
            "Un código solo entra con fuente fechada y el estado REPORTED.",
            "Las recompensas solo aparecen cuando se ven en la confirmación del propio juego.",
            "La página se reverifica como conjunto, así que la fecha de arriba siempre describe toda la tabla.",
        ]),
        ("note", "Si la tabla de arriba y una fuente más nueva no coinciden, confía en la fuente más nueva en el "
                 "juego. Esta página existe para estar fechada y ser honesta, no para ser la lista más larga de "
                 "internet."),
    ],
    "faq": [
        ("¿Hay códigos de " + G + " funcionando ahora?", "A " + LC + " una fuente secundaria fechada reportaba unos 14 códigos activos, incluidos 10KCCU, 2MVISITS, 20KFAVORITES, NEWPORTAL y NEWSHADOW. Prueba cada uno en el juego — el estado cambia más rápido que cualquier lista."),
        ("¿Qué dan los códigos de " + G + "?", "El snapshot fechado lista cadenas de código, no recompensas detalladas, así que no imprimimos valores. La confirmación dentro del juego es la respuesta autorizada."),
        ("¿Cómo canjeo códigos de " + G + "?", "Entra en la experiencia oficial, abre la entrada de código en el juego (normalmente en un menú o panel de ajustes, que cambia entre builds), escribe el código exacto y confirma."),
        ("¿Por qué un código que ayer funcionaba ya no funciona?", "Los códigos de hito se retiran al alcanzarse la meta. Un código expirado y uno mal escrito se ven igual en la interfaz — escribe de nuevo una vez y luego asume expirado."),
        ("¿Sirven códigos de otros juegos de anime?", "No. Cada experiencia tiene su propio conjunto de códigos."),
        ("¿Cada cuánto se actualiza esta página?", "Cada vez que se reverifica el conjunto. La fecha de arriba siempre describe la tabla de abajo."),
    ],
    "related": [("Actualizaciones", "/es/updates/", "A qué línea pertenecen los códigos"),
                ("Guía F2P", "/es/guides/f2p/", "Convierte recompensas gratis en progreso"),
                ("Guía para Principiantes", "/es/guides/beginner-guide/", "Qué hacer con tus primeras recompensas")],
}

# ---------- 5. Updates ----------
PAGES["updates/index.html"] = {
    "path": "updates/index.html",
    "title": "Anime Breaker Actualizaciones – Estado CLASS TREE y Cambios",
    "meta": ("Hub de actualizaciones de " + G + ": el estado actual del título CLASS TREE, qué está verificado en "
             "la página oficial y qué solo está reportado."),
    "pill": "En vivo", "h1": G + " Actualizaciones",
    "lead": ("Un hub fechado de los cambios de " + G + " — hecho para impedir que 'un registro público cambió' se "
             "convierta en 'esta función está activa'."),
    "breadcrumb": [("Inicio", "/es/"), ("Actualizaciones", "/es/updates/")],
    "sections": [
        ("p", "Revisado el <strong>" + LC + "</strong>. La página oficial muestra hoy el título como "
              "<strong>" + G + " [🌳CLASS TREE]</strong>. Esa marca es la señal de actualización más fuerte "
              "disponible sin inventar notas de parche: indica una línea activa de clases/progresión en el propio "
              "nombre del juego."),
        ("h2", "Qué está verificado ahora"),
        ("table", {"head": ["Elemento", "Estado (" + LC + ")", "Nota"],
                   "rows": [
                       ["Título oficial", "VERIFIED", G + " [🌳CLASS TREE] según la página oficial de Roblox."],
                       ["Bucle principal", "VERIFIED", "Energía → Cartas → Companions → recursos → Avatares / Armas → Rank Up / Mejoras → Raids."],
                       ["Dispositivos", "VERIFIED", "Ordenadores, teléfonos, tablets y consolas."],
                       ["Sistema de códigos", "REPORTED activo", "Cobertura secundaria del 2026-09-22 contaba unos 14 códigos activos. Mira la página de códigos."],
                   ]}),
        ("h2", "Lo que esta página no hará"),
        ("ul", [
            "<strong>Nada de notas de parche inventadas</strong> — la marca CLASS TREE no se expande a números de balance por suposición.",
            "<strong>Nada de valores de lanzamiento congelados</strong> — cuando un sistema cambia, el valor se reetiqueta en vez de mantenerse en silencio.",
            "<strong>Nada de 'detectado, luego activo'</strong> — que un registro público o una página rival cambie es una pista, no una confirmación.",
        ]),
        ("h2", "Cómo leer una actualización con este sitio"),
        ("ol", [
            "<strong>Comprueba la fecha</strong> — cada página imprime el día de su última verificación.",
            "<strong>Comprueba la etiqueta</strong> — VERIFIED, REPORTED, OBSERVED y UNVERIFIED significan cosas distintas a propósito.",
            "<strong>Vuelve a probarlo en el juego</strong> — el cliente actual vale más que cualquier página, incluida esta.",
        ]),
        ("note", "Páginas afectadas por actualizaciones: <a href=\"/es/codes/\">Códigos</a>, "
                 "<a href=\"/es/guides/rank-up/\">Rank Up</a> (costes), <a href=\"/es/guides/upgrades/\">Mejoras</a> "
                 "(prioridades), <a href=\"/es/guides/raids/\">Raids</a> (tickets y recompensas) y "
                 "<a href=\"/es/wiki/weapons/\">Armas</a> (estadísticas)."),
    ],
    "faq": [
        ("¿Cuál es la última actualización de " + G + "?", "A " + LC + " la página oficial lleva la marca CLASS TREE en el título, y el sistema de códigos está reportado activo con códigos de hito y de actualización. Ambos quedan fechados aquí, no descritos como permanentes."),
        ("¿CLASS TREE significa un sistema de clases nuevo?", "La marca forma parte del título oficial, así que una línea activa de clase/progresión es la lectura razonable. Este sitio no publica listas de funciones ni números sin fuente actual."),
        ("¿Cada cuánto se actualiza " + G + "?", "Ningún calendario público forma parte del registro verificado, así que no prometemos uno. Las páginas llevan fecha de revisión."),
        ("¿Por qué esta página es corta?", "Porque la longitud no es evidencia. Solo entran cambios con fuente fechada; el resto queda fuera hasta poder probarse."),
    ],
    "related": [("Códigos", "/es/codes/", "La página más sensible a actualizaciones"),
                ("Guía de Progresión", "/es/guides/progression/", "Replanifica tras un parche"),
                ("Rank Up", "/es/guides/rank-up/", "Los costes cambian con las actualizaciones")],
}

# ---------- 6. Beginner Guide ----------
PAGES["guides/beginner-guide/index.html"] = {
    "path": "guides/beginner-guide/index.html",
    "title": "Anime Breaker Guía para Principiantes – Cómo Jugar",
    "meta": ("Cómo jugar " + G + " en Roblox: el bucle oficial impulsado por Energía explicado paso a paso, tu "
             "primera sesión y los errores que más cuestan al principio."),
    "pill": "Guías", "h1": G + " Guía para Principiantes",
    "lead": ("Tu primera sesión mapeada sobre el bucle oficial: entra Energía, se abren Cartas, salen Companions y "
             "se gastan recursos — en el orden correcto."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Guía para Principiantes", "/es/guides/beginner-guide/")],
    "sections": [
        ("p", "La descripción oficial de " + G + " te da el bucle directamente: <strong>gana Energía → abre Cartas "
              "para conseguir Companions → lucha contra enemigos por recursos → desbloquea Avatares, Armas y objetos "
              "raros → Rank Up / Mejoras → Raids</strong>. Una guía de principiantes consiste sobre todo en no romper "
              "el orden de ese bucle."),
        ("h2", "Requisitos"),
        ("ul", [
            "<strong>Roblox instalado</strong> — " + G + " corre en ordenadores, teléfonos, tablets y consolas.",
            "<strong>La página oficial</strong> — <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX + "</a>.",
            "<strong>Motivo para leer antes</strong> — los recursos iniciales son lo más escaso que tienes; el bucle castiga el gasto aleatorio.",
        ]),
        ("h2", "Tu primera sesión, paso a paso"),
        ("ol", [
            "<strong>Aprende de dónde sale la Energía</strong> — es la entrada del bucle. Descubre cómo la gana tu cuenta antes de gastar nada. <a href=\"/es/guides/energy/\">Guía de Energía</a>",
            "<strong>Abre Cartas con criterio</strong> — las Cartas son la vía oficial a los Companions. Ábrelas por lotes, no de una en una, para ver qué le falta a tu plantilla. <a href=\"/es/wiki/cards/\">Cartas</a>",
            "<strong>Pon los Companions en combate</strong> — son los que luchan en la descripción oficial, y los recursos que ayudan a generar son la moneda de todo lo posterior. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Guarda recursos antes de gastar</strong> — Avatares, Armas, Rank Up y Mejoras beben del mismo pozo. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>Toma una decisión de progresión, no cinco</strong> — elige una mejora o un empujón de rango y termínalo. <a href=\"/es/guides/upgrades/\">Mejoras</a> · <a href=\"/es/guides/rank-up/\">Rank Up</a>",
            "<strong>Solo después mira Avatares y Armas</strong> — son la capa de desbloqueo y compensan cuando tu flujo de recursos es estable. <a href=\"/es/wiki/avatars/\">Avatares</a> · <a href=\"/es/wiki/weapons/\">Armas</a>",
        ]),
        ("h2", "Errores de principiante que más cuestan"),
        ("ul", [
            "<strong>Gastar Energía en cuanto la tienes</strong> — sin conocer tu ingreso, no distingues una buena sesión de una mala.",
            "<strong>Buscar rareza antes que flujo</strong> — un desbloqueo raro en una cuenta sin ingresos se atasca enseguida.",
            "<strong>Confiar en un número copiado</strong> — costes, multiplicadores y tasas cambian entre actualizaciones; una captura del mes pasado es un rumor.",
            "<strong>Ignorar los códigos</strong> — el sistema está activo y las recompensas gratis al principio valen más que después. <a href=\"/es/codes/\">Códigos</a>",
        ]),
        ("note", "Sensibilidad a actualizaciones: el bucle en sí está verificado por la página oficial y es estable; "
                 "los números alrededor no. Si una guía cita cantidades exactas de Energía, costes de rango o tasas "
                 "sin fecha, trátala como no verificada."),
    ],
    "faq": [
        ("¿Cómo se juega a " + G + "?", "Sigue el bucle oficial: gana Energía, abre Cartas para conseguir Companions, lucha contra enemigos por recursos, desbloquea Avatares, Armas y objetos raros, sube de Rank y haz Mejoras hasta las Raids. Los dispositivos compatibles son ordenadores, teléfonos, tablets y consolas."),
        ("¿Qué hago primero en " + G + "?", "Aprende cómo gana Energía tu cuenta, gástala en Cartas por lotes para ver qué le falta a tu plantilla, pon los Companions en combate, farmea recursos y toma una decisión de progresión por vez."),
        ("¿" + G + " es pay to win?", "El registro verificado describe un bucle de progresión dentro de la experiencia, no un bucle de compras. Existen compras opcionales con Robux en muchas experiencias, pero este sitio no publica afirmaciones de compra que no puede verificar — la guía F2P cubre jugar sin ellas."),
        ("¿Cuánto tarda el primer Companion?", "No imprimimos tiempos: dependen de tu ingreso de Energía y del pool de Cartas, que cambian entre actualizaciones. La página de Cartas explica la mecánica."),
        ("¿Cuál es el mayor error de principiante?", "Repartir los recursos iniciales entre Avatares, Armas, Mejoras y Rank Up a la vez. Guarda primero y luego comprométete con un camino."),
    ],
    "related": [("Energía", "/es/guides/energy/", "La entrada del bucle"),
                ("Cartas", "/es/wiki/cards/", "Cómo se consiguen los Companions"),
                ("Mejoras", "/es/guides/upgrades/", "Tu primera decisión real")],
}

# ---------- 7. Progression ----------
PAGES["guides/progression/index.html"] = {
    "path": "guides/progression/index.html",
    "title": "Anime Breaker Guía de Progresión – Inicio a Fin",
    "meta": ("Guía de progresión de " + G + " como mapa de cuellos de botella: qué te limita al principio, en el "
             "medio y al final, y qué decisión mueve la pared."),
    "pill": "Guías", "h1": G + " Guía de Progresión",
    "lead": ("No es una lista de niveles — es un mapa de qué te está frenando de verdad en cada fase y qué palanca "
             "lo mueve."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Progresión", "/es/guides/progression/")],
    "sections": [
        ("p", "La progresión en " + G + " corre sobre el bucle oficial: la Energía alimenta las Cartas, las Cartas "
              "producen Companions, los Companions y el combate producen recursos, los recursos se convierten en "
              "Avatares, Armas, Rank y Mejoras, y ese resultado se prueba en las Raids. Cuando la progresión se "
              "atasca, el atasco está siempre en un eslabón concreto — y la solución rara vez es 'jugar más'."),
        ("h2", "Fase 1 — inicio: cuello de flujo"),
        ("ul", [
            "<strong>Síntoma:</strong> siempre te quedas sin Energía o sin el recurso del siguiente paso.",
            "<strong>Problema real:</strong> la tasa de ingreso, no la rareza. Un desbloqueo raro en una cuenta lenta sigue siendo lento.",
            "<strong>Palanca:</strong> revisa primero cómo se gana y se gasta la Energía. <a href=\"/es/guides/energy/\">Energía</a> → <a href=\"/es/wiki/cards/\">Cartas</a>",
        ]),
        ("h2", "Fase 2 — medio: cuello de compromiso"),
        ("ul", [
            "<strong>Síntoma:</strong> varios sistemas a medias, nada lo bastante fuerte para avanzar.",
            "<strong>Problema real:</strong> recursos repartidos entre Rank Up, Mejoras, Avatares y Armas a la vez.",
            "<strong>Palanca:</strong> elige una línea y termínala. <a href=\"/es/guides/upgrades/\">Mejoras</a> · <a href=\"/es/guides/rank-up/\">Rank Up</a>",
        ]),
        ("h2", "Fase 3 — final: cuello de techo"),
        ("ul", [
            "<strong>Síntoma:</strong> el contenido normal es cómodo, pero ciertos desafíos son paredes.",
            "<strong>Problema real:</strong> huecos de equipo y rareza — accesorios, amuletos y armas deciden el techo, no las horas jugadas.",
            "<strong>Palanca:</strong> apunta a la fuente del drop a propósito. <a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a> → <a href=\"/es/wiki/accessories/\">Accesorios</a> → <a href=\"/es/wiki/amulets/\">Amuletos</a> → <a href=\"/es/guides/raids/\">Raids</a>",
        ]),
        ("h2", "La regla de decisión que sobrevive a cada actualización"),
        ("ol", [
            "<strong>Nombra la pared en una frase</strong> — 'no puedo terminar este desafío' o 'me quedo sin Energía'.",
            "<strong>Asóciala a un eslabón del bucle</strong> — Energía, Cartas, Companions, recursos, desbloqueo, poder, desafío.",
            "<strong>Gasta solo en ese eslabón</strong> — el resto espera. Esto es lo que mantiene avanzando una cuenta de medio juego tras un rebalanceo.",
        ]),
        ("note", "Deliberadamente ausente: umbrales numéricos de progresión, costes de rango, puntos de ruptura de "
                 "multiplicadores y tasas de drop. Esos valores cambian entre actualizaciones y el bucle de arriba no "
                 "depende de ellos."),
    ],
    "faq": [
        ("¿Cómo progresar rápido en " + G + "?", "Resuelve el eslabón que te bloquea. Al principio es el ingreso de Energía; en el medio son compromisos inacabados repartidos entre demasiados sistemas; al final son techos de equipo y rareza."),
        ("¿Cuál es la forma más rápida de hacerse fuerte en " + G + "?", "Termina una línea antes de abrir otra — un empujón de rango o de mejoras. Repartir recursos es la forma más fiable de seguir débil."),
        ("¿" + G + " tiene límite de nivel?", "Ningún límite verificado forma parte del registro oficial. Las escaleras de rango y los multiplicadores son valores que se mueven entre builds, así que no imprimimos uno."),
        ("¿Cuándo empezar las Raids?", "Cuando tu problema de techo sea el desafío y no los recursos — ahí el acceso y las recompensas de raid valen más que otra ruta de farmeo."),
    ],
    "related": [("Rank Up", "/es/guides/rank-up/", "El paso de poder"),
                ("Jefes Secretos", "/es/guides/secret-boss-locations/", "Donde se rompe el techo"),
                ("Raids", "/es/guides/raids/", "El nivel de desafío")],
}

# ---------- 8. Energy ----------
PAGES["guides/energy/index.html"] = {
    "path": "guides/energy/index.html",
    "title": G + " Energía – Cómo Conseguirla, Usarla y Estirarla",
    "meta": ("Energía en " + G + ": la entrada del bucle oficial. Cómo se gana, en qué se gasta y cómo dejar de "
             "desperdiciarla — sin inventar tasas ni límites."),
    "pill": "Guías", "h1": G + " Energía",
    "lead": ("La Energía es el primer eslabón del bucle oficial. Esta guía cubre qué hace, cómo se gasta y cómo leer "
             "tu propio ingreso."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Energía", "/es/guides/energy/")],
    "sections": [
        ("p", "La descripción oficial de " + G + " abre con la Energía: <strong>ganas Energía</strong>, y la Energía "
              "es lo que te permite <strong>abrir Cartas para conseguir Companions</strong>. Todo lo demás en el "
              "juego es consecuencia de esa primera conversión."),
        ("h2", "Qué hace la Energía"),
        ("ul", [
            "<strong>Controla la capa de Cartas</strong> — las Cartas son la vía oficial a los Companions, y la Energía es lo que se gasta para abrirlas. <a href=\"/es/wiki/cards/\">Cartas</a>",
            "<strong>Marca el ritmo de la sesión</strong> — al ser un recurso de gastar y esperar, la calidad de tu sesión depende de cómo lo gastas, no de cuánto tiempo juegas.",
            "<strong>Se convierte en todo lo demás</strong> — los Companions generan el combate y el farmeo que se vuelven recursos. <a href=\"/es/wiki/companions/\">Companions</a> · <a href=\"/es/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Cómo ganar Energía"),
        ("p", "El registro oficial establece la Energía como entrada del bucle; no publica una tasa. En lugar de "
              "copiar una tasa de otra wiki, mide la tuya:"),
        ("ol", [
            "<strong>Anota tu Energía antes de la sesión</strong> — número y hora.",
            "<strong>Juega con normalidad una ventana fija</strong> — mismo contenido, mismo patrón de gasto.",
            "<strong>Anótala otra vez</strong> — la diferencia es tu ingreso real en esa ventana, en la build actual.",
            "<strong>Vuelve a medir tras una actualización grande</strong> — las fuentes de ingreso son justo el tipo de valor que cambian.",
        ]),
        ("note", "Este hábito de medición es el truco completo. Las tasas publicadas se quedan viejas en un ciclo de "
                 "parche; tu medición de dos puntos no."),
        ("h2", "Cómo gastar bien la Energía"),
        ("ul", [
            "<strong>Gasta por lotes, no a sorbos</strong> — abrir Cartas en lote muestra qué le falta a tu plantilla antes de comprometerte. <a href=\"/es/wiki/cards/\">Cartas</a>",
            "<strong>No gastes para 'salvar' una mala sesión</strong> — si una sesión no dio nada útil, la respuesta es el siguiente lote, no más gasto.",
            "<strong>Sepa qué no compra la Energía</strong> — Rank Up, Mejoras, Avatares, Armas y Raids usan recursos y progresión. <a href=\"/es/guides/rank-up/\">Rank Up</a>",
            "<strong>Sigue tu conversión</strong> — Energía que entra, Companions o recursos útiles que salen. Esa razón es la única métrica que importa al principio.",
        ]),
        ("h2", "Energía y la ruta gratuita"),
        ("p", "En una cuenta sin Robux, el ritmo de la Energía es tu palanca principal: las recompensas de código y "
              "las sesiones diarias constantes importan más que cualquier compra grande. La "
              "<a href=\"/es/guides/f2p/\">guía F2P</a> cubre el resto de la ruta, y la "
              "<a href=\"/es/codes/\">página de códigos</a> sigue las recompensas que podemos fechar."),
        ("note", "No publicamos límites de Energía, tasas de regeneración, costes de recarga ni tasas de pull: "
                 "ninguna fuente actual lo respalda, y cambian. Si necesitas un número, mide como arriba."),
    ],
    "faq": [
        ("¿Cómo se consigue Energía en " + G + "?", "La Energía es la entrada del bucle oficial — la ganas y la gastas para abrir Cartas. El registro oficial no publica tasa, así que mide tu propio ingreso en una ventana fija."),
        ("¿En qué se gasta la Energía en " + G + "?", "En abrir Cartas. Las Cartas son la vía oficial a los Companions, y los Companions generan el combate y los recursos que financian todo lo demás."),
        ("¿La Energía es igual que un sistema de stamina?", "Funcionalmente marca el ritmo de la sesión como un recurso de stamina, y la descripción oficial la trata como entrada del bucle. Los límites y la regeneración exactos no se publican aquí porque no están verificados."),
        ("¿Y si desperdicio Energía?", "No puedes deshacer el gasto, pero sí cambiar el patrón: gastar por lotes, medir entrada frente a salida útil y volver a medir tras las actualizaciones en vez de seguir una guía vieja."),
    ],
    "related": [("Cartas", "/es/wiki/cards/", "A dónde va la Energía"),
                ("Guía para Principiantes", "/es/guides/beginner-guide/", "El orden de la primera sesión"),
                ("Guía F2P", "/es/guides/f2p/", "Ritmo de Energía sin Robux")],
}

# ---------- 9. Rank Up ----------
PAGES["guides/rank-up/index.html"] = {
    "path": "guides/rank-up/index.html",
    "title": G + " Rank Up – Cuándo Subir y De Qué Depende",
    "meta": ("Rank Up en " + G + ": qué incluye el bucle oficial, cuándo merece la pena un empujón de rango y por "
             "qué no publicamos tabla de costes ni multiplicadores."),
    "pill": "Guías", "h1": G + " Rank Up",
    "lead": ("Subir de rango es uno de los dos pasos de poder del bucle oficial. Esta guía va del momento correcto — "
             "y de ser honestos con que sus costes dependen de la versión."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Rank Up", "/es/guides/rank-up/")],
    "sections": [
        ("p", "El bucle oficial de " + G + " incluye <strong>Rank Up</strong> como paso diferenciado, después de "
              "desbloquear Avatares, Armas y objetos raros. Esa colocación importa: subir de rango es un paso de "
              "poder que haces cuando tu economía lo soporta, no un objetivo del primer día."),
        ("h2", "Para qué sirve el rango"),
        ("ul", [
            "<strong>Es un paso de poder, no un sistema lateral</strong> — el bucle oficial lo coloca junto a las mejoras, tras la capa de desbloqueo.",
            "<strong>Compite por los mismos recursos</strong> que <a href=\"/es/guides/upgrades/\">Mejoras</a>, <a href=\"/es/wiki/avatars/\">Avatares</a> y <a href=\"/es/wiki/weapons/\">Armas</a> — por eso el momento lo es todo.",
            "<strong>Depende de la versión</strong> — las escaleras de rango se rebalancean, así que los costes y multiplicadores se recomprueban en vez de memorizarse.",
        ]),
        ("h2", "Cuándo merece la pena subir de rango"),
        ("ol", [
            "<strong>Tu ingreso es estable</strong> — sabes más o menos cuánto recurso ganas por sesión. <a href=\"/es/guides/energy/\">Energía</a>",
            "<strong>Tu plantilla no es la pared</strong> — si las luchas fallan por lo que tienes, el equipo y los Companions van primero. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Puedes absorber el siguiente nivel de coste</strong> — subir de rango adelanta coste; si el siguiente nivel te atasca, cambiaste una subida lenta por un frenazo.",
            "<strong>No estás a medias de una línea de mejoras</strong> — termínala. Las líneas abandonadas son el clásico sumidero de medio juego. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
        ]),
        ("h2", "Cuándo esperar"),
        ("ul", [
            "<strong>Justo después de una actualización grande</strong> — la línea actual marcada CLASS TREE es justo el tipo de cambio que mueve el valor de clase y rango. <a href=\"/es/updates/\">Actualizaciones</a>",
            "<strong>Cuando hay una oleada de códigos activa</strong> — las recompensas gratis cambian cuánto necesitas farmear. <a href=\"/es/codes/\">Códigos</a>",
            "<strong>Cuando tu cuello es un desafío, no una estadística</strong> — eso es un problema de equipo; ve a <a href=\"/es/guides/secret-boss-locations/\">farmeo de jefes</a> o <a href=\"/es/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "Lo que no publicamos sobre el rango"),
        ("p", "Tablas de coste de rango, multiplicadores por rango, valores de requisito y el número exacto de rangos "
              "quedan retenidos a propósito. Varias páginas secundarias no coinciden en esos números, y una "
              "discrepancia es una pista, no un hecho. Cuando una fuente actual pueda respaldarlo, esta página ganará "
              "una tabla fechada — hasta entonces sigue siendo una guía de decisión."),
        ("note", "Si solo te llevas una cosa de esta página: sube de rango cuando tu economía pueda cargar el "
                 "siguiente nivel, no cuando aparezca el botón."),
    ],
    "faq": [
        ("¿Cuándo subir de rango en " + G + "?", "Cuando tu ingreso sea estable, tu plantilla no sea lo que falla y puedas absorber el siguiente nivel de coste. Si una línea de mejoras o equipo está a medias, termínala antes."),
        ("¿Cuánto cuesta subir de rango en " + G + "?", "Aquí no se publica ninguna tabla de costes verificada. Las fuentes secundarias no coinciden y los costes cambian con las actualizaciones. Trata cualquier tabla sin fecha como no verificada."),
        ("¿Subir de rango hace más fuerte que mejorar?", "El bucle oficial trata Rank Up y Mejoras como dos pasos de poder que compiten por los mismos recursos. Cuál compensa más depende de tu cuello actual."),
        ("¿Debería subir de rango justo tras una actualización?", "Normalmente espera. Las actualizaciones — la actual va marcada CLASS TREE — son justo cuando se mueven los valores de clase y rango."),
    ],
    "related": [("Mejoras", "/es/guides/upgrades/", "El otro paso de poder"),
                ("Guía de Progresión", "/es/guides/progression/", "Qué pared atacar"),
                ("Actualizaciones", "/es/updates/", "Por qué se mueven los valores")],
}

# ---------- 10. Upgrades ----------
PAGES["guides/upgrades/index.html"] = {
    "path": "guides/upgrades/index.html",
    "title": "Anime Breaker Mejoras – Marco de Prioridades",
    "meta": ("Las mejores mejoras de " + G + " como marco de priorización en lugar de tier list congelada: qué "
             "alimentar primero, qué aparcar y por qué el orden cambia."),
    "pill": "Guías", "h1": G + " Mejoras",
    "lead": ("Un marco de prioridades aplicable a tu cuenta ahora mismo — porque la 'mejor mejora' en una "
             "experiencia de Roblox es un objetivo móvil."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Mejoras", "/es/guides/upgrades/")],
    "sections": [
        ("p", "Las Mejoras son el segundo paso de poder del bucle oficial de " + G + ", junto a Rank Up y después de "
              "la capa de desbloqueo. Mucha gente busca 'mejores mejoras' esperando una lista ordenada; la respuesta "
              "honesta es que una lista correcta esta semana falla tras el siguiente rebalanceo. Así que aquí va la "
              "lógica de decisión."),
        ("h2", "La prueba de prioridad, en orden"),
        ("ol", [
            "<strong>¿Qué está fallando?</strong> Nombra el contenido concreto que no puedes superar. Una mejora que no cambia ese resultado no es prioridad, sea cual sea su rareza.",
            "<strong>¿Qué eslabón es más débil?</strong> Daño (luchas y farmeo), supervivencia o flujo de recursos. Alimenta el más débil. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>¿Qué compone?</strong> Entre dos opciones, elige la que acelere tus próximas sesiones — normalmente la que mejora tu ruta de farmeo.",
            "<strong>¿Qué es más barato por paso?</strong> Las curvas de coste difieren; una línea barata que terminas gana a una cara que abandonas. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>¿Qué sobrevive a la siguiente actualización?</strong> Las mejoras ligadas al núcleo del bucle (Companions, armas que usas) mantienen valor entre parches.",
        ]),
        ("h2", "Qué mejorar primero como principiante"),
        ("ul", [
            "<strong>Tu configuración de farmeo</strong> — todo lo que suba el recurso producido por sesión. <a href=\"/es/guides/energy/\">Energía</a>",
            "<strong>Tu línea principal de Companion</strong> — son los que entran en combate en el bucle oficial. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Un arma que sigas usando después</strong> — repartir mejoras entre muchas armas es el desperdicio inicial más común. <a href=\"/es/wiki/weapons/\">Armas</a>",
        ]),
        ("h2", "Qué aparcar"),
        ("ul", [
            "<strong>Cualquier cosa comprada para un evento único</strong> — salvo que ese evento sea tu pared actual.",
            "<strong>Segunda y tercera línea de arma</strong> — hasta que la primera supere el contenido que te atasca.",
            "<strong>Desbloqueos cosméticos</strong> — no mueven el bucle. Los <a href=\"/es/wiki/avatars/\">Avatares</a> merecen desbloquearse, pero no al precio de una línea de ataque atascada.",
        ]),
        ("h2", "Por qué no hay tabla ordenada de 'mejores mejoras'"),
        ("p", "Porque una tabla ordenada exige números por nivel, y ninguna fuente actual publica un conjunto "
              "consistente para esta build. Las páginas secundarias se contradicen en multiplicadores y costes. "
              "Publicar un ranking seguro sobre fuentes que discrepan sería inventar un hecho, así que esta página te "
              "da el marco y fecha su propia revisión."),
        ("note", "Sensibilidad: tras un parche de balance, repite la prueba de prioridad desde el paso uno. Tu "
                 "eslabón más débil puede haber cambiado aunque tu cuenta no."),
    ],
    "faq": [
        ("¿Cuáles son las mejores mejoras en " + G + "?", "Las que resuelven tu cuello actual: producción de farmeo primero en la mayoría de cuentas, luego una línea de Companion y luego una línea de arma. Un ranking estático quedaría mal tras el siguiente rebalanceo."),
        ("¿Mejoro o subo de rango primero en " + G + "?", "Ambos son pasos de poder que comparten recursos. Mejora cuando tu ingreso sea estable; sube de rango cuando tu economía pueda cargar el siguiente nivel de coste. Termina una línea antes de abrir la otra."),
        ("¿Merece la pena mejorar muchas armas?", "No, no al principio. Una línea de arma que funciona gana a tres inacabadas, y los valores de arma son justo lo que cambian las actualizaciones."),
        ("¿Cada cuánto cambian las prioridades en " + G + "?", "Cada vez que el juego se rebalancea — la línea actual va marcada CLASS TREE. Revisa tras cada actualización grande."),
    ],
    "related": [("Rank Up", "/es/guides/rank-up/", "El momento del otro paso de poder"),
                ("Recursos", "/es/wiki/resources/", "Lo que consumen las mejoras"),
                ("Armas", "/es/wiki/weapons/", "En qué línea comprometerte")],
}

# ---------- 11. Cards ----------
PAGES["wiki/cards/index.html"] = {
    "path": "wiki/cards/index.html",
    "title": "Anime Breaker Cartas – Cómo Desbloquear Companions",
    "meta": ("Cartas en " + G + ": la capa oficial de adquisición. Qué hacen, cómo se conectan a la Energía y a los "
             "Companions, y por qué no publicamos tasas de pull."),
    "pill": "Wiki", "h1": G + " Cartas",
    "lead": ("Las Cartas son el puente oficial entre Energía y Companions — la capa de adquisición del bucle."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Cartas", "/es/wiki/cards/")],
    "sections": [
        ("p", "En la descripción oficial de " + G + " el bucle dice: gana Energía y luego <strong>abre Cartas para "
              "conseguir Companions</strong>. Así que las Cartas no son un coleccionable lateral — son el mecanismo "
              "que convierte tu Energía en la plantilla con la que luchas."),
        ("h2", "Qué hacen las Cartas"),
        ("table", {"head": ["Pregunta", "Respuesta", "Confianza"],
                   "rows": [
                       ["¿Para qué sirven?", "Abrir Cartas es la vía oficial de conseguir Companions.", "VERIFIED (página oficial)"],
                       ["¿Cuánto cuestan?", "Son el lado de gasto del paso de Energía — la Energía es lo que se gana primero.", "VERIFIED (página oficial)"],
                       ["¿Cómo se abren?", "Dentro de la experiencia; la interfaz cambia entre builds, usa la actual.", "OBSERVED"],
                       ["¿Cuáles son las tasas de pull?", "No se publican aquí — ninguna fuente actual respalda una tabla de tasas.", "UNVERIFIED"],
                   ]}),
        ("h2", "Las Cartas en el bucle"),
        ("ol", [
            "<strong>Gana Energía</strong> — la entrada del bucle. <a href=\"/es/guides/energy/\">Energía</a>",
            "<strong>Abre Cartas</strong> — gasta Energía; es la vía oficial a nuevos Companions.",
            "<strong>Pon los Companions en combate</strong> — lo que sale de las Cartas es lo que lucha por ti. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Convierte el combate en recursos</strong> — lo que financia todos los pasos siguientes. <a href=\"/es/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Cómo abrir Cartas con criterio"),
        ("ul", [
            "<strong>Abre por lotes</strong> — un conjunto de resultados muestra qué le falta a tu plantilla; un pull suelto no muestra casi nada.",
            "<strong>Juzga la plantilla, no el pull</strong> — un lote lleno de repetidos solo es problema si no mejora tu ruta de farmeo.",
            "<strong>No persigas tasas que no ves</strong> — si un sitio cita porcentajes sin fuente ni fecha, trátalos como una suposición.",
        ]),
        ("note", "Deliberadamente ausente de esta página: tasas de pull, tablas de rareza, número de cartas y "
                 "probabilidades de Companions concretos. Esos números cambian con las actualizaciones y discrepan "
                 "entre fuentes secundarias."),
    ],
    "faq": [
        ("¿Qué son las Cartas en " + G + "?", "La capa oficial de adquisición del bucle. Ganas Energía, abres Cartas, y las Cartas son cómo consigues Companions para luchar."),
        ("¿Cómo se consiguen Cartas en " + G + "?", "Las Cartas están ligadas al paso de Energía en la descripción oficial — la Energía es el primer recurso del bucle, y abrir Cartas es en lo que se gasta."),
        ("¿Cuáles son las tasas de pull en " + G + "?", "No se publican aquí. Ninguna fuente actual respalda una tabla consistente, y las tasas son justo lo que cambian las actualizaciones. Abre por lotes y juzga la plantilla."),
        ("¿Importan los repetidos?", "Pueden importar, pero la prueba útil es si el lote mejoró tu ruta de farmeo o la cobertura de plantilla — no cuántos repetidos aparecieron."),
    ],
    "related": [("Companions", "/es/wiki/companions/", "Lo que dan las Cartas"),
                ("Energía", "/es/guides/energy/", "El recurso que consumen las Cartas"),
                ("Guía para Principiantes", "/es/guides/beginner-guide/", "Cartas en tu primera sesión")],
}

# ---------- 12. Companions ----------
PAGES["wiki/companions/index.html"] = {
    "path": "wiki/companions/index.html",
    "title": "Anime Breaker Companions – Cómo Conseguirlos",
    "meta": ("Companions en " + G + ": cómo los produce el bucle oficial vía Cartas, cómo se usan en combate y en "
             "qué se diferencian de los Avatares."),
    "pill": "Wiki", "h1": G + " Companions",
    "lead": ("Los Companions son la salida de combate del bucle oficial — lo que sale de las Cartas y lo que pones "
             "en el campo."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Companions", "/es/wiki/companions/")],
    "sections": [
        ("p", "En el bucle oficial de " + G + " <strong>abres Cartas para conseguir Companions</strong> y luego "
              "<strong>luchas contra enemigos por recursos</strong>. Los Companions están entre esos dos pasos: son "
              "el resultado de tu gasto de Energía y lo que sostiene tu combate y tu farmeo."),
        ("h2", "Cómo consigues Companions"),
        ("ol", [
            "<strong>Gana Energía</strong> — la entrada del bucle. <a href=\"/es/guides/energy/\">Energía</a>",
            "<strong>Abre Cartas</strong> — la vía oficial de adquisición. <a href=\"/es/wiki/cards/\">Cartas</a>",
            "<strong>Ponlos en el campo</strong> — en la descripción del bucle ya son utilizables en combate.",
            "<strong>Mejora el conjunto con el tiempo</strong> — mejoras y desbloqueos suben tu producción. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
        ]),
        ("h2", "Companion vs Avatar"),
        ("table", {"head": ["Aspecto", "Companions", "Avatares"],
                   "rows": [
                       ["Papel en el bucle", "Se obtienen vía Cartas y se usan para luchar y farmear.", "Se listan como desbloqueo junto a Armas y objetos raros."],
                       ["Cómo se obtienen", "Abriendo Cartas (oficial).", "Se desbloquean por progresión; fuentes de la comunidad citan rutas de farmeo adicionales que este sitio no ha verificado."],
                       ["Qué cambian", "Tu producción de combate y farmeo.", "Con qué juegas, por eso se tratan como capa de colección e identidad además de poder."],
                       ["Confianza", "VERIFIED (página oficial)", "VERIFIED para el desbloqueo; PARTIAL para las mecánicas"],
                   ]}),
        ("h2", "Usar bien los Companions"),
        ("ul", [
            "<strong>Cubre tus huecos</strong> — un lote de Cartas suele dejar agujeros; cubre roles que te faltan en lugar de apilar lo que ya tienes.",
            "<strong>Alimenta los que se quedan</strong> — una mejora gastada en un Companion que vas a cambiar es el desperdicio más común. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Encaja con el contenido</strong> — las rutas de farmeo y los desafíos premian perfiles distintos; mantén un conjunto de farmeo y otro de lucha. <a href=\"/es/guides/progression/\">Progresión</a>",
        ]),
        ("note", "Multiplicadores de Companion, tier lists y tasas de pull no se publican aquí: ninguna fuente actual "
                 "respalda un conjunto consistente, y 'mejor Companion' cambia en cada rebalanceo. La página de "
                 "<a href=\"/es/wiki/avatars/\">Avatares</a> sigue la misma regla."),
    ],
    "faq": [
        ("¿Qué son los Companions en " + G + "?", "Las unidades que consigues abriendo Cartas en el bucle oficial, y lo que pones en el campo para luchar y ganar recursos."),
        ("¿Cómo se consiguen Companions en " + G + "?", "Abriendo Cartas. La descripción oficial coloca las Cartas justo antes de los Companions, y la Energía es lo que se gasta para abrirlas."),
        ("¿Cuál es la diferencia entre Companion y Avatar en " + G + "?", "Los Companions son tu plantilla, se consiguen con Cartas y se usan en combate. Los Avatares son un desbloqueo del mismo bucle oficial y funcionan más como capa de identidad y progresión."),
        ("¿Cuál es el mejor Companion en " + G + "?", "Aquí no se publica ninguna tier list. 'Mejor' sigue al parche actual y al contenido que juegas, así que la pregunta útil es qué rol le falta a tu plantilla."),
    ],
    "related": [("Cartas", "/es/wiki/cards/", "De dónde salen los Companions"),
                ("Avatares", "/es/wiki/avatars/", "La otra capa de desbloqueo"),
                ("Mejoras", "/es/guides/upgrades/", "En cuáles invertir")],
}

# ---------- 13. Avatars ----------
PAGES["wiki/avatars/index.html"] = {
    "path": "wiki/avatars/index.html",
    "title": G + " Avatares – Desbloqueo, Crecimiento y Farmeo",
    "meta": ("Avatares en " + G + ": la capa oficial de desbloqueo. Cómo se desbloquean y crecen, qué reporta la "
             "comunidad sobre farmearlos y qué valores quedan fuera."),
    "pill": "Wiki", "h1": G + " Avatares",
    "lead": ("Los Avatares son la capa de desbloqueo del bucle — con qué juegas y la colección que más se farmea."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Avatares", "/es/wiki/avatars/")],
    "sections": [
        ("p", "El bucle oficial de " + G + " dice que <strong>desbloqueas Avatares, Armas y objetos raros</strong> "
              "cuando tus luchas ya producen recursos. Los Avatares quedan por tanto en medio del bucle: no son lo "
              "primero con lo que empiezas, pero tampoco algo que ignorar."),
        ("h2", "Desbloquear Avatares"),
        ("ol", [
            "<strong>Construye primero tu flujo de recursos</strong> — la capa de desbloqueo se financia con combate y farmeo. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>Sigue la ruta de desbloqueo</strong> — en la descripción oficial, los Avatares se ganan con la progresión dentro de la experiencia.",
            "<strong>Espera una colección, no una elección</strong> — el bucle habla de Avatares en plural, así que montar un conjunto es la intención.",
        ]),
        ("h2", "Crecimiento y uso de Avatares"),
        ("ul", [
            "<strong>Trata cada Avatar como su propia línea</strong> — invertir por completo en uno gana a repartir entre varios. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Mantén un Avatar de farmeo y uno de lucha</strong> — los roles rara vez coinciden. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Prueba antes de comprometerte</strong> — con los balances, el Avatar fuerte del parche pasado puede no serlo tras el siguiente. <a href=\"/es/updates/\">Actualizaciones</a>",
        ]),
        ("h2", "Rutas de farmeo reportadas por la comunidad"),
        ("p", "Las páginas secundarias describen rutas de obtención de Avatares con luchas repetidas contra conjuntos "
              "concretos de NPC, y algunas listan roles y niveles máximos <em>estimados</em>. Son pistas de "
              "descubrimiento: las estimaciones vienen de cobertura de terceros, no coinciden entre sí y están "
              "fechadas. Esta página no las repite como hechos."),
        ("note", "Fuera a propósito: multiplicadores de Avatar, probabilidades exactas de drop o desbloqueo, valores "
                 "de nivel máximo y rankings por Avatar. Cada uno depende de la versión y es inconsistente entre "
                 "fuentes. La <a href=\"/es/guides/secret-boss-locations/\">caza de jefes</a> se cubre aparte, "
                 "incluidos los valores que nos negamos a congelar allí."),
    ],
    "faq": [
        ("¿Cómo se consiguen Avatares en " + G + "?", "Son la capa de desbloqueo del bucle oficial: cuando tus luchas producen recursos, los Avatares, Armas y objetos raros se vuelven alcanzables por la progresión dentro de la experiencia."),
        ("¿Se pueden subir de nivel los Avatares en " + G + "?", "Los Avatares crecen como parte de la capa de progresión, y las mejoras son uno de los dos pasos de poder del bucle oficial. Los valores por nivel no se publican aquí porque cambian entre actualizaciones."),
        ("¿Cómo se farmean Avatares en " + G + "?", "Fuentes de la comunidad describen luchas repetidas contra NPC como ruta de farmeo. Eso es REPORTED, no verificado, y las probabilidades que se citan al lado son estimaciones — así que esta página describe el enfoque, no números inventados."),
        ("¿Cuál es el Avatar más fuerte en " + G + "?", "Aquí no se publica ningún ranking. Los multiplicadores discrepan entre fuentes y se mueven con los parches, así que el consejo honesto es: elige una línea, termínala y reevalúa tras una actualización."),
    ],
    "related": [("Companions", "/es/wiki/companions/", "Companion vs Avatar comparados"),
                ("Energía", "/es/guides/energy/", "Financiar la capa de desbloqueo"),
                ("Armas", "/es/wiki/weapons/", "El otro desbloqueo del bucle")],
}

# ---------- 14. Weapons ----------
PAGES["wiki/weapons/index.html"] = {
    "path": "wiki/weapons/index.html",
    "title": G + " Armas – Obtención y Papel en el Bucle",
    "meta": ("Armas en " + G + ": cómo las desbloquea el bucle oficial, cómo elegir en cuál comprometerte y por qué "
             "no publicamos tabla de estadísticas."),
    "pill": "Wiki", "h1": G + " Armas",
    "lead": ("Las Armas son la segunda mitad de la capa oficial de desbloqueo — y donde los novatos más recursos "
             "desperdician en líneas inacabadas."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Armas", "/es/wiki/weapons/")],
    "sections": [
        ("p", "El bucle oficial dice que <strong>desbloqueas Avatares, Armas y objetos raros</strong> cuando el "
              "combate ya produce recursos. Las Armas quedan por tanto detrás de la misma economía que los Avatares: "
              "gana primero, desbloquea después."),
        ("h2", "Cómo encajan las Armas"),
        ("table", {"head": ["Pregunta", "Respuesta", "Confianza"],
                   "rows": [
                       ["¿Están en el bucle oficial?", "Sí — nombradas en el paso de desbloqueo junto a Avatares y objetos raros.", "VERIFIED (página oficial)"],
                       ["¿Cómo se obtienen?", "Por la progresión dentro de la experiencia; fuentes de la comunidad también reportan rutas ligadas a jefes.", "PARTIAL (oficial en el bucle, REPORTED en los vínculos con jefes)"],
                       ["¿Qué cambian?", "Tu producción de combate — que alimenta el paso de recursos.", "OBSERVED"],
                       ["¿Se publican tablas de estadísticas?", "No. Daño, escalado y costes de mejora dependen de la versión y son inconsistentes entre fuentes.", "UNVERIFIED"],
                   ]}),
        ("h2", "Elegir una línea de arma"),
        ("ol", [
            "<strong>Elige una</strong> — comprométete con una sola línea hasta superar el contenido que te atasca. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Mira la fuente, no la captura</strong> — un ranking de armas sin fecha es un rumor; las armas se rebalancean. <a href=\"/es/updates/\">Actualizaciones</a>",
            "<strong>Encájala con tu ruta</strong> — un arma que acelera el farmeo se paga antes que una que gana una sola lucha. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Luego persigue el drop raro</strong> — los jefes y desafíos guardan los objetos que rompen el techo. <a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a> · <a href=\"/es/guides/raids/\">Raids</a>",
        ]),
        ("h2", "Armas, jefes y raids"),
        ("p", "La cobertura secundaria liga las armas de nivel alto al contenido de jefes y raids. Este sitio lo "
              "mantiene como vínculo REPORTED, no como tabla fija: <a href=\"/es/wiki/accessories/\">Accesorios</a> "
              "cubre lo que podemos decir sobre drops de jefes, y <a href=\"/es/guides/raids/\">Raids</a> cubre el "
              "nivel de desafío."),
        ("note", "Fuera a propósito: valores de daño, curvas de escalado, tablas de coste de mejora y rankings de "
                 "tier. Los cuatro son justo los campos que se rompen cuando el cliente se rebalancea."),
    ],
    "faq": [
        ("¿Cómo se consiguen Armas en " + G + "?", "Las Armas están en la capa oficial de desbloqueo del bucle: cuando tus luchas producen recursos, Armas, Avatares y objetos raros se vuelven alcanzables por la progresión."),
        ("¿Cuál es la mejor arma en " + G + "?", "Aquí no se publica ningún ranking. Los valores de arma se mueven con los parches y discrepan entre fuentes, así que la regla útil es comprometerse con una línea y revisar tras cada actualización."),
        ("¿Los jefes sueltan armas en " + G + "?", "Fuentes secundarias reportan rutas de armas y equipo ligadas a jefes. Eso es REPORTED, no verificado, así que describimos la ruta sin imprimir tasas."),
        ("¿Mejoro armas o Avatares primero?", "Lo que resuelva tu pared actual. Si las luchas fallan por daño, mejora la línea de arma; si no alcanzas el contenido, el desbloqueo y el farmeo van primero."),
    ],
    "related": [("Jefes Secretos", "/es/guides/secret-boss-locations/", "Dónde están los drops raros"),
                ("Accesorios", "/es/wiki/accessories/", "Equipo que sale de jefes"),
                ("Mejoras", "/es/guides/upgrades/", "Comprometerte con una línea")],
}

# ---------- 15. Secret Boss Locations ----------
PAGES["guides/secret-boss-locations/index.html"] = {
    "path": "guides/secret-boss-locations/index.html",
    "title": "Anime Breaker Jefes Secretos – Cómo Encontrarlos",
    "meta": ("Jefes secretos en " + G + ": cómo abordarlos, para qué sirve farmearlos y por qué ningún HP ni tasa de "
             "drop se congela en esta página."),
    "pill": "Guías", "h1": G + " Jefes Secretos",
    "lead": ("Una guía de encontrar y farmear basada en el enfoque y el propósito — no en HP congelado ni "
             "probabilidades copiadas."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Jefes Secretos", "/es/guides/secret-boss-locations/")],
    "sections": [
        ("p", "Cazar jefes es como los jugadores rompen el techo de fin de juego en " + G + ": el bucle oficial te "
              "manda luchar contra enemigos por recursos y desbloquear objetos raros, y la cobertura de la comunidad "
              "trata a los jefes secretos como la versión concentrada de ese paso. La diferencia entre una buena "
              "ruta de jefes y una mala es la puntería, no la suerte."),
        ("h2", "Para qué sirven los jefes secretos"),
        ("ul", [
            "<strong>Farmeo concentrado</strong> — un objetivo en lugar de una ruta, por eso los jugadores de fin de juego gastan sesiones en ellos.",
            "<strong>Drops que rompen el techo</strong> — la capa de equipo y objetos raros que mantiene la progresión. <a href=\"/es/wiki/accessories/\">Accesorios</a>",
            "<strong>Una puerta al nivel de desafío</strong> — lo que farmeas alimenta las <a href=\"/es/guides/raids/\">Raids</a> y el bucle del <a href=\"/es/guides/trial/\">Trial</a>.",
        ]),
        ("h2", "Encontrar jefes: el método honesto"),
        ("ol", [
            "<strong>Avanza hasta que el mundo se abra</strong> — el acceso a jefes está limitado por la progresión. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Explora el mundo actual, no una captura antigua</strong> — los diseños y zonas de aparición cambian entre actualizaciones. <a href=\"/es/wiki/worlds/\">Mundos</a>",
            "<strong>Vigila la línea de actualización</strong> — la marca CLASS TREE señala una línea activa, y es cuando se mueve el contenido de jefes. <a href=\"/es/updates/\">Actualizaciones</a>",
            "<strong>Registra lo que encuentres</strong> — tu propia nota fechada vale más que una lista de coordenadas copiada.",
        ]),
        ("h2", "Cómo farmear un jefe con eficiencia"),
        ("ul", [
            "<strong>Lleva un conjunto de farmeo, no de escaparate</strong> — repetir importa más que una victoria lucida. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Corrige la ruta antes que las estadísticas</strong> — si una limpieza tarda demasiado, el cuello suele ser el enfoque, no tu daño.",
            "<strong>Para cuando el drop deje de pagar</strong> — cuando tengas la mejora que buscabas, el siguiente objetivo está en otro sitio.",
        ]),
        ("h2", "Lo que esta página no publica"),
        ("p", "Valores de HP de jefes, temporizadores de aparición o reaparición, porcentajes exactos de drop y "
              "listas de coordenadas copiadas de otras wikis. Las páginas secundarias citan esos números y no "
              "coinciden entre sí — una discrepancia no es una fuente. Cuando los valores puedan verificarse en el "
              "cliente actual, entrarán aquí con fecha; hasta entonces, el método de arriba es la parte duradera."),
        ("note", "La misma regla aplica a <a href=\"/es/wiki/accessories/\">Accesorios</a>, que cubre para qué "
                 "sirven los drops de jefes en lugar de prometer una tabla."),
    ],
    "faq": [
        ("¿Dónde están los jefes secretos en " + G + "?", "El acceso está limitado por la progresión y el diseño de los mundos cambia entre actualizaciones, así que no publicamos una lista de coordenadas congelada. El método: avanza, explora el mundo actual, vigila la actualización y registra lo que encuentres."),
        ("¿Cómo se farmean jefes en " + G + "?", "Usa un conjunto de farmeo repetible en vez de escaparate, corrige la ruta de enfoque antes del daño y pasa al siguiente objetivo cuando consigas la mejora buscada."),
        ("¿Qué sueltan los jefes en " + G + "?", "Los jefes son la fuente reportada de equipo y objetos raros que rompen el techo de fin de juego, alimentando Accesorios y Raids. Las tasas exactas no se imprimen a propósito."),
        ("¿Cambian las posiciones de los jefes tras las actualizaciones?", "Asume que sí. Las experiencias de Roblox reformulan mundos entre actualizaciones, y el título actual lleva la marca CLASS TREE — justo cuando se mueve este tipo de contenido."),
    ],
    "related": [("Accesorios", "/es/wiki/accessories/", "Para qué se farmean los jefes"),
                ("Mundos", "/es/wiki/worlds/", "Dónde estás cazando"),
                ("Raids", "/es/guides/raids/", "El nivel después de los jefes")],
}

# ---------- 16. Accessories ----------
PAGES["wiki/accessories/index.html"] = {
    "path": "wiki/accessories/index.html",
    "title": "Anime Breaker Accesorios – Drops de Jefes",
    "meta": ("Accesorios en " + G + ": la capa de equipo que sale de los jefes, cómo decidir qué conservar y "
             "mejorar, y por qué las tasas y estadísticas quedan fuera."),
    "pill": "Wiki", "h1": G + " Accesorios",
    "lead": ("Los Accesorios son la capa de equipo que sale del farmeo de jefes — y donde las cuentas de fin de "
             "juego gastan sus recursos."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Accesorios", "/es/wiki/accessories/")],
    "sections": [
        ("p", "El bucle oficial de " + G + " cierra el paso de desbloqueo con <strong>objetos raros</strong> y te "
              "manda a las Raids; la cobertura de la comunidad coloca los accesorios exactamente en esa banda, "
              "provenientes de las luchas de jefes descritas en la página de "
              "<a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a>."),
        ("h2", "De dónde vienen los accesorios"),
        ("table", {"head": ["Fuente", "Estado", "Nota"],
                   "rows": [
                       ["Drops de jefes", "REPORTED", "La cobertura secundaria liga los accesorios al farmeo de jefes; se trata como la banda que rompe techos de fin de juego."],
                       ["Paso de objetos raros", "VERIFIED (página oficial)", "El bucle oficial nombra objetos raros en la capa de desbloqueo junto a Avatares y Armas."],
                       ["Recompensas de raid", "REPORTED", "El contenido de raid está verificado como nivel de desafío; el contenido concreto de sus recompensas no se publica aquí."],
                   ]}),
        ("h2", "Decidir qué conservar y mejorar"),
        ("ol", [
            "<strong>Pregunta qué resuelve</strong> — un accesorio que no cambia una lucha que pierdes es una pieza de colección por ahora. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Prefiere lo que compone</strong> — el equipo que acelera el farmeo se paga en todas las sesiones futuras.",
            "<strong>Mejora una ranura por completo</strong> — repartir recursos entre accesorios es la versión de fin de juego del error de principiante. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Revisa tras las actualizaciones</strong> — los valores de equipo están entre los primeros en rebalancearse. <a href=\"/es/updates/\">Actualizaciones</a>",
        ]),
        ("h2", "Accesorios, amuletos y armas"),
        ("ul", [
            "<strong><a href=\"/es/wiki/amulets/\">Amuletos</a></strong> — una ranura de equipo adicional reportada en las mismas fases de cuello, con la misma regla: nada de nombres o valores inventados.",
            "<strong><a href=\"/es/wiki/weapons/\">Armas</a></strong> — la mitad de daño de la capa de equipo.",
            "<strong><a href=\"/es/guides/raids/\">Raids</a></strong> — donde se prueba lo que montaste.",
        ]),
        ("note", "Fuera a propósito: tasas de drop de accesorios, valores por objeto, tablas de coste de mejora y "
                 "listas de mejor de la ranura. Los cuatro dependen de la versión y son inconsistentes entre "
                 "fuentes."),
    ],
    "faq": [
        ("¿Qué son los accesorios en " + G + "?", "La capa de equipo que va junto a los objetos raros nombrados en el paso oficial de desbloqueo, y que la cobertura de la comunidad origina en el farmeo de jefes."),
        ("¿Cómo se consiguen accesorios en " + G + "?", "Las rutas reportadas son drops de jefes y la capa de progresión de objetos raros; el contenido de raid está verificado como nivel de desafío, pero el contenido de sus recompensas no se publica aquí."),
        ("¿Qué accesorio es el mejor en " + G + "?", "No se publica ninguna lista de mejor de la ranura. La prueba práctica es si el accesorio cambia una lucha que pierdes hoy — si no, es una pieza de colección."),
        ("¿Mejoro accesorios o armas primero?", "Resuelve la pared actual: los problemas de daño apuntan a las armas, los de techo al equipo. Comprométete con una ranura por vez."),
    ],
    "related": [("Jefes Secretos", "/es/guides/secret-boss-locations/", "De dónde vienen los drops"),
                ("Amuletos", "/es/wiki/amulets/", "La siguiente ranura de equipo"),
                ("Raids", "/es/guides/raids/", "Probar lo que montaste")],
}

# ---------- 17. Raids ----------
PAGES["guides/raids/index.html"] = {
    "path": "guides/raids/index.html",
    "title": "Anime Breaker Raids – Acceso, Oleadas y Recompensas",
    "meta": "Raids en Anime Breaker: el nivel de desafío del bucle oficial. Acceso y oleadas, cómo tratar las recompensas y por qué los costes de ticket quedan fuera.",
    "pill": "Guías", "h1": G + " Raids",
    "lead": ("Las Raids son donde termina el bucle — el punto en que todo lo que farmeaste se prueba a la vez."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Raids", "/es/guides/raids/")],
    "sections": [
        ("p", "Las Raids se nombran explícitamente en el bucle oficial de " + G + ", tras los pasos de poder. Ese "
              "orden es el mensaje: las raids no son un punto de entrada, son el nivel al que tu cuenta se gradúa."),
        ("h2", "Cómo encajan las raids en el bucle"),
        ("ol", [
            "<strong>Gradúate del farmeo</strong> — necesitas un bucle de recursos estable antes de que el acceso tenga sentido. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Lleva tu conjunto real</strong> — Companions, Armas, Avatares y equipo importan aquí como no lo hacen en el farmeo normal. <a href=\"/es/wiki/companions/\">Companions</a>",
            "<strong>Lee la estructura de oleadas</strong> — la cobertura de la comunidad describe raids por oleadas; cada oleada es un punto de control de lo que le falta a tu cuenta. <a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a>",
            "<strong>Gasta las recompensas con criterio</strong> — lo que sale de una raid debe alimentar la pared que te frenó. <a href=\"/es/wiki/accessories/\">Accesorios</a>",
        ]),
        ("h2", "Acceso, tickets y coste"),
        ("p", "Fuentes de la comunidad describen el acceso a las raids limitado por la progresión y por un coste de "
              "entrada tipo consumible. Este sitio lo trata como estructura REPORTED y no imprime precios de ticket, "
              "número de oleadas ni tablas de recompensas — son de los valores más rebalanceados en una experiencia "
              "de Roblox, y las fuentes secundarias no coinciden."),
        ("h2", "Planificar tus primeras raids"),
        ("ul", [
            "<strong>Arregla la oleada que falla, no la raid entera</strong> — identifica la oleada que termina tu intento y qué exige.",
            "<strong>Mantén una ruta de farmeo al lado</strong> — las raids consumen recursos además de darlos. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>No lo cambies todo a la vez</strong> — un cambio por intento te dice qué funcionó. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Sigue la línea de actualización</strong> — el ajuste de raids se mueve con las actualizaciones. <a href=\"/es/updates/\">Actualizaciones</a>",
        ]),
        ("note", "Capas relacionadas: <a href=\"/es/wiki/amulets/\">Amuletos</a> y "
                 "<a href=\"/es/wiki/resources/\">Recursos</a> para lo que las raids consumen y devuelven, y "
                 "<a href=\"/es/guides/trial/\">Trial</a> para el otro bucle de desafío."),
    ],
    "faq": [
        ("¿Cómo se desbloquean las raids en " + G + "?", "Las raids están al final del bucle oficial, tras tus pasos de poder. En la práctica: un bucle de recursos estable y un conjunto capaz de superar contenido de desafío antes de que el acceso compense."),
        ("¿Cuántas oleadas tienen las raids de " + G + "?", "La cobertura de la comunidad describe raids por oleadas, pero el número exacto no se publica aquí — cambia con las actualizaciones y las fuentes discrepan."),
        ("¿Las raids cuestan tickets en " + G + "?", "Se reporta un coste de entrada tipo consumible. No se imprime ningún precio aquí por el mismo motivo: es un valor que se rebalancea a menudo."),
        ("¿En qué gasto las recompensas de raid?", "En la pared que te frenó. Si una oleada concreta terminó tu intento, alimenta la solución de esa oleada en lugar del siguiente desbloqueo."),
    ],
    "related": [("Amuletos", "/es/wiki/amulets/", "Una ranura de equipo cercana a raids"),
                ("Recursos", "/es/wiki/resources/", "Lo que consumen las raids"),
                ("Trial", "/es/guides/trial/", "El otro bucle de desafío")],
}

# ---------- 18. Trial ----------
PAGES["guides/trial/index.html"] = {
    "path": "guides/trial/index.html",
    "title": G + " Trial (Pasillo) – Bucle, Mejoras y Recompensas",
    "meta": ("El bucle de desafío Trial / pasillo en " + G + ": cómo funciona la estructura de la carrera, para qué "
             "sirve y cómo convertir sus recompensas en progreso."),
    "pill": "Guías", "h1": G + " Trial",
    "lead": ("El Trial (a menudo llamado pasillo) es un bucle de desafío repetible — una prueba medible de lo que has "
             "construido."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("Trial", "/es/guides/trial/")],
    "sections": [
        ("p", "La cobertura de la comunidad trata el Trial como una carrera tipo pasillo: avanzas por encuentros "
              "repetidos y la carrera termina cuando tu configuración falla. Esa estructura lo convierte en el "
              "diagnóstico más limpio del juego — la carrera muestra exactamente qué eslabón del bucle es más débil."),
        ("h2", "Cómo funciona el bucle del Trial"),
        ("ol", [
            "<strong>Entra y avanza</strong> — cada encuentro es un punto de control y no una única lucha de jefe.",
            "<strong>Anota dónde termina la carrera</strong> — el encuentro que falla nombra tu cuello de botella. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Mejora solo el eslabón que falló</strong> — un cambio y vuelve a correr. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Convierte las recompensas en el siguiente avance</strong> — la salida del Trial alimenta progresión. <a href=\"/es/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Para qué sirve el Trial"),
        ("ul", [
            "<strong>Diagnosticar builds</strong> — una carrera aísla lo que le falta a tu cuenta mejor que el farmeo abierto.",
            "<strong>Financiar mejoras de forma repetible</strong> — reportado como fuente de recursos de progresión.",
            "<strong>Puente hacia las raids</strong> — la presión por oleadas de las <a href=\"/es/guides/raids/\">Raids</a> es más fácil cuando sobrevives a acumulaciones tipo Trial.",
        ]),
        ("h2", "Reportado vs verificado en esta página"),
        ("table", {"head": ["Elemento", "Estado"],
                   "rows": [
                       ["El Trial/pasillo existe como bucle de desafío repetible", "REPORTED (cobertura secundaria de gameplay)"],
                       ["Estructura de carrera por oleadas/acumulación", "REPORTED"],
                       ["Tablas exactas de recompensa y costes por carrera", "No publicadas aquí — dependen de la versión y son inconsistentes"],
                       ["Posición en el bucle (nivel de desafío junto a Raids)", "VERIFIED (la página oficial nombra Raids; el Trial se documenta aquí como el bucle adyacente)"],
                   ]}),
        ("note", "Como en <a href=\"/es/wiki/accessories/\">Accesorios</a> y <a href=\"/es/wiki/amulets/\">Amuletos</a>, "
                 "la mecánica está documentada y los números no. Un valor de Trial correcto esta semana puede estar "
                 "mal tras la siguiente actualización."),
    ],
    "faq": [
        ("¿Qué es el Trial en " + G + "?", "Un bucle de desafío repetible tipo pasillo, reportado por la cobertura de la comunidad. Avanzas por encuentros acumulados hasta que tu configuración falla, lo que lo hace un buen diagnóstico."),
        ("¿Cómo se consiguen recompensas del Trial?", "Reportado como fuente de recursos de progresión: avanzas hasta donde tu configuración permite y conviertes la salida en mejoras para el eslabón que falló."),
        ("¿El Trial es lo mismo que las raids en " + G + "?", "No. Las raids se nombran en el bucle oficial como nivel de desafío; el Trial es un bucle separado y reportado, que comparte la presión por oleadas y combina bien con la preparación de raids."),
        ("¿Por qué faltan números del Trial?", "Porque se rebalancean y las fuentes discrepan. Esta página documenta el bucle y la lógica de decisión en lugar de congelar un valor."),
    ],
    "related": [("Recursos", "/es/wiki/resources/", "En qué se convierten las recompensas"),
                ("Raids", "/es/guides/raids/", "El nivel para el que te prepara"),
                ("Guía de Progresión", "/es/guides/progression/", "Leer la oleada que falla")],
}

# ---------- 19. Amulets ----------
PAGES["wiki/amulets/index.html"] = {
    "path": "wiki/amulets/index.html",
    "title": "Anime Breaker Amuletos – Obtención y Uso",
    "meta": "Amuletos en Anime Breaker: la ranura de equipo de la fase de cuello de botella — para qué sirve, cómo decidir y por qué no se publican nombres ni stats.",
    "pill": "Wiki", "h1": G + " Amuletos",
    "lead": ("Los Amuletos son la decisión de equipo que los jugadores buscan cuando las mejoras normales dejan de "
             "mover la pared."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Amuletos", "/es/wiki/amulets/")],
    "sections": [
        ("p", "Los Amuletos aparecen en la cobertura de la comunidad como una capa de equipo adicional que importa en "
              "el cuello de botella de fin de juego — el punto en que tu cuenta está cómoda en contenido normal pero "
              "ciertos desafíos, las <a href=\"/es/guides/raids/\">Raids</a> y el "
              "<a href=\"/es/guides/trial/\">Trial</a>, siguen terminando tus intentos. Esta página documenta la "
              "decisión, no una tier list copiada."),
        ("h2", "Cuándo un amuleto es la respuesta correcta"),
        ("ul", [
            "<strong>Tu básico está hecho</strong> — armas, una línea de Companion y una ruta de farmeo funcionando. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Pierdes contra la misma pared repetidamente</strong> — un fallo repetible indica un hueco de estadística, no mala suerte. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Una mejora cambiaría ese resultado</strong> — si no lo haría, el amuleto es una pieza de colección por ahora.",
        ]),
        ("h2", "Cómo abordar la obtención de amuletos"),
        ("ol", [
            "<strong>Identifica primero el requisito</strong> — sabe qué desafío falla antes de farmear la respuesta. <a href=\"/es/guides/secret-boss-locations/\">Jefes Secretos</a>",
            "<strong>Farmea una ruta, no un rumor</strong> — elige una fuente repetible y cronométrala, en lugar de confiar en una tabla de probabilidades sin fecha.",
            "<strong>Comprométete con uno</strong> — repartir la inversión entre varios amuletos repite el error clásico de medio juego con mayor coste. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>Revisa tras las actualizaciones</strong> — las bandas de equipo se retocan, y el título actual lleva la marca CLASS TREE. <a href=\"/es/updates/\">Actualizaciones</a>",
        ]),
        ("h2", "Por qué esta página no tiene lista de amuletos"),
        ("p", "Nombres, valores, orígenes y costes de mejora de amuletos están entre los datos peor documentados de "
              "la cobertura secundaria actual — sitios distintos listan objetos distintos y ninguno fecha sus "
              "tablas. Bajo la regla de este sitio, una discrepancia es una pista y no un hecho, así que la lista "
              "queda fuera hasta que una fuente actual la respalde."),
        ("note", "El mismo estándar se aplica a la banda de equipo: <a href=\"/es/wiki/accessories/\">Accesorios</a>, "
                 "<a href=\"/es/wiki/weapons/\">Armas</a> y <a href=\"/es/guides/raids/\">Raids</a> documentan "
                 "mecánicas y decisiones dejando fuera los números rebalanceados."),
    ],
    "faq": [
        ("¿Qué son los amuletos en " + G + "?", "Una capa de equipo adicional reportada, que importa en el cuello de botella de fin de juego — la fase en que el contenido normal es cómodo pero ciertos desafíos siguen terminando tus intentos."),
        ("¿Cómo se consiguen amuletos en " + G + "?", "La cobertura de la comunidad describe obtención ligada a jefes y desafíos. Este sitio lo trata como ruta reportada y no imprime tasas ni orígenes de objetos concretos."),
        ("¿Farmeo amuletos o mejoras primero?", "Mejoras y tu equipo central primero. Un amuleto compensa cuando un fallo repetible ya te ha mostrado qué te falta."),
        ("¿Por qué no hay tier list de amuletos?", "Porque las fuentes actuales discrepan sobre los objetos y ninguna fecha sus tablas. Publicar una sería congelar un valor que el cliente puede contradecir."),
    ],
    "related": [("Accesorios", "/es/wiki/accessories/", "La capa de equipo de al lado"),
                ("Raids", "/es/guides/raids/", "Donde se prueba"),
                ("Recursos", "/es/wiki/resources/", "Lo que cuesta el farmeo de equipo")],
}

# ---------- 20. Resources ----------
PAGES["wiki/resources/index.html"] = {
    "path": "wiki/resources/index.html",
    "title": G + " Recursos – Monedas, Fuentes y En Qué Gastar",
    "meta": ("Recursos en " + G + ": la economía detrás del bucle oficial — de dónde salen, qué compran y cómo "
             "dejar de filtrarlos."),
    "pill": "Wiki", "h1": G + " Recursos",
    "lead": ("Los recursos son en lo que se convierte todo el bucle — y la forma más rápida de perder progreso es "
             "gastarlos en el eslabón equivocado."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Recursos", "/es/wiki/resources/")],
    "sections": [
        ("p", "El bucle oficial de " + G + " dice explícitamente que <strong>luchas contra enemigos por "
              "recursos</strong>. Esos recursos financian la capa de desbloqueo (Avatares, Armas, objetos raros) y "
              "los pasos de poder (Rank Up, Mejoras), antes de que la cuenta entera se pruebe en las Raids. Toda "
              "pregunta sobre recursos es, por tanto, una pregunta de orden de gasto."),
        ("h2", "Fuente → uso → gasto"),
        ("table", {"head": ["Etapa", "Qué ocurre", "Dónde se cubre"],
                   "rows": [
                       ["Fuente", "El combate y el farmeo producen recursos, impulsados por Energía → Cartas → Companions.", "Energía · Cartas · Companions"],
                       ["Uso", "Los recursos financian desbloqueos y pasos de poder: Avatares, Armas, Rank Up, Mejoras.", "Avatares · Armas · Rank Up · Mejoras"],
                       ["Prueba de gasto", "¿Resuelve la pared que estás golpeando?", "Progresión"],
                       ["Techo", "El equipo y los niveles de desafío suben el techo: jefes, accesorios, amuletos, raids, trial.", "Jefes Secretos · Accesorios · Amuletos · Raids · Trial"],
                   ]}),
        ("h2", "Cómo se filtran los recursos"),
        ("ul", [
            "<strong>Compromisos paralelos</strong> — financiar un empujón de rango y una línea de mejoras a la vez es el mayor sumidero de una cuenta de medio juego. <a href=\"/es/guides/rank-up/\">Rank Up</a>",
            "<strong>Gasto de moda</strong> — perseguir lo que un vídeo llamó mejor sin fuente fechada. <a href=\"/es/updates/\">Actualizaciones</a>",
            "<strong>Farmear sin objetivo</strong> — las sesiones que producen recursos pero ninguna decisión no producen progreso.",
            "<strong>Ignorar fuentes gratis</strong> — el sistema de códigos está activo y los recursos gratis al principio valen más. <a href=\"/es/codes/\">Códigos</a>",
        ]),
        ("h2", "La regla de gasto"),
        ("ol", [
            "<strong>Guarda primero</strong> — mantén un colchón dimensionado para la siguiente decisión, no a cero.",
            "<strong>Una línea por vez</strong> — termina lo que empezaste antes de abrir un segundo frente.",
            "<strong>Vuelve a medir tras las actualizaciones</strong> — costes e ingresos se mueven; una regla del mes pasado puede ya no aplicar. <a href=\"/es/guides/progression/\">Progresión</a>",
        ]),
        ("note", "Aquí no se publica ninguna cantidad de moneda, rendimiento por sesión, tabla de costes ni tasa de "
                 "cambio. El ingreso de Energía, los costes de rango y de mejora dependen de la versión, y esta "
                 "página documenta la forma de la economía en lugar de congelar sus números."),
    ],
    "faq": [
        ("¿Qué son los recursos en " + G + "?", "La salida del paso de combate y farmeo del bucle oficial — el pozo que financia Avatares, Armas, objetos raros, Rank Up y Mejoras antes de la prueba en las Raids."),
        ("¿Cómo se consiguen recursos en " + G + "?", "Luchando contra enemigos, como describe el bucle oficial. En la práctica: una cadena Energía → Cartas → Companions funcionando y una ruta de farmeo repetible."),
        ("¿En qué gasto recursos primero en " + G + "?", "En lo que resuelva la pared actual — normalmente producción de farmeo al principio y una línea comprometida de mejora o rango después. Repartir recursos entre líneas paralelas es el error más común."),
        ("¿Cuánto de cada recurso necesito?", "Aquí no se publican cantidades, porque costes e ingresos se rebalancean entre actualizaciones. Guarda un colchón dimensionado para tu siguiente decisión."),
    ],
    "related": [("Trial", "/es/guides/trial/", "Una fuente repetible de recursos"),
                ("Rank Up", "/es/guides/rank-up/", "Un gran sumidero de recursos"),
                ("Guía F2P", "/es/guides/f2p/", "Disciplina de recursos sin Robux")],
}

# ---------- 21. Worlds ----------
PAGES["wiki/worlds/index.html"] = {
    "path": "wiki/worlds/index.html",
    "title": G + " Mundos – Orden de Mundos y Navegación",
    "meta": ("Mundos en " + G + ": cómo el orden funciona como escalera de progresión y cómo navegar de cada mundo "
             "a los sistemas, jefes y raids que alimenta."),
    "pill": "Wiki", "h1": G + " Mundos",
    "lead": ("Los mundos son la capa de mapa del bucle — una escalera de paradas de progresión, no un conjunto de "
             "subpáginas vacías."),
    "breadcrumb": [("Inicio", "/es/"), ("Wiki", "/es/wiki/"), ("Mundos", "/es/wiki/worlds/")],
    "sections": [
        ("p", "En " + G + " el mundo en el que estás te dice qué debería estar haciendo tu cuenta: farmear, "
              "desbloquear o empujar un desafío. La cobertura de la comunidad documenta varios mundos con dificultad "
              "creciente, y el título actual lleva la marca CLASS TREE — el tipo de cambio que reorganiza el "
              "contenido de los mundos."),
        ("h2", "Cómo usar el orden de mundos"),
        ("ol", [
            "<strong>Trata los mundos como puertas</strong> — si un mundo parece imposible, tu cuello está un eslabón atrás en el bucle. <a href=\"/es/guides/progression/\">Progresión</a>",
            "<strong>Farmea en el mundo que limpias más rápido</strong> — la velocidad gana al prestigio en producción de recursos. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>Desbloquea hacia delante, farmea hacia atrás</strong> — avanza para desbloquear y mantén una ruta repetible donde limpias con seguridad. <a href=\"/es/wiki/avatars/\">Avatares</a>",
            "<strong>Reexplora tras las actualizaciones</strong> — los diseños y las posiciones de jefes cambian entre builds. <a href=\"/es/updates/\">Actualizaciones</a>",
        ]),
        ("h2", "Navegación desde aquí"),
        ("cards", [
            ("Jefes Secretos", "Cómo se encuentran y farmean los jefes en el mundo actual.", "/es/guides/secret-boss-locations/"),
            ("Accesorios", "Para qué sirve farmear jefes en mundos avanzados.", "/es/wiki/accessories/"),
            ("Raids", "El nivel de desafío que prueba el mundo alcanzado.", "/es/guides/raids/"),
            ("Trial", "El bucle de desafío repetible fuera de la escalera de mundos.", "/es/guides/trial/"),
            ("Armas", "Desbloqueos que pasan entre mundos.", "/es/wiki/weapons/"),
            ("Recursos", "Lo que produce el farmeo de cada mundo.", "/es/wiki/resources/"),
        ]),
        ("note", "Esta página no crea una subpágina por mundo a propósito. Una página que solo cambia el nombre del "
                 "mundo no aporta decisión — la información útil es el orden, el cuello de botella y lo que alimenta "
                 "cada mundo, que es lo que se documenta aquí. Los nombres de mundos, límites y tablas por mundo "
                 "quedan fuera hasta que una fuente actual los respalde."),
    ],
    "faq": [
        ("¿Cuántos mundos hay en " + G + "?", "La cobertura de la comunidad documenta varios mundos con dificultad creciente, y el conteo es de las cosas que cambian las actualizaciones. Este sitio no publica un conteo sin fecha."),
        ("¿Cuál es el orden de los mundos en " + G + "?", "El orden es de dificultad creciente, y cada mundo actúa como puerta: si uno parece imposible, la solución suele estar un eslabón atrás en el bucle."),
        ("¿Debería farmear en el mundo más nuevo que desbloqueé?", "No necesariamente. Las limpiezas rápidas producen más que las lentas, así que muchos jugadores desbloquean hacia delante y farmean hacia atrás."),
        ("¿Por qué no hay página por mundo en " + G + "?", "Porque una página que solo cambia el nombre del mundo no aporta nada. Esta página documenta la escalera, la lógica del cuello y los enlaces a jefes, raids y sistemas."),
    ],
    "related": [("Jefes Secretos", "/es/guides/secret-boss-locations/", "Jefes por zona de mundo"),
                ("Guía de Progresión", "/es/guides/progression/", "En qué puerta estás atascado"),
                ("Actualizaciones", "/es/updates/", "El contenido de mundos se mueve con las actualizaciones")],
}

# ---------- 22. F2P ----------
PAGES["guides/f2p/index.html"] = {
    "path": "guides/f2p/index.html",
    "title": G + " Guía F2P – Progresar Sin Robux",
    "meta": "Guía F2P de Anime Breaker: progresar sin gastar Robux, dónde ayudan de verdad las recompensas gratis y qué hábitos mantienen la cuenta avanzando.",
    "pill": "Guías", "h1": G + " Guía F2P",
    "lead": ("Las cuentas gratuitas no son cuentas más lentas — son cuentas que no pueden permitirse un mal orden de "
             "gasto."),
    "breadcrumb": [("Inicio", "/es/"), ("Guías", "/es/guides/"), ("F2P", "/es/guides/f2p/")],
    "sections": [
        ("p", "El bucle oficial de " + G + " es de progresión, no de compras: Energía → Cartas → Companions → "
              "recursos → desbloqueos → Rank Up / Mejoras → Raids. Nada de esa cadena se describe como de pago. Lo "
              "que le falta a una cuenta gratuita es tolerancia a recursos desperdiciados."),
        ("h2", "Las reglas F2P que de verdad importan"),
        ("ol", [
            "<strong>Nunca gastes sin un objetivo nombrado</strong> — las cuentas gratuitas no pueden forzar un error. <a href=\"/es/wiki/resources/\">Recursos</a>",
            "<strong>Toma toda recompensa gratis fechada</strong> — el sistema de códigos está activo y es la inyección de recursos más barata disponible. <a href=\"/es/codes/\">Códigos</a>",
            "<strong>Mide tu ingreso de Energía</strong> — una medición de dos puntos gana a cualquier tasa copiada. <a href=\"/es/guides/energy/\">Energía</a>",
            "<strong>Comprométete con una línea</strong> — una línea de Companion, una de arma y luego un paso de poder. <a href=\"/es/guides/upgrades/\">Mejoras</a>",
            "<strong>Farmea donde limpias rápido</strong> — la calidad de la ruta es el principal multiplicador del jugador gratuito. <a href=\"/es/wiki/worlds/\">Mundos</a>",
        ]),
        ("h2", "Dónde se atascan las cuentas gratuitas"),
        ("ul", [
            "<strong>Huecos de plantilla, no de moneda</strong> — una plantilla fina limita el farmeo, y eso limita todo. <a href=\"/es/wiki/cards/\">Cartas</a>",
            "<strong>Mejoras repartidas</strong> — el mismo error pagado más caro. <a href=\"/es/guides/rank-up/\">Rank Up</a>",
            "<strong>Perseguir tier lists</strong> — los rankings sin fecha llevan a las cuentas gratuitas a callejones caros. <a href=\"/es/guides/progression/\">Progresión</a>",
        ]),
        ("h2", "Un orden realista para F2P"),
        ("ol", [
            "<strong>Sesiones 1–3:</strong> entiende el ingreso de Energía, abre Cartas por lotes y monta un conjunto de farmeo. <a href=\"/es/guides/beginner-guide/\">Guía para Principiantes</a>",
            "<strong>Semana 1:</strong> guarda recursos, termina una línea de mejoras y canjea todo código con fecha.",
            "<strong>Después:</strong> desbloquea hacia delante con <a href=\"/es/wiki/avatars/\">Avatares</a> y "
            "<a href=\"/es/wiki/weapons/\">Armas</a>, farmea la banda de equipo vía "
            "<a href=\"/es/guides/secret-boss-locations/\">jefes</a> y solo entonces empuja las "
            "<a href=\"/es/guides/raids/\">Raids</a>.",
        ]),
        ("note", "Esta página no afirma qué contienen ni cuánto cuestan las compras con Robux. Las experiencias de "
                 "Roblox cambian sus tiendas sin aviso, y este sitio no publica detalles de compra no verificables — "
                 "la ruta F2P de arriba se basa enteramente en el bucle verificado."),
    ],
    "faq": [
        ("¿Se puede jugar a " + G + " sin gastar Robux?", "Sí en estructura: el bucle oficial describe progresión por Energía, Cartas, Companions, recursos y desbloqueos, no por compras. Una cuenta gratuita necesita sobre todo disciplina de recursos."),
        ("¿Qué debería hacer primero un jugador F2P en " + G + "?", "Medir el ingreso de Energía, abrir Cartas por lotes para un conjunto de farmeo y luego comprometerse con una línea de mejoras mientras guarda recursos."),
        ("¿Merecen la pena los códigos para F2P?", "Sí — son la inyección de recursos más barata disponible, y la página de códigos sigue lo reportado activo con su fecha de revisión."),
        ("¿" + G + " es pay to win?", "Ninguna afirmación verificada lo respalda, y este sitio no publica detalles de compra que no puede comprobar. El bucle se mueve por esfuerzo; el riesgo real del F2P es desperdiciar recursos en compromisos paralelos."),
    ],
    "related": [("Códigos", "/es/codes/", "Recursos gratis, fechados"),
                ("Guía para Principiantes", "/es/guides/beginner-guide/", "Las tres primeras sesiones"),
                ("Energía", "/es/guides/energy/", "La palanca principal del jugador gratuito")],
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
