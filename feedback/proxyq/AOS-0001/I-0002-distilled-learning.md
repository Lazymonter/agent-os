# Distilled Learning — AOS-0001 after I-0002

## 通用学习

Agent OS 需要区分三类来源：

- 用户当前请求。
- 项目内已生成的 Task Packet。
- 项目外部或项目专属的执行手册、prompt registry、路线图或迭代序列。

Task Packet 能授权一次具体任务的允许路径和验收标准，但不能替代项目的迭代序列，也不能让 Agent 自行决定下一个迭代。

## 新规则

1. 如果项目维护外部执行手册、prompt registry 或明确迭代序列，Agent 必须将其视为源资产读取并遵守。
2. Agent 不得自行发明新的迭代 ID、跳转到未被用户指定的 prompt，或跳过项目要求的迭代后置步骤。
3. 当前迭代生成的 Task Packet 不等于无限执行授权。若当前 prompt 限定为需求、架构、契约、评审或发布准备，继续执行实现类任务必须确认仍被当前用户请求授权。
4. 这些规则应写入通用 workflow、policy 和项目 AGENTS 模板，而不是写入项目专属路径。

## 已吸收位置

- `workflows/iteration-workflow.md`
- `policies/forbidden-behavior-policy.md`
- `policies/source-artifact-policy.md`
- `templates/project/base/AGENTS.md.tpl`
- `CHANGELOG.md`

## 不吸收内容

- 项目专用 prompts 路径。
- ProxyQ 产品形态、平台范围、schema 字段、CLI 输出语义。
- ProxyQ fixtures、代码路径、测试输出、私有日志或运行时细节。
