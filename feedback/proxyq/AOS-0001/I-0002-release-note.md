# Release Note Draft — AOS-0001 after I-0002

## 建议版本

`1.3.1`

## 原因

本变更增强 Agent OS 的迭代序列治理：当项目维护外部执行手册、prompt registry、路线图或明确迭代序列时，Agent 必须遵守该来源，不能自行发明、跳转或跳过迭代。

## 发布摘要

- 迭代流程新增“确认迭代来源”步骤。
- 禁止行为策略新增“不得擅自发明、跳转或跳过迭代”。
- 源资产策略新增执行手册、prompt registry、路线图和迭代序列。
- 项目 AGENTS 模板新增外部迭代序列优先规则。

## 发布前验证

- `python3 scripts/verify_agent_os.py .`
- 人工复核规则是否保持运行时中立。
- 人类批准发布。
