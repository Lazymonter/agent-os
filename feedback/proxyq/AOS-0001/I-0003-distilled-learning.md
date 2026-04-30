# Distilled Learning — AOS-0001 after I-0003

## 分类结论

本轮没有需要立即吸收进 Agent OS 主规则的通用变更。

## 观察到的经验

1. 当 Task Packet 要求 `isolated_worktree`，但当前会话未实际创建独立 worktree 时，执行记录必须说明偏差原因，并用更窄的 allowed paths 和 forbidden paths 复核抵消风险。
2. QA 不能只依赖泛化的测试发现命令。如果测试目录结构导致根目录发现结果为 0，必须改用明确的 required tests 列表，并记录实际执行命令。
3. 同一 machine-readable code 在项目业务中可能按上下文表现为 warning 或 error；这类语义应留在项目契约文档中，不应泛化到 Agent OS。

## 是否需要更新 Agent OS

不需要。

原因：

- 第 1 点已由 Agent OS v1.4.0 的 execution model 和 task-execution workflow 覆盖。
- 第 2 点已由 Task Packet required tests 和 QA rubric 覆盖。
- 第 3 点属于项目数据契约和业务语义，不适合进入通用 Agent OS。

## 不吸收内容

- ProxyQ config schema、semantic validation code、fixtures、测试数量和错误码表。
- ProxyQ 产品红线和代理安全语义。
- 项目迭代目录中的过程性产物。
