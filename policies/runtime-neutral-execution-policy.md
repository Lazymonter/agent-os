# 运行时中立执行策略

## 目的

保证 Agent OS 不依赖特定 Agent Runtime。

## 规则

- 统一使用 `AGENTS.md`、`.agents/skills/`、Task Packet。
- 不要求运行时支持专用目录。
- 不在通用流程中写入厂商专属命令。
- 运行时可以调用 Skill scripts，但必须说明执行结果。

## 执行者最低要求

- 能读取文件。
- 能执行命令。
- 能修改文件。
- 能输出变更摘要。
- 能遵守 forbidden changes。
