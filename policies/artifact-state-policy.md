# 工件状态策略

## 状态机

```text
draft
specified
designed
decomposed
assigned
implemented
verified
reviewed
human_decision_required
approved
baselined
closed
```

## 规则

- Agent 不能直接把工件标记为 approved。
- 需要人类批准的工件必须进入 `human_decision_required`。
- 迭代关闭后，临时过程文件可以被归档或删除。
- 已沉淀的知识必须移动到项目知识目录或 Agent OS 学习提案。
