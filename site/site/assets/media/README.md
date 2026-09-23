# 图片规格(第五套模板)

| 文件 | 规格 | 用途 | 必须 |
|---|---|---|---|
| `screenshot-1.jpg` ~ `screenshot-4.jpg` | 1200×675(16:9),≤300KB | 首页截图轨道(4 张) | 建议放官方宣传图并保留页脚署名 |
| `favicon.svg` | 48×48 矢量 | 浏览器标签图标 | 建议替换 |
| `favicon.ico` | 16/32/48 多尺寸 | 兼容旧浏览器 | 建议替换 |

说明:
- hero 背景**不需要图片**——已用 CSS 渐变(深空 + 品牌色光晕),避免使用官方素材做品牌资产。
- 截图版权:用官方商店宣传图(Steam App 页 screenshots / App Store screenshotUrls),页脚已内置免责声明。
- 换 favicon 后,同步替换 `config.py` 的 `LOGO_SVG`(header/footer 内的 logo 是内联 SVG,需与 favicon 风格一致)。
- 图片放 `assets/media/` 后重新生成(`python3 build/generate.py`)即可被 `sync_static` 复制到预览/部署目录。
