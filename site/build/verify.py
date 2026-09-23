# -*- coding: utf-8 -*-
"""第五套模板 — 上线前全站验证。
用法:cd 站点根 && python3 build/verify.py [站点目录,默认 site]
检查:页面数 / h1 / title / meta / canonical 自指 / hreflang 交叉 / x-default / JSON-LD /
      红线词 / 站内链接 / sitemap 条数 / 占位残留。全部通过输出 0 错误。
"""
import glob
import json
import os
import re
import sys

SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")

# 红线词(零命中;按需增删。下载/作弊类词不得出现在页面任何位置)
REDLINE = {
    "en": ["download", "cheat", "unblocked", "hack", "apk", "crack"],
    "zh": ["下载", "作弊", "破解", "外挂"],
    "ja": ["ダウンロード", "チート", "ハック", "ハッキング"],
}

errs = []


def check(cond, msg):
    if not cond:
        errs.append(msg)


def main():
    if not os.path.isdir(SITE):
        print("站点目录不存在:", SITE)
        sys.exit(1)
    pages = sorted(p for p in glob.glob(SITE + "/**/*.html", recursive=True) if not p.endswith("404.html"))
    sm_path = os.path.join(SITE, "sitemap.xml")
    check(os.path.exists(sm_path), "缺少 sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read() if os.path.exists(sm_path) else ""
    sm_urls = set(re.findall(r"<loc>(https?://[^<]+)</loc>", sm))
    global SITE_DOMAIN, SITE_SCHEME
    m = re.search(r"<loc>((https?)://[^/<]+)", sm)
    if m:
        SITE_DOMAIN = re.sub(r"^https?://", "", m.group(1))
        SITE_SCHEME = m.group(2)
    else:
        SITE_DOMAIN, SITE_SCHEME = "", "https"
    hl_map = {}  # canonical -> {hreflang hrefs} 用于互认交叉

    for p in pages:
        rel = p[len(SITE):].lstrip("/")
        h = open(p, encoding="utf-8").read()

        # h1 / title / meta 唯一
        check(len(re.findall(r"<h1[^>]*>.*?</h1>", h, re.S)) == 1, f"{rel}: h1 != 1")
        check(h.count("<title>") == 1, f"{rel}: title != 1")
        check(h.count('name="description"') == 1, f"{rel}: meta description != 1")

        # canonical 自指(目录式,与生成器 site_url 一致)
        can = re.search(r'<link rel="canonical" href="([^"]+)"', h)
        check(can is not None, f"{rel}: 缺 canonical")
        if can:
            exp = "/" if rel == "index.html" else "/" + rel[: -len("index.html")]
            ok = SITE_DOMAIN in can.group(1) and can.group(1).rstrip("/").endswith(exp.rstrip("/"))
            check(ok, f"{rel}: canonical 非自指 {can.group(1)}")

        # hreflang:精确 en/pt-BR/es 三集合 + 互认;x-default 仅英文首页
        hrefs = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', h))
        hset = set(hrefs.keys()) - {"x-default"}
        check(hset == {"en", "pt-BR", "es"}, f"{rel}: hreflang 集合 {hset} (期望 en/pt-BR/es)")
        for hf, url in hrefs.items():
            fp = url.replace("https://", "").replace("http://", "")
            fp = fp[fp.find("/"):].lstrip("/")
            fp = fp if fp.endswith(".html") else fp + "index.html"
            check(os.path.exists(os.path.join(SITE, fp)), f"{rel}: hreflang {hf} -> {url} 目标缺失")
        if can:
            hl_map.setdefault(can.group(1), set()).update(u for u in hrefs.values())
        if "x-default" in h and rel != "index.html":
            errs.append(f"{rel}: x-default 只应出现在英文首页")
        if rel == "index.html" and "x-default" not in h:
            errs.append("index.html: 缺 x-default")

        # og:url 与 canonical 一致
        ogu = re.search(r'<meta property="og:url" content="([^"]+)"', h)
        check(ogu is not None and can is not None and ogu.group(1) == can.group(1),
              f"{rel}: og:url ≠ canonical")

        # JSON-LD 可解析
        for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(m)
            except Exception as e:
                errs.append(f"{rel}: JSON-LD {str(e)[:60]}")

        # 红线词
        lang = "en"
        if rel.startswith("pt/") or rel.startswith("es/"):
            lang = "en"  # pt/es 页面复用英文红线词表(英文作弊/下载词在三语中均不出现)
        low = h.lower()
        for w in REDLINE[lang]:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                errs.append(f"{rel}: 红线词 '{w}'")

        # 占位残留(零容忍:本站不允许任何模板占位符/开发残留;TODO/FIXME 大小写敏感防与葡语 "Todo" 误报)
        for ph in set(re.findall(r"\[\[[A-Za-z0-9_-]+\]\]|\{\{[^}]+\}\}|CTA_URL|\bTODO\b|\bFIXME\b|\blorem\b", h)):
            errs.append(f"{rel}: 占位/残留 {ph}")

        # 站内链接存在(外部域名/占位域名跳过,只检查本站链接)
        for u in re.findall(r'href="(https?://[^"#]+|\.\.?/[^"#]+)"', h):
            if u.startswith("http"):
                if "[[DOMAIN]]" in u:
                    continue
                host = re.sub(r"^https?://([^/]+).*$", r"\1", u)
                if host != SITE_DOMAIN:  # 外部链接(Steam/字体等)不检查
                    continue
                path = "/" + u.split("/", 3)[3] if u.count("/") >= 3 else "/"
            else:
                path = os.path.normpath(os.path.join(os.path.dirname("/" + rel), u))
            if path.startswith(("/assets/", "/favicon", "/sitemap.xml", "/robots.txt")):
                continue
            fpath = os.path.join(SITE, path.lstrip("/"))
            if os.path.isdir(fpath):
                fpath = os.path.join(fpath, "index.html")
            check(os.path.exists(fpath), f"{rel}: 死链 {u}")

    # sitemap 与页面一一对应
    for p in pages:
        rel = p[len(SITE):].lstrip("/")
        if rel.endswith("index.html"):
            u = "/" + rel[:-10]
        else:
            u = "/" + rel
        check(any(x.endswith(u) or x.endswith(u + "index.html") for x in sm_urls),
              f"sitemap 缺 {u}")
    check(len(sm_urls) == len(pages), f"sitemap 条数 {len(sm_urls)} != 页面数 {len(pages)}")

    # hreflang 互认:每个 hreflang 目标页必须回指本页 canonical
    for can, hrefs in hl_map.items():
        for h in hrefs:
            tgt = hl_map.get(h)
            check(tgt is not None, f"hreflang 互认: {can} -> {h} 目标无对应页")
            if tgt is not None:
                check(can in tgt, f"hreflang 互认缺失: {can} 未在 {h} 的反向集合中")

    # 404 页:自指 canonical + noindex
    p404 = os.path.join(SITE, "404.html")
    check(os.path.exists(p404), "缺少 404.html")
    if os.path.exists(p404):
        h404 = open(p404, encoding="utf-8").read()
        m404 = re.search(r'<link rel="canonical" href="([^"]+)"', h404)
        check(m404 is not None and m404.group(1) == SITE_SCHEME + "://" + SITE_DOMAIN + "/404.html",
              "404 canonical 应为 /404.html")
        check('content="noindex"' in h404, "404 缺 noindex")

    # robots.txt:Sitemap 行指向本域
    rb_path = os.path.join(SITE, "robots.txt")
    check(os.path.exists(rb_path), "缺少 robots.txt")
    if os.path.exists(rb_path):
        rb = open(rb_path, encoding="utf-8").read()
        check(f"Sitemap: {SITE_SCHEME}://{SITE_DOMAIN}/sitemap.xml" in rb, "robots.txt Sitemap 行缺失/域错误")
        check("Allow: /" in rb, "robots.txt 缺 Allow: /")

    # 部署配置 vercel.json 随产物存在
    check(os.path.exists(os.path.join(SITE, "vercel.json")), "缺 vercel.json(部署配置未随产物)")

    print(f"pages={len(pages)} sitemap={len(sm_urls)} errors={len(errs)}")
    for e in errs[:30]:
        print(" ERR", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
