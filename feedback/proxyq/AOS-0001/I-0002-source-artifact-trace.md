# Source Artifact Trace — AOS-0001 after I-0002

## 范围

本次 AOS-0001 增量执行只吸收 I-0002 暴露出的通用 Agent OS 流程学习。ProxyQ 产品范围、平台选择、schema 字段、代码路径、测试 fixture 和业务实现细节不进入 Agent OS 通用规则。

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
- `proxyq/AGENTS.md`
- `proxyq/knowledge/project-pack/`
- `proxyq/knowledge/source-assets/source-assets.yaml`
- `proxyq/iterations/I-0002-architecture-data-contract-baseline/`

## 学习输入

`proxyq/knowledge/learning-proposals/` 当前不存在可读取提案。本次学习来自人类反馈：

- 项目步骤来源于外部 prompts 目录，Agent 不应自行开启新迭代。
- 每个项目迭代完成后必须执行指定的 AOS 后置学习步骤。
- 架构/契约迭代内生成 task packets 后，继续实现任务需要确认仍被当前用户请求授权。

## 分类

- Workflow learning：迭代流程必须读取并遵守项目的外部执行手册、prompt registry 或迭代序列。
- Policy learning：禁止 Agent 自行发明、跳转或跳过迭代。
- Template learning：项目 AGENTS 模板应提示外部迭代序列优先。
- Do-not-learn：ProxyQ 专用 prompts 路径、产品形态、schema 字段和实现文件不进入通用主干。

## 脱敏

通用规则只使用抽象表述：外部执行手册、prompt registry、迭代序列、Task Packet 授权边界。未写入凭据、token、完整私有代理 URL、私有日志或项目业务数据。
