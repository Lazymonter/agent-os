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

## 标准步骤

0. 执行 `policies/task-intake-exit-gate-policy.md` 的 Task Intake Gate，并在首次修改文件前输出 Intake 记录。
1. 读取 Task Packet。
2. 检查 allowed changes 和 forbidden changes。
3. 检查是否需要 Contract / Security / UX gatekeeper。
4. 只修改任务包允许的路径。
5. 编写或更新必要测试。
6. 运行指定测试。
7. 执行 Exit Gate，确认验收、测试、forbidden paths、secret scan 和项目红线。
8. 生成实现摘要。
9. 如果无法满足某项验收，明确说明原因。
10. 如果需要越权修改，停止并生成 Decision Pack。

## 禁止行为

- 未执行或未记录 Intake Gate 就修改文件。
- 未授权修改 schema。
- 未授权修改 CLI 命令语义。
- 为了让测试通过而随意更新 golden files。
- 删除未归档文件。
- 记录或输出敏感凭据。
- 把不确定结论写成确定结论。

## 输出

- 代码变更。
- 测试变更。
- 实现摘要。
- 测试结果。
- 未完成项或需要人类决策的事项。

## 准出条件

- Exit Gate 已完成。
- 修改文件均在 allowed changes 内。
- forbidden changes 未被触碰。
- 指定测试已运行或说明无法运行的原因。
- QA 可根据输出复核。
