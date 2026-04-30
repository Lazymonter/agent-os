# Agent 执行线程与实例化模式

## 目的

本文定义 Agent OS 中一次需求、设计、实现、验证或发布迭代的执行线程模型。它解决三个问题：

1. 哪些工作由主线程完成。
2. 哪些工作需要实例化独立 Agent。
3. 哪些工作必须由独立评审 Agent 或人类决策完成。

核心原则：

```text
角色不等于一定要独立实例。
默认由主线程负责目标理解、流程编排、任务拆解和结果汇总。
当任务需要隔离上下文、独立判断、并行执行或风险控制时，才实例化独立 Agent。
```

## 核心概念

| 概念 | 定义 |
|---|---|
| 主线程 | 本轮工作的控制线程，通常采用 Workflow Supervisor、Product & Requirements、Solution Architect & Task Planner 的组合视角。负责目标理解、范围判断、Agent 介入判断、任务拆解、汇总和 Decision Pack。 |
| 角色视角 | 主线程临时采用某个角色的方法论进行分析，不创建独立实例。 |
| 独立 Agent 实例 | 一个独立 Agent 会话，拥有明确角色、Task Packet、工作目录或分支、allowed paths、forbidden paths 和验收标准。 |
| 独立评审实例 | 专门用于 QA、Security、Contract 或 UX Review 的独立 Agent 实例，不参与实现，避免自证正确。 |
| 执行模式 | Agent Engagement Plan 和 Task Packet 中声明的执行方式。 |

## 执行模式

| execution_mode | 含义 | 适用场景 |
|---|---|---|
| `inline` | 主线程内完成，不创建独立实例。 | 目标理解、需求归类、范围判断、高层任务拆解、结果汇总。 |
| `isolated_task` | 独立实例执行，但可以在同一工作区中进行。 | 低风险文档、局部非代码产物、单文件更新、发布材料草拟。 |
| `isolated_worktree` | 独立实例加独立 worktree 或 branch。 | 代码实现、并行开发、跨多文件变更、可能影响共享行为的任务。 |
| `independent_review` | 独立评审实例，不参与实现。 | QA、Security、Contract、UX Review。 |
| `human_decision` | 必须由人类决策。 | 范围变化、架构重大变更、破坏性 schema 变更、安全风险接受、发布批准。 |

## 角色默认策略

| 角色 | 默认执行模式 | 说明 |
|---|---|---|
| Workflow Supervisor | `inline` | 负责流程、任务状态、汇总和 Decision Pack。 |
| Product & Requirements | `inline` | 需求判断与目标理解高度耦合，默认在主线程完成。 |
| Solution Architect & Task Planner | `inline` / `isolated_task` | 默认主线程；复杂架构或跨模块方案可独立实例化。 |
| Implementation | `isolated_worktree` | 涉及代码变更，必须通过 Task Packet 限制范围。 |
| QA & Verification | `independent_review` | 必须独立验证实现、测试、golden 和 forbidden changes。 |
| Security & Risk | `independent_review` | 涉及凭据、token、远程控制、文件删除、吞吐等高风险能力时必须独立审查。 |
| Contract & Data Model | `independent_review` / `isolated_task` | schema、API、CLI JSON、报告结构需要单独守门。 |
| UX/UI Design | `isolated_task` / `isolated_worktree` | 需要产出可评审原型、设计稿或交互说明。 |
| Release & Documentation | `isolated_task` | 发布材料、安装说明、Release Notes 适合独立产出；发布批准仍由人类完成。 |
| Agent OS Maintainer | `isolated_worktree` | Agent OS 维护应与项目迭代隔离。 |

## 实例化判断

| 场景 | 是否独立实例化 | 推荐方式 |
|---|---:|---|
| 目标理解 | 否 | `inline` |
| 需求归类 | 否 | `inline` |
| Agent 介入判断 | 否 | `inline` |
| 高层架构分析 | 通常否 | `inline`，复杂时 `isolated_task` |
| 详细架构设计 | 视复杂度 | `inline` 或 `isolated_task` |
| 任务拆解 | 通常否 | `inline` |
| 写代码 | 是 | `isolated_worktree` |
| 写测试 | 通常是 | 与实现绑定的单测可随 Implementation；验收验证建议 QA 独立 |
| QA 验证 | 是 | `independent_review` |
| Security 审查 | 是 | `independent_review` |
| Schema / API 审查 | 是 | `independent_review` |
| UI 原型和设计稿 | 是 | `isolated_task` 或 `isolated_worktree` |
| 发布准备 | 是 | `isolated_task` |
| Decision Pack | 否 | `inline` |
| 最终批准 | Agent 不可替代 | `human_decision` |

## Agent Engagement Plan 要求

每个 `selected_agents[]` 条目必须声明 `execution_mode`：

```yaml
selected_agents:
  - agent: product-requirements
    role: owner
    execution_mode: inline
    reason: "需要定义需求和验收标准，但不需要独立执行实例。"

  - agent: implementation
    role: owner
    execution_mode: isolated_worktree
    reason: "需要修改代码，必须限制在任务包授权范围内。"

  - agent: qa-verification
    role: gatekeeper
    execution_mode: independent_review
    reason: "需要独立验证实现结果，避免自证正确。"
```

## Task Packet 要求

每个 Task Packet 必须声明 `execution` 块：

```yaml
execution:
  mode: isolated_worktree
  branch: feature/I-0001/T-002-config-validator
  worktree: .worktrees/I-0001-T-002-config-validator
  owner_agent: implementation
  reviewer_agents:
    - qa-verification
    - contract-data-model
  human_approval_required: false
```

规则：

- `execution.mode` 必须是 `inline`、`isolated_task`、`isolated_worktree`、`independent_review` 或 `human_decision`。
- 代码实现任务默认使用 `isolated_worktree`。
- QA、Security、Contract 和 UX Review 默认使用 `independent_review`。
- 发布批准、范围变化、架构重大变更、破坏性 schema 变更和安全风险接受必须进入 `human_decision`。
- `execution.owner_agent` 必须与任务所有者一致。
- `execution.reviewer_agents` 必须覆盖 Task Packet 中要求的 gatekeeper。

## 标准执行顺序

```text
先串行：目标理解 -> 需求 -> schema / contract -> 任务拆解
再并行：实现任务、局部文档、低风险独立任务
最后串行：QA -> Security / Contract / UX -> Decision Pack -> 人类决策
```

## 独立实例最小上下文

实例化独立 Agent 时，至少提供：

- 项目或 Agent OS 的 `AGENTS.md`。
- 当前 Task Packet。
- Project Pack 或维护目标摘要。
- 相关 schema、contract、workflow、policy 和 rubric。
- 相关 source-artifact-trace。
- allowed paths 和 forbidden paths。
- acceptance criteria。
- required tests。
- 当前工作目录、branch 或 worktree 约束。

## 禁止行为

- 不得把角色名称等同于必须实例化。
- 不得让实现 Agent 自己完成最终 QA、Security 或 Contract 结论。
- 不得在没有 Task Packet 的情况下执行普通实现。
- 不得用 `inline` 执行跨多文件代码实现来绕过隔离要求。
- 不得由 Agent 替代人类批准发布、安全风险接受或重大范围变化。

## 迭代关闭检查项

- Agent Engagement Plan 是否为每个参与 Agent 声明 `execution_mode`。
- 每个实现任务是否有独立 Task Packet。
- 代码任务是否使用 `isolated_worktree` 或记录了例外理由。
- QA、Security、Contract、UX Review 是否按风险独立审查。
- Decision Pack 是否汇总所有独立评审结论。
- 所有人类决策项是否明确列出，且未被 Agent 代替批准。
