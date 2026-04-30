# 迭代保留与清理策略

## 目的

控制 `iterations/` 目录膨胀。

## 原则

每轮迭代目录是临时工作区，不是永久知识库。

## 关闭后必须沉淀

- 需求结论 -> `docs/requirements/` 或 `knowledge/project-pack/`
- 架构决策 -> `adr/` 或 `docs/architecture/`
- schema -> `schemas/`
- 测试 -> `tests/`、`golden/`
- 项目学习 -> `knowledge/lessons/`
- 通用学习提案 -> `knowledge/learning-proposals/`
- 最小账本 -> `knowledge/iteration-ledger.md`

## 删除条件

只有满足以下条件，才能删除 `iterations/<id>/`：

1. 生成 iteration-close-report。
2. 生成或更新 iteration-ledger。
3. 知识已分类沉淀。
4. 学习提案已生成或明确不需要。
5. 人类确认允许删除。

## 可选归档

如果需要审计，可先压缩到项目外部归档目录，再删除工作区。
