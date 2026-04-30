# 迭代文件爆炸控制

## 背景

每轮迭代会产生大量临时文件：分析、草稿、评审、任务包、脚本输出、测试日志、学习反馈等。若长期保留，项目仓库会迅速膨胀。

## 原则

`iterations/` 是过程工作区，不是长期知识库。

长期保留的内容应进入：

- `knowledge/project-pack/`
- `docs/`
- `adr/`
- `schemas/`
- `tests/`
- `golden/`
- `knowledge/lessons/`
- `knowledge/learning-proposals/`

临时过程文件应在迭代关闭后删除或转为外部归档。

## 迭代关闭流程

1. 汇总本轮目标和结果。
2. 判断哪些内容进入项目知识。
3. 判断哪些内容成为 Agent OS 学习提案。
4. 生成 `iteration-close-report.md`。
5. 生成最小 `iteration-ledger` 条目。
6. 可选打包临时文件到外部归档。
7. 经人类批准后删除该轮 `iterations/<id>/` 临时目录。

## 保留最小账本

建议项目保留：

```text
knowledge/iteration-ledger.md
```

其中只记录：

- 迭代 ID。
- 目标。
- 完成状态。
- 关键产物落点。
- 决策摘要。
- 学习提案 ID。
- 归档位置。

## 禁止

- 禁止未生成关闭报告就删除迭代目录。
- 禁止未沉淀项目知识就删除迭代目录。
- 禁止把临时过程文件直接复制到 Agent OS。
