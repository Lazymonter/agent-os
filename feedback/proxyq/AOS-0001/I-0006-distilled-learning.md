# Distilled Learning — AOS-0001 after I-0006

## 分类结论

本轮没有需要立即吸收进 Agent OS 主规则的通用变更。

## 观察到的经验

1. 当 prompt 要求的“评分需求”或“统计规则说明”没有独立文档时，Agent 不应假装已读取；应在 source trace 和 iteration brief 中明确标记缺口。
2. 对基础算法任务，最好先在本轮 requirements 中固化最小规则，再实现代码和边界测试。
3. 从 feature skeleton 中抽出 shared utility 时，必须保留原有 golden / regression tests，证明行为未漂移。
4. 算法基础实现不等于产品评分实现，review 和 decision pack 必须明确未实现权重、阈值和质量等级。

## 是否需要更新 Agent OS

不需要。

原因：

- 第 1 点已由 source artifact policy 和 Task Intake Gate 覆盖。
- 第 2 点已由 iteration workflow 的 requirements / acceptance criteria 阶段覆盖。
- 第 3 点已由 task-execution workflow 和 QA rubric 的 regression 覆盖。
- 第 4 点已由 project red lines、Exit Gate 和 Decision Pack 覆盖。

## 不吸收内容

- ProxyQ nearest-rank、jitter、flap_count、tail_ratio、spike_rate 的具体语义。
- ProxyQ statistics API、测试数据和 reporting 集成。
- ProxyQ 评分边界、产品红线和报告语义。

## 后续观察

如果多个项目都出现“prompt 要求材料缺失，但需要补充本轮最小规则”的情况，可以考虑强化 source artifact policy 的缺失输入记录格式。当前只有单项目证据，不发布通用规则。
