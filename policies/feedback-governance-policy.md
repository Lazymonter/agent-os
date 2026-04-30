# 反馈治理策略

## 目的

管理项目向 Agent OS 提交学习反馈的流程。

## 反馈分类

- Project-only：留在项目仓库。
- Agent-skill：进入 skill-packs。
- Domain-generic：进入 domain-packs。
- Workflow：进入 workflows。
- Policy：进入 policies。
- Template：进入 templates。
- Do-not-learn：不沉淀。

## 流程

1. 项目产生 Learning Proposal。
2. 进行敏感信息检查。
3. 分类归属。
4. 若进入 Agent OS，生成脱敏后的通用变更提案。
5. Agent OS Maintainer 审查。
6. 人类批准后合入。

## 禁止

未经脱敏的过程内容不得进入 Agent OS main。
