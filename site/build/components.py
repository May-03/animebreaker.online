# -*- coding: utf-8 -*-
"""渲染组件:head/header/footer/nav/正文 blocks/FAQ/related/JSON-LD。"""
import re
import config
from config import LANGS, LANG_ORDER, NAV, LOGO_SVG, HERO_TITLE

SITE_NAME = config.SITE["name"] + " Wiki & Guides"

# 导航下拉(语言切换器/移动菜单)点击/悬停/焦点切走自动收回 —— 渐进增强,内容不依赖 JS(2026-09-09 合入;2026-09-12 加 mouseover/focusin 修复"切到旁边不收起")
NAV_SCRIPT = """<script>
(function(){if(window.__navUiInit)return;window.__navUiInit=true;
function navClose(e){var s=document.querySelectorAll('details.lang-switcher[open],details.mobile-group[open],details.mobile-menu-wrap[open]');for(var i=0;i<s.length;i++){if(!s[i].contains(e.target)){s[i].removeAttribute('open');}}}
document.addEventListener('click',navClose);
document.addEventListener('mouseover',navClose);
document.addEventListener('focusin',navClose);
})();
</script>"""


def abs_url(path):
    """站点绝对 URL(path 以 / 开头)。本地预览(127.0.0.1/localhost)用 http,线上用 https。"""
    d = config.SITE["domain"]
    scheme = "http" if d.startswith(("127.0.0.1", "localhost")) else "https"
    return f"{scheme}://{d}{path}"


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


def lang_url(lang_key, path):
    """path 是语言根相对路径(以 / 开头,如 /wiki/),返回该语言绝对 URL。"""
    return abs_url("/" + LANGS[lang_key]["dir"] + path.lstrip("/"))


def hreflang_links(lang, path, is_home=False):
    out = [f'<link rel="alternate" hreflang="{LANGS[l]["hreflang"]}" href="{lang_url(l, _switcher_path(path))}">' for l in LANG_ORDER]
    if is_home and lang == "en":
        out.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url(path)}">')
    return "\n".join(out)


# ---------- 正文 blocks 渲染 ----------

def render_table(t):
    head = "".join(f"<th>{c}</th>" for c in t.get("head", []))
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t.get("rows", []))
    thead = f"<thead><tr>{head}</tr></thead>" if head else ""
    return f'<div class="table-wrap"><table>{thead}<tbody>{rows}</tbody></table></div>'


def render_video(v):
    thumb = v.get("thumb", "")
    img = f'<img src="{thumb}" alt="" width="480" height="270" loading="lazy" decoding="async">' if thumb else ""
    play = ('<span class="play-mark"><svg viewBox="0 0 24 24" width="52" height="52" fill="currentColor" aria-hidden="true">'
            '<path d="M8 5.5v13l11-6.5z"/></svg></span>')
    return (f'<a class="video-card" href="{v["url"]}" target="_blank" rel="noopener">'
            f'<span class="video-thumb">{img}{play}</span><span class="video-caption">{v["title"]}</span></a>')


def render_cards(cards):
    out = []
    for title, desc, url in cards:
        out.append(
            f'<a href="{abs_url(url)}" class="card card-hover article-card">'
            f'<span class="eyebrow">Guide</span><h3>{title}</h3><p>{desc}</p>'
            f'<span class="article-cta">Read guide<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h9M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"></path></svg></span></a>')
    return f'<div class="grid grid-3">{"".join(out)}</div>'


def render_blocks(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if k == "h2":
            out.append(f'<h2 id="{slugify(b[1])}">{b[1]}</h2>')
        elif k == "p":
            out.append(f"<p>{b[1]}</p>")
        elif k in ("ul", "ol"):
            tag = k
            items = "".join(f"<li>{x}</li>" for x in b[1])
            out.append(f"<{tag}>{items}</{tag}>")
        elif k == "table":
            out.append(render_table(b[1]))
        elif k == "video":
            out.append(render_video(b[1]))
        elif k == "note":
            out.append(f'<p class="doc-meta"><strong>{b[1]}</strong></p>')
        elif k == "cards":
            out.append(render_cards(b[1]))
    return "\n".join(out)


def render_faq(faq, label="FAQ"):
    if not faq:
        return ""
    items = "".join(
        f'<details class="faq-item"><summary><span>{q}</span>'
        f'<svg viewBox="0 0 14 14" width="15" height="15" aria-hidden="true"><path d="M3 5l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"></path></svg></summary>'
        f'<div class="faq-answer"><p>{a}</p></div></details>' for q, a in faq)
    return (f'<section class="section container-wide" aria-labelledby="faq-title"><div class="faq-head">'
            f'<span class="eyebrow">{label}</span><h2 id="faq-title">{label}</h2>'
            f'<p>Common questions about this topic.</p></div><div class="faq-list">{items}</div></section>')


def render_related(related, label="Keep reading"):
    if not related:
        return ""
    cards = "".join(
        f'<a href="{abs_url(u)}" class="card card-hover related-card"><h3>{t}</h3><p>{d}</p>'
        f'<span class="related-cta">Read<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h9M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"></path></svg></span></a>'
        for t, u, d in related)
    return (f'<section class="related" aria-labelledby="related-title"><div class="container-wide">'
            f'<div class="related-head"><span class="eyebrow">Related guides</span><h2 id="related-title">{label}</h2></div>'
            f'<div class="related-grid">{cards}</div></div></section>')


def render_breadcrumbs(crumbs, label_home="Home", label_sep="/"):
    lis = []
    n = len(crumbs)
    for i, (name, url) in enumerate(crumbs):
        if i == n - 1:
            lis.append(f'<li><span aria-current="page">{name}</span></li>')
        else:
            lis.append(f'<li><a href="{abs_url(url)}">{name}</a><span class="sep" aria-hidden="true">/</span></li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


# ---------- 导航 ----------

def _nav_active(nav, path):
    """返回 (home_active, col_index_active or None, item_active or None)。"""
    if path in ("/", "/zh/", "/ja/"):
        return True, None, None
    for ci, (_, items) in enumerate(nav["cols"]):
        for label, _d, url in items:
            if path == url:
                return False, ci, label
    return False, None, None


def _desktop_nav(lang, path, nav):
    home_label, home_url = nav["home"]
    home_active, col_active, _item = _nav_active(nav, path)
    home_cls = ' class="nav-link active" aria-current="page"' if home_active else ' class="nav-link"'
    lis = [f'<li class="nav-item"><a href="{abs_url(home_url)}"{home_cls}>{home_label}</a></li>']
    for ci, (title, items) in enumerate(nav["cols"]):
        first_url = items[0][2]
        cls = "nav-link has-panel" + (" active" if col_active == ci else "")
        lis.append(
            f'<li class="nav-item nav-item-dd"><a href="{abs_url(first_url)}" class="{cls}" aria-haspopup="true">{title}'
            f'<svg class="caret" viewBox="0 0 12 12" width="11" height="11" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></a>'
            f'<div class="nav-panel" role="menu"><div class="panel-inner"><ul class="panel-list">')
        for label, desc, url in items:
            lis.append(f'<li><a href="{abs_url(url)}" class="panel-link" role="menuitem"><span class="panel-label">{label}</span><span class="panel-desc">{desc}</span></a></li>')
        lis.append(f'<li><a href="{abs_url(first_url)}" class="panel-link panel-link-all" role="menuitem"><span class="panel-label">View all</span></a></li>')
        lis.append("</ul></div></div></li>")
    lis.append(_lang_switcher_desktop(lang, path))
    return f'<nav class="desktop-nav" aria-label="Primary navigation"><ul class="nav-list">{"".join(lis)}</ul></nav>'



def _switcher_path(path):
    """语言切换器使用的路径;404 等无语言版本的页面回退到语言首页。"""
    return "/" if path in ("/404.html", "404.html") else path

def _lang_switcher_desktop(lang, path):
    entries = []
    for l in LANG_ORDER:
        if l == lang:
            entries.append(f'<a href="{lang_url(l, _switcher_path(path))}" class="current" aria-current="page">{LANGS[l]["name"]}</a>')
        else:
            entries.append(f'<a href="{lang_url(l, _switcher_path(path))}">{LANGS[l]["name"]}</a>')
    globe = ('<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
             '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9S14.5 18.4 12 21c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3z"/></svg>')
    caret = '<svg viewBox="0 0 16 16" width="10" height="10" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 5l5 5 5-5"/></svg>'
    return (f'<li class="nav-item lang"><details class="lang-switcher"><summary>{globe}{LANGS[lang]["short"]}{caret}</summary>'
            f'<div class="lang-switcher-menu">{"".join(entries)}</div></details></li>')


def _mobile_nav(lang, path, nav):
    home_label, home_url = nav["home"]
    groups = []
    for title, items in nav["cols"]:
        uls = "".join(f'<li><a href="{abs_url(u)}">{t}</a></li>' for t, _d, u in items)
        groups.append(
            f'<details class="mobile-group"><summary><span>{title}</span>'
            f'<svg viewBox="0 0 12 12" width="13" height="13" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></summary><ul>{uls}</ul></details>')
    lang_entries = []
    for l in LANG_ORDER:
        if l == lang:
            lang_entries.append(f'<li><span aria-current="true">{LANGS[l]["name"]}</span></li>')
        else:
            lang_entries.append(f'<li><a href="{lang_url(l, _switcher_path(path))}">{LANGS[l]["name"]}</a></li>')
    groups.append(
        f'<details class="mobile-group"><summary><span>Language</span>'
        f'<svg viewBox="0 0 12 12" width="13" height="13" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></summary><ul>{"".join(lang_entries)}</ul></details>')
    cta_label, cta_url = nav["cta"]
    mobile_links = "".join(groups)
    return (f'<details class="mobile-menu-wrap"><summary class="hamburger" aria-label="Open menu"><span></span><span></span><span></span></summary>'
            f'<nav class="mobile-nav" aria-label="Mobile navigation"><a href="{abs_url(home_url)}" class="mobile-home">{home_label}</a>'
            f'{mobile_links}<a class="btn btn-primary mobile-cta" href="{cta_url}" target="_blank" rel="noopener">{cta_label}</a></nav></details>')


def render_header(lang, path, nav, rel):
    game = config.SITE["name"]
    logo = (f'<a href="{abs_url(nav["home"][1])}" class="header-logo" aria-label="{game} Wiki home"><span class="logo">'
            f'{LOGO_SVG}<span class="logo-text"><span class="logo-text-top">{game}</span><span class="logo-text-sub">WIKI &amp; GUIDES</span></span></span></a>')
    cta_label, cta_url = nav["cta"]
    return (f'<header class="site-header"><div class="container-wide header-inner">{logo}'
            f'{_desktop_nav(lang, path, nav)}<div class="header-right">{_mobile_nav(lang, path, nav)}'
            f'<a class="btn btn-primary" href="{cta_url}" target="_blank" rel="noopener">{cta_label}</a></div></div></header>')


def render_footer(lang, nav, rel):
    cta_label, cta_url = nav["cta"]

    def col_html(title, items):
        lis = "".join('<li><a href="' + abs_url(u) + '">' + t + "</a></li>" for t, u in items)
        return "<div><h3>" + title + "</h3><ul>" + lis + "</ul></div>"

    cols = "".join(col_html(title, items) for title, items in nav["footer_cols"])
    site = "".join('<li><a href="' + abs_url(u) + '">' + t + "</a></li>" for t, u in nav["footer_site"])
    cols += '<div><h3>Site</h3><ul>' + site + '<li><a href="' + cta_url + '" target="_blank" rel="noopener">' + cta_label + "</a></li></ul></div>"
    brand = (f'<span class="logo">{LOGO_SVG}<span class="logo-text"><span class="logo-text-top">{config.SITE["name"]}</span>'
             f'<span class="logo-text-sub">WIKI &amp; GUIDES</span></span></span>')
    return (f'<footer class="site-footer"><div class="container-wide footer-grid"><div class="footer-brand">{brand}'
            f'<p>Unofficial fan resource. Not affiliated with, endorsed by, or sponsored by {config.SITE["developer"]}. '
            f'{config.SITE["name"]} and related names are trademarks of their respective owners. '
            f'Game screenshots are from the official store page and remain the property of their owners; shown for reference only.</p></div>'
            f'<div class="footer-cols">{cols}</div></div>'
            f"<div class=\"container-wide footer-bottom\"><span>&copy; 2026 {config.SITE['name']} Wiki &middot; Unofficial fan site, not affiliated with {config.SITE['developer']}</span></div></footer>")


# ---------- head / JSON-LD ----------

def _jsonld_faq(faq, url):
    if not faq:
        return ""
    ents = ",".join(
        f'{{"@type":"Question","name":{__j(q)},"acceptedAnswer":{{"@type":"Answer","text":{__j(a)}}}}}'
        for q, a in faq)
    return f'{{"@type":"FAQPage","mainEntity":[{ents}]}}'


def __j(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _jsonld_breadcrumb(crumbs):
    if not crumbs:
        return ""
    els = ",".join(
        f'{{"@type":"ListItem","position":{i+1},"name":{__j(name)},"item":{__j(abs_url(url))}}}'
        for i, (name, url) in enumerate(crumbs))
    return f'{{"@type":"BreadcrumbList","itemListElement":[{els}]}}'


def build_jsonld(page, lang, url):
    graph = []
    if page.get("home"):
        graph.append(f'{{"@type":"WebSite","name":{__j(SITE_NAME)},"url":{__j(abs_url("/" if lang=="en" else "/"+LANGS[lang]["dir"]))},"inLanguage":{__j(LANGS[lang]["hreflang"])}}}')
    else:
        graph.append(
            '{"@type":"Article","headline":' + __j(page["title"]) +
            ',"url":' + __j(abs_url(url)) +
            ',"inLanguage":' + __j(LANGS[lang]["hreflang"]) +
            ',"datePublished":"2026-08-23","dateModified":"2026-08-23"'
            ',"author":{"@type":"Organization","name":' + __j(config.SITE["name"] + " Wiki") + '}}')
    bc = _jsonld_breadcrumb(page.get("breadcrumb", []))
    if bc:
        graph.append(bc)
    faq = _jsonld_faq(page.get("faq", []), url)
    if faq:
        graph.append(faq)
    return '{"@context":"https://schema.org","@graph":[' + ",".join(graph) + "]}"


def render_head(lang, path, page, rel, is_home=False, include_alternate=True):
    url = "/" + LANGS[lang]["dir"] + page["path"].lstrip("/")
    title = page["title"]
    meta = page["meta"]
    og_type = "website" if is_home else "article"
    jsonld = build_jsonld(page, lang, url)
    alt_block = hreflang_links(lang, "/" + page["path"].lstrip("/"), is_home) if include_alternate else ""
    _ga = config.SITE.get("ga_id", "")
    if _ga and not _ga.startswith("G-XX"):   # 占位(未配置/示例值)时不输出 gtag
        ga_block = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={_ga}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{_ga}');
</script>
"""
    else:
        ga_block = ""
    return f"""<!DOCTYPE html>
<html lang="{LANGS[lang]['lang']}">
<head>
{ga_block}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0c0a08">
<link rel="icon" type="image/svg+xml" href="{rel}favicon.svg">
<link rel="icon" href="{rel}favicon.ico" sizes="any">
<meta name="description" content="{meta}">
<title>{title}</title>
<link rel="canonical" href="{abs_url(url)}">
{alt_block}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{abs_url(url)}">
<meta property="og:image" content="{abs_url('/assets/media/screenshot-1.jpg')}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{rel}styles.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
"""


# ---------- 首页 hero ----------

def hero_section(lang, page):
    nav = NAV[lang]
    stats = "".join(f'<div class="stat"><dt>{s[0]}</dt><dd>{s[1]}</dd></div>' for s in page.get("stats", []))
    cta1_label, cta1_url = nav["cta"]
    return f"""<section class="hero">
<div class="hero-media" aria-hidden="true"><img src="{abs_url('/assets/media/hero-bg.jpg')}" alt="" width="2560" height="1440" fetchpriority="high" decoding="async"><div class="hero-bg"></div></div>
<div class="container-wide hero-inner">
<span class="pill hero-pill">{page["pill"]}</span>
<h1 class="hero-title"><span class="text-gradient">{config.SITE["name"]}</span> {HERO_TITLE[lang].replace(config.SITE["name"] + " ", "")}</h1>
<p class="hero-tagline">{page["tagline"]}</p>
<p class="hero-intro">{page["intro"]}</p>
<div class="hero-cta">
<a href="{cta1_url}" class="btn btn-primary" target="_blank" rel="noopener">{cta1_label}</a>
<a href="{abs_url(page["cta2_url"])}" class="btn btn-ghost hero-cta2">{page["cta2_label"]}</a>
</div>
<dl class="hero-stats">{stats}</dl>
</div>
</section>"""


def gallery_section(lang, page):
    imgs = ""
    for i in range(1, 5):
        imgs += f'<figure><img src="{abs_url(f"/assets/media/screenshot-{i}.jpg")}" alt="{page["shot_alt"][i-1]}" width="1200" height="675" loading="lazy" decoding="async"></figure>'
    return f'<section class="section gallery-section" aria-label="{config.SITE["name"]} screenshots"><div class="container-wide"><div class="gallery-rail">{imgs}</div><p class="gallery-credit">{page["gallery_credit"]}</p></div></section>'
