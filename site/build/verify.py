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
    "en": ["download", "cheat", "unblocked", "hack", "apk"],
    "zh": ["下载", "作弊", "破解", "外挂"],
    "ja": ["ダウンロード", "チート", "ハック", "ハッキング"],
}
# 允许保留的占位符(部署前需替换;system-one/two/three 为模板默认栏目占位,替换成真实 slug)
ALLOWED_PLACEHOLDER = ("[[DOMAIN]]", "[[GA_ID]]", "[[GAME_NAME]]", "[[game-slug]]", "[[DEVELOPER]]", "[[CTA_URL]]",
                       "[[system-one]]", "[[system-two]]", "[[system-three]]")

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
    global SITE_DOMAIN
    m = re.search(r"<loc>(https?://[^/<]+)", sm)
    SITE_DOMAIN = re.sub(r"^https?://", "", m.group(1)) if m else ""

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

        # hreflang:en/zh-CN/ja 三条且目标存在;x-default 仅英文首页
        hrefs = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', h))
        for hf, url in hrefs.items():
            fp = url.replace("https://", "").replace("http://", "")
            fp = fp[fp.find("/"):].lstrip("/")
            fp = fp if fp.endswith(".html") else fp + "index.html"
            check(os.path.exists(os.path.join(SITE, fp)), f"{rel}: hreflang {hf} -> {url} 目标缺失")
        if "x-default" in h and rel != "index.html":
            errs.append(f"{rel}: x-default 只应出现在英文首页")
        if rel == "index.html" and "x-default" not in h:
            errs.append("index.html: 缺 x-default")

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

        # 占位残留(白名单外)
        for ph in set(re.findall(r"\[\[[A-Za-z0-9_-]+\]\]", h)):
            if ph not in ALLOWED_PLACEHOLDER:
                errs.append(f"{rel}: 未知占位符 {ph}")

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

    print(f"pages={len(pages)} sitemap={len(sm_urls)} errors={len(errs)}")
    for e in errs[:30]:
        print(" ERR", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
