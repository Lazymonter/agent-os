#!/usr/bin/env python3
import argparse
from pathlib import Path

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding='utf-8')

def main():
    ap = argparse.ArgumentParser(description='创建一轮项目迭代目录和基础工件。')
    ap.add_argument('--project', required=True)
    ap.add_argument('--id', required=True)
    ap.add_argument('--goal', required=True)
    args = ap.parse_args()
    root = Path(args.project)
    it = root/'iterations'/args.id
    for d in ['task-packets','reviews','learning','architecture','contracts','ux','outputs']:
        (it/d).mkdir(parents=True, exist_ok=True)
    write(it/'goal.yaml', f'''iteration_id: {args.id}\ngoal:\n  title: {args.goal}\n  description: {args.goal}\nstatus: goal_created\n''')
    write(it/'iteration-brief.md', f'# {args.id} 迭代简报\n\n## 目标\n\n{args.goal}\n')
    write(it/'agent-engagement-plan.yaml', f'''iteration_id: {args.id}\nselected_agents: []\nhuman_decision_required: []\n''')
    write(it/'source-artifact-trace.md', f'''# Source Artifact Trace — {args.id}\n\n## 本轮目标\n\n{args.goal}\n\n## 相关源资产\n\n请读取项目的 `knowledge/source-assets/source-assets.yaml`，列出本轮需要使用的产品说明、原型、UI 设计稿、截图或设计系统。\n\n## 提取出的约束\n\n待补充。\n\n## 不适用资产\n\n待补充。\n''')
    print(f'迭代已创建：{it}')

if __name__ == '__main__':
    main()
