# 原型与 UI 设计稿集成流程

## 目标

确保项目实现与已评审的产品原型、设计稿、设计系统、评审 PDF 和截图保持一致。该流程尤其适用于 App、Web、CLI 交互、报告页面、设置页面、确认弹窗和用户流程。

## 为什么需要该流程

产品原型和 UI 设计稿是已经评审过的产品意图。如果开发迭代只读取代码和需求，而不读取原型，就容易出现：

- 页面结构偏离设计稿。
- CLI 输出与原型中的终端交互不一致。
- 配置字段与设置页不一致。
- 报告内容与评审版报告不一致。
- iOS / Desktop 的角色边界被误实现。

## 源资产类型

```text
product_doc
review_deck
html_prototype
design_system
ui_screenshot
cli_prototype
mobile_prototype
desktop_prototype
```

## 标准流程

1. **登记源资产**  
   在 `knowledge/source-assets/source-assets.yaml` 中登记所有产品说明、原型、UI 截图和评审材料。

2. **判断相关性**  
   每轮迭代开始时，Product & Requirements 和 UX/UI 判断本轮是否涉及用户可见行为。

3. **生成源资产追踪**  
   在 `iterations/<id>/source-artifact-trace.md` 中列出本轮使用的原型和 UI 资产。

4. **提取约束**  
   从原型中提取页面、组件、文案、状态、命令输出、用户流程、确认弹窗和错误状态。

5. **写入任务包**  
   如果实现任务涉及用户可见输出，Task Packet 必须引用相关源资产。

6. **UX/UI 审查**  
   UX/UI Agent 检查实现是否符合源资产。

7. **QA 验证**  
   QA 检查 CLI 输出、报告内容、页面状态或截图是否和设计基线一致。

## 源资产追踪模板

```md
# Source Artifact Trace

## 本轮迭代

I-xxxx

## 相关源资产

| 资产 ID | 类型 | 路径 | 本轮用途 | 是否必须符合 |
|---|---|---|---|---|
| prototype-review-deck | review_deck | docs/design/prototype/ProxyQ_Review_Deck.pdf | 页面和产品边界参考 | 是 |

## 提取出的约束

- Dashboard 必须展示总体等级、流量、baseline、吞吐状态。
- Throughput 必须默认关闭，Full-speed 必须强确认。

## 不适用资产

列出为什么某些设计稿本轮不使用。
```

## 准出条件

- 涉及 UI / CLI / 报告 / 配置语义的迭代必须有 source-artifact-trace。
- 任务包引用了相关源资产。
- UX 或 QA 至少一个角色检查了用户可见输出。
- 如果实现偏离设计稿，必须形成 Decision Pack 并由人类批准。
