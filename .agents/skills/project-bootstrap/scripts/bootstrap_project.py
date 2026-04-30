#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT_DIRS = [
    'docs/product','docs/requirements','docs/architecture','docs/design','docs/security','docs/testing','docs/release',
    'knowledge/project-pack','knowledge/source-assets','knowledge/domain-overlays','knowledge/lessons','knowledge/learning-proposals',
    'adr','schemas','iterations/I-0000-project-initialization','src/core','src/cli','src/agent','src/desktop','src/ios',
    'tests/unit','tests/integration','tests/e2e','golden/raw','golden/hourly','golden/reports','golden/cli-output',
    '.agent','.agents/skills'
]

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding='utf-8')

def main():
    ap = argparse.ArgumentParser(description='初始化一个运行时中立的 Agent OS 项目结构。')
    ap.add_argument('--name', required=True)
    ap.add_argument('--path', required=True)
    ap.add_argument('--agent-os-path', required=True)
    ap.add_argument('--template', default='base')
    ap.add_argument('--summary', default='')
    ap.add_argument('--source-artifact', action='append', default=[], help='源资产登记项，格式 id:type:path:status，例如 prototype:review_deck:artifacts/prototype.zip:approved')
    args = ap.parse_args()
    project = Path(args.path)
    project.mkdir(parents=True, exist_ok=True)
    for d in ROOT_DIRS:
        (project/d).mkdir(parents=True, exist_ok=True)
    write(project/'README.md', f'# {args.name}\n\n{args.summary or "项目说明待补充。"}\n')
    write(project/'AGENTS.md', f'''# AGENTS.md — {args.name}\n\n## 项目规则\n\n- 所有 Agent 必须先读取本文件。\n- 不得越过当前 Task Packet 修改文件。\n- 不得修改 forbidden changes 中列出的内容。\n- 需要人类决策的事项必须停止并提出 Decision Pack。\n\n## 项目摘要\n\n{args.summary or "待补充。"}\n''')
    write(project/'.agent/agent-config.yaml', f'''agent_system:\n  local_path: {args.agent_os_path}\n  template: {args.template}\nproject:\n  name: {args.name}\n  project_pack_path: knowledge/project-pack\n  default_iteration_dir: iterations\nexecution:\n  runtime: neutral\n  skill_dir: .agents/skills\n''')
    write(project/'.agent/agent-os.lock', f'''agent_os:\n  local_path: {args.agent_os_path}\n  version: 1.2.0-runtime-neutral-cn\n  locked_at: {datetime.now(timezone.utc).isoformat()}\n''')
    for name, title in [('overview.md','项目概览'),('scope.md','一期范围'),('non-scope.md','非一期范围'),('red-lines.md','项目红线'),('terminology.md','术语表'),('technical-route.md','技术路线')]:
        write(project/f'knowledge/project-pack/{name}', f'# {title}\n\n待补充。\n')
    source_lines = ['assets:']
    if args.source_artifact:
        for item in args.source_artifact:
            parts = item.split(':', 3)
            if len(parts) == 4:
                sid, stype, spath, status = parts
                source_lines.extend([
                    f'  - id: {sid}',
                    f'    type: {stype}',
                    f'    path_or_uri: {spath}',
                    '    source: user_provided',
                    f'    status: {status}',
                    '    used_for: []',
                    '    notes: 待补充。'
                ])
    else:
        source_lines.append('  []')
    write(project/'knowledge/source-assets/source-assets.yaml', '\n'.join(source_lines) + '\n')
    write(project/'docs/design/prototype/README.md', '# 原型与设计稿\n\n本目录用于保存或引用项目原型、评审 PDF、UI 截图和设计系统。请同时维护 `knowledge/source-assets/source-assets.yaml`。\n')
    write(project/'iterations/I-0000-project-initialization/goal.yaml', f'''iteration_id: I-0000-project-initialization\ngoal:\n  title: 项目初始化\n  description: 初始化 {args.name} 项目结构、Project Pack 和 Agent 配置。\nstatus: created\n''')
    write(project/'iterations/I-0000-project-initialization/iteration-brief.md', f'# I-0000 项目初始化\n\n项目已初始化。\n')
    write(project/'iterations/I-0000-project-initialization/decision-pack.md', '# Decision Pack\n\n等待人类确认项目初始化是否通过。\n')
    print(f'项目初始化完成：{project}')

if __name__ == '__main__':
    main()
