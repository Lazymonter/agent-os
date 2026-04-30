# Decision Pack — AOS-0001 after I-0002

## 决策标题

是否批准 Agent OS 增加“外部迭代序列 / prompt registry 优先”和“Task Packet 非无限授权”的通用规则。

## 背景

I-0002 执行后，人类反馈指出项目步骤来源于外部 prompts 目录，并要求每个项目迭代完成后执行 AOS-0001。此前 Agent 依据已生成 task packets 和自身推断建议开启新迭代，存在越过项目执行序列的风险。

## 推荐方案

批准本次 `Unreleased` 更新，作为后续小版本候选。

包含变更：

- `iteration-workflow` 增加迭代来源确认步骤。
- `forbidden-behavior-policy` 禁止 Agent 擅自发明、跳转或跳过迭代。
- `source-artifact-policy` 将执行手册、prompt registry 和迭代序列列为源资产类型。
- 项目 `AGENTS.md` 模板增加外部迭代序列优先规则。
- `CHANGELOG.md` 记录 Unreleased 更新。

## 风险评估

- 兼容性：低。规则只约束存在外部执行手册或明确迭代序列的项目。
- 安全：正向改进，减少越权推进和范围扩大风险。
- 流程：发布新版本需要人类批准。

## 需要人类决策

- 是否批准将本次 `Unreleased` 发布为后续 Agent OS 版本。
- 是否需要为已接入项目补充“外部执行手册 / prompt registry”字段模板。

## 发布建议

建议版本：`1.3.1`。这是流程约束增强，不是破坏性 schema 变更。
