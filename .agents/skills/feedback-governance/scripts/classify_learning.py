#!/usr/bin/env python3
import argparse

def main():
    ap = argparse.ArgumentParser(description='学习反馈分类占位脚本。')
    ap.add_argument('text')
    args = ap.parse_args()
    print('建议分类：需要人工确认。可选：project-only / agent-skill / domain / workflow / policy / do-not-learn')

if __name__ == '__main__':
    main()
