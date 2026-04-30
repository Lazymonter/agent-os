# Source Artifact Trace — I-0001-config-validate

## 本轮迭代

I-0001-config-validate：定义并拆解 config schema、配置加载和 validate 命令。

## 相关源资产

| 资产 ID | 类型 | 本轮用途 | 是否必须符合 |
|---|---|---|---|
| proxyq-product-doc-pdf | 产品说明 | 一期范围、红线、技术路线、平台边界 | 是 |
| proxyq-cli-prototype | CLI 原型 | validate / status 类命令的输出风格 | 是 |
| proxyq-desktop-prototype | Desktop 原型 | Settings、Throughput、Baseline、Agent 页面配置字段参考 | 是 |
| proxyq-ios-prototype | iOS 原型 | iOS 可见字段和权限边界参考 | 是 |
| proxyq-design-system | 设计系统 | 状态名称、等级 badge、风险文案参考 | 是 |

## 本轮提取的约束

- `throughput.enabled` 默认必须为 false。
- `full_speed.manual_only` 必须为 true。
- `global_proxy.user_confirmed_global_proxy=false` 时 subject 可以保存，但不可作为代理质量等级。
- `direct.user_confirmed_direct_path=false` 时 comparative score 不可计算。
- CLI 输出应使用分组式文本结构，并支持 JSON 输出。
- Desktop 和 iOS 不应展示完整代理密码。

## 本轮不适用资产

- Desktop Dashboard 视觉截图：本轮不实现 UI，但保留为后续 UI 实现基线。
- iOS Home 视觉截图：本轮不实现 UI，但用于确认移动端只读 / 远程控制边界。

## 偏离项

暂无。如果后续 config schema 与原型中的字段命名不一致，必须生成 Decision Pack。
