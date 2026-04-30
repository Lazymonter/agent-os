#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED = ['AGENTS.md','.agent/agent-config.yaml','.agent/agent-os.lock','knowledge/project-pack','iterations']

def main():
    ap = argparse.ArgumentParser(description='校验项目初始化结构。')
    ap.add_argument('project')
    args = ap.parse_args()
    root = Path(args.project)
    missing = [p for p in REQUIRED if not (root/p).exists()]
    if missing:
        print('项目初始化校验失败，缺少：')
        for m in missing:
            print('-', m)
        raise SystemExit(1)
    print('项目初始化校验通过。')

if __name__ == '__main__':
    main()
