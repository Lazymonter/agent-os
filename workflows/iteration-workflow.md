# 迭代流程

## 目标

迭代流程用于把一个目标、需求、缺陷或技术任务转成结构化工件、Agent 介入计划、任务包、验证结果、决策包和学习反馈。Agent OS 不按每日或每周节奏推进，而是按一次迭代完成一个功能包、需求包或工程产物包。

## 适用场景

- 新功能开发。
- 功能变更。
- Bug 修复。
- 技术方案设计。
- UI / 交互设计。
- 数据契约变更。
- 安全审查。
- 发布准备。
- 项目知识更新。

## 标准状态机

```text
goal_created
↓
classified
↓
engagement_planned
↓
requirements_defined
↓
designed
↓
task_packets_created
↓
implemented
↓
verified
↓
reviewed
↓
human_decision_required
↓
approved / rework_required / rejected
↓
baselined
```

## 参与角色

| 阶段 | 默认角色 | 说明 |
|---|---|---|
| Goal Intake | Workflow Supervisor | 创建迭代目录和 goal.yaml。 |
| 目标分类 | Product & Requirements | 判断目标类型、产品影响、需求影响。 |
| Agent 介入 | Workflow Supervisor | 根据规则选择 owner / reviewer / consultant / gatekeeper。 |
| 架构与任务 | Solution Architect & Task Planner | 输出方案、依赖图和任务包。 |
| 数据契约 | Contract & Data Model | 当涉及 schema / API / CLI JSON / 报告格式时介入。 |
| UI / 交互 | UX/UI Design | 当涉及页面、流程、CLI 输出、确认弹窗时介入。 |
| 安全风险 | Security & Risk | 当涉及凭据、远程控制、文件删除、token、吞吐等高风险能力时介入。 |
| 实现 | Implementation | 执行任务包授权范围内的实现。 |
| 验证 | QA & Verification | 验证测试、任务边界、验收标准和 golden files。 |
| 决策 | 人类决策者 | 批准、驳回或要求返工。 |

## 标准步骤

0. **执行 Intake Gate**  
   对任何会生成或修改迭代工件的步骤，先执行 `policies/task-intake-exit-gate-policy.md`，读取项目规则、Project Pack、Skill、相关 workflow/policy/rubric，并记录允许修改范围。

1. **创建目标**  
   在 `iterations/<iteration-id>/goal.yaml` 中记录目标、背景、约束、预期输出。

2. **读取项目上下文**  
   读取 `AGENTS.md`、Project Pack、源资产清单、已有 ADR、相关 schema 和相关原型。

3. **目标分类**  
   输出 primary_type 和 secondary_types，例如 `new_feature`、`implementation`、`data_contract`、`ui_ux_design`、`security_review`。

4. **影响分析**  
   对以下维度给出 none / low / medium / high：
   `product_scope`、`requirements`、`architecture`、`data_contract`、`ui_ux`、`implementation`、`testing`、`security`、`release`、`documentation`。

5. **Agent 介入判断**  
   使用 `registry/engagement-rules.yaml` 生成 `agent-engagement-plan.yaml`。

6. **需求和验收标准**  
   Product & Requirements 生成 `requirements.md`、`acceptance-criteria.md` 或相应片段。

7. **源资产追踪**  
   如果已有原型或设计稿，本轮迭代必须在 `source-artifact-trace.md` 中说明哪些资产被使用，哪些不适用。

8. **架构设计与任务拆解**  
   Architect 生成 `architecture/design.md`、`task-decomposition.md`、`dependency-graph.md`。

9. **生成任务包**  
   在 `task-packets/` 下生成每个可执行任务。每个任务包必须包含 allowed changes、forbidden changes、输入、输出、测试要求。

10. **执行任务**  
    Implementation 只执行任务包授权范围。若需要越权修改，必须停下并生成 Decision Pack。

11. **验证和审查**  
    QA 检查测试、约束、输出、golden files。Security / Contract / UX 按介入计划审查。

12. **生成决策包**  
    Supervisor 汇总结果、风险、未决问题和建议，提交人类决策。

13. **学习反馈**  
    迭代结束后，将项目专属学习写入项目仓库；可泛化学习通过 Learning Proposal 提交给 Agent OS。

14. **执行 Exit Gate**  
    关闭或交付阶段前，记录验收、测试、forbidden paths、secret scan、项目红线和人类决策状态。

## 输出工件

```text
iterations/<id>/goal.yaml
iterations/<id>/iteration-brief.md
iterations/<id>/agent-engagement-plan.yaml
iterations/<id>/requirements.md
iterations/<id>/acceptance-criteria.md
iterations/<id>/source-artifact-trace.md
iterations/<id>/architecture/design.md
iterations/<id>/architecture/task-decomposition.md
iterations/<id>/task-packets/*.yaml
iterations/<id>/reviews/*.md
iterations/<id>/decision-pack.md
iterations/<id>/learning/*.md
```

## 与原型和 UI 的关系

任何涉及用户操作、页面、CLI 输出、配置文件含义、报告内容、确认弹窗的迭代，都必须读取源资产清单。即使本轮是后端或 Core 任务，也要判断该任务是否会影响 UI / CLI / 报告呈现。

## 准出条件

- `goal.yaml`、`iteration-brief.md`、`agent-engagement-plan.yaml` 已存在。
- 相关需求和验收标准清楚。
- 已判断是否需要 UX / Contract / Security 介入。
- 如存在相关原型或 UI，已生成源资产追踪。
- 任务包已拆到可独立执行和验证。
- QA 已给出验证结论。
- 需要人类决策的事项已明确。
