# 决策包 — AOS-0001

## 决策标题

将 Task Intake / Exit Gate 作为 Agent OS 通用执行规则。

## 背景

ProxyQ 执行过程中暴露出一个流程问题：Agent 可能在实质上遵守了项目规则，但如果没有在规则和输出中明确记录“任务前读取了哪些输入、任务后验证了哪些边界”，后续审计仍然不够可靠。

因此，正式任务需要可重复、可检查的证据，证明 Agent 在动手前已经读取项目规则、Skill、Task Packet、Project Pack、workflow、policy 和 rubric，并在完成前验证测试、forbidden paths、敏感信息、项目红线和人类决策状态。

## 推荐方案

批准 Agent OS `Unreleased` 中的本轮更新，作为一个小版本候选。

包含变更：

- Task Intake / Exit Gate 策略。
- Skill 和 workflow 对该策略的引用。
- task-packet 模板和 schema 加固。
- rubric 更新，要求提供 Gate 证据。
- `verify_agent_os.py` 增加 task-packet 模板治理字段检查。
- changelog 记录。

## 风险评估

- 兼容性：task-packet schema 更严格。成熟任务包应包含这些治理字段；旧的极简任务包需要迁移。
- 安全：本轮不包含凭据、token、完整私有代理 URL 或私有日志。
- 流程：正式发布需要人类批准。

## 需要人类决策

发布为 Agent OS 版本前需要人类批准。

建议发布级别：`1.3.0`，因为 task-packet schema 要求变得更严格。
