# Agent 介入判断流程

## 目标

在每一轮目标提出后，判断需要哪些 Agent 角色介入，以及它们是 owner、reviewer、consultant 还是 gatekeeper。该流程不是项目初始化时的一次性动作，而是每轮迭代都必须执行。

## 判断输入

- `goal.yaml`
- Project Pack
- 项目红线规则
- 源资产清单
- 当前迭代类型
- Engagement Rules
- Agent Registry

## 分类维度

目标类型：

```text
new_feature
feature_change
bug_fix
technical_design
implementation
testing
security_review
ui_ux_design
data_contract
release
documentation
research_spike
refactor
```

影响维度：

```text
product_scope
requirements
architecture
data_contract
ui_ux
implementation
testing
security
release
documentation
```

影响等级：

```text
none
low
medium
high
```

## 介入角色类型

| 模式 | 含义 |
|---|---|
| owner | 主产出者，负责生成核心工件。 |
| reviewer | 审查者，负责检查产物质量。 |
| consultant | 顾问，提供约束和建议。 |
| gatekeeper | 守门者，可以阻断进入下一状态。 |

## 执行模式

每个被选中的 Agent 都必须声明 `execution_mode`，用于说明它是在主线程中作为角色视角工作，还是需要实例化独立执行或评审实例。

| execution_mode | 含义 |
|---|---|
| `inline` | 主线程内完成，不创建独立实例。 |
| `isolated_task` | 独立实例执行，可在同一工作区完成低风险局部任务。 |
| `isolated_worktree` | 独立实例加独立 worktree 或 branch，默认用于代码实现。 |
| `independent_review` | 独立评审实例，不参与实现。 |
| `human_decision` | 人类决策事项，Agent 只能提出选项和风险，不能代替批准。 |

## 必须介入规则

- `data_contract = high`：Contract & Data Model 必须介入。
- `security = high`：Security & Risk 必须作为 gatekeeper。
- `ui_ux = high`：UX/UI Design 必须介入。
- `implementation = high`：Solution Architect、Implementation、QA 必须介入。
- `release = high`：Release & Documentation、QA、Security 必须介入。
- 涉及 schema 破坏性变更：必须人类批准。
- 涉及项目范围变化：必须人类批准。

## 默认执行策略

- Workflow Supervisor、Product & Requirements 默认 `inline`。
- Solution Architect & Task Planner 默认 `inline`，复杂架构或跨模块方案可使用 `isolated_task`。
- Implementation 默认 `isolated_worktree`。
- QA & Verification、Security & Risk、Contract & Data Model、UX Review 默认 `independent_review`。
- Release & Documentation 默认 `isolated_task`；发布批准本身必须是 `human_decision`。
- 范围变化、架构重大变更、破坏性 schema 变更、安全风险接受必须加入 `human_decision_required`。

## 输出

生成 `agent-engagement-plan.yaml`，至少包含：

```yaml
iteration_id: string
classification:
  primary_type: string
  secondary_types: []
impact:
  product_scope: low|medium|high|none
selected_agents:
  - agent: string
    role: owner|reviewer|consultant|gatekeeper
    execution_mode: inline|isolated_task|isolated_worktree|independent_review|human_decision
    reason: string
human_decision_required: []
```

## 准出条件

- 每个高影响维度都有对应 Agent。
- 每个 gatekeeper 都说明阻断条件。
- 每个 selected agent 都声明 execution_mode。
- 实现类 owner 默认隔离到 isolated_worktree，若例外必须说明理由。
- QA、Security、Contract 和 UX Review 的最终结论必须来自 independent_review 或 human_decision。
- 需要人类决策的事项已列出。
- 没有把项目红线绕过去。
