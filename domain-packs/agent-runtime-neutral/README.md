# Agent Runtime Neutral Domain Pack

## 适用场景

项目希望同时支持多种 Agent Runtime，不绑定具体工具。

## 核心规则

- 只依赖通用文件：`AGENTS.md`、`.agents/skills/`、Task Packet。
- 不创建运行时专用目录。
- 不将运行时特有能力写成项目必须条件。
- 确定性动作尽量通过 Skill scripts 完成。
