# Anime Breaker (animebreaker.online) — Hermes 交接

> 生成时间:2026-09-23。站点已本地构建并通过全站验证(verify errors=0)。
> 与本站相关的游戏事实来自 PRD Source Snapshot(2026-09-23):官方 Roblox listing、
> Pro Game Guides codes 覆盖(2026-09-22)、anime-breaker.wiki / animebreaker.wiki(仅作 discovery)。
> 未经核实的事实一律未写入页面,并以 VERIFIED / REPORTED / OBSERVED / UNVERIFIED 分级标注。

## 1. 仓库与构建

- 站点根:`/Users/hym/谷歌游戏网站/animebreaker.online`(Git 仓库,main 分支)
- 站点代码:`animebreaker.online/site`(第五套模板生成器:config.py + content_en/pt/es.py + generate.py/verify.py)
- 构建产物:`animebreaker.online/site/site`(正式,66 页 + sitemap + robots + 404)
- 本地预览:`animebreaker.online/site/site-preview`(链接指向 `127.0.0.1:8792`)

构建与验证(以 Git HEAD 为准执行):

```bash
cd /Users/hym/谷歌游戏网站/animebreaker.online/site
python3 build/generate.py                       # 正式构建 → site/site
python3 build/verify.py site                    # 验证:pages=66 sitemap=66 errors=0
python3 build/generate.py site-preview --domain 127.0.0.1:8792   # 预览版
```

## 2. 站点信息(与线上发布相关)

- 域名:`animebreaker.online`(正式,已写入 config.SITE["domain"])
- 语言:English(/) + Português-BR(/pt/) + Español(/es/),hreflang 交叉,不含中文
- 官方 CTA:https://www.roblox.com/games/109928390521457/ (Anime Breaker [🌳CLASS TREE])
- 开发者署名:HF x Anime Breaker(页脚免责声明;本网为玩家非官方资料站)
- GA4:目前为空(config.SITE["ga_id"]="";部署时填入,重启 generate.py 即可生效,无占位残留)
- 版权图:assets/media/*.jpg 与 hero-bg.jpg 来自官方 Roblox 体验页缩略图(universeId 10675117523),
  首页截图轨道与页内均有免责署名;favicon.svg/.ico 为本站自绘火焰主题(非官方素材)

## 3. 页面与事实分级(22 URL 全量,无 HOLD)

| 分区 | URL | 事实状态 |
|---|---|---|
| 核心 | `/` 首页、`/wiki/`、`/guides/`、`/codes/`、`/updates/` | READY(官方 loop+标题+码表 REPORTED 带日期) |
| 攻略 | `/guides/beginner-guide/`、`/guides/energy/`、`/guides/progression/` | READY(官方 loop) |
| 攻略 | `/guides/rank-up/`、`/guides/upgrades/`、`/guides/f2p/` | PARTIAL(决策框架;数值不发布) |
| 攻略 | `/guides/secret-boss-locations/`、`/guides/raids/`、`/guides/trial/` | PARTIAL(结构 REPORTED;HP/掉率/门票冻结) |
| Wiki | `/wiki/cards/`、`/wiki/companions/`、`/wiki/avatars/`、`/wiki/weapons/` | PARTIAL(pull rates/倍率/数值不发布) |
| Wiki | `/wiki/accessories/`、`/wiki/amulets/`、`/wiki/resources/`、`/wiki/worlds/` | PARTIAL(名称/数值不发布;worlds 为导航页) |

Codes 状态:上次核实 2026-09-22,REPORTED 约 14 个活跃码;站点列出
10KCCU / 2MVISITS / 20KFAVORITES / NEWPORTAL / NEWSHADOW,奖励留空待游戏内确认(快照无奖励明细)。

## 4. 未解决的事实缺口(供后续复核,勿补编造值)

- rank 成本/倍率、boss HP 与掉率、Avatar 倍率与掉率、武器数值、accessory/amulet 名称与数值、
  raid ticket 与波次奖励、card pull rates、trial 奖励 —— 二次来源互相矛盾,站内一律按 UNVERIFIED 处理
- 世界具体名称与顺序(仅"难度递增"框架)、秘密 boss 具体位置/名称 —— 未冻结
- 官方更新补丁细节(CLASS TREE 仅作为标题 tag 引用,未扩写成补丁内容)

## 5. 发布硬门禁(Hermes 执行)

```bash
python3 /Users/hym/谷歌游戏网站/scripts/verify_vercel_release.py \
  --repo /Users/hym/谷歌游戏网站/animebreaker.online/site/site \
  --domain animebreaker.online \
  --route / \
  --deploy
```

要求:worktree clean;Vercel Production READY 且 commit SHA = 本地 HEAD;
正式域名首页 200、canonical 指正式域名;robots.txt 与 sitemap.xml 可访问。

上线待办(需用户批准逐项执行):① 填 GA4 ID 后重建;② Vercel 项目(属主邮箱)创建并接 Git;
③ 域名 animebreaker.online 接入云flare 橙云 + SSL full;④ GSC 提交 sitemap + 首页与 P0 巡检;
⑤ 第 7/14 天按 GSC Query/Page 决定是否拆实体页(当前 HOLD:/tier-list/、/best-*/、单个 boss/weapon/companion/world 页、/rank-costs/)。

## 6. 已知约定(fifth-gen 模板)

- URL 规范(2026-09-23 修复):**全站统一目录式** — canonical / sitemap / hreflang / og:url / JSON-LD 均输出 `/codes/` 形态(与站内导航一致),仅 404.html 保持文件式;`build/components.py::site_url/site_path` 是唯一 URL 构造入口,改 URL 形态改这里。
- 导航当前页高亮按完整站点路径(含 pt/ es/ 前缀)匹配 `config.NAV` 的 url;语言切换器剥离当前语言前缀后互链。
- hero 背景:components.py 输出 hero-bg.jpg 实图 + `.hero-bg` 半透明渐变层(alpha 保留,可透出真实截图);
  styles.css :root 已换肤为实测官方截图色(火焰橙 #b8461c / 夜空蓝底 / 金沙点缀)
- 无旧游戏名/域名硬编码;占位符零残留(verify 覆盖)
- 红线词:download/cheat/hack/unblocked/apk 等零命中