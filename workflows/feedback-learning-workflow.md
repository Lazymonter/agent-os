# 反馈学习流程

## 目标

将项目迭代中产生的反馈、失败案例、评审意见和改进建议进行分类，判断它们应留在项目仓库，还是作为通用学习提案提交给 Agent OS。

## 反馈来源

- 人类评审意见。
- QA 缺陷。
- Security 审查问题。
- Agent 越权修改。
- schema 漂移。
- 原型不一致。
- 测试遗漏。
- 项目红线被违反。

## 分类

```text
project_only
agent_skill_learning
domain_learning
workflow_learning
policy_learning
template_learning
do_not_learn
```

## 标准步骤

1. 收集反馈。
2. 判断是否包含敏感信息。
3. 判断是否项目专属。
4. 如果是项目专属，写入项目 `knowledge/lessons/`。
5. 如果可泛化，创建 Learning Proposal。
6. 脱敏证据。
7. 由 Agent OS Maintainer 判断是否吸收。
8. 提炼成通用规则、模板或检查清单。
9. 发布 Agent OS 新版本。
10. 项目选择是否升级 Agent OS。

## 准出条件

- 每条反馈都有分类。
- 敏感内容没有进入 Agent OS 主干。
- 通用学习有证据和提炼规则。
- 项目专属学习没有误写入通用仓库。
