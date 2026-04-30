#!/usr/bin/env python3
import argparse, re
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description='脱敏学习反馈文本。')
    ap.add_argument('input')
    ap.add_argument('output')
    args = ap.parse_args()
    text = Path(args.input).read_text(encoding='utf-8')
    text = re.sub(r'(password|token|secret|api_key)\s*[:=]\s*\S+', r'\1: [REDACTED]', text, flags=re.I)
    Path(args.output).write_text(text, encoding='utf-8')
    print('反馈已脱敏。')

if __name__ == '__main__':
    main()
