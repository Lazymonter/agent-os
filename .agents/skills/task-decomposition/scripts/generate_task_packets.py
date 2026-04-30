#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description='生成基础任务包。')
    ap.add_argument('--iteration', required=True)
    ap.add_argument('--task-id', required=True)
    ap.add_argument('--title', required=True)
    args = ap.parse_args()
    it = Path(args.iteration)
    p = it/'task-packets'/f'{args.task_id}.yaml'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f'''task_id: {args.task_id}\ntask_name: {args.title}\nowner_agent: implementation\ninputs: []\noutputs: []\nconstraints: []\nforbidden_changes: []\nacceptance_criteria: []\n''', encoding='utf-8')
    print(f'任务包已生成：{p}')

if __name__ == '__main__':
    main()
