# Agent 权限策略

## 目的

限制不同 Agent 对仓库的修改范围。

## 权限原则

- Product & Requirements：可写需求和用例，不改代码。
- Architect：可写架构、ADR、任务拆解，不直接改生产代码。
- Implementation：只能修改任务包授权路径。
- QA：可写测试和评审，不为通过测试擅自改业务代码。
- Security：可阻断高风险任务，不直接接受风险。
- UX/UI：可写设计、原型和设计系统，不擅自改核心逻辑。
- Agent OS Maintainer：可提炼通用学习，但不得合并未脱敏项目过程内容。

## 禁止

任何 Agent 都不得越过任务包修改 forbidden paths。
