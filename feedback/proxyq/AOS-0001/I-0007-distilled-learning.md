# Distilled Learning — ProxyQ I-0007

## 分类

- 类型：Workflow / QA governance。
- 处理：记录为项目反馈，不修改 Agent OS 主规则。

## 可泛化观察

1. 当任务会直接影响用户可见判断、质量等级、风险提示或安全边界时，即使本轮不修改 UI 文件或 schema，也应将相关 impact 维度提升为 high。
2. 若某个 impact 被提升为 high，对应 reviewer / gatekeeper 必须同时出现在 Agent Engagement Plan、Task Packet reviewer 列表和 review 产物中。
3. 当运行时没有实例化独立评审 agent 时，评审文件必须明确标注为主线程复核，不能伪装成 independent review。
4. 对高风险算法任务，draft 公式可以作为实现输入，但是否冻结为产品规则必须显式进入人类决策。

## 不吸收内容

- ProxyQ scoring 公式、权重和阈值。
- ProxyQ scoring golden。
- ProxyQ 产品红线的具体业务含义。

## 是否建议修改 Agent OS 主规则

暂不建议。

理由：

- Agent OS 已有 impact high、gatekeeper、independent review、人类决策和 Task Packet reviewer 的规则。
- I-0007 的问题属于执行时严格度不足，已在项目反馈中记录。
- 尚无跨项目重复证据证明需要改动通用 workflow 或 policy。
