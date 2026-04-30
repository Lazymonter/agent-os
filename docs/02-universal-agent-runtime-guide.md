# 通用 Agent Runtime 使用指南

## 目标

让任何支持代码读写和命令执行的 Agent Runtime 使用同一套 Agent OS。

## Runtime 必须具备的能力

- 能读取仓库文件。
- 能按 `AGENTS.md` 执行规则。
- 能读取 `.agents/skills/<skill>/SKILL.md`。
- 能调用 Skill 中的 `scripts/`。
- 能修改文件并生成差异摘要。
- 能运行测试或说明无法运行的原因。

## Runtime 不需要具备的能力

- 不需要支持特定厂商的 skill 格式。
- 不需要专属目录。
- 不需要专用适配器。

## 使用约定

用户给 Agent 的指令应包含：

```text
请读取 AGENTS.md，并使用 .agents/skills/<skill-name> 完成任务。
```

如果项目还未初始化，则读取 Agent OS 仓库中的：

```text
agent-os/AGENTS.md
agent-os/.agents/skills/project-bootstrap/SKILL.md
```
