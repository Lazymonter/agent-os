# 发布建议 — AOS-0001

## 建议版本

`1.3.0`

## 原因

本变更加强 Agent OS 治理：将 Intake / Exit Gate 证据纳入标准执行模型，并围绕 source artifacts、allowed paths、forbidden paths、required tests 和 human approval 加强 task-packet 模板与 schema。

## 发布摘要

- 新增正式 Agent 工作必须执行的 Intake / Exit Gate 策略。
- 要求 Skill 和 workflow 引用 Gate 策略。
- 更新项目 `AGENTS.md` 模板，使后续新项目默认继承该规则。
- 加固 task-packet 模板和 schema，显式加入治理字段。
- 更新 rubrics，要求提供 Gate 证据。
- 更新校验脚本，检查 task-packet 模板字段覆盖情况。

## 发布前验证

- `python3 scripts/verify_agent_os.py .`
- 人工复核更严格的 task-packet schema 是否影响兼容性。
- 人类批准发布。

## 已知迁移说明

旧任务包如果缺少 `source_artifacts`、`allowed_paths`、`forbidden_paths`、`required_tests` 或 `human_approval_required`，需要在下游项目启用 schema 校验前补齐。
