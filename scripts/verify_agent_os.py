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
    'policies/task-intake-exit-gate-policy.md',
    'workflows/iteration-workflow.md','workflows/iteration-close-workflow.md',
    'workflows/ui-prototype-design-workflow.md','docs/agent-execution-threading-model.md',
    'schemas/task-packet.schema.json','schemas/agent-engagement-plan.schema.json'
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
task_packet_template = (root/'templates/task-packet/task-packet.yaml.tpl').read_text(encoding='utf-8')
required_task_packet_fields = [
    'task_id', 'task_name', 'iteration_id', 'owner_agent', 'execution', 'objective',
    'source_artifacts', 'inputs', 'outputs', 'constraints', 'allowed_paths',
    'forbidden_paths', 'forbidden_changes', 'acceptance_criteria',
    'required_tests', 'human_approval_required'
]
missing_template_fields = [
    field for field in required_task_packet_fields
    if f'{field}:' not in task_packet_template
]
if missing_template_fields:
    print('task-packet 模板缺失字段:', *missing_template_fields, sep='\n- ')
    sys.exit(1)
required_task_packet_execution_fields = [
    'mode', 'branch', 'worktree', 'owner_agent', 'reviewer_agents',
    'human_approval_required'
]
missing_execution_fields = [
    field for field in required_task_packet_execution_fields
    if f'{field}:' not in task_packet_template
]
if missing_execution_fields:
    print('task-packet execution 模板缺失字段:', *missing_execution_fields, sep='\n- ')
    sys.exit(1)
agent_engagement_template = (root/'templates/iteration/agent-engagement-plan.yaml.tpl').read_text(encoding='utf-8')
required_agent_engagement_fields = [
    'iteration_id', 'goal_title', 'classification', 'impact',
    'selected_agents', 'agent', 'role', 'execution_mode', 'reason',
    'human_decision_required'
]
missing_agent_engagement_fields = [
    field for field in required_agent_engagement_fields
    if f'{field}:' not in agent_engagement_template
]
if missing_agent_engagement_fields:
    print('agent-engagement-plan 模板缺失字段:', *missing_agent_engagement_fields, sep='\n- ')
    sys.exit(1)
print('Agent OS 校验通过。')
