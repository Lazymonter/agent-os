#!/usr/bin/env python3
'''生成一个可给人看的静态 HTML 原型骨架。'''
from pathlib import Path
import argparse, html
parser = argparse.ArgumentParser()
parser.add_argument('--out', required=True)
parser.add_argument('--title', default='产品原型')
parser.add_argument('--pages', default='Dashboard,Settings,Report')
args = parser.parse_args()
out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
pages = [p.strip() for p in args.pages.split(',') if p.strip()]
body = ''
for p in pages:
    body += f'''<section class="page"><h2>{html.escape(p)}</h2><div class="card"><h3>页面目标</h3><p>说明此页面要解决的用户问题。</p></div><div class="grid"><div class="card">关键指标</div><div class="card">主要操作</div><div class="card">状态与提示</div></div></section>'''
(out/'prototype.html').write_text(f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(args.title)}</title><style>body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f8fafc;margin:0;color:#111827}}header{{background:#111827;color:white;padding:24px}}.page{{margin:24px;background:white;border:1px solid #e5e7eb;border-radius:14px;padding:24px}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.card{{border:1px solid #e5e7eb;border-radius:12px;padding:16px;background:#fff}}</style></head><body><header><h1>{html.escape(args.title)}</h1><p>静态评审原型</p></header>{body}</body></html>''', encoding='utf-8')
(out/'README.md').write_text(f'# {args.title}\n\n打开 `prototype.html` 查看原型。\n', encoding='utf-8')
print(f'已生成原型: {out / "prototype.html"}')
