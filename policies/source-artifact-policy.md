# 源资产策略

## 目的

确保需求和实现引用已有产品说明、原型、UI 设计稿、截图、评审文档等源资产。

## 源资产类型

- 产品说明文档。
- 原型包。
- 设计系统。
- CLI 原型。
- Desktop 原型。
- Mobile 原型。
- 评审 PDF。
- 关键截图。
- 项目执行手册、prompt registry、路线图或明确的迭代序列。

## 项目侧要求

项目必须维护：

```text
knowledge/source-assets/source-assets.yaml
```

每轮相关迭代必须维护：

```text
iterations/<id>/source-artifact-trace.md
```

## 规则

- 不能只根据口头目标实现 UI 或配置。
- 若源资产影响需求或设计，必须在 trace 中说明。
- 若源资产缺失，必须标记为风险。
- 若项目存在明确的执行手册或 prompt registry，迭代启动和迭代后置步骤必须追踪到该来源；Agent 不得仅根据上一轮产物自行推断下一个迭代。
