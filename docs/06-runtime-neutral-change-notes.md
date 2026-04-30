# 运行时中立版变化说明

本版删除了运行时专用目录和专用规则。Agent OS 不再区分 Codex、Claude Code 或其他 Runtime。

## 删除的概念

- 运行时专用 Skill 目录。
- 运行时专用适配器。
- 运行时专用项目配置模板。

## 保留的概念

- `AGENTS.md`
- `.agents/skills/`
- Task Packet
- Project Pack
- Decision Pack
- Learning Proposal

## 新增机制

- UI 原型与设计稿产出 Skill。
- 迭代关闭 Skill。
- 文件爆炸控制策略。
- 完整示例目录。
