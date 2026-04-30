# Task Intake / Exit Gate 策略

## 目的

防止 Agent 在未读取项目规则、Skill、Task Packet、Project Pack、policy、rubric 或 workflow 的情况下直接进入实现、测试、评审或收尾。

## 适用范围

任何会修改文件、生成正式工件、执行任务包、更新 golden、修改 schema、进行评审或关闭迭代的工作，都必须执行本策略。

只读探索、状态查询和用户明确要求的简单命令可以不执行完整 Gate，但输出不得声称完成了任务包。

## Task Intake Gate

开始任务前必须先读取并记录以下输入：

1. 项目或 Agent OS 根目录的 `AGENTS.md`。
2. 项目 `.agent/agent-config.yaml`，如果存在。
3. 当前 Project Pack 或 Agent OS 维护目标，至少包含 scope、non-scope、red-lines、technical-route 中与任务相关的部分。
4. 当前 Iteration Brief、source artifact trace 和 Task Packet。
5. 与任务角色匹配的 Skill，例如 `task-execution`、`qa-verification`、`contract-review`、`security-review`、`iteration-close` 或 `agent-os-maintenance`。
6. 最小相关 workflow、policy 和 rubric。
7. 当前任务的 allowed paths、forbidden paths、forbidden changes、acceptance criteria、required tests 和 stop conditions。

如果是无 Task Packet 的治理维护任务，必须满足全部条件：

- 用户明确要求维护规则、流程、策略、模板或 Agent OS。
- 读取 `agent-os-maintenance` Skill 和相关维护 workflow/policy。
- 只修改治理文件、模板或项目入口规则。
- 不执行普通实现任务，不改业务代码、schema、UI 或测试逻辑。

## 必须输出的 Intake 记录

在首次修改文件前，Agent 必须输出简短 Intake 记录：

```text
Intake Gate:
- AGENTS.md: read
- Agent config: read/not present
- Project Pack: read/not applicable
- Iteration / Task Packet: read / governance exception
- Skill: <name> read
- Workflow / Policy / Rubric: read
- Allowed paths: <paths>
- Forbidden paths: <paths>
- Stop conditions: <conditions>
```

## 执行中规则

- 只能修改 Intake Gate 中确认允许的路径。
- 如果发现必须修改 allowed paths 之外的文件，必须停止并生成 Decision Pack 或等待人类授权。
- 如果发现 Task Packet、Project Pack、policy、rubric 或 workflow 冲突，必须停止并说明冲突。
- 不得为了通过测试而绕过 policy、弱化验证规则或无解释更新 golden。
- 不得把敏感信息、凭据、token、完整私有代理 URL 或未脱敏日志写入输出、文档、测试或 golden。

## Exit Gate

任务结束前必须输出或记录 Exit Gate：

```text
Exit Gate:
- Acceptance criteria: pass/fail/not applicable
- Required tests: pass/fail/not run with reason
- Forbidden paths touched: none / list
- Secret scan: pass/fail/not applicable
- Project red lines: pass/fail/not applicable
- Open risks: none / list
- Human decision required: yes/no
```

## 违规处理

如果未执行 Intake Gate 就开始修改文件，必须：

1. 停止当前任务。
2. 标记为 `rework_required`。
3. 生成 Review Finding。
4. 补做 Intake Gate。
5. 由人类确认后再继续。
