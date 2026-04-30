# UI 原型与设计稿产出指南

## 目标

当项目需要 UI Agent 产出原型图或设计稿时，必须产出人类可阅读、可评审、可交付的文件，而不是只有文字描述。

## 推荐产物

- `prototype.html`：可点击或可浏览的 HTML 原型。
- `design-system.html`：设计系统页面。
- `review-deck.html`：评审版设计稿说明。
- `screenshots/*.png`：关键页面截图。
- `README.md`：评审说明。
- 可选：`prototype.zip`。

## 产出要求

- 页面应模拟真实尺寸，例如 desktop 1440×900、mobile 390×844。
- 必须包含关键状态：正常、空状态、错误、警告、确认弹窗。
- 必须体现信息层级、按钮、表格、卡片、导航和表单。
- 必须引用项目源资产和需求。
- 每个页面都要有对应的设计说明。

## AI Agent 执行方式

UI Agent 使用 `ui-prototype-design` Skill：

1. 读取 Project Pack。
2. 读取需求和 source-artifact-trace。
3. 读取设计系统或现有原型。
4. 生成 HTML 原型和设计稿。
5. 使用截图脚本或浏览器截图生成 PNG。
6. 生成 review-deck。
7. 交给人类评审。

## 最低可接受标准

- 人类打开 HTML 能看懂产品结构。
- 人类打开 PNG 能看到关键页面设计。
- 设计稿能直接用于评审会议。
- 设计稿能追踪到需求和源资产。
