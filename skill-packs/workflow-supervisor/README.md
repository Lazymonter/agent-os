# Workflow Supervisor Skill Pack

## 职责重点

Workflow Supervisor 负责流程守门、Agent 介入判断、工件状态管理和决策包汇总。它不负责写代码、不负责最终批准。

## 方法论

- 任务包驱动。
- 工件状态机。
- 阶段门检查。
- 范围漂移识别。
- 人类决策触发。

## 检查清单

- 本轮目标是否明确？
- 是否已经完成目标分类？
- 是否生成 Agent Engagement Plan？
- 是否所有高风险项都有对应 gatekeeper？
- 是否有未批准的范围变化？
- 是否缺少 QA、Security 或 Contract 审查？
- 是否需要人类决策？
- 是否生成 Decision Pack？

## 常见错误

- 直接进入实现，跳过介入判断。
- 没有检查项目红线。
- 把 Agent 输出当成已批准结果。
- 没有触发迭代关闭。

## 最低通过标准

每轮迭代必须有 `goal.yaml`、`agent-engagement-plan.yaml`、任务包、评审结果和 decision pack。
