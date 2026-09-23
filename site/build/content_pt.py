# -*- coding: utf-8 -*-
"""Anime Breaker (Roblox) — conteúdo em Português (Brasil). Estrutura idêntica ao content_en.py
(mesmos 22 paths, mesmos H2, mesmas FAQ por página). Termos de sistema mantidos como no jogo
(Companions, Avatars, Weapons, Raids, Trial), termos gerais localizados.
Regra factual (PRD §8/§17): VERIFIED / REPORTED / OBSERVED / UNVERIFIED. Nenhum valor não verificado é publicado.
Última verificação: 2026-09-23.
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
    "title": "Anime Breaker Roblox: Códigos, Guias e Wiki",
    "meta": "Wiki e guia não oficial de Anime Breaker no Roblox: o loop oficial, status dos códigos, guias para iniciantes. Fatos rotulados, nunca inventados.",
    "pill": "Wiki de Fãs · Verificação Primeiro",
    "tagline": "A referência de " + G + " que separa fato verificado de boato",
    "intro": ("Recurso de fãs, não afiliado a " + DEV + ". O título oficial no Roblox aparece hoje como "
              "<strong>" + G + " [🌳CLASS TREE]</strong>. Cada mecânica aqui recebe um rótulo "
              "VERIFIED / REPORTED / OBSERVED, e números que não podemos confirmar ficam de fora em vez de "
              "serem chutados."),
    "cta2_label": "Começar pelo Guia para Iniciantes",
    "cta2_url": "/pt/guides/beginner-guide/",
    "stats": [("ATIVO", "Jogável no Roblox"), ("8", "Sistemas no loop oficial"),
              ("4", "Tipos de dispositivo"), ("3", "Idiomas do guia")],
    "shot_alt": ["Arte oficial de " + G + " – personagens", G + " gameplay – combate",
                 G + " cenário – mundo noturno", G + " gameplay – recompensas e melhorias"],
    "gallery_credit": ("As imagens vêm da página oficial do Roblox e continuam sendo propriedade de " + DEV +
                       "; exibidas apenas como referência."),
    "sections": [
        ("h2", "O que é " + G + " no Roblox?"),
        ("p", G + " é uma experiência de progressão com estética de anime no Roblox, feita por " + DEV + ". A página "
              "oficial descreve um <strong>loop movido a Energia</strong>: você ganha Energia, abre "
              "<strong>Cartas</strong> para conseguir <strong>Companions</strong>, combate inimigos por recursos, "
              "desbloqueia <strong>Avatares</strong>, <strong>Armas</strong> e itens raros, e então sobe de "
              "<strong>Rank</strong> e faz <strong>Melhorias</strong> até as <strong>Raids</strong>. A mesma página "
              "lista computadores, celulares, tablets e consoles como dispositivos suportados."),
        ("p", "Este site é organizado em torno da próxima decisão real do jogador: gastar ou guardar Energia, subir "
              "de rank ou investir em melhorias, farmar um <a href=\"/pt/guides/secret-boss-locations/\">boss "
              "secreto</a> ou empurrar a <a href=\"/pt/guides/progression/\">progressão</a>. Comece pelo "
              "<a href=\"/pt/guides/beginner-guide/\">guia para iniciantes</a>, ou vá direto aos "
              "<a href=\"/pt/codes/\">códigos</a> se só precisa deles."),
        ("h2", "O loop principal (descrição oficial)"),
        ("p", "A descrição oficial apresenta o loop como uma corrente. Esta é a forma verificada dele:"),
        ("ol", [
            "<strong>Ganhe Energia</strong> — a Energia é a entrada do loop; tudo começa aqui. Mais: <a href=\"/pt/guides/energy/\">guia de Energia</a>.",
            "<strong>Abra Cartas para conseguir Companions</strong> — é o caminho oficial de aquisição. Mais: <a href=\"/pt/wiki/cards/\">Cartas</a> · <a href=\"/pt/wiki/companions/\">Companions</a>.",
            "<strong>Combata inimigos por recursos</strong> — o combate e o farm alimentam a economia. Mais: <a href=\"/pt/wiki/resources/\">Recursos</a>.",
            "<strong>Desbloqueie Avatares, Armas e itens raros</strong> — a camada de desbloqueio. Mais: <a href=\"/pt/wiki/avatars/\">Avatares</a> · <a href=\"/pt/wiki/weapons/\">Armas</a> · <a href=\"/pt/wiki/accessories/\">Acessórios</a>.",
            "<strong>Rank Up / Melhorias</strong> — o passo de poder. Mais: <a href=\"/pt/guides/rank-up/\">Rank Up</a> · <a href=\"/pt/guides/upgrades/\">Melhorias</a>.",
            "<strong>Raids</strong> — o nível de desafio no fim do loop. Mais: <a href=\"/pt/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "Status atual (" + LC + ")"),
        ("p", "O título oficial contém atualmente <strong>CLASS TREE</strong>, o que indica uma linha de atualização "
              "de classes/progressão em andamento — veja o <a href=\"/pt/updates/\">hub de atualizações</a>. Os "
              "códigos são um sistema ativo, e os que acompanhamos ficam datados na "
              "<a href=\"/pt/codes/\">página de códigos</a>."),
        ("h2", G + " em resumo"),
        ("table", {"head": ["Campo", "Detalhes"],
                   "rows": [
                       ["Título oficial", G + " [🌳CLASS TREE] (página do Roblox, checado em " + LC + ")"],
                       ["Desenvolvedor / publicador", DEV],
                       ["Plataforma", "Roblox — computadores, celulares, tablets e consoles"],
                       ["Gênero", "Experiência de progressão e coleção com estética de anime"],
                       ["Loop principal", "Energia → Cartas → Companions → combate por recursos → Avatares / Armas → Rank Up / Melhorias → Raids"],
                       ["Sistemas ativos", "Códigos (ativos), linha de atualização marcada como CLASS TREE"],
                       ["Verificação", "Cada afirmação é rotulada VERIFIED, REPORTED, OBSERVED ou UNVERIFIED"],
                   ]}),
        ("note", "Jogue pela página oficial: <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX + "</a>. Códigos, "
                 "custos, taxas de drop e valores de balanceamento mudam entre atualizações — este site reconfere e "
                 "mostra a data da checagem."),
        ("h2", "Jornada do jogador: o que ler em seguida"),
        ("p", "O site é uma rota pelo loop, não um amontoado de páginas. Siga a ordem ou pule para o passo onde você "
              "travou:"),
        ("ul", [
            "<strong>Passo 1 — Entenda o loop:</strong> <a href=\"/pt/guides/beginner-guide/\">Guia para Iniciantes</a>",
            "<strong>Passo 2 — Resolva a Energia:</strong> <a href=\"/pt/guides/energy/\">Energia</a> → <a href=\"/pt/wiki/cards/\">Cartas</a> → <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Passo 3 — Escolha o poder:</strong> <a href=\"/pt/guides/upgrades/\">Melhorias</a> → <a href=\"/pt/guides/rank-up/\">Rank Up</a> → <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Passo 4 — Desbloqueie:</strong> <a href=\"/pt/wiki/avatars/\">Avatares</a> → <a href=\"/pt/wiki/weapons/\">Armas</a> → <a href=\"/pt/wiki/worlds/\">Mundos</a>",
            "<strong>Passo 5 — Farme e desafie:</strong> <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a> → <a href=\"/pt/wiki/accessories/\">Acessórios</a> → <a href=\"/pt/guides/raids/\">Raids</a> → <a href=\"/pt/guides/trial/\">Trial</a> → <a href=\"/pt/wiki/amulets/\">Amuletos</a>",
            "<strong>Sem Robux?</strong> <a href=\"/pt/guides/f2p/\">Guia F2P</a> · <a href=\"/pt/codes/\">Códigos</a>",
        ]),
        ("h2", "Principais sistemas na wiki"),
        ("cards", [
            ("Cartas", "Como as Cartas funcionam e levam aos Companions.", "/pt/wiki/cards/"),
            ("Companions", "Aquisição, uso e a diferença para Avatares.", "/pt/wiki/companions/"),
            ("Avatares", "Desbloqueio, evolução e farm de Avatares.", "/pt/wiki/avatars/"),
            ("Armas", "Aquisição e o papel das armas.", "/pt/wiki/weapons/"),
            ("Acessórios e Amuletos", "Drops de boss e decisões de equipamento.", "/pt/wiki/accessories/"),
            ("Recursos e Mundos", "Moedas, fontes e navegação entre mundos.", "/pt/wiki/resources/"),
        ]),
        ("h2", "Por que esta wiki verifica primeiro"),
        ("p", "Wikis de Roblox se copiam, e números sensíveis à versão (custos de rank, HP de boss, taxas de drop, "
              "multiplicadores) acabam congelados em valores de lançamento que já não batem com o cliente atual. "
              "Este site usa quatro rótulos:"),
        ("ul", [
            "<strong>VERIFIED</strong> — afirmado pela página oficial do Roblox ou reproduzível no cliente atual.",
            "<strong>REPORTED</strong> — publicado por fonte secundária datada (por exemplo o snapshot de códigos de " + LC + ").",
            "<strong>OBSERVED</strong> — visto em jogo no build atual, ainda em reconfirmação.",
            "<strong>UNVERIFIED</strong> — afirmado em algum lugar, confirmado em nenhum. Fica listado para você testar, nunca como fato.",
        ]),
        ("note", "Valores de alto risco — custos e multiplicadores de rank, HP e taxas de drop de boss, "
                 "multiplicadores de Avatar, status de armas, status de acessórios, custo de ticket de raid, valores "
                 "de Amuleto, taxas de pull de cartas e recompensas do Trial — ficam deliberadamente ausentes sem "
                 "fonte atual."),
        ("h2", "Entre na wiki"),
        ("cards", [
            ("Guia para Iniciantes", "O loop e a primeira sessão, passo a passo.", "/pt/guides/beginner-guide/"),
            ("Códigos", "Códigos ativos e expirados com a data da checagem.", "/pt/codes/"),
            ("Hub da Wiki", "Todos os sistemas documentados em um lugar.", "/pt/wiki/"),
            ("Hub de Guias", "Guias de tarefas e otimização.", "/pt/guides/"),
            ("Atualizações", "O que mudou e o que é apenas detectado.", "/pt/updates/"),
            ("Guia F2P", "Decisões de progresso sem Robux.", "/pt/guides/f2p/"),
        ]),
    ],
    "faq": [
        ("O que é " + G + " no Roblox?", "Uma experiência de progressão com estética de anime no Roblox, de " + DEV + ". A página oficial descreve um loop movido a Energia: ganhe Energia, abra Cartas para conseguir Companions, combata inimigos por recursos, desbloqueie Avatares, Armas e itens raros, suba de Rank e faça Melhorias até as Raids."),
        ("O " + G + " é grátis?", "Roda dentro do Roblox, que é gratuito para instalar. Compras opcionais com Robux existem dentro da experiência e não são necessárias para seguir o loop descrito oficialmente."),
        ("O que significa CLASS TREE no título de " + G + "?", "O título oficial aparece hoje como " + G + " [🌳CLASS TREE], sinalizando uma linha de atualização de classes/progressão ativa. Este site não inventa detalhes de patch além do que o título e fontes datadas mostram."),
        ("Onde eu resgato códigos de " + G + "?", "Os códigos são resgatados dentro da experiência. A lista atual que acompanhamos, com data de verificação, está na página de códigos."),
        ("Existe tier list ou página de melhores unidades em " + G + "?", "Ainda não, de propósito. Tier lists congelam valores que mudam a cada atualização; enquanto uma fonte atual não sustentar isso, publicamos frameworks de decisão — veja os guias de Melhorias e Progressão."),
        ("Por onde um jogador novo deve começar?", "Pelo guia para iniciantes, depois Energia e Cartas. Esses três cobrem a parte do loop que a primeira sessão realmente usa."),
        ("Por que faltam alguns números?", "Porque número não verificado é pior que número nenhum. Custos de rank, taxas de drop, multiplicadores e HP de boss só aparecem quando uma fonte atual sustenta."),
    ],
    "related": [("Guia para Iniciantes", "/pt/guides/beginner-guide/", "Comece sua primeira sessão"),
                ("Códigos", "/pt/codes/", "Status ao vivo com data de verificação"),
                ("Guia de Progressão", "/pt/guides/progression/", "Onde o loop fica difícil")],
}

# ---------- 2. Wiki hub ----------
PAGES["wiki/index.html"] = {
    "path": "wiki/index.html",
    "title": "Anime Breaker Wiki – Cartas, Companions e Avatares",
    "meta": "Hub da wiki de Anime Breaker: Cartas, Companions, Avatares, Armas, Acessórios, Amuletos, Recursos e Mundos, com rótulos de verificação.",
    "pill": "Wiki", "h1": G + " Wiki",
    "lead": ("A camada de referência do site: cada sistema documentado, o que ele faz no loop e o quanto "
             "confiamos nele."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/")],
    "sections": [
        ("p", "Este hub cobre os sistemas citados na descrição oficial de " + G + " mais as camadas de equipamento e "
              "de mundos que os jogadores mais procuram. Cada página diz o que é VERIFIED, o que é REPORTED e o que "
              "é apenas OBSERVED no cliente atual — e toda página carrega a data da última checagem."),
        ("h2", "Sistemas do loop oficial"),
        ("table", {"head": ["Sistema", "Papel no loop", "Confiança"],
                   "rows": [
                       ["Energia", "Entrada: ganha, gasta e guardada para abrir Cartas.", "VERIFIED (página oficial)"],
                       ["Cartas", "Camada de aquisição: abrir Cartas pelos Companions.", "VERIFIED (página oficial)"],
                       ["Companions", "Lutam com você e alimentam a economia de recursos.", "VERIFIED (página oficial)"],
                       ["Avatares", "Camada de desbloqueio: muda o que você joga.", "VERIFIED (página oficial)"],
                       ["Armas", "Camada de desbloqueio: mudam o dano do combate.", "VERIFIED (página oficial)"],
                       ["Rank Up", "Passo de poder: sobe sua conta na escada de rank.", "VERIFIED (página oficial)"],
                       ["Melhorias", "Passo de poder: gastar recursos para fortalecer o que você tem.", "VERIFIED (página oficial)"],
                       ["Raids", "Nível de desafio no fim do loop.", "VERIFIED (página oficial)"],
                   ]}),
        ("h2", "Camadas de equipamento, economia e mundos"),
        ("ul", [
            "<strong><a href=\"/pt/wiki/accessories/\">Acessórios</a></strong> — equipamento vindo de bosses e as decisões em torno dele.",
            "<strong><a href=\"/pt/wiki/amulets/\">Amuletos</a></strong> — slot adicional relatado na fase de gargalo da progressão.",
            "<strong><a href=\"/pt/wiki/resources/\">Recursos</a></strong> — as moedas e materiais que o loop consome.",
            "<strong><a href=\"/pt/wiki/worlds/\">Mundos</a></strong> — a ordem dos mundos usada para navegação, sem subpáginas vazias.",
        ]),
        ("h2", "Como a wiki trata valores desconhecidos"),
        ("p", "Experiências do Roblox rebalanceiam no lugar, então um valor copiado de uma wiki pode ficar errado na "
              "mesma semana. Por isso publicamos mecânicas e lógica de decisão, e só imprimimos números que uma "
              "fonte atual sustenta — a mesma regra das páginas de <a href=\"/pt/wiki/avatars/\">Avatares</a> e "
              "<a href=\"/pt/wiki/weapons/\">Armas</a> para multiplicadores e tabelas de status."),
        ("note", "Quando uma página diz que os dados são parciais, isso é intencional: o sistema é real e "
                 "documentado, e os números exatos ficam retidos até a verificação. Nada é preenchido com um chute "
                 "plausível."),
    ],
    "faq": [
        ("O que é a wiki de " + G + "?", "Uma referência feita por jogadores para os sistemas e equipamentos de " + G + " no Roblox, com cada afirmação rotulada pelo nível de fonte. Não afiliada a " + DEV + "."),
        ("Por que faltam tabelas de status de " + G + "?", "Porque o cliente pode mudar multiplicadores, custos e taxas sem aviso. As tabelas aparecem quando uma fonte atual sustenta os números."),
        ("Qual sistema ler primeiro?", "Energia, depois Cartas, depois Companions — é a ordem em que o loop oficial roda."),
    ],
    "related": [("Hub de Guias", "/pt/guides/", "Guias de tarefas e otimização"),
                ("Guia para Iniciantes", "/pt/guides/beginner-guide/", "O loop em ordem"),
                ("Atualizações", "/pt/updates/", "O que mudou e quando")],
}

# ---------- 3. Guides hub ----------
PAGES["guides/index.html"] = {
    "path": "guides/index.html",
    "title": "Anime Breaker Guias: Iniciante, Energia e Raids",
    "meta": ("Todos os guias de " + G + ": iniciante, progressão, Energia, Rank Up, Melhorias, Bosses Secretos, "
             "Raids, Trial e a rota F2P."),
    "pill": "Guias", "h1": G + " Guias",
    "lead": ("Cada guia responde a uma decisão, na ordem em que o jogador a encontra, a partir do loop oficial."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/")],
    "sections": [
        ("p", "Os guias são escritos como decisões, não como descrições: gastar ou guardar, subir de rank ou "
              "melhorar, farmar aqui ou avançar. Cada um traz pré-requisitos, o passo a passo, os erros comuns e o "
              "quanto depende da próxima atualização."),
        ("h2", "Comece aqui"),
        ("cards", [
            ("Guia para Iniciantes", "Loop, primeira sessão e os erros a evitar.", "/pt/guides/beginner-guide/"),
            ("Energia", "Como a Energia é ganha, gasta e esticada.", "/pt/guides/energy/"),
            ("Progressão", "O mapa de gargalos do meio e do fim de jogo.", "/pt/guides/progression/"),
        ]),
        ("h2", "Guias de otimização"),
        ("cards", [
            ("Rank Up", "Quando vale subir de rank — e do que o custo realmente depende.", "/pt/guides/rank-up/"),
            ("Melhorias", "Um framework de prioridade em vez de tier list congelada.", "/pt/guides/upgrades/"),
            ("Raids", "Acesso, ondas, recompensas e como gastá-las.", "/pt/guides/raids/"),
            ("Trial", "O loop de desafio estilo corredor e sua rota de melhorias.", "/pt/guides/trial/"),
        ]),
        ("h2", "Guias de tarefa e F2P"),
        ("cards", [
            ("Bosses Secretos", "Como bosses são encontrados, farmados e registrados.", "/pt/guides/secret-boss-locations/"),
            ("Guia F2P", "Decisões de progresso sem gastar Robux.", "/pt/guides/f2p/"),
            ("Códigos", "Status dos códigos com data de verificação.", "/pt/codes/"),
        ]),
        ("note", "Os guias são reconferidos no cliente atual: valores que mudam com balanceamento ficam rotulados em "
                 "vez de impressos como constantes."),
    ],
    "faq": [
        ("Qual guia de " + G + " ler primeiro?", "O guia para iniciantes. Depois Energia e Cartas, porque a primeira sessão acontece quase inteira nessa parte do loop."),
        ("Os guias usam números reais?", "Só números que uma fonte atual sustenta. Custos, taxas de drop e multiplicadores que mudam entre atualizações aparecem como lógica de decisão, não como constante congelada."),
        ("Existe página de melhores melhorias ou melhores armas?", "Não. Essas páginas envelhecem em um patch. O guia de Melhorias traz um framework de priorização aplicável ao que sua conta tem hoje."),
    ],
    "related": [("Hub da Wiki", "/pt/wiki/", "A camada de referência"),
                ("Atualizações", "/pt/updates/", "Sensibilidade à atualização"),
                ("Códigos", "/pt/codes/", "Recursos grátis enquanto durm")],
}

# ---------- 4. Codes ----------
PAGES["codes/index.html"] = {
    "path": "codes/index.html",
    "title": G + " Códigos (Setembro 2026) – Ativos e Expirados",
    "meta": "Status dos códigos de Anime Breaker em setembro de 2026: códigos de marco e de atualização relatados ativos, como resgatar e lidar com expirados.",
    "pill": "Ao vivo", "h1": G + " Códigos",
    "lead": ("Uma página datada, não eterna. Cada código aqui está relatado ativo por fonte datada ou tratado como "
             "expirado — e todos pedem que você teste em jogo."),
    "breadcrumb": [("Início", "/pt/"), ("Códigos", "/pt/codes/")],
    "sections": [
        ("p", "<strong>Última verificação: " + LC + "</strong>. Os códigos de " + G + " são um "
              "<strong>sistema ativo</strong> (REPORTED — cobertura secundária de códigos datada de 2026-09-22). "
              "Essa cobertura contava cerca de <strong>14 códigos ativos</strong> naquela data, incluindo códigos de "
              "marco e de atualização. Códigos de marco costumam ser aposentados quando a meta da comunidade passa, "
              "então trate a lista abaixo como datada, não permanente."),
        ("h2", "Códigos relatados ativos (" + LC + ")"),
        ("table", {"head": ["Código", "Status", "O que a fonte diz"],
                   "rows": [
                       ["10KCCU", "REPORTED ativo", "Código de marco (contagem de comunidade) — teste em jogo; este site não imprime recompensas que não pode verificar."],
                       ["2MVISITS", "REPORTED ativo", "Código de marco (meta de visitas)."],
                       ["20KFAVORITES", "REPORTED ativo", "Código de marco (meta de favoritos)."],
                       ["NEWPORTAL", "REPORTED ativo", "Código de atualização, relatado junto a uma linha de portal."],
                       ["NEWSHADOW", "REPORTED ativo", "Código de atualização, relatado junto a uma linha de shadow."],
                   ]}),
        ("note", "Os valores de recompensa ficam em branco de propósito: o snapshot secundário lista as strings dos "
                 "códigos, não recompensas itemizadas, e tabelas de recompensa copiadas são exatamente como páginas "
                 "de código erram. Digite o código em jogo e leia a recompensa na confirmação."),
        ("h2", "Códigos expirados"),
        ("p", "Sistemas de código do Roblox expiram em silêncio — um código que funcionava semana passada pode parar "
              "sem anúncio. Esta página não publica uma lista de expirados que não pode verificar, pelo mesmo motivo "
              "que não publica recompensas inventadas: data de expiração não verificada é desinformação. Se um "
              "código listado falhar, trate como expirado para o seu build e veja o "
              "<a href=\"/pt/updates/\">hub de atualizações</a>."),
        ("h2", "Como resgatar códigos em " + G),
        ("ol", [
            "<strong>Entre na experiência oficial</strong> — abra " + G + " pela página oficial no Roblox.",
            "<strong>Ache a entrada de código</strong> — experiências do Roblox colocam o resgate em um menu, nas configurações ou em um painel próprio; o lugar muda entre builds, então use a interface atual.",
            "<strong>Digite exatamente</strong> — códigos do Roblox diferenciam maiúsculas e caracteres; use copiar e colar quando o campo permitir.",
            "<strong>Confirme e leia a recompensa</strong> — se nada for entregue, o código expirou ou já foi resgatado naquela conta.",
        ]),
        ("h2", "Onde novos códigos aparecem"),
        ("ul", [
            "<strong>Códigos de marco</strong> — ligados a números da comunidade (visitas, favoritos, jogadores simultâneos), por isso os códigos acima parecem contadores.",
            "<strong>Códigos de atualização</strong> — lançados junto de linhas de conteúdo, que é como NEWPORTAL e NEWSHADOW aparecem.",
            "<strong>Ritmo de checagem</strong> — a página é redatada sempre que o conjunto é reverificado, e as regras abaixo mostram o que um código precisa para entrar na lista.",
        ]),
        ("h2", "Por que um código pode não funcionar"),
        ("ul", [
            "<strong>Expirou</strong> — a causa mais comum; códigos de marco são os primeiros a sair.",
            "<strong>Erro de digitação</strong> — digite novamente caractere por caractere.",
            "<strong>Já resgatado</strong> — a maioria dos sistemas permite um resgate por conta.",
            "<strong>Jogo errado</strong> — títulos de anime com nomes parecidos têm seus próprios códigos; não são transferíveis entre experiências.",
        ]),
        ("h2", "Como esta página é mantida"),
        ("ul", [
            "Um código só entra com fonte datada e o status REPORTED.",
            "Recompensas só aparecem quando visíveis na confirmação do próprio jogo.",
            "A página é reverificada como conjunto, então a data no topo sempre descreve a tabela inteira.",
        ]),
        ("note", "Se a tabela acima e uma fonte mais nova discordarem, confie na fonte mais nova em jogo. Esta página "
                 "existe para ser datada e honesta, não para ser a maior lista da internet."),
    ],
    "faq": [
        ("Existem códigos de " + G + " funcionando agora?", "Em " + LC + " uma fonte secundária datada relatava cerca de 14 códigos ativos, incluindo 10KCCU, 2MVISITS, 20KFAVORITES, NEWPORTAL e NEWSHADOW. Teste cada um em jogo — o status muda mais rápido que qualquer lista."),
        ("O que os códigos de " + G + " dão?", "O snapshot datado lista as strings de código, não recompensas itemizadas, então não imprimimos valores. A confirmação dentro do jogo é a resposta autoritativa."),
        ("Como resgatar códigos de " + G + "?", "Entre na experiência oficial, abra a entrada de código no jogo (normalmente em um menu ou painel de configurações, que muda entre builds), digite exatamente e confirme."),
        ("Por que um código que funcionava ontem parou?", "Códigos de marco são aposentados quando a meta da comunidade é atingida. Um código expirado e um digitado errado parecem iguais na interface — digite de novo uma vez e depois assuma expirado."),
        ("Códigos de outros jogos de anime funcionam aqui?", "Não. Cada experiência tem seu próprio conjunto de códigos."),
        ("Com que frequência esta página é atualizada?", "Sempre que o conjunto é reverificado. A data no topo sempre descreve a tabela abaixo."),
    ],
    "related": [("Atualizações", "/pt/updates/", "A qual linha os códigos pertencem"),
                ("Guia F2P", "/pt/guides/f2p/", "Transforme recompensas grátis em progresso"),
                ("Guia para Iniciantes", "/pt/guides/beginner-guide/", "O que fazer com as primeiras recompensas")],
}

# ---------- 5. Updates ----------
PAGES["updates/index.html"] = {
    "path": "updates/index.html",
    "title": "Anime Breaker Atualizações – Status CLASS TREE e Mudanças",
    "meta": ("Hub de atualizações de " + G + ": o status atual do título CLASS TREE, o que está verificado na "
             "página oficial e o que é apenas relatado."),
    "pill": "Ao vivo", "h1": G + " Atualizações",
    "lead": ("Um hub datado das mudanças de " + G + " — feito para impedir que 'um registro público mudou' vire "
             "'esse recurso está no ar'."),
    "breadcrumb": [("Início", "/pt/"), ("Atualizações", "/pt/updates/")],
    "sections": [
        ("p", "Checado em <strong>" + LC + "</strong>. A página oficial mostra hoje o título como "
              "<strong>" + G + " [🌳CLASS TREE]</strong>. Essa marca é o sinal de atualização mais forte disponível "
              "sem inventar patch notes: indica uma linha de atualização de classes/progressão ativa no próprio "
              "nome do jogo."),
        ("h2", "O que está verificado agora"),
        ("table", {"head": ["Item", "Status (" + LC + ")", "Observação"],
                   "rows": [
                       ["Título oficial", "VERIFIED", G + " [🌳CLASS TREE] conforme a página oficial do Roblox."],
                       ["Loop principal", "VERIFIED", "Energia → Cartas → Companions → recursos → Avatares / Armas → Rank Up / Melhorias → Raids."],
                       ["Dispositivos", "VERIFIED", "Computadores, celulares, tablets e consoles."],
                       ["Sistema de códigos", "REPORTED ativo", "Cobertura secundária de 2026-09-22 contava cerca de 14 códigos ativos. Veja a página de códigos."],
                   ]}),
        ("h2", "O que esta página não fará"),
        ("ul", [
            "<strong>Nada de patch notes inventadas</strong> — a marca CLASS TREE não é expandida em números de balanceamento por chute.",
            "<strong>Nada de valores de lançamento congelados</strong> — quando um sistema muda, o valor é rerrotulado em vez de mantido em silêncio.",
            "<strong>Nada de 'detectado, logo ativo'</strong> — um registro público ou uma página concorrente mudando é uma pista, não uma confirmação.",
        ]),
        ("h2", "Como ler uma atualização com este site"),
        ("ol", [
            "<strong>Confira a data</strong> — toda página mostra o dia da última verificação.",
            "<strong>Confira o rótulo</strong> — VERIFIED, REPORTED, OBSERVED e UNVERIFIED significam coisas diferentes de propósito.",
            "<strong>Reteste em jogo</strong> — o cliente atual vale mais que qualquer página, inclusive esta.",
        ]),
        ("note", "Páginas afetadas por atualização: <a href=\"/pt/codes/\">Códigos</a>, "
                 "<a href=\"/pt/guides/rank-up/\">Rank Up</a> (custos), <a href=\"/pt/guides/upgrades/\">Melhorias</a> "
                 "(prioridades), <a href=\"/pt/guides/raids/\">Raids</a> (tickets e recompensas) e "
                 "<a href=\"/pt/wiki/weapons/\">Armas</a> (status)."),
    ],
    "faq": [
        ("Qual é a última atualização de " + G + "?", "Em " + LC + " a página oficial carrega a marca CLASS TREE no título, e o sistema de códigos está relatado ativo com códigos de marco e de atualização. Ambos ficam datados aqui, não descritos como permanentes."),
        ("CLASS TREE significa um novo sistema de classes?", "A marca faz parte do título oficial, então uma linha de classe/progressão ativa é a leitura razoável. Este site não publica listas de recursos ou números sem fonte atual."),
        ("Com que frequência o " + G + " é atualizado?", "Nenhum cronograma público faz parte do registro verificado, então não prometemos um. As páginas trazem data de checagem."),
        ("Por que esta página é curta?", "Porque tamanho não é evidência. Só mudanças com fonte datada entram; o resto fica de fora até poder ser testado."),
    ],
    "related": [("Códigos", "/pt/codes/", "A página mais sensível a atualizações"),
                ("Guia de Progressão", "/pt/guides/progression/", "Replaneje após um patch"),
                ("Rank Up", "/pt/guides/rank-up/", "Custos mudam com atualizações")],
}

# ---------- 6. Beginner Guide ----------
PAGES["guides/beginner-guide/index.html"] = {
    "path": "guides/beginner-guide/index.html",
    "title": "Anime Breaker Guia para Iniciantes – Como Jogar",
    "meta": ("Como jogar " + G + " no Roblox: o loop oficial movido a Energia explicado passo a passo, sua "
             "primeira sessão e quais erros custam mais no começo."),
    "pill": "Guias", "h1": G + " Guia para Iniciantes",
    "lead": ("Sua primeira sessão mapeada no loop oficial: Energia entra, Cartas abrem, Companions saem, recursos "
             "são gastos — na ordem certa."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Guia para Iniciantes", "/pt/guides/beginner-guide/")],
    "sections": [
        ("p", "A descrição oficial de " + G + " entrega o loop direto: <strong>ganhe Energia → abra Cartas para "
              "conseguir Companions → combata inimigos por recursos → desbloqueie Avatares, Armas e itens raros → "
              "Rank Up / Melhorias → Raids</strong>. Um guia de iniciante é, em grande parte, sobre não quebrar a "
              "ordem desse loop."),
        ("h2", "Pré-requisitos"),
        ("ul", [
            "<strong>Roblox instalado</strong> — " + G + " roda em computadores, celulares, tablets e consoles.",
            "<strong>A página oficial</strong> — <a href=\"" + RPX + "\" rel=\"noopener\">" + RPX + "</a>.",
            "<strong>Motivo para ler antes</strong> — recursos iniciais são o que você tem de mais escasso; o loop pune gasto aleatório.",
        ]),
        ("h2", "Sua primeira sessão, passo a passo"),
        ("ol", [
            "<strong>Entenda de onde vem a Energia</strong> — é a entrada do loop. Descubra como sua conta ganha antes de gastar. <a href=\"/pt/guides/energy/\">Guia de Energia</a>",
            "<strong>Abra Cartas com critério</strong> — Cartas são o caminho oficial para Companions. Abra em lote, não uma por uma, para ver o que falta no seu elenco. <a href=\"/pt/wiki/cards/\">Cartas</a>",
            "<strong>Coloque os Companions em campo</strong> — são eles que lutam na descrição oficial, e os recursos que ajudam a gerar são a moeda de tudo depois. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Guarde recursos antes de gastar</strong> — Avatares, Armas, Rank Up e Melhorias bebem do mesmo poço. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Tome uma decisão de progressão, não cinco</strong> — escolha uma melhoria ou um push de rank e vá até o fim. <a href=\"/pt/guides/upgrades/\">Melhorias</a> · <a href=\"/pt/guides/rank-up/\">Rank Up</a>",
            "<strong>Só depois olhe Avatares e Armas</strong> — são a camada de desbloqueio e compensam quando o fluxo de recursos estabiliza. <a href=\"/pt/wiki/avatars/\">Avatares</a> · <a href=\"/pt/wiki/weapons/\">Armas</a>",
        ]),
        ("h2", "Erros de iniciante que mais custam"),
        ("ul", [
            "<strong>Gastar Energia assim que ela aparece</strong> — sem conhecer sua renda, você não distingue uma boa sessão de uma ruim.",
            "<strong>Buscar raridade antes de fluxo</strong> — um desbloqueio raro numa conta sem renda trava na hora.",
            "<strong>Confiar em número copiado</strong> — custos, multiplicadores e taxas mudam entre atualizações; print do mês passado é boato.",
            "<strong>Ignorar os códigos</strong> — o sistema é ativo e recompensa grátis no começo vale mais que depois. <a href=\"/pt/codes/\">Códigos</a>",
        ]),
        ("note", "Sensibilidade à atualização: o loop em si é verificado pela página oficial e é estável; os números "
                 "em volta não são. Se um guia cita quantidades exatas de Energia, custos de rank ou taxas sem data, "
                 "trate como não verificado."),
    ],
    "faq": [
        ("Como se joga " + G + "?", "Siga o loop oficial: ganhe Energia, abra Cartas para conseguir Companions, combata inimigos por recursos, desbloqueie Avatares, Armas e itens raros, suba de Rank e faça Melhorias até as Raids. Os dispositivos suportados são computadores, celulares, tablets e consoles."),
        ("O que fazer primeiro em " + G + "?", "Entenda como sua conta ganha Energia, gaste em Cartas por lote para ver o que falta no elenco, coloque os Companions em campo, farme recursos e tome uma decisão de progressão por vez."),
        ("O " + G + " é pay to win?", "O registro verificado descreve um loop de progressão dentro da experiência, não um loop de compras. Compras opcionais com Robux existem em muitas experiências, mas este site não publica afirmações de compra que não pode verificar — o guia F2P cobre jogar sem elas."),
        ("Quanto tempo até o primeiro Companion?", "Não imprimimos tempos: dependem da sua renda de Energia e do pool de Cartas, que mudam entre atualizações. A página de Cartas explica a mecânica."),
        ("Qual é o maior erro de iniciante?", "Dividir recursos iniciais entre Avatares, Armas, Melhorias e Rank Up ao mesmo tempo. Guarde primeiro e depois comprometa-se com um caminho."),
    ],
    "related": [("Energia", "/pt/guides/energy/", "A entrada do loop"),
                ("Cartas", "/pt/wiki/cards/", "Como os Companions são obtidos"),
                ("Melhorias", "/pt/guides/upgrades/", "Sua primeira decisão real")],
}

# ---------- 7. Progression ----------
PAGES["guides/progression/index.html"] = {
    "path": "guides/progression/index.html",
    "title": "Anime Breaker Guia de Progressão – Início ao Fim",
    "meta": ("Guia de progressão de " + G + " como mapa de gargalos: o que limita no começo, no meio e no fim, e "
             "qual decisão move a parede."),
    "pill": "Guias", "h1": G + " Guia de Progressão",
    "lead": ("Não é lista de níveis — é um mapa do que realmente está te travando em cada fase, e qual alavanca "
             "move isso."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Progressão", "/pt/guides/progression/")],
    "sections": [
        ("p", "A progressão em " + G + " roda sobre o loop oficial: Energia alimenta Cartas, Cartas geram "
              "Companions, Companions e combate geram recursos, recursos viram Avatares, Armas, Rank e Melhorias, e "
              "esse resultado é testado nas Raids. Quando a progressão trava, o gargalo está sempre em um elo "
              "específico — e a solução raramente é 'jogar mais'."),
        ("h2", "Fase 1 — início: gargalo de fluxo"),
        ("ul", [
            "<strong>Sintoma:</strong> você vive sem Energia ou sem o recurso do próximo passo.",
            "<strong>Problema real:</strong> taxa de renda, não raridade. Desbloqueio raro em conta lenta continua lento.",
            "<strong>Alavanca:</strong> veja primeiro como a Energia é ganha e gasta. <a href=\"/pt/guides/energy/\">Energia</a> → <a href=\"/pt/wiki/cards/\">Cartas</a>",
        ]),
        ("h2", "Fase 2 — meio: gargalo de compromisso"),
        ("ul", [
            "<strong>Sintoma:</strong> vários sistemas pela metade, nada forte o bastante para avançar.",
            "<strong>Problema real:</strong> recursos divididos entre Rank Up, Melhorias, Avatares e Armas ao mesmo tempo.",
            "<strong>Alavanca:</strong> escolha uma linha e termine. <a href=\"/pt/guides/upgrades/\">Melhorias</a> · <a href=\"/pt/guides/rank-up/\">Rank Up</a>",
        ]),
        ("h2", "Fase 3 — fim: gargalo de teto"),
        ("ul", [
            "<strong>Sintoma:</strong> o conteúdo comum é confortável, mas desafios específicos são paredes.",
            "<strong>Problema real:</strong> lacunas de equipamento e raridade — acessórios, amuletos e armas definem o teto, não horas jogadas.",
            "<strong>Alavanca:</strong> mire na fonte de drop. <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a> → <a href=\"/pt/wiki/accessories/\">Acessórios</a> → <a href=\"/pt/wiki/amulets/\">Amuletos</a> → <a href=\"/pt/guides/raids/\">Raids</a>",
        ]),
        ("h2", "A regra de decisão que sobrevive a toda atualização"),
        ("ol", [
            "<strong>Nomeie a parede em uma frase</strong> — 'não consigo terminar este desafio' ou 'fico sem Energia'.",
            "<strong>Case com um elo do loop</strong> — Energia, Cartas, Companions, recursos, desbloqueio, poder, desafio.",
            "<strong>Gaste só nesse elo</strong> — o resto espera. Isso é o que mantém uma conta de meio de jogo andando depois de um rebalanceamento.",
        ]),
        ("note", "Deliberadamente ausente: limiares numéricos de progressão, custos de rank, pontos de quebra de "
                 "multiplicador e taxas de drop. Esses valores mudam entre atualizações e o loop acima não depende "
                 "deles."),
    ],
    "faq": [
        ("Como progredir rápido em " + G + "?", "Resolva o elo que está travando. No começo é renda de Energia; no meio são compromissos inacabados espalhados por muitos sistemas; no fim são tetos de equipamento e raridade."),
        ("Qual a forma mais rápida de ficar forte em " + G + "?", "Termine uma linha antes de abrir outra — um push de rank ou de melhorias. Dividir recursos é a forma mais confiável de continuar fraco."),
        ("O " + G + " tem limite de nível?", "Nenhum limite verificado faz parte do registro oficial. Escadas de rank e multiplicadores são valores que se movem entre builds, então não imprimimos um."),
        ("Quando começar as Raids?", "Quando seu problema de teto for desafio e não recurso — é aí que acesso e recompensas de raid valem mais que outra rota de farm."),
    ],
    "related": [("Rank Up", "/pt/guides/rank-up/", "O passo de poder"),
                ("Bosses Secretos", "/pt/guides/secret-boss-locations/", "Onde o teto quebra"),
                ("Raids", "/pt/guides/raids/", "O nível de desafio")],
}

# ---------- 8. Energy ----------
PAGES["guides/energy/index.html"] = {
    "path": "guides/energy/index.html",
    "title": G + " Energia – Como Ganhar, Usar e Esticar",
    "meta": ("Energia em " + G + ": a entrada do loop oficial. Como é ganha, no que é gasta e como parar de "
             "desperdiçar — sem inventar taxas ou limites."),
    "pill": "Guias", "h1": G + " Energia",
    "lead": ("Energia é o primeiro elo do loop oficial. Este guia cobre o que ela faz, como é gasta e como ler a sua "
             "própria renda."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Energia", "/pt/guides/energy/")],
    "sections": [
        ("p", "A descrição oficial de " + G + " abre com Energia: você <strong>ganha Energia</strong>, e a Energia é "
              "o que permite <strong>abrir Cartas para conseguir Companions</strong>. Todo o resto do jogo é "
              "consequência dessa primeira conversão."),
        ("h2", "O que a Energia faz"),
        ("ul", [
            "<strong>Ela controla a camada de Cartas</strong> — Cartas são o caminho oficial para Companions, e a Energia é o que se gasta para abri-las. <a href=\"/pt/wiki/cards/\">Cartas</a>",
            "<strong>Ela marca o ritmo da sessão</strong> — como é um recurso de gastar e esperar, a qualidade da sessão depende de como você gasta, não de quanto tempo joga.",
            "<strong>Ela converte em todo o resto</strong> — Companions geram combate e farm, que viram recursos. <a href=\"/pt/wiki/companions/\">Companions</a> · <a href=\"/pt/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Como ganhar Energia"),
        ("p", "O registro oficial estabelece a Energia como entrada do loop; não publica uma taxa. Em vez de copiar "
              "uma taxa de outra wiki, meça a sua:"),
        ("ol", [
            "<strong>Anote sua Energia antes da sessão</strong> — número e horário.",
            "<strong>Jogue normalmente por uma janela fixa</strong> — mesmo conteúdo, mesmo padrão de gasto.",
            "<strong>Anote de novo</strong> — a diferença é sua renda real naquela janela, no build atual.",
            "<strong>Re-meça após uma atualização grande</strong> — fontes de renda são exatamente o tipo de valor que atualizações mudam.",
        ]),
        ("note", "Esse hábito de medição é o truque inteiro. Taxas publicadas ficam velhas em um ciclo de patch; a "
                 "sua medição de dois pontos não fica."),
        ("h2", "Como gastar Energia bem"),
        ("ul", [
            "<strong>Gaste em lotes, não em goles</strong> — abrir Cartas em lote mostra o que falta no elenco antes de você comprometer. <a href=\"/pt/wiki/cards/\">Cartas</a>",
            "<strong>Não gaste para 'salvar' uma sessão ruim</strong> — se a sessão não rendeu nada útil, a resposta é o próximo lote, não mais gasto.",
            "<strong>Saiba o que a Energia não compra</strong> — Rank Up, Melhorias, Avatares, Armas e Raids usam recursos e progressão. <a href=\"/pt/guides/rank-up/\">Rank Up</a>",
            "<strong>Acompanhe sua conversão</strong> — Energia entra, Companions ou recursos úteis saem. Essa razão é a única métrica que importa no começo.",
        ]),
        ("h2", "Energia e a rota gratuita"),
        ("p", "Numa conta sem Robux, o ritmo da Energia é sua alavanca principal: recompensas de código e sessões "
              "diárias consistentes valem mais que qualquer compra grande. O <a href=\"/pt/guides/f2p/\">guia F2P</a> "
              "cobre o resto da rota, e a <a href=\"/pt/codes/\">página de códigos</a> acompanha o que conseguimos "
              "datar."),
        ("note", "Não publicamos limites de Energia, taxas de regeneração, custos de recarga ou taxas de pull: "
                 "nenhuma fonte atual sustenta, e eles mudam. Se precisar de número, meça como acima."),
    ],
    "faq": [
        ("Como ganhar Energia em " + G + "?", "A Energia é a entrada do loop oficial — você a ganha e gasta para abrir Cartas. O registro oficial não publica taxa, então meça sua própria renda em uma janela fixa."),
        ("No que se gasta Energia em " + G + "?", "Em abrir Cartas. Cartas são o caminho oficial para Companions, e Companions geram o combate e os recursos que financiam todo o resto."),
        ("Energia é igual a sistema de stamina?", "Funcionalmente ela marca o ritmo da sessão como um recurso de stamina, e a descrição oficial a trata como entrada do loop. Limites e regeneração exatos não são publicados aqui por não serem verificados."),
        ("E se eu desperdiçar Energia?", "Não dá para desfazer o gasto, mas dá para mudar o padrão: gastar em lotes, medir entrada versus saída útil e re-medir após atualizações em vez de seguir um guia velho."),
    ],
    "related": [("Cartas", "/pt/wiki/cards/", "Para onde a Energia vai"),
                ("Guia para Iniciantes", "/pt/guides/beginner-guide/", "A ordem da primeira sessão"),
                ("Guia F2P", "/pt/guides/f2p/", "Ritmo de Energia sem Robux")],
}

# ---------- 9. Rank Up ----------
PAGES["guides/rank-up/index.html"] = {
    "path": "guides/rank-up/index.html",
    "title": G + " Rank Up – Quando Subir e Do Que Depende",
    "meta": ("Rank Up em " + G + ": o que o loop oficial inclui, quando um push de rank vale os recursos e por que "
             "não publicamos tabela de custo ou multiplicador."),
    "pill": "Guias", "h1": G + " Rank Up",
    "lead": ("Subir de rank é um dos dois passos de poder do loop oficial. Este guia é sobre o momento certo — e "
             "sobre ser honesto que os custos dependem da versão."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Rank Up", "/pt/guides/rank-up/")],
    "sections": [
        ("p", "O loop oficial de " + G + " inclui <strong>Rank Up</strong> como passo separado, depois de você "
              "desbloquear Avatares, Armas e itens raros. Essa posição importa: subir de rank é um passo de poder "
              "que você toma quando a economia aguenta, não uma meta do primeiro dia."),
        ("h2", "Para que serve o rank"),
        ("ul", [
            "<strong>É passo de poder, não sistema lateral</strong> — o loop oficial o coloca junto das melhorias, depois da camada de desbloqueio.",
            "<strong>Concorre pelos mesmos recursos</strong> que <a href=\"/pt/guides/upgrades/\">Melhorias</a>, <a href=\"/pt/wiki/avatars/\">Avatares</a> e <a href=\"/pt/wiki/weapons/\">Armas</a> — por isso o momento é toda a questão.",
            "<strong>Depende da versão</strong> — escadas de rank são rebalanceadas, então custos e multiplicadores são reconferidos em vez de memorizados.",
        ]),
        ("h2", "Quando um push de rank vale a pena"),
        ("ol", [
            "<strong>Sua renda está estável</strong> — você sabe mais ou menos quanto recurso ganha por sessão. <a href=\"/pt/guides/energy/\">Energia</a>",
            "<strong>Seu elenco não é a parede</strong> — se as lutas falham pelo que você tem, equipamento e Companions vêm primeiro. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Você aguenta o próximo nível de custo</strong> — subir de rank adianta custo; se o próximo nível te travar, você trocou uma subida lenta por um travamento duro.",
            "<strong>Você não está no meio de uma linha de melhorias</strong> — termine. Linhas abandonadas são o clássico ralo do meio de jogo. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
        ]),
        ("h2", "Quando esperar"),
        ("ul", [
            "<strong>Logo depois de uma atualização grande</strong> — a linha atual marcada CLASS TREE é exatamente o tipo de mudança que mexe no valor de classe e rank. <a href=\"/pt/updates/\">Atualizações</a>",
            "<strong>Quando há onda de códigos ativa</strong> — recompensas grátis mudam quanto você precisa farmar. <a href=\"/pt/codes/\">Códigos</a>",
            "<strong>Quando seu gargalo é desafio, não atributo</strong> — isso é problema de equipamento; vá para <a href=\"/pt/guides/secret-boss-locations/\">farm de boss</a> ou <a href=\"/pt/guides/raids/\">Raids</a>.",
        ]),
        ("h2", "O que não publicamos sobre rank"),
        ("p", "Tabelas de custo de rank, multiplicadores por rank, valores de requisito e o número exato de ranks "
              "ficam retidos de propósito. Várias páginas secundárias discordam entre si nesses números, e discordar "
              "é pista, não fato. Quando uma fonte atual puder sustentar, esta página ganha tabela datada — até lá "
              "continua um guia de decisão."),
        ("note", "Se você levar só uma coisa desta página: suba de rank quando sua economia aguentar o próximo "
                 "nível, não quando o botão aparecer."),
    ],
    "faq": [
        ("Quando subir de rank em " + G + "?", "Quando sua renda estiver estável, o elenco não estiver falhando e você aguentar o próximo nível de custo. Se uma linha de melhoria ou equipamento está pela metade, termine antes."),
        ("Quanto custa subir de rank em " + G + "?", "Nenhuma tabela de custo verificada é publicada aqui. Fontes secundárias discordam e os custos mudam com atualizações. Trate tabela sem data como não verificada."),
        ("Subir de rank deixa mais forte que melhorias?", "O loop oficial trata Rank Up e Melhorias como dois passos de poder que competem pelos mesmos recursos. Qual compensa mais depende do seu gargalo atual."),
        ("Devo subir de rank logo após uma atualização?", "Normalmente espere. Atualizações — a linha atual é marcada CLASS TREE — são exatamente quando valores de classe e rank se movem."),
    ],
    "related": [("Melhorias", "/pt/guides/upgrades/", "O outro passo de poder"),
                ("Guia de Progressão", "/pt/guides/progression/", "Qual parede atacar"),
                ("Atualizações", "/pt/updates/", "Por que valores mudam")],
}

# ---------- 10. Upgrades ----------
PAGES["guides/upgrades/index.html"] = {
    "path": "guides/upgrades/index.html",
    "title": "Anime Breaker Melhorias – Framework de Prioridades",
    "meta": "Melhores upgrades em Anime Breaker como framework de priorização, sem tier list congelada: o que alimentar primeiro e por que a ordem muda.",
    "pill": "Guias", "h1": G + " Melhorias",
    "lead": ("Um framework de prioridade aplicável à sua conta agora — porque a 'melhor melhoria' num jogo de Roblox "
             "é um alvo móvel."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Melhorias", "/pt/guides/upgrades/")],
    "sections": [
        ("p", "Melhorias são o segundo passo de poder do loop oficial de " + G + ", ao lado do Rank Up, depois da "
              "camada de desbloqueio. Muita gente busca 'melhores melhorias' esperando lista ranqueada; a resposta "
              "honesta é que uma lista certa nesta semana fica errada no próximo rebalanceamento. Então aqui vai a "
              "lógica de decisão."),
        ("h2", "O teste de prioridade, em ordem"),
        ("ol", [
            "<strong>O que está falhando?</strong> Nomeie o conteúdo que você não consegue limpar. Uma melhoria que não muda esse resultado não é prioridade, seja qual for a raridade.",
            "<strong>Qual elo está mais fraco?</strong> Dano (lutas e farm), sobrevivência ou fluxo de recursos. Alimente o mais fraco. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>O que compõe?</strong> Entre duas opções, escolha a que acelera as próximas sessões — normalmente a que melhora sua rota de farm.",
            "<strong>O que é mais barato por passo?</strong> Curvas de custo diferem; uma linha barata que você termina bate uma cara que você abandona. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>O que sobrevive à próxima atualização?</strong> Melhorias ligadas ao núcleo do loop (Companions, armas que você usa) mantêm valor entre patches.",
        ]),
        ("h2", "O que melhorar primeiro como iniciante"),
        ("ul", [
            "<strong>Sua configuração de farm</strong> — tudo que aumenta o recurso produzido por sessão. <a href=\"/pt/guides/energy/\">Energia</a>",
            "<strong>Sua linha principal de Companion</strong> — são eles que entram em combate no loop oficial. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Uma arma que você ainda vai usar depois</strong> — espalhar melhorias por várias armas é o desperdício inicial mais comum. <a href=\"/pt/wiki/weapons/\">Armas</a>",
        ]),
        ("h2", "O que deixar parado"),
        ("ul", [
            "<strong>Qualquer coisa comprada para um evento único</strong> — a não ser que ese evento seja sua parede atual.",
            "<strong>Segunda e terceira linha de arma</strong> — até a primeira limpar o conteúdo que te trava.",
            "<strong>Desbloqueios cosméticos</strong> — não movem o loop. <a href=\"/pt/wiki/avatars/\">Avatares</a> valem o desbloqueio, mas não ao custo de uma linha de ataque travada.",
        ]),
        ("h2", "Por que não existe tabela ranqueada de 'melhores melhorias'"),
        ("p", "Porque uma tabela ranqueada exige números por nível, e nenhuma fonte atual publica um conjunto "
              "consistente para este build. Páginas secundárias se contradizem em multiplicadores e custos. "
              "Publicar um ranking confiante sobre fontes que discordam seria inventar fato, então esta página "
              "entrega o framework e data a própria checagem."),
        ("note", "Sensibilidade: após um patch de balanceamento, rode o teste de prioridade de novo. Seu elo mais "
                 "fraco pode ter mudado mesmo que sua conta não tenha."),
    ],
    "faq": [
        ("Quais são as melhores melhorias em " + G + "?", "As que resolvem seu gargalo atual: produção de farm primeiro na maioria das contas, depois uma linha de Companion e depois uma linha de arma. Ranking estático ficaria errado após o próximo rebalanceamento."),
        ("Melhoro ou subo de rank primeiro em " + G + "?", "Os dois são passos de poder que dividem os mesmos recursos. Melhore quando a renda está estável; suba de rank quando a economia aguenta o próximo nível de custo. Termine uma linha antes de abrir a outra."),
        ("Vale melhorar muitas armas?", "Não, não no começo. Uma linha de arma que funciona bate três inacabadas, e valores de arma são justamente o que atualizações mudam."),
        ("Com que frequência as prioridades mudam em " + G + "?", "Sempre que o jogo é rebalanceado — a linha atual é marcada CLASS TREE. Reconfira após cada atualização grande."),
    ],
    "related": [("Rank Up", "/pt/guides/rank-up/", "O momento do outro passo de poder"),
                ("Recursos", "/pt/wiki/resources/", "O que as melhorias consomem"),
                ("Armas", "/pt/wiki/weapons/", "Em qual linha se comprometer")],
}

# ---------- 11. Cards ----------
PAGES["wiki/cards/index.html"] = {
    "path": "wiki/cards/index.html",
    "title": G + " Cartas – Como as Cartas Liberam Companions",
    "meta": ("Cartas em " + G + ": a camada oficial de aquisição. O que as Cartas fazem, como se ligam à Energia e "
             "aos Companions e por que não publicamos taxas."),
    "pill": "Wiki", "h1": G + " Cartas",
    "lead": ("As Cartas são a ponte oficial entre Energia e Companions — a camada de aquisição do loop."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Cartas", "/pt/wiki/cards/")],
    "sections": [
        ("p", "Na descrição oficial de " + G + " o loop diz: ganhe Energia e então <strong>abra Cartas para "
              "conseguir Companions</strong>. Então as Cartas não são colecionável lateral — são o mecanismo que "
              "converte sua Energia no elenco com o qual você luta."),
        ("h2", "O que as Cartas fazem"),
        ("table", {"head": ["Pergunta", "Resposta", "Confiança"],
                   "rows": [
                       ["Para que servem as Cartas?", "Abrir Cartas é o caminho oficial para conseguir Companions.", "VERIFIED (página oficial)"],
                       ["O que custam?", "São o lado de gasto do passo de Energia — a Energia é o que se ganha primeiro.", "VERIFIED (página oficial)"],
                       ["Como se abrem?", "Dentro da experiência; a interface muda entre builds, use a atual.", "OBSERVED"],
                       ["Quais são as taxas de pull?", "Não publicadas aqui — nenhuma fonte atual sustenta tabela de taxas.", "UNVERIFIED"],
                   ]}),
        ("h2", "As Cartas no loop"),
        ("ol", [
            "<strong>Ganhe Energia</strong> — a entrada do loop. <a href=\"/pt/guides/energy/\">Energia</a>",
            "<strong>Abra Cartas</strong> — gaste Energia; é a rota oficial para novos Companions.",
            "<strong>Coloque os Companions em campo</strong> — o que sai das Cartas é o que luta por você. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Converta combate em recursos</strong> — o que financia todos os passos seguintes. <a href=\"/pt/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Como abrir Cartas com bom senso"),
        ("ul", [
            "<strong>Abra em lotes</strong> — um conjunto de resultados mostra o que falta no elenco; um pull isolado não mostra quase nada.",
            "<strong>Julgue o elenco, não o pull</strong> — um lote cheio de repetidos só é problema se não melhora sua rota de farm.",
            "<strong>Não persiga taxas que você não vê</strong> — se um site cita percentuais sem fonte e sem data, trate como chute.",
        ]),
        ("note", "Deliberadamente ausente desta página: taxas de pull, tabelas de raridade, quantidade de cartas e "
                 "chances de Companions específicos. Esses números mudam com atualizações e divergem entre fontes "
                 "secundárias."),
    ],
    "faq": [
        ("O que são Cartas em " + G + "?", "A camada oficial de aquisição do loop. Você ganha Energia, abre Cartas, e as Cartas são como você consegue Companions para lutar."),
        ("Como conseguir Cartas em " + G + "?", "As Cartas estão ligadas ao passo de Energia na descrição oficial — a Energia é o primeiro recurso do loop, e abrir Cartas é no que ela é gasta."),
        ("Quais são as taxas de pull em " + G + "?", "Não publicadas aqui. Nenhuma fonte atual sustenta uma tabela consistente, e taxas são exatamente o que atualizações mudam. Abra em lotes e julgue o elenco."),
        ("Repetidos importam?", "Podem importar, mas o teste útil é se o lote melhorou sua rota de farm ou a cobertura do elenco — não quantos repetidos apareceram."),
    ],
    "related": [("Companions", "/pt/wiki/companions/", "O que as Cartas dão"),
                ("Energia", "/pt/guides/energy/", "O recurso que as Cartas consomem"),
                ("Guia para Iniciantes", "/pt/guides/beginner-guide/", "Cartas na primeira sessão")],
}

# ---------- 12. Companions ----------
PAGES["wiki/companions/index.html"] = {
    "path": "wiki/companions/index.html",
    "title": "Anime Breaker Companions – Como Conseguir",
    "meta": ("Companions em " + G + ": como o loop oficial os produz via Cartas, como são usados em combate e como "
             "diferem dos Avatares."),
    "pill": "Wiki", "h1": G + " Companions",
    "lead": ("Companions são o resultado de combate do loop oficial — o que sai das Cartas e o que você coloca em "
             "campo."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Companions", "/pt/wiki/companions/")],
    "sections": [
        ("p", "No loop oficial de " + G + " você <strong>abre Cartas para conseguir Companions</strong> e então "
              "<strong>combate inimigos por recursos</strong>. Os Companions ficam entre esses dois passos: são o "
              "resultado do seu gasto de Energia e o que carrega seu combate e seu farm."),
        ("h2", "Como conseguir Companions"),
        ("ol", [
            "<strong>Ganhe Energia</strong> — a entrada do loop. <a href=\"/pt/guides/energy/\">Energia</a>",
            "<strong>Abra Cartas</strong> — a rota oficial de aquisição. <a href=\"/pt/wiki/cards/\">Cartas</a>",
            "<strong>Coloque em campo</strong> — na descrição do loop, eles já são utilizáveis em combate.",
            "<strong>Melhore o conjunto com o tempo</strong> — melhorias e desbloqueios aumentam sua saída. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
        ]),
        ("h2", "Companion vs Avatar"),
        ("table", {"head": ["Aspecto", "Companions", "Avatares"],
                   "rows": [
                       ["Papel no loop", "Obtidos via Cartas, usados para lutar e farmar.", "Listados como desbloqueio junto de Armas e itens raros."],
                       ["Como obter", "Abrindo Cartas (oficial).", "Desbloqueados pela progressão; fontes da comunidade citam rotas de farm adicionais que este site não verificou."],
                       ["O que mudam", "Seu dano de combate e farm.", "O que você joga, por isso são tratados como coleção e identidade, além de poder."],
                       ["Confiança", "VERIFIED (página oficial)", "VERIFIED para o desbloqueio; PARTIAL para as mecânicas"],
                   ]}),
        ("h2", "Usar bem os Companions"),
        ("ul", [
            "<strong>Cubra lacunas</strong> — um lote de Cartas costuma deixar buracos; preencha funções que faltam em vez de empilhar o que já tem.",
            "<strong>Alimente os que ficam</strong> — melhoria gasta em Companion que você vai trocar é o desperdício mais comum. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Case com o conteúdo</strong> — rotas de farm e desafios premiam perfis diferentes; mantenha um conjunto de farm e um de luta. <a href=\"/pt/guides/progression/\">Progressão</a>",
        ]),
        ("note", "Multiplicadores de Companion, tier lists e taxas de pull não são publicados aqui: nenhuma fonte "
                 "atual sustenta um conjunto consistente, e 'melhor Companion' muda a cada rebalanceamento. A página "
                 "de <a href=\"/pt/wiki/avatars/\">Avatares</a> segue a mesma regra."),
    ],
    "faq": [
        ("O que são Companions em " + G + "?", "As unidades que você consegue abrindo Cartas no loop oficial, e o que você coloca em campo para lutar e ganhar recursos."),
        ("Como conseguir Companions em " + G + "?", "Abra Cartas. A descrição oficial coloca as Cartas diretamente antes dos Companions, e a Energia é o que se gasta para abrir."),
        ("Qual a diferença entre Companion e Avatar em " + G + "?", "Companions são seu elenco, obtidos por Cartas e usados em combate. Avatares são um desbloqueio do mesmo loop oficial e funcionam mais como camada de identidade e progressão."),
        ("Qual é o melhor Companion em " + G + "?", "Nenhuma tier list é publicada aqui. 'Melhor' segue o patch atual e o conteúdo que você roda, então a pergunta útil é qual função falta no seu elenco."),
    ],
    "related": [("Cartas", "/pt/wiki/cards/", "De onde vêm os Companions"),
                ("Avatares", "/pt/wiki/avatars/", "A outra camada de desbloqueio"),
                ("Melhorias", "/pt/guides/upgrades/", "Em quais investir")],
}

# ---------- 13. Avatars ----------
PAGES["wiki/avatars/index.html"] = {
    "path": "wiki/avatars/index.html",
    "title": G + " Avatares – Desbloqueio, Evolução e Farm",
    "meta": ("Avatares em " + G + ": a camada oficial de desbloqueio. Como são desbloqueados e evoluídos, o que a "
             "comunidade relata sobre farm e quais valores ficam fora."),
    "pill": "Wiki", "h1": G + " Avatares",
    "lead": ("Avatares são a camada de desbloqueio do loop — o que você joga e a coleção mais farmada."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Avatares", "/pt/wiki/avatars/")],
    "sections": [
        ("p", "O loop oficial de " + G + " diz que você <strong>desbloqueia Avatares, Armas e itens raros</strong> "
              "quando suas lutas já produzem recursos. Avatares ficam, portanto, no meio do loop: não são o que você "
              "começa usando, mas também não são para ignorar."),
        ("h2", "Desbloquear Avatares"),
        ("ol", [
            "<strong>Construa o fluxo de recursos primeiro</strong> — a camada de desbloqueio é financiada por combate e farm. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Siga a rota de desbloqueio</strong> — na descrição oficial, Avatares são ganhos na progressão dentro da experiência.",
            "<strong>Espere uma coleção, não uma escolha</strong> — o loop fala em Avatares no plural, então montar conjunto é a intenção.",
        ]),
        ("h2", "Evoluir e usar Avatares"),
        ("ul", [
            "<strong>Trate cada Avatar como linha própria</strong> — investir por completo em um bate dividir entre vários. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Mantenha um Avatar de farm e um de luta</strong> — as funções raramente coincidem. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Teste antes de comprometer</strong> — com balanceamento, o Avatar forte do patch passado pode não ser depois do próximo. <a href=\"/pt/updates/\">Atualizações</a>",
        ]),
        ("h2", "Rotas de farm relatadas pela comunidade"),
        ("p", "Páginas secundárias descrevem rotas de obtenção de Avatar com lutas repetidas contra conjuntos "
              "específicos de NPCs, e algumas listam funções e níveis máximos <em>estimados</em>. Isso são pistas de "
              "descoberta: as estimativas vêm de cobertura de terceiros, discordam entre si e são datadas. Esta "
              "página não as repete como fatos."),
        ("note", "Fora de propósito: multiplicadores de Avatar, chances exatas de drop ou desbloqueio, valores de "
                 "nível máximo e rankings por Avatar. Cada um depende da versão e é inconsistente entre fontes. "
                 "<a href=\"/pt/guides/secret-boss-locations/\">Caça a boss</a> é tratada separadamente, incluindo "
                 "os valores que nos recusamos a congelar lá."),
    ],
    "faq": [
        ("Como conseguir Avatares em " + G + "?", "Eles são a camada de desbloqueio do loop oficial: quando suas lutas produzem recursos, Avatares, Armas e itens raros ficam alcançáveis pela progressão dentro da experiência."),
        ("Dá para subir de nível os Avatares em " + G + "?", "Avatares evoluem como parte da camada de progressão, e melhorias são um dos dois passos de poder do loop oficial. Valores por nível não são publicados aqui porque mudam entre atualizações."),
        ("Como farmar Avatares em " + G + "?", "Fontes da comunidade descrevem lutas repetidas contra NPCs como rota de farm. Isso é REPORTED, não verificado, e as chances citadas ao lado são estimativas — então esta página descreve a abordagem, não números inventados."),
        ("Qual Avatar é o mais forte em " + G + "?", "Nenhum ranking é publicado aqui. Multiplicadores discordam entre fontes e se movem com patches, então o guia honesto é: escolha uma linha, termine e reavalie após uma atualização."),
    ],
    "related": [("Companions", "/pt/wiki/companions/", "Companion vs Avatar comparados"),
                ("Energia", "/pt/guides/energy/", "Financiando a camada de desbloqueio"),
                ("Armas", "/pt/wiki/weapons/", "O outro desbloqueio do loop")],
}

# ---------- 14. Weapons ----------
PAGES["wiki/weapons/index.html"] = {
    "path": "wiki/weapons/index.html",
    "title": G + " Armas – Aquisição e Papel no Loop",
    "meta": ("Armas em " + G + ": como o loop oficial as desbloqueia, como escolher em qual se comprometer e por "
             "que não publicamos tabela de status."),
    "pill": "Wiki", "h1": G + " Armas",
    "lead": ("As Armas são a segunda metade da camada oficial de desbloqueio — e onde novatos mais desperdiçam "
             "recursos em linhas inacabadas."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Armas", "/pt/wiki/weapons/")],
    "sections": [
        ("p", "O loop oficial diz que você <strong>desbloqueia Avatares, Armas e itens raros</strong> quando o "
              "combate já produz recursos. As Armas ficam, portanto, atrás da mesma economia dos Avatares: ganhe "
              "primeiro, desbloqueie depois."),
        ("h2", "Como as Armas se encaixam"),
        ("table", {"head": ["Pergunta", "Resposta", "Confiança"],
                   "rows": [
                       ["As Armas estão no loop oficial?", "Sim — citadas no passo de desbloqueio junto de Avatares e itens raros.", "VERIFIED (página oficial)"],
                       ["Como obtê-las?", "Pela progressão dentro da experiência; fontes da comunidade também relatam rotas ligadas a bosses.", "PARTIAL (oficial no loop, REPORTED nas ligações com boss)"],
                       ["O que mudam?", "Sua saída de combate — o que alimenta o passo de recursos.", "OBSERVED"],
                       ["Publicam tabelas de status?", "Não. Dano, escalonamento e custos de melhoria dependem da versão e são inconsistentes entre fontes.", "UNVERIFIED"],
                   ]}),
        ("h2", "Escolhendo uma linha de arma"),
        ("ol", [
            "<strong>Escolha uma</strong> — comprometa-se com uma linha até limpar o conteúdo que te trava. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Olhe a fonte, não o print</strong> — ranking de arma sem data é boato; armas são rebalanceadas. <a href=\"/pt/updates/\">Atualizações</a>",
            "<strong>Case com sua rota</strong> — arma que acelera o farm se paga mais rápido que uma que ganha uma luta. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Depois persiga o drop raro</strong> — bosses e desafios guardam os itens que quebram o teto. <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a> · <a href=\"/pt/guides/raids/\">Raids</a>",
        ]),
        ("h2", "Armas, bosses e raids"),
        ("p", "Cobertura secundária liga armas de nível alto a conteúdo de boss e raid. Este site mantém isso como "
              "liga REPORTED, não como tabela fixa: <a href=\"/pt/wiki/accessories/\">Acessórios</a> cobre o que "
              "podemos dizer sobre drops de boss, e <a href=\"/pt/guides/raids/\">Raids</a> cobre o nível de desafio."),
        ("note", "Fora de propósito: valores de dano, curvas de escalonamento, tabelas de custo de melhoria e "
                 "rankings de tier. Os quatro são exatamente os campos que quebram quando o cliente é "
                 "rebalanceado."),
    ],
    "faq": [
        ("Como conseguir Armas em " + G + "?", "Armas estão na camada oficial de desbloqueio do loop: quando as lutas produzem recursos, Armas, Avatares e itens raros ficam alcançáveis pela progressão."),
        ("Qual é a melhor arma em " + G + "?", "Nenhum ranking é publicado aqui. Valores de arma mudam com patches e divergem entre fontes, então a regra útil é comprometer-se com uma linha e reconferir após atualização."),
        ("Bosses dropam armas em " + G + "?", "Fontes secundárias relatam rotas de arma e equipamento ligadas a bosses. Isso é REPORTED, não verificado, então descrevemos a rota sem imprimir taxas."),
        ("Melhoro armas ou Avatares primeiro?", "O que resolver sua parede atual. Se as lutas falham por dano, melhore a linha de arma; se você não alcança o conteúdo, o desbloqueio vem antes."),
    ],
    "related": [("Bosses Secretos", "/pt/guides/secret-boss-locations/", "Onde estão os drops raros"),
                ("Acessórios", "/pt/wiki/accessories/", "Equipamento vindo de boss"),
                ("Melhorias", "/pt/guides/upgrades/", "Comprometer-se com uma linha")],
}

# ---------- 15. Secret Boss Locations ----------
PAGES["guides/secret-boss-locations/index.html"] = {
    "path": "guides/secret-boss-locations/index.html",
    "title": G + " Bosses Secretos – Como Encontrar e Farmar",
    "meta": ("Bosses secretos em " + G + ": como abordar, para que serve o farm e por que nenhum HP ou taxa de drop "
             "é congelado nesta página."),
    "pill": "Guias", "h1": G + " Bosses Secretos",
    "lead": ("Um guia de encontrar e farmar baseado em abordagem e propósito — não em HP congelado ou chances "
             "copiadas."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Bosses Secretos", "/pt/guides/secret-boss-locations/")],
    "sections": [
        ("p", "Caçar bosses é como jogadores quebram o teto do fim de jogo em " + G + ": o loop oficial manda "
              "combater inimigos por recursos e desbloquear itens raros, e a cobertura da comunidade trata bosses "
              "secretos como a versão concentrada disso. A diferença entre uma boa rota de boss e uma ruim é mira, "
              "não sorte."),
        ("h2", "Para que servem os bosses secretos"),
        ("ul", [
            "<strong>Farm concentrado</strong> — um alvo em vez de uma rota, por isso jogadores de fim de jogo gastam sessões neles.",
            "<strong>Drops que quebram o teto</strong> — a camada de equipamento e itens raros que mantém a progressão andando. <a href=\"/pt/wiki/accessories/\">Acessórios</a>",
            "<strong>Um portão para o nível de desafio</strong> — o que você farma alimenta <a href=\"/pt/guides/raids/\">Raids</a> e o loop do <a href=\"/pt/guides/trial/\">Trial</a>.",
        ]),
        ("h2", "Encontrar bosses: o método honesto"),
        ("ol", [
            "<strong>Avance até o mundo abrir</strong> — acesso a boss é liberado pela progressão. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Explore o mundo atual, não um print antigo</strong> — layouts e áreas de spawn mudam entre atualizações. <a href=\"/pt/wiki/worlds/\">Mundos</a>",
            "<strong>Acompanhe a linha de atualização</strong> — a marca CLASS TREE indica linha ativa, e é quando conteúdo de boss se move. <a href=\"/pt/updates/\">Atualizações</a>",
            "<strong>Registre o que encontrar</strong> — sua própria nota datada vale mais que uma lista de coordenadas copiada.",
        ]),
        ("h2", "Como farmar um boss com eficiência"),
        ("ul", [
            "<strong>Leve um conjunto de farm, não de vitrine</strong> — repetição importa mais que uma vitória bonita. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Corrija a rota antes dos atributos</strong> — se a limpeza demora, o gargalo costuma ser a abordagem.",
            "<strong>Pare quando o drop deixa de pagar</strong> — quando você tem a melhoria que veio buscar, o próximo alvo é outro.",
        ]),
        ("h2", "O que esta página não publica"),
        ("p", "Valores de HP, timers de spawn ou respawn, percentuais exatos de drop e listas de coordenadas "
              "copiadas de outras wikis. Páginas secundárias citam esses números e discordam entre si — discordância "
              "não é fonte. Quando os valores puderem ser verificados no cliente atual, entram aqui com data; até lá, "
              "o método acima é a parte durável."),
        ("note", "A mesma regra vale para <a href=\"/pt/wiki/accessories/\">Acessórios</a>, que cobre para que servem "
                 "os drops de boss em vez de prometer uma tabela."),
    ],
    "faq": [
        ("Onde ficam os bosses secretos em " + G + "?", "O acesso é liberado pela progressão e o layout dos mundos muda entre atualizações, então não publicamos lista de coordenadas congelada. O método: avance, explore o mundo atual, acompanhe a atualização e registre o que encontrar."),
        ("Como farmar bosses em " + G + "?", "Use um conjunto repetível de farm em vez de vitrine, corrija a rota de abordagem antes do dano e siga para o próximo alvo quando conseguir a melhoria desejada."),
        ("O que bosses dropam em " + G + "?", "Bosses são a fonte relatada de equipamento e itens raros que quebram o teto do fim de jogo, alimentando Acessórios e Raids. Taxas exatas não são impressas de propósito."),
        ("As posições de boss mudam após atualizações?", "Assuma que sim. Experiências do Roblox reformulam mundos entre atualizações, e o título atual carrega a marca CLASS TREE — exatamente quando esse tipo de conteúdo se move."),
    ],
    "related": [("Acessórios", "/pt/wiki/accessories/", "Para que servem os drops de boss"),
                ("Mundos", "/pt/wiki/worlds/", "Onde você está caçando"),
                ("Raids", "/pt/guides/raids/", "O nível depois dos bosses")],
}

# ---------- 16. Accessories ----------
PAGES["wiki/accessories/index.html"] = {
    "path": "wiki/accessories/index.html",
    "title": "Anime Breaker Acessórios – Drops de Boss",
    "meta": ("Acessórios em " + G + ": a camada de equipamento vinda de bosses, como decidir o que manter e "
             "melhorar, e por que taxas e status ficam fora."),
    "pill": "Wiki", "h1": G + " Acessórios",
    "lead": ("Acessórios são a camada de equipamento que sai do farm de boss — e onde contas de fim de jogo gastam "
             "seus recursos."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Acessórios", "/pt/wiki/accessories/")],
    "sections": [
        ("p", "O loop oficial de " + G + " termina o passo de desbloqueio com <strong>itens raros</strong> e te manda "
              "para as Raids; a cobertura da comunidade coloca os acessórios exatamente nessa faixa, vindos das "
              "lutas de boss descritas na página de <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a>."),
        ("h2", "De onde vêm os acessórios"),
        ("table", {"head": ["Fonte", "Status", "Observação"],
                   "rows": [
                       ["Drops de boss", "REPORTED", "Cobertura secundária liga acessórios ao farm de boss; tratado como a faixa que quebra tetos de fim de jogo."],
                       ["Passo de itens raros", "VERIFIED (página oficial)", "O loop oficial cita itens raros na camada de desbloqueio junto de Avatares e Armas."],
                       ["Recompensas de raid", "REPORTED", "Conteúdo de raid é verificado como nível de desafio; o conteúdo específico das recompensas não é publicado aqui."],
                   ]}),
        ("h2", "Decidir o que manter e melhorar"),
        ("ol", [
            "<strong>Pergunte o que resolve</strong> — um acessório que não muda uma luta que você perde é peça de coleção por enquanto. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Prefira o que compõe</strong> — equipamento que acelera o farm se paga em todas as sessões futuras.",
            "<strong>Melhore um slot por completo</strong> — espalhar recursos entre acessórios é a versão de fim de jogo do erro de iniciante. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Reconfira após atualizações</strong> — valores de equipamento estão entre os primeiros a serem rebalanceados. <a href=\"/pt/updates/\">Atualizações</a>",
        ]),
        ("h2", "Acessórios, amuletos e armas"),
        ("ul", [
            "<strong><a href=\"/pt/wiki/amulets/\">Amuletos</a></strong> — slot adicional relatado nos mesmos estágios de gargalo, com a mesma regra: nada de nomes ou valores inventados.",
            "<strong><a href=\"/pt/wiki/weapons/\">Armas</a></strong> — a metade de dano da camada de equipamento.",
            "<strong><a href=\"/pt/guides/raids/\">Raids</a></strong> — onde o que você montou é testado.",
        ]),
        ("note", "Fora de propósito: taxas de drop de acessório, valores por item, tabelas de custo de melhoria e "
                 "listas de melhor do slot. Os quatro dependem da versão e são inconsistentes entre fontes."),
    ],
    "faq": [
        ("O que são acessórios em " + G + "?", "A camada de equipamento que fica junto dos itens raros citados no passo oficial de desbloqueio, e que a cobertura da comunidade origina do farm de boss."),
        ("Como conseguir acessórios em " + G + "?", "As rotas relatadas são drops de boss e a camada de progressão de itens raros; conteúdo de raid é verificado como nível de desafio, mas o conteúdo das recompensas não é publicado aqui."),
        ("Qual acessório é o melhor em " + G + "?", "Nenhuma lista de melhor do slot é publicada. O teste prático é se o acessório muda uma luta que você perde hoje — caso contrário, é peça de coleção."),
        ("Melhoro acessórios ou armas primeiro?", "Resolva a parede atual: problema de dano aponta para armas, problema de teto para equipamento. Comprometa-se com um slot por vez."),
    ],
    "related": [("Bosses Secretos", "/pt/guides/secret-boss-locations/", "De onde vêm os drops"),
                ("Amuletos", "/pt/wiki/amulets/", "O próximo slot de equipamento"),
                ("Raids", "/pt/guides/raids/", "Testando o que você montou")],
}

# ---------- 17. Raids ----------
PAGES["guides/raids/index.html"] = {
    "path": "guides/raids/index.html",
    "title": "Anime Breaker Raids – Acesso, Ondas e Recompensas",
    "meta": ("Raids em " + G + ": o nível de desafio do loop oficial. Acesso e estrutura de ondas, como tratar "
             "recompensas e por que custos de ticket ficam fora."),
    "pill": "Guias", "h1": G + " Raids",
    "lead": ("As Raids são onde o loop termina — o ponto em que tudo que você farmou é testado de uma vez."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Raids", "/pt/guides/raids/")],
    "sections": [
        ("p", "As Raids são citadas explicitamente no loop oficial de " + G + ", depois dos passos de poder. Essa "
              "ordem é a mensagem: raids não são porta de entrada, são o nível para o qual sua conta se forma."),
        ("h2", "Como as raids se encaixam no loop"),
        ("ol", [
            "<strong>Forme-se no farm</strong> — você precisa de um loop estável antes que o acesso a raid faça sentido. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Leve seu conjunto real</strong> — Companions, Armas, Avatares e equipamento importam aqui de um jeito que o farm comum não exige. <a href=\"/pt/wiki/companions/\">Companions</a>",
            "<strong>Leia a estrutura de ondas</strong> — a cobertura da comunidade descreve raids em ondas; cada onda é um checkpoint do que falta na conta. <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a>",
            "<strong>Gaste as recompensas com critério</strong> — o que sai da raid deve alimentar a parede que te parou. <a href=\"/pt/wiki/accessories/\">Acessórios</a>",
        ]),
        ("h2", "Acesso, tickets e custo"),
        ("p", "Fontes da comunidade descrevem o acesso a raid liberado pela progressão e por um custo de entrada "
              "consumível. Este site trata isso como estrutura REPORTED e não imprime preços de ticket, número de "
              "ondas ou tabelas de recompensa — são valores entre os mais rebalanceados numa experiência do Roblox, "
              "e as fontes secundárias discordam entre si."),
        ("h2", "Planejando suas primeiras raids"),
        ("ul", [
            "<strong>Corrija a onda que falha, não a raid inteira</strong> — identifique a onda que encerra sua corrida e o que ela exige.",
            "<strong>Mantenha uma rota de farm ao lado</strong> — raids consomem recursos além de dar. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Não troque tudo de uma vez</strong> — uma mudança por tentativa mostra o que funcionou. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Acompanhe a linha de atualização</strong> — o ajuste de raid se move com atualizações. <a href=\"/pt/updates/\">Atualizações</a>",
        ]),
        ("note", "Camadas relacionadas: <a href=\"/pt/wiki/amulets/\">Amuletos</a> e "
                 "<a href=\"/pt/wiki/resources/\">Recursos</a> para o que as raids consomem e devolvem, e "
                 "<a href=\"/pt/guides/trial/\">Trial</a> para o outro loop de desafio."),
    ],
    "faq": [
        ("Como liberar as raids em " + G + "?", "As raids ficam no fim do loop oficial, depois dos passos de poder. Na prática: um loop estável de recursos e um conjunto capaz de limpar conteúdo de desafio antes que o acesso compense."),
        ("Quantas ondas têm as raids de " + G + "?", "A cobertura da comunidade descreve raids em ondas, mas o número exato não é publicado aqui — muda com atualizações e as fontes discordam."),
        ("Raids custam tickets em " + G + "?", "Um custo de entrada consumível é relatado. Nenhum preço é impresso aqui pelo mesmo motivo: é valor frequentemente rebalanceado."),
        ("Em que gastar as recompensas de raid?", "Na parede que te parou. Se uma onda específica encerrou sua corrida, alimente a correção dela em vez do próximo desbloqueio."),
    ],
    "related": [("Amuletos", "/pt/wiki/amulets/", "Slot de equipamento vizinho"),
                ("Recursos", "/pt/wiki/resources/", "O que as raids consomem"),
                ("Trial", "/pt/guides/trial/", "O outro loop de desafio")],
}

# ---------- 18. Trial ----------
PAGES["guides/trial/index.html"] = {
    "path": "guides/trial/index.html",
    "title": "Anime Breaker Trial (Corredor) – Loop e Recompensas",
    "meta": ("O loop de desafio Trial / corredor em " + G + ": como funciona a estrutura da corrida, para que serve "
             "e como transformar as recompensas em progressão."),
    "pill": "Guias", "h1": G + " Trial",
    "lead": ("O Trial (muitas vezes chamado de corredor) é um loop de desafio repetível — um teste mensurável do que "
             "você montou."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("Trial", "/pt/guides/trial/")],
    "sections": [
        ("p", "O Trial é tratado pela cobertura da comunidade como uma corrida estilo corredor: você avança por "
              "encontros repetidos e a corrida termina quando sua configuração falha. Essa estrutura faz dele o "
              "diagnóstico mais limpo do jogo — a corrida mostra exatamente qual elo do loop está mais fraco."),
        ("h2", "Como funciona o loop do Trial"),
        ("ol", [
            "<strong>Entre e avance</strong> — cada encontro é um checkpoint e não uma luta única de boss.",
            "<strong>Anote onde a corrida acaba</strong> — o encontro que falha nomeia seu gargalo. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Melhore só o elo que falhou</strong> — uma mudança e nova corrida. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Converta recompensas no próximo avanço</strong> — a saída do Trial é para alimentar progressão. <a href=\"/pt/wiki/resources/\">Recursos</a>",
        ]),
        ("h2", "Para que serve o Trial"),
        ("ul", [
            "<strong>Diagnosticar builds</strong> — uma corrida isola o que falta na conta melhor que farm aberto.",
            "<strong>Financiar melhorias de forma repetível</strong> — relatado como fonte de recursos de progressão.",
            "<strong>Ponte para as raids</strong> — a pressão em ondas das <a href=\"/pt/guides/raids/\">Raids</a> fica mais fácil quando você sobrevive a empilhamentos estilo Trial.",
        ]),
        ("h2", "Relatado vs verificado nesta página"),
        ("table", {"head": ["Item", "Status"],
                   "rows": [
                       ["Trial/corredor existe como loop de desafio repetível", "REPORTED (cobertura secundária de gameplay)"],
                       ["Estrutura de corrida em ondas/empilhamento", "REPORTED"],
                       ["Tabelas exatas de recompensa e custos por corrida", "Não publicados aqui — dependem da versão e são inconsistentes"],
                       ["Posição no loop (nível de desafio ao lado das Raids)", "VERIFIED (a página oficial cita Raids; o Trial é documentado aqui como o loop adjacente)"],
                   ]}),
        ("note", "Como em <a href=\"/pt/wiki/accessories/\">Acessórios</a> e <a href=\"/pt/wiki/amulets/\">Amuletos</a>, "
                 "a mecânica é documentada e os números não. Um valor de Trial certo esta semana pode estar errado "
                 "após a próxima atualização."),
    ],
    "faq": [
        ("O que é o Trial em " + G + "?", "Um loop de desafio repetível, estilo corredor, relatado pela cobertura da comunidade. Você avança por encontros empilhados até sua configuração falhar, o que o torna um bom diagnóstico."),
        ("Como conseguir recompensas no Trial?", "Relatado como fonte de recursos de progressão: você avança até onde sua configuração permite e converte a saída em melhorias para o elo que falhou."),
        ("Trial é o mesmo que raids em " + G + "?", "Não. Raids são citadas no loop oficial como nível de desafio; o Trial é um loop separado e reportado, que compartilha a pressão em ondas e combina com preparação para raid."),
        ("Por que faltam números de recompensa do Trial?", "Porque são rebalanceados e as fontes discordam. Esta página documenta o loop e a lógica de decisão em vez de congelar um valor."),
    ],
    "related": [("Recursos", "/pt/wiki/resources/", "No que as recompensas se transformam"),
                ("Raids", "/pt/guides/raids/", "O nível para o qual ele prepara"),
                ("Guia de Progressão", "/pt/guides/progression/", "Lendo a onda que falha")],
}

# ---------- 19. Amulets ----------
PAGES["wiki/amulets/index.html"] = {
    "path": "wiki/amulets/index.html",
    "title": "Anime Breaker Amuletos – Aquisição e Uso",
    "meta": ("Amuletos em " + G + ": o slot de equipamento relatado na fase de gargalo — para que serve, como "
             "decidir e por que nenhum nome ou status é publicado."),
    "pill": "Wiki", "h1": G + " Amuletos",
    "lead": ("Amuletos são a decisão de equipamento que os jogadores procuram quando melhorias comuns param de mover "
             "a parede."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Amuletos", "/pt/wiki/amulets/")],
    "sections": [
        ("p", "Amuletos aparecem na cobertura da comunidade como uma camada adicional de equipamento que importa no "
              "gargalo do fim de jogo — o ponto em que a conta está confortável no conteúdo normal, mas desafios "
              "específicos, <a href=\"/pt/guides/raids/\">Raids</a> e o <a href=\"/pt/guides/trial/\">Trial</a>, "
              "seguem encerrando corridas. Esta página documenta a decisão, não uma tier list copiada."),
        ("h2", "Quando um amuleto é a resposta certa"),
        ("ul", [
            "<strong>Seu básico está pronto</strong> — armas, uma linha de Companion e uma rota de farm funcionando. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Você perde para a mesma parede repetidamente</strong> — falha repetível indica lacuna de atributo, não azar. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Uma melhoria mudaria esse resultado</strong> — se não mudaria, o amuleto é peça de coleção por enquanto.",
        ]),
        ("h2", "Como abordar a obtenção de amuletos"),
        ("ol", [
            "<strong>Identifique o requisito primeiro</strong> — saiba qual desafio falha antes de farmar a resposta. <a href=\"/pt/guides/secret-boss-locations/\">Bosses Secretos</a>",
            "<strong>Farne uma rota, não um boato</strong> — escolha uma fonte repetível e cronometre, em vez de confiar em tabela de chances sem data.",
            "<strong>Comprometa-se com um</strong> — dividir investimento entre vários amuletos repete o erro clássico do meio de jogo com custo maior. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Reconfira após atualizações</strong> — faixas de equipamento são retocadas, e o título atual carrega a marca CLASS TREE. <a href=\"/pt/updates/\">Atualizações</a>",
        ]),
        ("h2", "Por que esta página não tem lista de amuletos"),
        ("p", "Nomes, valores, origens e custos de melhoria de amuletos estão entre os dados menos consistentemente "
              "documentados na cobertura secundária atual — sites diferentes listam itens diferentes e nenhum data "
              "as tabelas. Sob a regra deste site, discordância é pista e não fato, então a lista fica fora até uma "
              "fonte atual sustentar."),
        ("note", "O mesmo padrão vale para a faixa de equipamento: <a href=\"/pt/wiki/accessories/\">Acessórios</a>, "
                 "<a href=\"/pt/wiki/weapons/\">Armas</a> e <a href=\"/pt/guides/raids/\">Raids</a> documentam "
                 "mecânicas e decisões, deixando números rebalanceados de fora."),
    ],
    "faq": [
        ("O que são amuletos em " + G + "?", "Uma camada adicional de equipamento relatada, que importa no gargalo do fim de jogo — a fase em que o conteúdo normal é confortável mas desafios específicos seguem encerrando corridas."),
        ("Como conseguir amuletos em " + G + "?", "A cobertura da comunidade descreve aquisição ligada a boss e desafio. Este site trata como rota relatada e não imprime taxas nem origens de itens específicos."),
        ("Farne amuletos ou melhorias primeiro?", "Melhorias e equipamento central primeiro. Um amuleto compensa quando uma falha repetível já mostrou o que falta."),
        ("Por que não há tier list de amuletos?", "Porque fontes atuais discordam sobre os itens e nenhuma data as tabelas. Publicar uma seria congelar um valor que o cliente pode contradizer."),
    ],
    "related": [("Acessórios", "/pt/wiki/accessories/", "A camada de equipamento ao lado"),
                ("Raids", "/pt/guides/raids/", "Onde é testado"),
                ("Recursos", "/pt/wiki/resources/", "O que o farm de equipamento custa")],
}

# ---------- 20. Resources ----------
PAGES["wiki/resources/index.html"] = {
    "path": "wiki/resources/index.html",
    "title": G + " Recursos – Moedas, Fontes e Onde Gastar",
    "meta": ("Recursos em " + G + ": a economia por trás do loop oficial — de onde vêm, o que compram e como parar "
             "de vazar."),
    "pill": "Wiki", "h1": G + " Recursos",
    "lead": ("Recursos são no que o loop inteiro se converte — e a forma mais rápida de perder progresso é gastá-los "
             "no elo errado."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Recursos", "/pt/wiki/resources/")],
    "sections": [
        ("p", "O loop oficial de " + G + " diz explicitamente que você <strong>combate inimigos por recursos</strong>. "
              "Esses recursos financiam a camada de desbloqueio (Avatares, Armas, itens raros) e os passos de poder "
              "(Rank Up, Melhorias), antes de a conta ser testada nas Raids. Toda pergunta sobre recurso é, portanto, "
              "uma pergunta de ordem de gasto."),
        ("h2", "Fonte → uso → gasto"),
        ("table", {"head": ["Etapa", "O que acontece", "Onde é coberto"],
                   "rows": [
                       ["Fonte", "Combate e farm produzem recursos, movidos por Energia → Cartas → Companions.", "Energia · Cartas · Companions"],
                       ["Uso", "Recursos financiam desbloqueios e passos de poder: Avatares, Armas, Rank Up, Melhorias.", "Avatares · Armas · Rank Up · Melhorias"],
                       ["Teste de gasto", "Isso resolve a parede que você está batendo?", "Progressão"],
                       ["Teto", "Equipamento e níveis de desafio sobem o teto: bosses, acessórios, amuletos, raids, trial.", "Bosses Secretos · Acessórios · Amuletos · Raids · Trial"],
                   ]}),
        ("h2", "Como os recursos vazam"),
        ("ul", [
            "<strong>Compromissos paralelos</strong> — financiar um push de rank e uma linha de melhoria ao mesmo tempo é o maior ralo do meio de jogo. <a href=\"/pt/guides/rank-up/\">Rank Up</a>",
            "<strong>Gasto da moda</strong> — perseguir o que um vídeo chamou de melhor sem fonte datada. <a href=\"/pt/updates/\">Atualizações</a>",
            "<strong>Farmar sem alvo</strong> — sessões que produzem recursos mas nenhuma decisão não produzem progresso.",
            "<strong>Ignorar fontes grátis</strong> — o sistema de códigos está ativo e recursos grátis no começo valem mais. <a href=\"/pt/codes/\">Códigos</a>",
        ]),
        ("h2", "A regra de gasto"),
        ("ol", [
            "<strong>Guarde primeiro</strong> — mantenha um colchão dimensionado para a próxima decisão, não para zero.",
            "<strong>Uma linha por vez</strong> — termine o que começou antes de abrir uma segunda frente.",
            "<strong>Re-meça após atualizações</strong> — custos e rendas se movem; uma regra do mês passado pode não valer mais. <a href=\"/pt/guides/progression/\">Progressão</a>",
        ]),
        ("note", "Nenhuma quantidade de moeda, rendimento por sessão, tabela de custo ou taxa de troca é publicada "
                 "aqui. Renda de Energia, custos de rank e de melhoria dependem da versão, e esta página documenta a "
                 "forma da economia em vez de congelar seus números."),
    ],
    "faq": [
        ("O que são recursos em " + G + "?", "A saída do passo de combate e farm do loop oficial — o poço que financia Avatares, Armas, itens raros, Rank Up e Melhorias antes do teste nas Raids."),
        ("Como conseguir recursos em " + G + "?", "Combatendo inimigos, como o loop oficial descreve. Na prática, isso significa uma corrente Energia → Cartas → Companions funcionando e uma rota de farm repetível."),
        ("Em que gastar recursos primeiro em " + G + "?", "No que resolve a parede atual — geralmente produção de farm no começo e uma linha comprometida de melhoria ou rank depois. Dividir recursos entre linhas paralelas é o erro mais comum."),
        ("Quanto de cada recurso é preciso?", "Nenhuma quantidade é publicada aqui, porque custos e rendas são rebalanceados entre atualizações. Guarde um colchão para a próxima decisão."),
    ],
    "related": [("Trial", "/pt/guides/trial/", "Uma fonte repetível de recursos"),
                ("Rank Up", "/pt/guides/rank-up/", "Um grande ralo de recursos"),
                ("Guia F2P", "/pt/guides/f2p/", "Disciplina de recursos sem Robux")],
}

# ---------- 21. Worlds ----------
PAGES["wiki/worlds/index.html"] = {
    "path": "wiki/worlds/index.html",
    "title": G + " Mundos – Ordem dos Mundos e Navegação",
    "meta": ("Mundos em " + G + ": como a ordem funciona como escada de progressão e como navegar de cada mundo "
             "para os sistemas, bosses e raids que ele alimenta."),
    "pill": "Wiki", "h1": G + " Mundos",
    "lead": ("Mundos são a camada de mapa do loop — uma escada de paradas de progressão, não um conjunto de "
             "subpáginas vazias."),
    "breadcrumb": [("Início", "/pt/"), ("Wiki", "/pt/wiki/"), ("Mundos", "/pt/wiki/worlds/")],
    "sections": [
        ("p", "Em " + G + " o mundo em que você está diz o que sua conta deveria estar fazendo: farmar, desbloquear "
              "ou empurrar um desafio. A cobertura da comunidade documenta vários mundos com dificuldade "
              "crescente, e o título atual carrega a marca CLASS TREE — o tipo de mudança que mexe no conteúdo dos "
              "mundos."),
        ("h2", "Como usar a ordem dos mundos"),
        ("ol", [
            "<strong>Veja mundos como portões</strong> — se um mundo parece impossível, seu gargalo está um elo atrás no loop. <a href=\"/pt/guides/progression/\">Progressão</a>",
            "<strong>Farne no mundo que você limpa mais rápido</strong> — velocidade vale mais que prestígio para produção de recursos. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Desbloqueie para frente, farne para trás</strong> — avance para desbloquear e mantenha uma rota repetível onde você limpa com segurança. <a href=\"/pt/wiki/avatars/\">Avatares</a>",
            "<strong>Reescuteie após atualizações</strong> — layouts e posições de boss mudam entre builds. <a href=\"/pt/updates/\">Atualizações</a>",
        ]),
        ("h2", "Navegação a partir daqui"),
        ("cards", [
            ("Bosses Secretos", "Como bosses são encontrados e farmados no mundo atual.", "/pt/guides/secret-boss-locations/"),
            ("Acessórios", "Para que serve o farm de boss em mundos mais avançados.", "/pt/wiki/accessories/"),
            ("Raids", "O nível de desafio que testa o mundo alcançado.", "/pt/guides/raids/"),
            ("Trial", "O loop de desafio repetível fora da escada de mundos.", "/pt/guides/trial/"),
            ("Armas", "Desbloqueios que atravessam mundos.", "/pt/wiki/weapons/"),
            ("Recursos", "O que o farm de cada mundo produz.", "/pt/wiki/resources/"),
        ]),
        ("note", "Esta página não cria uma subpágina por mundo de propósito. Uma página que só troca o nome do mundo "
                 "não agrega decisão — a informação útil é a ordem, o gargalo e o que cada mundo alimenta, que é o "
                 "que está documentado aqui. Nomes de mundo, limites e tabelas por mundo ficam fora até uma fonte "
                 "atual sustentar."),
    ],
    "faq": [
        ("Quantos mundos tem em " + G + "?", "A cobertura da comunidade documenta vários mundos em dificuldade crescente, e a contagem é o tipo de coisa que atualizações mudam. Este site não publica contagem sem data."),
        ("Qual é a ordem dos mundos em " + G + "?", "A ordem é de dificuldade crescente, e cada mundo age como portão: se um parece impossível, a correção costuma estar um elo atrás no loop."),
        ("Devo farmar no mundo mais novo que liberei?", "Não necessariamente. Limpezas rápidas produzem mais que lentas, então muitos jogadores desbloqueiam para frente e farmam para trás."),
        ("Por que não existe página por mundo em " + G + "?", "Porque uma página que só muda o nome do mundo não agrega nada. Esta página documenta a escada, a lógica de gargalo e os links para bosses, raids e sistemas."),
    ],
    "related": [("Bosses Secretos", "/pt/guides/secret-boss-locations/", "Bosses por área de mundo"),
                ("Guia de Progressão", "/pt/guides/progression/", "Em qual portão você travou"),
                ("Atualizações", "/pt/updates/", "Conteúdo de mundo se move com atualizações")],
}

# ---------- 22. F2P ----------
PAGES["guides/f2p/index.html"] = {
    "path": "guides/f2p/index.html",
    "title": G + " Guia F2P – Progredindo sem Robux",
    "meta": "Guia F2P de Anime Breaker: progredir sem gastar Robux, onde recompensas grátis ajudam de verdade e quais hábitos mantêm a conta avançando.",
    "pill": "Guias", "h1": G + " Guia F2P",
    "lead": ("Contas gratuitas não são contas lentas — são contas que não podem se dar ao luxo de uma ordem de gasto "
             "ruim."),
    "breadcrumb": [("Início", "/pt/"), ("Guias", "/pt/guides/"), ("F2P", "/pt/guides/f2p/")],
    "sections": [
        ("p", "O loop oficial de " + G + " é de progressão, não de compra: Energia → Cartas → Companions → recursos → "
              "desbloqueios → Rank Up / Melhorias → Raids. Nada nessa corrente é descrito como pago. O que falta a "
              "uma conta gratuita é perdão para recursos desperdiçados."),
        ("h2", "As regras F2P que realmente importam"),
        ("ol", [
            "<strong>Nunca gaste sem alvo nomeado</strong> — contas gratuitas não podem forçar a barra num erro. <a href=\"/pt/wiki/resources/\">Recursos</a>",
            "<strong>Pegue toda recompensa grátis datada</strong> — o sistema de códigos está ativo e é a injeção de recurso mais barata disponível. <a href=\"/pt/codes/\">Códigos</a>",
            "<strong>Meça sua renda de Energia</strong> — medição de dois pontos bate qualquer taxa copiada. <a href=\"/pt/guides/energy/\">Energia</a>",
            "<strong>Comprometa-se com uma linha</strong> — uma linha de Companion, uma de arma e depois um passo de poder. <a href=\"/pt/guides/upgrades/\">Melhorias</a>",
            "<strong>Farne onde limpa rápido</strong> — qualidade de rota é o principal multiplicador do jogador grátis. <a href=\"/pt/wiki/worlds/\">Mundos</a>",
        ]),
        ("h2", "Onde contas gratuitas travam"),
        ("ul", [
            "<strong>Lacunas de elenco, não de moeda</strong> — um elenco fino limita a taxa de farm e, com isso, tudo. <a href=\"/pt/wiki/cards/\">Cartas</a>",
            "<strong>Melhorias espalhadas</strong> — o mesmo erro pago mais caro. <a href=\"/pt/guides/rank-up/\">Rank Up</a>",
            "<strong>Perseguir tier lists</strong> — rankings sem data levam contas gratuitas a becos caros. <a href=\"/pt/guides/progression/\">Progressão</a>",
        ]),
        ("h2", "Uma ordem realista para F2P"),
        ("ol", [
            "<strong>Sessões 1–3:</strong> entenda a renda de Energia, abra Cartas em lotes, monte um conjunto de farm. <a href=\"/pt/guides/beginner-guide/\">Guia para Iniciantes</a>",
            "<strong>Semana 1:</strong> guarde recursos, termine uma linha de melhoria, resgate todo código datado.",
            "<strong>Depois:</strong> desbloqueie para frente com <a href=\"/pt/wiki/avatars/\">Avatares</a> e "
            "<a href=\"/pt/wiki/weapons/\">Armas</a>, farne a faixa de equipamento via "
            "<a href=\"/pt/guides/secret-boss-locations/\">bosses</a> e só então empurre as "
            "<a href=\"/pt/guides/raids/\">Raids</a>.",
        ]),
        ("note", "Esta página não faz afirmações sobre o que compras com Robux contêm ou custam. Experiências do "
                 "Roblox mudam suas lojas sem aviso, e este site não publica detalhes de compra não verificáveis — a "
                 "rota F2P acima é construída inteiramente sobre o loop verificado."),
    ],
    "faq": [
        ("Dá para jogar " + G + " sem gastar Robux?", "Sim, em estrutura: o loop oficial descreve progressão por Energia, Cartas, Companions, recursos e desbloqueios, não por compras. Uma conta gratuita precisa principalmente de disciplina de recursos."),
        ("O que um jogador F2P deve fazer primeiro em " + G + "?", "Medir a renda de Energia, abrir Cartas em lotes para um conjunto de farm e depois comprometer-se com uma linha de melhoria enquanto guarda recursos."),
        ("Códigos valem a pena para F2P?", "Sim — são a injeção de recurso mais barata disponível, e a página de códigos acompanha o que está relatado ativo com a data da checagem."),
        ("O " + G + " é pay to win?", "Nenhuma afirmação verificada sustenta isso, e este site não publica detalhes de compra que não pode checar. O loop é movido a esforço; o risco real do F2P é desperdiçar recursos em compromissos paralelos."),
    ],
    "related": [("Códigos", "/pt/codes/", "Recursos grátis, datados"),
                ("Guia para Iniciantes", "/pt/guides/beginner-guide/", "As três primeiras sessões"),
                ("Energia", "/pt/guides/energy/", "A principal alavanca do jogador grátis")],
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
