---
name: task-decomposition
description: 任务拆解：将需求和架构拆成可执行任务包。
---

# task-decomposition

## 用途

任务拆解：将需求和架构拆成可执行任务包。

## 使用条件

当用户目标、迭代目标或当前任务需要本 Skill 描述的能力时使用。

## 通用步骤

1. 读取项目或 Agent OS 的 `AGENTS.md`。
2. 读取当前 Project Pack、Iteration Brief、Task Packet。
3. 检查是否有明确输入和输出。
4. 检查 forbidden changes、项目红线和人类决策点。
5. 按本 Skill 的职责产出工件。
6. 产出后说明修改文件、假设、风险和需要人类决策的事项。

## 输出要求

- 输出必须可审查。
- 输出必须可追踪到输入目标。
- 不得虚构测试结果。
- 不得越权修改项目结构或 schema。

## 可选脚本

如果本 Skill 目录存在 `scripts/`，应优先使用脚本完成确定性生成或校验。
