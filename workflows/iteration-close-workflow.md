# 迭代关闭流程

## 目的

避免每轮迭代产生的大量过程文件长期堆积在 `iterations/` 目录。

## 输入

- `iterations/<id>/goal.yaml`
- `iteration-brief.md`
- `agent-engagement-plan.yaml`
- `task-packets/`
- `reviews/`
- `decision-pack.md`
- `learning/`

## 流程

1. 汇总本轮目标、实际完成内容和未完成内容。
2. 将长期有价值的内容迁移到项目目录：
   - 需求 -> `docs/requirements/`
   - 架构 -> `docs/architecture/` 或 `adr/`
   - schema -> `schemas/`
   - 测试 -> `tests/`、`golden/`
   - 项目经验 -> `knowledge/lessons/`
3. 将通用化经验生成 Learning Proposal。
4. 更新 `knowledge/iteration-ledger.md`。
5. 生成 `iteration-close-report.md`。
6. 人类确认后删除或外部归档该迭代目录。

## 输出

- `iteration-close-report.md`
- 更新后的 `knowledge/iteration-ledger.md`
- 可能的 `knowledge/learning-proposals/*.yaml`
