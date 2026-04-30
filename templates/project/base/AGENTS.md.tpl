# AGENTS.md — {{project_name}}

## 项目摘要

{{project_summary}}

## 硬性规则

- 所有 Agent 必须先读取本文件。
- 执行任何会修改文件或生成正式工件的任务前，必须读取对应 Skill、Task Packet、Project Pack、相关 workflow/policy/rubric，并输出 Intake Gate。
- 任务结束前必须输出 Exit Gate，覆盖验收、测试、forbidden paths、secret scan、项目红线和人类决策项。
- 不得越过 Task Packet 修改文件。
- 不得擅自修改 schema、接口契约或项目红线。
- 需要人类决策的事项必须停止并生成 Decision Pack。
