# Anime Breaker — 部署上线文档 (animebreaker.online)

> 依据:`VERCEL-DEPLOYMENT-RUNBOOK-HERMES.md`(强制规范)+ `HERMES-HANDOFF.md`(本站交接)+ PRD §14/§15。
> 状态:本地构建与验证已通过;Vercel 项目/线上部署**未执行**(需用户逐项批准后再跑)。

## 1. 站点与项目标识

| 项 | 值 |
|---|---|
| 正式域名 | `animebreaker.online` |
| Git 仓库 | `/Users/hym/谷歌游戏网站/animebreaker.online`,`main` 分支 |
| 初始 commit | `8e7be020cb9fadaf21b65f3e6fda0da10d7b3264`(部署前更新为最新 HEAD) |
| 构建源码 | `animebreaker.online/site/build`(generate.py / config.py / content_en|pt|es.py) |
| 构建产物 | `animebreaker.online/site/site`(66 页 + sitemap.xml + robots.txt + 404.html) |
| Vercel rootDirectory | **`site/site`**(相对仓库根,两层 site 确实存在 → 允许) |
| Vercel 配置文件 | `site/site/vercel.json`(新建;静态站点,内容见 §3) |
| Vercel 团队 | `mays-projects-5ac61d10`(`team_o9hPMCsKkEHxEdT6VsksX7d5`) |
| 项目名建议 | 官方域名不可用时可 `animebreaker-online`;**禁止**新建名为 `site` 的项目 |
| 生产分支 | `main` |
| 官方 CTA | https://www.roblox.com/games/109928390521457/ |
| 语言 | en `/` · pt-BR `/pt/` · es `/es/`(hreflang 交叉,无 x-default 错误) |

## 2. 部署前门禁(逐项打勾后再动)

```bash
cd /Users/hym/谷歌游戏网站/animebreaker.online
git status --porcelain                                  # 必须为空(当前:空)
git rev-parse HEAD
python3 build/verify.py site                            # 由 site/build 目录执行;要求 pages=66 sitemap=66 errors=0
```

- [ ] ① 决定 GA4 ID:在 `site/build/config.py` 填 `SITE["ga_id"]` 后 `python3 build/generate.py` 重建再 verify;
- [ ] ② 提交:`git add -A && git commit`(允许新增/改动的文件:config.py、content_*.py、styles.css、*.md;禁止提交 `.vercel`、`site/site/`、`site/site-preview/`、`__pycache__/`——已写入 `.gitignore`);
- [ ] ③ `git push origin main`(GitHub 仓库连接 Vercel 后按 Git 生产部署);
- [ ] ④ 新建 Vercel 项目:`vercel project create animebreaker-online --scope mays-projects-5ac61d10`,绑定本仓库,rootDirectory=`site/site`,生产分支=`main`;
- [ ] ⑤ 单站点单绑定:仅允许 `<repo根>/.vercel/project.json`,projectId 全工作区唯一;不得在 `site/site/.vercel` 重复绑定;
- [ ] ⑥ 域名:`animebreaker.online` 接入 Cloudflare(橙云 + SSL Full),解析指向 Vercel 记录(NS 或 CNAME 按 Vercel 指引);改 DNS 需用户明确批准。

## 3. vercel.json(新建于 site/site/,部署前写入并与产物同目录提交)

```json
{
  "cleanUrls": false,
  "trailingSlash": true
}
```

- 静态输出无需构建命令(Build Command 留空或 `true`);`outputDirectory` 不设(产物即站点根);
- robots.txt 与 sitemap.xml 已在产物内,无需额外规则;不得把 `.vercel` 提交进 Git。

## 4. 部署(二选一,优先 Git)

Git 生产部署(推荐):

```bash
git push origin main
vercel ls animebreaker-online --scope mays-projects-5ac61d10
vercel inspect <deployment-id-or-url> --scope mays-projects-5ac61d10
```

必须确认:source=git、分支=main、commit SHA=本地 HEAD、projectId 正确、target=production、readyState=READY、aliasError=null。

CLI 预构建部署(仅全部门禁通过后,且必须从仓库根执行):

```bash
vercel pull --yes --environment=production --scope mays-projects-5ac61d10
vercel build --prod --scope mays-projects-5ac61d10
vercel deploy --prebuilt --prod --scope mays-projects-5ac61d10
```

禁止从 `site/site`、`site/` 自身或其他站点目录执行生产部署。

## 5. 线上验收门禁(缺一项不得报"上线成功")

```bash
curl -I -L --max-time 20 https://animebreaker.online/
curl -I -L --max-time 20 https://animebreaker.online/sitemap.xml
curl -I -L --max-time 20 https://animebreaker.online/pt/
curl -I -L --max-time 20 https://animebreaker.online/es/
curl -I -L --max-time 20 https://animebreaker.online/codes/
```

通过标准:首页/关键路由 200(或明确设计的 3xx);不能 404/5xx;不能出现旧项目内容串站。
内容核对:页面标题含 “Anime Breaker Roblox” 与品牌(火焰橙 #b8461c);sitemap `<loc>` 全部位于 `https://animebreaker.online/`;canonical 自指正式域名;robots.txt 可访问。
本站无广告位(`.ad-*`),跳过 §六.4;无 Serverless Function,`vercel logs --level error` 仅作无异常确认。

## 6. 上线后数据接入

1. GA4:填 config 后重建部署(§2 步骤 ①)。
2. GSC:以 `HTTPS://animebreaker.online` 添加资源 → 提交 `/sitemap.xml` → 巡检首页 + P0 路由(`/`、`/wiki/`、`/guides/`、`/codes/`、`/updates/`)canonical/indexability。
3. IndexNow:站点无动态推送后端,可跳过或按站内规则手工提交首页与 P0 路由。
4. 复查节奏:上线第 7 天、第 14 天各看一次 GSC Query/Page 曝光;若个别实体词(如单一 boss/weapon)出现独立意图且有可验证数据,再按 PRD §6 放开对应页面;批量实体页与 Tier/Best 页维持 HOLD。

## 7. 事实缺口复核清单(上线后随数据/官方来源补充,勿补编造值)

- rank 成本与倍率、boss HP/掉率、Avatar 倍率与掉率、武器数值、accessory/amulet 名称与数值、
  raid ticket/波次奖励、card pull rates、trial 奖励 → 当前一律 UNVERIFIED(站内已说明);
- Coach 码奖励(10KCCU 等 5 个)需在游戏内确认后补进 `/codes/` 表格奖励列;
- CLASS TREE 后续官方补丁细节,有官方来源后更新 `/updates/`;
- 世界具体名称/顺序、秘密 boss 名称/位置,实测后按 OBSERVED 分级补入对应 PARTIAL 页。

## 8. 部署记录(每次部署必须按此记账)

```text
日期/时区:
项目名:
Vercel projectId:
Git 仓库:
生产分支:
commit SHA:
rootDirectory: site/site
vercel.json 路径: site/site/vercel.json
部署 ID:
部署 source:
target: production
readyState:
aliasError:
正式域名: animebreaker.online
首页 HTTP 状态:
关键路由 HTTP 状态(/pt/ /es/ /codes/):
sitemap HTTP 状态:
运行时错误检查:
结论: PASS / FAIL
```