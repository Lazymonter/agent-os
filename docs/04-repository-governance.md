# 双仓库治理

## agent-os 仓库

只保存项目无关知识：

- Agent 角色。
- Skill。
- Skill Pack。
- Domain Pack。
- Workflow。
- Policy。
- Rubric。
- Template。
- Schema。

## project 仓库

保存项目专属内容：

- 产品说明。
- 需求。
- 原型。
- 设计稿。
- 项目代码。
- 项目测试。
- 项目迭代。
- 项目知识。

## 跨仓库学习

项目反馈必须先进入项目仓库：

```text
knowledge/learning-proposals/
```

只有通用化、脱敏、经过 Agent OS Maintainer 审查的内容，才能进入 agent-os。

## 禁止

- 禁止把项目原始过程文件放进 agent-os main。
- 禁止项目 Agent 直接改 agent-os 通用规则。
- 禁止未脱敏反馈跨仓库提交。
