#!/usr/bin/env python3
'''关闭迭代：生成关闭报告和最小账本条目。不会自动删除目录。'''
from pathlib import Path
import argparse, datetime, shutil

parser = argparse.ArgumentParser()
parser.add_argument('--project', required=True)
parser.add_argument('--iteration', required=True)
parser.add_argument('--allow-delete', action='store_true')
args = parser.parse_args()
project = Path(args.project)
it = project / 'iterations' / args.iteration
if not it.exists():
    raise SystemExit(f'迭代目录不存在: {it}')
now = datetime.datetime.now().isoformat(timespec='seconds')
report = it / 'iteration-close-report.md'
report.write_text(f'''# 迭代关闭报告：{args.iteration}

生成时间：{now}

## 关闭状态

- 状态：待人类确认
- 自动删除：{'允许' if args.allow_delete else '不允许'}

## 需要沉淀的位置

- 项目知识：knowledge/project-pack、docs、adr、schemas、tests、golden
- 项目学习：knowledge/lessons
- Agent OS 学习提案：knowledge/learning-proposals

## 删除条件

只有在本报告经人类确认后，才能删除本轮迭代过程目录。
''', encoding='utf-8')
ledger = project / 'knowledge' / 'iteration-ledger.md'
ledger.parent.mkdir(parents=True, exist_ok=True)
with ledger.open('a', encoding='utf-8') as f:
    f.write(f'\n## {args.iteration}\n\n- 关闭报告：iterations/{args.iteration}/iteration-close-report.md\n- 关闭时间：{now}\n- 状态：待确认\n')
print(f'已生成关闭报告: {report}')
print(f'已更新迭代账本: {ledger}')
