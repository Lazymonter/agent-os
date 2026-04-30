# Changelog

## Unreleased

- 暂无。

## 1.3.1 - 2026-04-30

- 明确项目存在外部执行手册、prompt registry 或迭代序列时，Agent 必须将其作为源资产读取并遵守，不得自行发明、跳转或跳过迭代。
- 明确当前迭代生成的 Task Packet 不等于无限执行授权；当迭代 prompt 限定为需求、架构、契约、评审或发布准备时，继续执行实现类任务必须得到当前用户请求授权。

## 1.3.0 - 2026-04-30

- 新增 Task Intake / Exit Gate 规则，要求正式任务在修改文件前读取项目规则、Skill、Task Packet、Project Pack、相关 workflow/policy/rubric，并在结束前输出验收、测试、forbidden paths、secret scan、项目红线和人类决策状态。
- 将 Intake / Exit Gate 接入 Agent OS Skill、任务执行流程、迭代流程、迭代关闭流程和项目 AGENTS 模板。
- 强化 task-packet 模板和 schema，要求任务包显式包含 `iteration_id`、`objective`、`source_artifacts`、`allowed_paths`、`forbidden_paths`、`forbidden_changes`、`required_tests` 和 `human_approval_required`。
- 更新实现、QA、契约、安全和发布 rubric，将 Intake / Exit Gate 证据纳入最低验收。
- 更新 `verify_agent_os.py`，校验 task-packet 模板是否包含必需治理字段。

## 1.2.0

- 修正运行时中立原则：不再为 Codex、Claude Code 等运行时建立专用目录。
- 将 docs 限定为项目无关内容，ProxyQ 示例统一放入 examples/proxyq。
- 补齐 workflows、skill-packs、policies、schemas、rubrics 的可执行级内容。
- 新增 `ui-prototype-design` Skill，用于产出人类可评审的原型图与设计稿。
- 新增 `iteration-close` Skill，用于迭代结束后的知识沉淀、文件清理与防止 iterations 爆炸。
- 新增完整示例：项目初始化、第一轮需求迭代、第一轮开发迭代、Agent OS 自我迭代。
- 新增迭代归档与清理策略、源资产追踪策略、仓库结构治理策略。
