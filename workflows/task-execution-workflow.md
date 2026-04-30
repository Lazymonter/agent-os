# 任务执行流程

## 目标

确保任何实现任务都在 Task Packet 约束下执行，避免 Agent 擅自扩大范围、修改冻结契约或绕过测试。

## 输入

- Task Packet
- 项目根目录 `AGENTS.md`
- 相关目录规则
- 相关 schema / API 契约
- 相关测试和 golden files
- 相关源资产追踪文件
- Task Packet `execution` 块，包含 mode、owner_agent、reviewer_agents、branch / worktree 约束和 human_approval_required

## 标准步骤

0. 执行 `policies/task-intake-exit-gate-policy.md` 的 Task Intake Gate，并在首次修改文件前输出 Intake 记录。
1. 读取 Task Packet。
2. 检查 `execution.mode` 是否符合任务类型：代码实现默认 `isolated_worktree`，低风险局部文档可用 `isolated_task`，评审任务必须使用 `independent_review`，人类批准事项必须使用 `human_decision`。
3. 检查 allowed changes 和 forbidden changes。
4. 检查是否需要 Contract / Security / UX gatekeeper，并确认它们在 `execution.reviewer_agents` 或 Review 计划中出现。
5. 只修改任务包允许的路径。
6. 如果 `execution.mode` 是 `isolated_worktree`，必须遵守 Task Packet 记录的 branch / worktree 约束；如果当前运行时无法创建独立 worktree，必须记录原因并确保 allowed paths 足够窄。
7. 编写或更新必要测试。
8. 运行指定测试。
9. 执行 Exit Gate，确认验收、测试、forbidden paths、secret scan 和项目红线。
10. 生成实现摘要。
11. 如果无法满足某项验收，明确说明原因。
12. 如果需要越权修改，停止并生成 Decision Pack。

## 禁止行为

- 未执行或未记录 Intake Gate 就修改文件。
- 未授权修改 schema。
- 未授权修改 CLI 命令语义。
- 为了让测试通过而随意更新 golden files。
- 删除未归档文件。
- 记录或输出敏感凭据。
- 把不确定结论写成确定结论。
- 用 `inline` 绕过代码实现隔离要求。
- 由实现 Agent 自己给出最终 QA、Security 或 Contract 审批结论。
- 由 Agent 代替人类批准 `human_decision` 事项。

## 输出

- 代码变更。
- 测试变更。
- 实现摘要。
- 测试结果。
- 未完成项或需要人类决策的事项。
- 实际执行模式，以及与 Task Packet `execution` 块的偏差说明。

## 准出条件

- Exit Gate 已完成。
- 修改文件均在 allowed changes 内。
- forbidden changes 未被触碰。
- Task Packet 的 `execution.mode` 已执行或偏差已记录并得到允许。
- 指定测试已运行或说明无法运行的原因。
- QA 可根据输出复核。
