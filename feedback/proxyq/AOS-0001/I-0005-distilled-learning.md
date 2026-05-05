# Distilled Learning — AOS-0001 after I-0005

## 分类结论

本轮没有需要立即吸收进 Agent OS 主规则的通用变更。

## 观察到的经验

1. 当同一输入生成多个 golden 形态时，Task Packet 应分别列出结构化 JSON、Markdown、人类可读 CLI snapshot 等输出，并为每种形态设置验收。
2. 报告类任务如果尚未实现评分、推荐或风险判断，golden 必须显式输出能力边界，不能用看似真实的占位分数或等级。
3. 新增 draft schema 时，即使不修改既有 schema，也需要 Contract Review 明确新增契约状态、兼容性和后续升级边界。
4. 报告 golden 应同时检查确定性、章节形态、schema conformance、敏感信息和项目红线。

## 是否需要更新 Agent OS

不需要。

原因：

- 第 1 点已由 Task Packet `outputs`、`acceptance_criteria` 和 QA rubric 的 golden file 合理性覆盖。
- 第 2 点已由项目红线、human decision policy 和 Exit Gate 的项目红线检查覆盖。
- 第 3 点已由 contract review rubric 覆盖。
- 第 4 点已由 QA rubric、source artifact policy、sensitive data policy 和 task-intake-exit-gate policy 覆盖。

## 不吸收内容

- ProxyQ hourly summary schema 字段。
- ProxyQ raw sample golden、report markdown、CLI snapshot 和固定样本。
- ProxyQ percentile skeleton、报告章节命名和评分边界文案。
- ProxyQ 产品红线和代理质量语义。

## 后续观察

如果多个项目都需要“同一输入生成多形态 golden”的统一模板，可以考虑新增一个通用 `golden-matrix` Task Packet 模板。当前只有 ProxyQ 单项目证据，不发布通用模板。
