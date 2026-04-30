#!/usr/bin/env python3
"""Agent OS 基础结构校验。"""
from pathlib import Path
import sys, json
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
required = [
    'AGENTS.md','README.md','.agents/skills/project-bootstrap/SKILL.md',
    '.agents/skills/iteration-start/SKILL.md','.agents/skills/agent-engagement/SKILL.md',
    '.agents/skills/task-decomposition/SKILL.md','.agents/skills/task-execution/SKILL.md',
    '.agents/skills/qa-verification/SKILL.md','.agents/skills/security-review/SKILL.md',
    '.agents/skills/contract-review/SKILL.md','.agents/skills/feedback-governance/SKILL.md',
    '.agents/skills/agent-os-maintenance/SKILL.md','.agents/skills/iteration-close/SKILL.md',
    '.agents/skills/ui-prototype-design/SKILL.md','agents/ROLE_INDEX.md',
    'registry/agent-registry.yaml','registry/engagement-rules.yaml','registry/skill-registry.yaml',
    'policies/human-decision-policy.md','policies/iteration-retention-policy.md',
    'workflows/iteration-workflow.md','workflows/iteration-close-workflow.md',
    'workflows/ui-prototype-design-workflow.md','schemas/task-packet.schema.json'
]
missing=[p for p in required if not (root/p).exists()]
empty=[p for p in required if (root/p).exists() and (root/p).stat().st_size < 20]
if missing or empty:
    if missing: print('缺失文件:', *missing, sep='\n- ')
    if empty: print('疑似空文件:', *empty, sep='\n- ')
    sys.exit(1)
# ensure schemas are valid JSON
for p in (root/'schemas').glob('*.json'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'Schema 不是有效 JSON: {p}: {e}')
        sys.exit(1)
print('Agent OS 运行时中立版 v1.2 校验通过。')
