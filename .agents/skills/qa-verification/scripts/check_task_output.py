#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description='基础任务输出检查。')
    ap.add_argument('--task', required=True)
    args = ap.parse_args()
    p = Path(args.task)
    if not p.exists():
        print('任务包不存在。')
        raise SystemExit(1)
    text = p.read_text(encoding='utf-8')
    required = ['task_id:', 'acceptance_criteria:', 'forbidden_changes:']
    missing = [r for r in required if r not in text]
    if missing:
        print('任务包检查失败，缺少字段：', ', '.join(missing))
        raise SystemExit(1)
    print('任务包基础检查通过。')

if __name__ == '__main__':
    main()
