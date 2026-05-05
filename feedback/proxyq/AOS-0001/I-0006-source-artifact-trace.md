# Source Artifact Trace — AOS-0001 after I-0006

## 来源

- ProxyQ I-0006 prompt：Core 时间窗口与统计算法。
- ProxyQ I-0006 Task Packet：`T-001-core-statistics`。
- ProxyQ I-0006 Decision Pack、Security Review、QA Review。
- Agent OS `AGENTS.md`、feedback governance policy、agent-os maintenance workflow、QA rubric。

## 本轮涉及的源资产

I-0006 使用了 ProxyQ 架构基线、I-0005 close report 和 reporting golden 作为统计规则来源。AOS 反馈只记录通用执行经验，不复制统计实现或项目统计规则。

## 脱敏边界

- 不复制 ProxyQ statistics 源码。
- 不复制 raw sample、reporting golden 或项目探测数据。
- 不复制代理地址、认证片段、token、私有日志或真实指标数据。

## 可追踪结论

- 当 prompt 要求“评分需求 / 统计规则说明”，但仓库缺少独立文档时，任务应在本轮 requirements 中显式记录缺口与最小规则来源。
- 上述经验已由 source artifact policy、Task Intake Gate 和 implementation notes 基本覆盖。
