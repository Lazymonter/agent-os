# 源资产追踪 — AOS-0001

## 范围

本轮 Agent OS 自我维护迭代吸收 ProxyQ 项目中可泛化的流程学习。本轮不会把 ProxyQ 产品行为、私有日志、凭据、代理 URL 或项目专属实现细节写入 Agent OS 通用规则。

## 已读取输入

- `proxyq_agent_execution_manual/prompts/AOS-0001-Agent-OS-自我迭代-吸收-ProxyQ-通用学习.md`
- `agent_os/AGENTS.md`
- `agent_os/.agents/skills/feedback-governance/SKILL.md`
- `agent_os/.agents/skills/agent-os-maintenance/SKILL.md`
- `agent_os/.agents/skills/qa-verification/SKILL.md`
- `agent_os/policies/feedback-governance-policy.md`
- `agent_os/policies/task-intake-exit-gate-policy.md`
- `agent_os/workflows/feedback-learning-workflow.md`
- `agent_os/workflows/agent-os-maintenance-workflow.md`
- `agent_os/skill-packs/agent-os-maintainer/README.md`
- `proxyq/AGENTS.md`
- `proxyq/knowledge/project-pack/`
- `proxyq/knowledge/source-assets/source-assets.yaml`

## 学习输入

已检查 `proxyq/knowledge/learning-proposals/`，当前没有文件。

本轮使用的通用学习来自用户批准的流程反馈：Agent OS 任务必须在正式工作前后显式执行并记录 Intake / Exit Gate。

## 分类

- Workflow learning：在 task execution、iteration、iteration close 和 Agent OS maintenance workflow 中要求 Intake / Exit Gate。
- Policy learning：把正式任务缺少 Intake / Exit Gate 证据列为禁止行为。
- Skill learning：要求 Skill 在生成正式工件前引用 Intake / Exit Gate 策略。
- Template learning：task-packet 模板必须暴露 source artifacts、allowed paths、forbidden paths、tests 和 human approval 字段。
- Rubric learning：implementation、QA、contract、security 和 release rubric 必须评价 Gate 证据。

## 脱敏

通用 Agent OS 规则不需要 ProxyQ 专属产品事实。ProxyQ 仅作为本隔离反馈迭代的来源项目被引用。
