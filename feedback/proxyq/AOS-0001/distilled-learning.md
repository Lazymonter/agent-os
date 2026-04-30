# 提炼学习 — AOS-0001

## 通用学习

Agent 可能在行为上遵守项目规则，但如果任务前和任务后的检查没有固化为规则，也没有形成输出证据，后续仍然难以审计。

本轮提炼出的通用规则是：

正式工作必须以 Intake Gate 开始，以 Exit Gate 结束。

## Intake Gate 要求

在修改文件或生成正式工件前，Agent 必须读取并记录：

- 根目录 `AGENTS.md`。
- 项目 agent config，如果存在。
- Project Pack 或 Agent OS 维护目标。
- 当前迭代和 Task Packet；治理维护例外除外。
- 相关 Skill。
- 相关 workflow、policy 和 rubric。
- allowed paths、forbidden paths、forbidden changes、acceptance criteria、required tests 和 stop conditions。

## Exit Gate 要求

在声称完成前，Agent 必须记录：

- 验收标准状态。
- required tests 状态。
- forbidden paths 状态。
- secret scan 状态。
- 项目红线状态。
- 未决风险。
- 是否需要人类决策。

## Agent OS 变更

本学习已作为通用 Agent OS 更新落地：

- 新增或复用 Task Intake / Exit Gate 策略。
- 将所有 Skill 接入该策略。
- 将 task execution、iteration、iteration close 和 maintenance workflow 接入该策略。
- 更新 task-packet 模板和 schema，使任务边界显式化。
- 更新 rubrics，要求提供 Gate 证据。
- 在 `Unreleased` 中增加 changelog 记录。

## 不吸收内容

以下内容不会被泛化进入 Agent OS：

- ProxyQ 产品范围。
- ProxyQ 平台选择。
- ProxyQ config schema 字段名。
- ProxyQ CLI 输出语义。
- ProxyQ fixtures、路径、项目私有日志或运行时细节。
