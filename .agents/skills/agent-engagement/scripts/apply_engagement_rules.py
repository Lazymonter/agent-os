#!/usr/bin/env python3
import argparse, json

def main():
    ap = argparse.ArgumentParser(description='根据影响维度给出建议介入角色。')
    ap.add_argument('--impact', default='{}', help='JSON 字符串，如 {"data_contract":"high"}')
    args = ap.parse_args()
    impact = json.loads(args.impact)
    agents = set(['product-requirements','solution-architect-task-planner','qa-verification'])
    if impact.get('data_contract') == 'high': agents.add('contract-data-model')
    if impact.get('security') == 'high': agents.add('security-risk')
    if impact.get('ui_ux') == 'high': agents.add('ux-ui-design')
    if impact.get('implementation') in ('medium','high'): agents.add('implementation')
    print(json.dumps({'selected_agents': sorted(agents)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
