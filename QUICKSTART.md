# 快速开始

## 1. 初始化项目

对任意 Agent Runtime 输入：

```text
请读取 ../agent-os/AGENTS.md，并使用 ../agent-os/.agents/skills/project-bootstrap 初始化项目。
项目名：ProxyQ
目标路径：./proxyq
模板：apple-native-shared-core
一期范围：macOS CLI、macOS Desktop、macOS Agent、iOS Mobile
技术路线：Apple-native UI + Shared Core
```

## 2. 开启迭代

```text
请读取 ./proxyq/AGENTS.md，并使用 ../agent-os/.agents/skills/iteration-start 开启迭代。
迭代 ID：I-0001-config-validate
目标：实现 config schema、配置加载、配置校验和 validate 命令的需求与任务拆解。
```

## 3. 执行任务

```text
请使用 ../agent-os/.agents/skills/task-execution 执行：
iterations/I-0001-config-validate/task-packets/T-002-config-validator.yaml
```

## 4. 验证任务

```text
请使用 ../agent-os/.agents/skills/qa-verification 验证本轮任务输出。
```

## 5. 关闭迭代

```text
请使用 ../agent-os/.agents/skills/iteration-close 对 I-0001-config-validate 做知识沉淀、归档摘要和清理建议。
```
