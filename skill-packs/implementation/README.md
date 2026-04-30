# Implementation Skill Pack

## 职责重点

根据 Task Packet 最小化实现代码、测试和必要文档。

## 方法论

- 小步修改。
- 先读规则再改代码。
- 只改任务允许的文件。
- 测试驱动。
- 输出可审查 diff。

## 检查清单

- 是否读取项目 `AGENTS.md`？
- 是否读取 Task Packet？
- 是否明确 allowed paths？
- 是否避免 forbidden changes？
- 是否运行要求的测试？
- 是否说明无法测试的原因？
- 是否生成实现摘要？

## 常见错误

- 擅自改 schema。
- 顺手重构无关代码。
- 只实现 happy path。
- 没有处理错误场景。
- 没有更新测试。

## 最低通过标准

代码变更必须满足任务包，测试必须通过或给出明确阻塞原因。
