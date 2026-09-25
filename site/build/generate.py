# -*- coding: utf-8 -*-
"""主生成脚本:渲染 66 页(English / Português / Español)+ sitemap + robots + 404。
用法:python3 build/generate.py [site | site-preview --domain ...]"""
import os
import sys
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from components import (abs_url, site_url, site_path, render_head, render_header, render_footer,
                        render_blocks, render_faq, render_related,
                        render_breadcrumbs, hero_section, gallery_section,
                        NAV_SCRIPT)
import content_en, content_pt, content_es

OUT = None  # 由 main() 决定输出目录

CONTENT = {"en": content_en, "pt": content_pt, "es": content_es}

# 首页 hero 下方广告槽(crummyneedle container-div 原生容器,防 CLS)
AD_HOME = """    <div class="ad-home">
      <script async="async" data-cfasync="false" src="https://crummyneedle.com/9c9d8397530a34d70aa6a13dd9e181d5/invoke.js"></script>
      <div id="container-9c9d8397530a34d70aa6a13dd9e181d5"></div>
    </div>
"""

# 正文中段广告槽(crummyneedle atOptions iframe 300x250,防 CLS) — 插在正文主体与 FAQ 之间
AD_MID = """    <div class="ad-mid">
      <script>
        atOptions = {
          'key' : 'cc3cbc5fbcfe1d620cf2a39a66cfdfb9',
          'format' : 'iframe',
          'height' : 250,
          'width' : 300,
          'params' : {}
        };
      </script>
      <script src="https://crummyneedle.com/cc3cbc5fbcfe1d620cf2a39a66cfdfb9/invoke.js"></script>
    </div>
"""

# 政策页豁免(路径前缀)
POLICY_PREFIXES = ("about/", "contact/", "privacy", "terms")


def _skip_ads(path):
    return str(path or "").startswith(POLICY_PREFIXES)

# 首页 section 分组时的 eyebrow 映射(可选:按 h2 文本自定义;留空则用默认值)
EYEBROW = {"en": {}, "pt": {}, "es": {}}
EYEBROW_DEFAULT = {"en": "Explore", "pt": "Explorar", "es": "Explorar"}


def split_sections(blocks):
    """按 ('h2', ...) 切组,返回 [(h2_text, [blocks...]), ...]"""
    groups = []
    cur = None
    for b in blocks:
        if b[0] == "h2":
            cur = (b[1], [])
            groups.append(cur)
        elif cur is not None:
            cur[1].append(b)
        else:
            # 第一个 h2 之前的导语:并入第一组
            if groups:
                groups[0][1].append(b)
            else:
                groups.append(("", [b]))
    return groups


def render_home_sections(lang, blocks):
    """首页 sections → 多个 .section.container-wide(与模板一致)"""
    out = []
    for i, (h2, inner) in enumerate(split_sections(blocks), start=1):
        sid = f"home-section-{i}"
        eyebrow = EYEBROW.get(lang, {}).get(h2, EYEBROW_DEFAULT[lang])
        h2_html = f'<h2 id="{sid}">{h2}</h2>' if h2 else ""
        body = render_blocks(inner) if inner else ""
        out.append(
            f'<section class="section container-wide" aria-labelledby="{sid}">'
            f'<div class="section-head"><span class="eyebrow">{eyebrow}</span>{h2_html}</div>'
            f'<div class="prose-content">{body}</div></section>')
    return "\n".join(out)


def render_article(lang, page):
    crumbs = page.get("breadcrumb", [])
    nav = config.NAV[lang]
    ad_mid = "" if _skip_ads(page.get("path")) else AD_MID
    return f"""<main id="main">
<div class="container-wide doc-top">
{render_breadcrumbs(crumbs)}
<div class="doc-hero">
<span class="pill">{page["pill"]}</span>
<h1>{page["h1"]}</h1>
<p class="doc-lead">{page["lead"]}</p>
</div>
</div>
<div class="container-wide doc-grid">
<div class="doc-body prose-content">
{render_blocks(page["sections"])}
</div>
</div>
{ad_mid}
{render_faq(page.get("faq", []))}
{render_related(page.get("related", []))}
</main>
{render_footer(lang, nav, "")}"""


def render_home(lang, page):
    nav = config.NAV[lang]
    faq_label = "FAQ"
    return f"""<main id="main">
{hero_section(lang, page)}
{AD_HOME}
{gallery_section(lang, page)}
{render_home_sections(lang, page["sections"])}
{render_faq(page.get("faq", []), label=faq_label)}
</main>
{render_footer(lang, nav, "")}"""


def render_page(lang, key, page):
    nav = config.NAV[lang]
    is_home = bool(page.get("home"))
    rel = _rel_prefix(lang, page["path"])
    path_url = site_path(lang, page["path"])  # 完整站点路径(含语言前缀),供导航高亮/语言切换器
    head = render_head(lang, path_url, page, rel, is_home)
    body = render_home(lang, page) if is_home else render_article(lang, page)
    return f"{head}<a href=\"#main\" class=\"skip-link\">Skip to content</a>\n{render_header(lang, path_url, nav, rel)}\n{body}\n{NAV_SCRIPT}\n</body>\n</html>\n"


def _rel_prefix(lang, path):
    depth = path.count("/") + (1 if lang != "en" else 0)
    return "../" * depth if depth else "./"


def sync_static(src_dir, out_dir):
    """把静态资源(styles/favicon/assets)从源目录复制到输出目录;输出=源时跳过。"""
    if os.path.abspath(src_dir) == os.path.abspath(out_dir):
        return
    for item in ("styles.css", "favicon.ico", "favicon.svg"):
        s = os.path.join(src_dir, item)
        if os.path.exists(s):
            shutil.copy2(s, os.path.join(out_dir, item))
    assets = os.path.join(src_dir, "assets")
    if os.path.isdir(assets):
        shutil.copytree(assets, os.path.join(out_dir, "assets"), dirs_exist_ok=True)
    print("static resources synced ->", out_dir)


def main():
    # 用法:python3 build/generate.py [--domain 127.0.0.1:8792] [输出目录]
    global OUT
    args = sys.argv[1:]
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
    if args and not args[0].startswith("--"):
        out_dir = args[0]
        args = args[1:]
    OUT = os.path.abspath(out_dir)
    domain = None
    if args and args[0] == "--domain" and len(args) > 1:
        domain = args[1]
    if domain:
        config.SITE["domain"] = domain
    lang_dirs = {"en": "", "pt": "pt/", "es": "es/"}
    os.makedirs(OUT, exist_ok=True)
    sitemap_urls = []
    for lang in ["en", "pt", "es"]:
        content = CONTENT[lang]
        base = os.path.join(OUT, lang_dirs[lang])
        for key in content.PAGE_ORDER:
            page = content.PAGES[key]
            out_path = os.path.join(base, key)
            os.makedirs(os.path.dirname(out_path) or base, exist_ok=True)
            html = render_page(lang, key, page)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            # 站点 URL(语言根相对,目录式)
            url = "/" + lang_dirs[lang] + site_url(page["path"]).lstrip("/")
            sitemap_urls.append(url)
            print("wrote", out_path)
    # sitemap
    sitemap = _sitemap(sitemap_urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    # Vercel 配置(随产物部署:trailingSlash 规范目录式 URL)
    with open(os.path.join(OUT, "vercel.json"), "w", encoding="utf-8") as f:
        f.write('{\n  "cleanUrls": false,\n  "trailingSlash": true\n}\n')
    # robots
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {abs_url('/sitemap.xml')}\n")
    # 404
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(_render_404())
    # 静态资源同步(预览目录需要 styles/favicon/assets;源 = 项目根,与 build/ 平级)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sync_static(project_root, OUT)
    print("sitemap/robots/404 written")


def _sitemap(urls):
    items = "".join(
        f'<url><loc>{abs_url(u)}</loc><lastmod>{config.SITE["pub_date"]}</lastmod><changefreq>weekly</changefreq></url>'
        for u in sorted(urls))
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>\n'


def _render_404():
    nav = config.NAV["en"]
    head = render_head("en", "/404.html", {
        "path": "404.html",
        "title": "Page not found – " + config.SITE["name"] + " Wiki",
        "meta": "Page not found on the " + config.SITE["name"] + " Wiki.",
    }, "", is_home=False, include_alternate=False, noindex=True)
    links = "".join(f'<li><a href="{abs_url(p)}">{t}</a></li>' for t, p in [
        ("Home", "/"), ("Wiki Hub", "/wiki/"), ("Guides", "/guides/"),
        ("Codes", "/codes/"), ("Updates", "/updates/"), ("Español", "/es/")])
    return f"""{head}<a href="#main" class="skip-link">Skip to content</a>
{render_header("en", "/404.html", nav, "./")}
<main id="main">
<div class="container-wide doc-top">
<div class="doc-hero">
<span class="pill">404</span>
<h1>Page not found</h1>
<p class="doc-lead">The page you are looking for does not exist or has moved. Try one of these instead:</p>
<ul>{links}</ul>
</div>
</div>
</main>
{render_footer("en", nav, "./")}
</body>
</html>
"""


if __name__ == "__main__":
    main()
