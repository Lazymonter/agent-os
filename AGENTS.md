# AGENTS.md — Agent OS 运行时中立规则

## 目的

本仓库定义可复用的 AI Agent 软件工程操作系统。任何 Agent Runtime 都应读取并遵守本文件。

## 运行时中立规则

- 不为某个特定 Agent Runtime 建立专用知识目录。
- 不在通用规则中写入 Codex、Claude Code 或其他运行时的专属行为。
- 所有运行时都应通过同一套 `AGENTS.md`、`.agents/skills/`、templates、policies、rubrics 工作。
- 若某运行时需要特殊启动方式，只能放入用户自己的启动说明，不进入 Agent OS 通用流程。

## 仓库治理规则

- `docs/` 只放项目无关内容。
- 具体项目示例放入 `examples/<project>/`。
- 项目专属知识不得合入 Agent OS 主干。
- 多项目反馈必须先进入隔离反馈区，经脱敏、分类、提炼后才能成为通用规则。
- 原始项目过程内容不得进入 Agent OS main。

## 执行红线

- 执行任何会修改文件或生成正式工件的任务前，必须通过 `policies/task-intake-exit-gate-policy.md` 的 Intake Gate；结束前必须通过 Exit Gate。
- 不得擅自扩大项目范围。
- 不得修改已冻结 schema，除非任务包明确授权。
- 不得将项目特例写成通用规则。
- 不得把敏感信息、凭据、token、私有日志写入 Agent OS。
- 不得为了让测试通过而无解释地更新 golden files。
- 不得删除迭代目录，除非已执行 `iteration-close` 并通过人类确认。

## 输出要求

所有 Agent 输出至少包含：

1. 已读取的关键输入。
2. 完成的产物。
3. 未完成或不确定事项。
4. 是否需要人类决策。
5. 是否产生项目学习或 Agent OS 学习提案。
6. 对应任务的 Intake Gate / Exit Gate 摘要；只读探索或简单状态查询可说明不适用。
