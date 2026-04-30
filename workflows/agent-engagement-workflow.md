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

## 必须介入规则

- `data_contract = high`：Contract & Data Model 必须介入。
- `security = high`：Security & Risk 必须作为 gatekeeper。
- `ui_ux = high`：UX/UI Design 必须介入。
- `implementation = high`：Solution Architect、Implementation、QA 必须介入。
- `release = high`：Release & Documentation、QA、Security 必须介入。
- 涉及 schema 破坏性变更：必须人类批准。
- 涉及项目范围变化：必须人类批准。

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
    reason: string
human_decision_required: []
```

## 准出条件

- 每个高影响维度都有对应 Agent。
- 每个 gatekeeper 都说明阻断条件。
- 需要人类决策的事项已列出。
- 没有把项目红线绕过去。
