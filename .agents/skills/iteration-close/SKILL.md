---
name: iteration-close
description: 当一轮迭代完成、需要沉淀项目知识、生成学习提案、更新账本并清理 iterations 临时文件时使用。
---

# Iteration Close Skill

## 使用时机

- 迭代任务已经实现并通过验证。
- 人类已经批准或要求关闭本轮迭代。
- 需要防止 `iterations/` 目录持续膨胀。

## 输入

- 项目 `AGENTS.md`。
- 本轮 `goal.yaml`。
- 本轮 `decision-pack.md`。
- 本轮 `reviews/`。
- 本轮 `learning/`。
- 项目 `knowledge/source-assets/source-assets.yaml`。

## 步骤

1. 汇总本轮目标、范围、结果和遗留问题。
2. 判断哪些内容应进入项目知识库。
3. 判断哪些内容应形成 Agent OS Learning Proposal。
4. 生成 `iteration-close-report.md`。
5. 更新 `knowledge/iteration-ledger.md`。
6. 生成可删除清单。
7. 如需审计，先压缩归档迭代目录。
8. 只有在人类批准后，才能删除本轮迭代目录。

## 禁止

- 禁止未生成关闭报告就删除迭代目录。
- 禁止将项目原始过程内容复制到 Agent OS。
- 禁止删除尚未沉淀的需求、设计、测试或决策。
