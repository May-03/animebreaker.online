# 第五套 · 生成器版多语言游戏 Wiki 站模板(直接用)

> 来源:由 Project Tomorrow 站(2026-08)实战沉淀。核心不是"静态页面",而是**生成器做法**:
> 一套 `config.py`(站点配置)+ 三份 `content_*.py`(内容)+ `components.py`(渲染组件)即可生成全站
> 任意语言的页面,自动保证:三语结构一致、hreflang 交叉、canonical 自指、JSON-LD、sitemap、红线词零命中。
>
> ⚠️ 模板只读:建站前先读父目录 `使用规范.md`。**复制整个第五套到你的项目再用,原始模板不动。**

---

## 这套模板解决什么(与其他套的区别)

| 其他套(1-4) | 第五套 |
|---|---|
| 纯静态 HTML,每页手改,多语言易不一致 | 生成器,改内容后一次生成全站 |
| 多语言 hreflang/切换器要手动维护 | 自动:3 语互链 + x-default + 语言切换器(桌面/移动) |
| 页面结构靠人保持一致 | 组件统一渲染,结构天然一致 |
| SEO 元数据易漏 | canonical/hreflang/JSON-LD/sitemap 全自动 |
| 验证靠肉眼 | 内置 `build/verify.py` 一键检查 h1/红线词/死链/JSON-LD |

适合:**Steam/PC 游戏的信息/攻略/百科站,需要 多语言(默认英+简中+日语),追求 SEO 规范**。

---

## 快速开始(建新站 6 步)

### 1. 复制模板到项目
```bash
cp -R "模版/网站模版/第五套" <新站>/site
```

### 2. 改 `build/config.py`(站点级配置,唯一必改)
| 位置 | 改什么 |
|---|---|
| `SITE["name"]` | 游戏显示名(各语言页面保留原文) |
| `SITE["developer"]` | 开发商/版权方(页脚免责声明) |
| `SITE["domain"]` | 正式域名(部署前替换成真实域名) |
| `SITE["cta_url"]` | 官方商店页(Steam App 页,务必核实真实存在) |
| `SITE["ga_id"]` | GA4 ID(可后补) |
| `NAV` | 三栏导航条目:换成你游戏的栏目(每语言一份;条目 url 与 content 页面 path 对应) |
| `HERO_TITLE` / `BRAND` / `LOGO_SVG` | 首页大标题、品牌色、logo(可选) |
| `LANGS` / `LANG_ORDER` | 增减语言(默认 en/zh/ja;删语言 = 从 LANG_ORDER 删 key + 删 content import) |

> 占位路径 `/[[system-one]]/` 等:全局替换成真实 slug(如 `/base-building/`),并在 content 里新建对应页面。

### 3. 填内容 `build/content_en.py` / `content_zh.py` / `content_ja.py`
- 每语言一份;页面数据模型与 block 类型见文件头注释(含 home/wiki/guides/beginner-guide/system/updates 六类示范)。
- **三语结构必须一致**(同页面数、同 h2、同 FAQ)——verify 会隐式检查 hreflang 目标存在,结构不一致会连锁报错。
- 想加页面:复制任一页面 dict,改 `path`(与 NAV url 对应)+ 内容,并加入 `PAGE_ORDER`。
- 内容红线(继承自实战):**只写官方/可验证事实**;数值/名称/配方不确定就写"未公布/暂不列出",绝不编造;`download/cheat/hack` 等词零命中(中/日/英各有列表,在 `build/verify.py` 可调)。

### 4. 生成 + 本地预览
```bash
cd <新站>/site
python3 build/generate.py                    # 生成到 site/(默认目录,占位符保留)
python3 build/generate.py site-preview --domain 127.0.0.1:8792   # 本地预览版(链接可点击)
python3 -m http.server 8792                   # 在 site-preview 下起服务,浏览器打开 http://127.0.0.1:8792/
```

### 5. 验证(上线前必须 0 错误)
```bash
python3 build/verify.py site-preview   # 或 site
# 检查:页面数/h1 唯一/canonical 自指/hreflang 交叉/x-default/JSON-LD 可解析/红线词/死链/sitemap 条数/占位残留
```

### 6. 部署
1. 全局替换占位符:`[[DOMAIN]]`(全站 + sitemap.xml + robots.txt)、`[[GA_ID]]`(每页 head)、`[[GAME_NAME]]`、`[[CTA_URL]]`(若 config 未填)
2. 替换 `favicon.svg` / `favicon.ico` / `LOGO_SVG`,放 4 张截图到 `assets/media/`
3. 提交(Vercel 属主邮箱)→ Vercel 部署 → 绑域名 → Cloudflare 橙云 + SSL full → IndexNow → GSC
   (完整流程见 `站上线Playbook.md`;上线后输出参照 `codex-review-handoff.md` 格式)

---

## 文件结构

```
第五套/
├── README.md              # 本说明(套用指南)
├── build/
│   ├── config.py          # ★ 站点配置:游戏名/域名/CTA/导航/语言/品牌色/logo(改这里)
│   ├── content_en.py      # ★ 英文内容(六类页面示范)
│   ├── content_zh.py      # ★ 简体中文内容(结构对应 en)
│   ├── content_ja.py      # ★ 日本語内容(结构对应 en)
│   ├── components.py      # 渲染组件(header/nav/footer/FAQ/related/JSON-LD)——不用改
│   ├── generate.py        # 生成器(支持 --domain 预览、静态资源同步)——不用改
│   └── verify.py          # 上线前验证脚本——不用改(红线词表可按站调整)
├── styles.css             # 设计系统(深色暖底;品牌色在 :root,换肤即改)
├── favicon.svg / favicon.ico   # 占位图标,换站必换
└── assets/media/README.md # 图片规格
```

## 页面自动生成的内容(无需手写)
- 每页:`<html lang>`、title/meta/canonical(自指)、hreflang(3 语交叉,x-default 仅英文首页)、
  Open Graph/Twitter Card、FAQPage+Article+BreadcrumbList JSON-LD、语言切换器(桌面+移动)、
  三栏下拉导航 + 移动分组菜单、页脚 4 列
- 首页:hero(背景图 `assets/media/hero-bg.jpg` 透过半透明渐变 + 四格统计 + 双 CTA)、截图轨道(4 张+署名)、Quick Facts 表格、卡片网格、FAQ
- 内容页:面包屑、doc-hero、正文(标题/列表/表格/提示/视频外链卡/卡片组)、FAQ、Keep reading(紧凑卡片)
- `sitemap.xml`(全部 indexable URL)、`robots.txt`、`404.html`(含三语入口)

## 样式定制点(styles.css)
| 目标 | 位置 |
|---|---|
| 品牌色 | `:root` 的 `--color-brand*` / `--color-accent*`(模板默认青绿+橙仅作占位;换肤前先按下一节「★ 品牌色怎么定」实测取色) |
| hero 背景 | `.hero-bg` = 半透明压暗渐变(带 alpha),让底层 `assets/media/hero-bg.jpg`(components 输出的 `<img>`)透出;⚠ 不要改成全不透明渐变,否则会遮住真实游戏图(2026-08-26 修复沉淀,见全局记忆 fifth-template-hero-bg) |
| hero 顶部间距 | `.hero` 的 `min-height`(默认 `min(62vh,34rem)`)与 `padding-top`(默认 `clamp(3rem,6vw,4.5rem)`):导航栏与 hero 标题之间的空隙,两处一起调(2026-08-24 由 Animal Hospital 站实测收敛) |
| 语言切换器 | `.lang-switcher*`(纯 CSS,无 JS) |
| Keep reading 卡片 | `.related-*`(已紧凑化:小内边距/小标题) |
| footer 4 列一排 | `@media (min-width:1024px) .footer-cols` |

## ★ 品牌色怎么定(必读,2026-08-27 MGS 站沉淀)

不要凭印象或直接用默认配色,抓**官方宣传图实测取色**,保证玩家一眼「对味」
(例:恐怖游戏用暗红深紫、童话游戏用粉蓝暖黄;MGS 黑金、MGS4 钢蓝灰都是实测出来的):

1. **取素材**:官网/商店页的 header、capsule、key art(如 Steam App 页 `header_image` / `capsule_imagev5`),必要时加 2–4 张官方截图。
2. **实测主色**(Python + PIL):跳过纯黑背景(`if (r+g+b)/3 < 50: continue`),对剩余像素低精度分桶(`r//16*16`)取高频色;
   高饱和色(如 key art 的标题色)就是 `--color-brand*` 候选,大面积低饱和灰调是氛围/accent 候选。
3. **映射 HSL** 到 `:root` 与 `build/config.py` 的 `BRAND`:
   - `--color-brand*` = 主视觉标题/logo 色;`--color-brand-ink` = 金字上放文字的深色;
   - `--color-accent*` = 场景氛围或次强调色;底色系 `--color-bg*`/`--color-surface*` 对齐主视觉底(黑底 key art → 冷黑)。
4. **同步**:`.hero-bg` 渐变里的 rgba 换成新主色(⚠ 必须保持带 alpha 半透明渐变,见上表 hero 背景行);
   `favicon.svg/.ico`、header/footer 的 `LOGO_SVG` 一起换同款配色。
5. **验证**:起预览目测导航 hover + 主按钮 + hero 区是否与官方视觉同调。

> 反例(不要做):直接用模板默认青绿/橙或凭感觉选色 —— MGS 站初版先用了默认蓝+橙,实测官方 key art 是
> 黑底+金黄标题(`#f0d000` hsl(52,100%,47%))+ 钢蓝灰场景,换成黑金后才「对味」。

## 常见问题
- **想只做单语站?** LANG_ORDER 留 `["en"]`,删掉 content_zh/ja 的 import(generate.py 顶部)即可;hreflang 自动只剩 en。
- **想加第 4 种语言?** LANGS 加一项(如 `"de": {"dir":"de/", "lang":"de", ...}`),新建 content_de.py,加进 generate.py 的 import。
- **内容改完没生效?** 改的是 content_*.py,必须重新跑 `python3 build/generate.py`;预览目录同理重新生成。
- **验证报死链?** 多半是 NAV 里加了条目但 content 里没建对应页面,或占位路径没替换。

## ★ 已内置修复(2026-09-09 theveil.pro / 2026-09-12 screamandrun.pro 实战回流,新站直接可用)
1. **导航下拉不自动收回**(语言切换器/移动菜单 `details` 点开后再点外部不收起):
   components.py 已内置 `NAV_SCRIPT` 并在 generate.py `render_page` 全局注入。
   **2026-09-12 增强**:除 click 外同时监听 `mouseover` 与 `focusin` —— 桌面端用 hover 切到旁边栏目/正文时也会收起
   (旧版只听 click,鼠标悬停切换不触发事件,用户会报"点开后切到旁边不收起");`window.__navUiInit` 防重;
   render_header 里旧的 close_script 已删除(与 NAV_SCRIPT 重复注册)。
2. **hero 次 CTA 在深色 hero 上"没填色"**(`.btn-ghost` 深表面色与 hero 背景同色):
   components.py 的 cta2 已带 `hero-cta2` 类,styles.css 已内置 `.hero .btn-ghost.hero-cta2`
   = 与主按钮同款实色品牌渐变 + 1px ink 描边(主次区分)。
3. **footer Site 列被挤到第二行**(4 组 footer_cols + footer_site 共 5 列,桌面 4 列 grid 会换行):
   styles.css 桌面媒体查询已改 `repeat(auto-fit, minmax(11rem, 1fr))`,按实际列数自适应。
4. **首页内容单薄**(模板示例首页只有 3 个 h2,套站后被用户报"内容太少、看不出信息量");
   **2026-09-13 已固化进模板**:`build/content_{en,zh,ja}.py` 示例首页现已直接是 **6 区块结构 + FAQ 7 条**
   (① What is X?(`p`×2) ② 核心循环 `h2`(`p` + `ol` 5 步) ③ X at a glance(`table` + `note`)
   ④ 模式与成长 `h2`(`p` + `ul` 3 条带内链) ⑤ 为什么本站以验证优先(`p` + `ul` + `note`) ⑥ 入口卡片(`cards` 6 张)),
   三语结构逐块一致;套站时只需把占位文本替换成真实内容,**不要删区块**。线上范例:`~/谷歌游戏网站/dumbwaystobuild.pro/site/build/content_en.py` 首页(2026-09-13 实战)。
5. **占位符残留(最易漏 LOGO 的 aria-label)**:
   部署前 `grep -rn '\[\[' site --include=*.html` 必须为空。config.py 里 `SITE["domain"]` 直接填真实域名
   (本地预览用 `generate.py site-preview --domain 127.0.0.1:PORT` 覆盖)、未配置 GA 时 `ga_id` 留空串(不输出 gtag)、
   LOGO 的 `aria-label` 已改为引用 `SITE["name"]`(2026-09-12 修复:旧版是 `[[GAME_NAME]]` 占位符,不在部署替换清单里最易漏)。
检查:起预览后目测①语言下拉点开再切到旁边/点外部都收回 ②hero 两按钮都有填色 ③footer 所有栏目同一排
④首页 ≥6 个内容区块 ⑤`grep '\[\['` 无残留。
