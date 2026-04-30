# Agent OS Runtime Neutral v1.2 中文版

Agent OS 是一套**运行时中立**的 AI Agent 软件工程操作系统。它不绑定 Codex、Claude Code 或任何特定 Agent Runtime；任何能够读取仓库文件、执行脚本、修改代码、运行测试的 Agent Runtime，都可以按同一套规则使用。

## 核心原则

- `AGENTS.md`：稳定规则、红线、执行边界。
- `.agents/skills/`：可复用工作流 Skill。
- `skill-packs/`：Agent 自身技能知识。
- `domain-packs/`：领域知识。
- `project-pack`：项目知识，在项目仓库维护。
- `task-packet`：单任务约束。
- `decision-pack`：人类决策包。
- `learning-proposal`：学习反馈提案。

## 本版重点

本版补齐了真实落地前缺失的内容：

1. `workflows/` 全部扩展为可执行流程。
2. `skill-packs/`、`policies/`、`schemas/`、`rubrics/` 不再是重复模板。
3. `docs/` 只保留项目无关内容。
4. `examples/proxyq/` 提供完整示例，包括初始化、需求迭代、开发迭代和 Agent OS 自我迭代。
5. 新增 UI 原型设计产出机制，确保设计稿能给人类评审。
6. 新增迭代关闭机制，防止 `iterations/` 文件爆炸。

## 快速使用

初始化一个项目：

```text
请读取 ../agent-os/AGENTS.md，并使用 ../agent-os/.agents/skills/project-bootstrap 初始化项目。
```

开启一轮迭代：

```text
请读取项目的 AGENTS.md，并使用 ../agent-os/.agents/skills/iteration-start 开启迭代。
```

关闭一轮迭代：

```text
请使用 ../agent-os/.agents/skills/iteration-close 对本轮迭代做知识沉淀、审计摘要和临时文件清理。
```
