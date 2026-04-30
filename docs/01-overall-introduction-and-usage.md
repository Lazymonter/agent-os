# Agent OS 整体介绍与使用说明

Agent OS 是项目无关的 AI Agent 软件工程操作系统。它将软件工程拆成可复用的角色、Skill、流程、模板、策略、评审标准和学习机制。

## 双仓库模式

```text
agent-os/
  通用 Agent 体系、Skill、流程、模板、策略。

project-repo/
  项目知识、需求、代码、测试、迭代记录和项目反馈。
```

## 基本运转方式

1. 项目初始化：通过 `project-bootstrap` Skill 生成项目结构和 Project Pack。
2. 目标进入：用户提出目标，写入 `iterations/<id>/goal.yaml`。
3. 介入判断：通过 `agent-engagement` Skill 判断需要哪些角色、审查和执行模式。
4. 任务拆解：通过 `task-decomposition` Skill 生成 task packets。
5. 任务执行：通过 `task-execution` Skill 完成代码、文档或设计。
6. 验证审查：通过 QA、Security、Contract 等 Skill 验证。
7. 决策：通过 decision pack 交给人类批准。
8. 迭代关闭：通过 `iteration-close` Skill 沉淀知识并清理临时过程信息。

## 运行时中立

Agent OS 不关心执行者是 Codex、Claude Code 还是其他工具。执行者只需要遵守：

- 读取 `AGENTS.md`。
- 读取 Project Pack。
- 使用 `.agents/skills/`。
- 遵守 task packet。
- 遵守 Agent Engagement Plan 和 Task Packet 中声明的 execution_mode / execution。
- 运行验证脚本。
- 输出可审查结果。
