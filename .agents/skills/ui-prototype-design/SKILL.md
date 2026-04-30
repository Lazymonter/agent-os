---
name: ui-prototype-design
description: 当需要产出人类可评审的 UI 原型图、设计稿、HTML 原型、截图或设计系统时使用。
---

# UI Prototype Design Skill

## 使用时机

- 需要设计 Desktop、Mobile、Web 或 CLI 交互。
- 需要把需求转成可评审原型。
- 需要补充设计系统或状态页面。
- 需要输出人类能直接打开查看的设计稿。

## 输入

- Project Pack。
- 本轮需求。
- 源资产追踪文件。
- 已有原型或设计系统。
- 平台范围。

## 必须输出

至少输出以下之一，复杂 UI 建议全部输出：

- `prototype.html`
- `design-system.html`
- `review-deck.html`
- `screenshots/*.png`
- `README.md`

## 设计要求

- 覆盖正常、空状态、错误、警告、确认弹窗。
- 标注页面目标、信息结构、关键交互。
- 如果是移动端，应使用移动尺寸画布。
- 如果是桌面端，应使用桌面尺寸画布。
- 设计稿必须能追踪到需求和源资产。

## 建议流程

0. 执行 `policies/task-intake-exit-gate-policy.md` 的 Intake Gate，并在首次修改文件前输出 Intake 记录。
1. 阅读需求和源资产。
2. 列出页面清单。
3. 生成低保真结构。
4. 生成 HTML 高保真原型。
5. 生成设计系统页面。
6. 生成截图或评审 deck。
7. 写评审说明。
8. 执行 Exit Gate，确认源资产追踪、平台范围、forbidden paths、测试或截图证据和未决风险。
