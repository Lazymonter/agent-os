---
name: feedback-governance
description: 反馈治理：分类、脱敏、路由和生成学习提案。
---

# feedback-governance

## 用途

反馈治理：分类、脱敏、路由和生成学习提案。

## 使用条件

当用户目标、迭代目标或当前任务需要本 Skill 描述的能力时使用。

## 通用步骤

0. 执行 `policies/task-intake-exit-gate-policy.md` 的 Intake Gate，并在首次修改文件前输出 Intake 记录。
1. 读取项目或 Agent OS 的 `AGENTS.md`。
2. 读取当前 Project Pack、Iteration Brief、Task Packet。
3. 读取本 Skill 对应的 workflow、policy 和 rubric。
4. 检查是否有明确输入和输出。
5. 检查 forbidden changes、项目红线和人类决策点。
6. 按本 Skill 的职责产出工件。
7. 执行 Exit Gate，并说明修改文件、假设、风险和需要人类决策的事项。

## 输出要求

- 输出必须可审查。
- 输出必须可追踪到输入目标。
- 不得虚构测试结果。
- 不得越权修改项目结构或 schema。

## 可选脚本

如果本 Skill 目录存在 `scripts/`，应优先使用脚本完成确定性生成或校验。
