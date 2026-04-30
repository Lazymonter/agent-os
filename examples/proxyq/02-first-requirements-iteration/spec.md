# 第一轮需求迭代 Spec：config validate

## 目标

明确 `config.yaml`、配置加载和 validate 命令在产品中的行为。

## 必须分析

- CLI `proxyq validate` 输出。
- Desktop Settings 里的配置字段。
- iOS 只读展示中哪些配置状态要显示。
- global_proxy 和 direct baseline 的确认状态。
- throughput 默认关闭和 full_speed 强确认。
- 本地文件路径和保留策略。

## 不在本轮实现

- 不写生产代码。
- 不实现 macOS Agent。
- 不实现 iOS 页面。

## 人类决策点

- 是否允许 config 文件包含代理明文密码。
- 是否将 Keychain 引用作为一期要求。
