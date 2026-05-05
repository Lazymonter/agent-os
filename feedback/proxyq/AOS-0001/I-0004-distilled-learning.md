# Distilled Learning — AOS-0001 after I-0004

## 分类结论

本轮没有需要立即吸收进 Agent OS 主规则的通用变更。

## 观察到的经验

1. CLI 命令输出一旦成为契约，应同时覆盖 text golden、JSON golden、schema conformance、exit code matrix 和脱敏断言。
2. 当生产实现已经满足任务目标时，迭代可以只补充 contract/golden/QA 工件，但必须在实现记录中明确说明未修改生产代码的原因。
3. Secret scan 可能命中测试中的负向脱敏断言。QA 可以把它标记为 false positive，但必须记录命中位置、原因和人工复核结论。
4. 如果 CLI 原型缺少某个命令的专属画面或输出样例，任务应明确以需求契约和 golden baseline 为权威来源，不能自行补造产品行为。

## 是否需要更新 Agent OS

不需要。

原因：

- 第 1 点已由 Task Packet required tests、QA rubric 和 golden file 合理性检查覆盖。
- 第 2 点属于任务执行记录规范，已由 task-execution workflow 的实现记录和 Exit Gate 覆盖。
- 第 3 点已由 sensitive data policy、QA rubric 和 Exit Gate 的 secret scan 状态覆盖。
- 第 4 点已由 source artifact policy 和 Task Intake Gate 覆盖。

## 不吸收内容

- ProxyQ CLI validate 的输出字段、错误码、退出码和 severity 语义。
- ProxyQ golden 文件内容、测试夹具和配置路径。
- ProxyQ 产品红线、代理质量业务判断和安全语义。
- I-0004 迭代目录中的过程性项目工件。

## 后续观察

如果多个项目都出现 secret scan false positive 需要统一记录格式，可以再考虑把“false positive 必须提供行号和解释”写入 QA rubric。当前只有单项目证据，不发布通用规则。
