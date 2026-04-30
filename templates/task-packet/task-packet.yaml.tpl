task_id: {{task_id}}
task_name: {{task_name}}
iteration_id: {{iteration_id}}
owner_agent: implementation
review_agents: []
execution:
  mode: isolated_worktree
  branch: feature/{{iteration_id}}/{{task_id}}
  worktree: .worktrees/{{iteration_id}}-{{task_id}}
  owner_agent: implementation
  reviewer_agents:
    - qa-verification
  human_approval_required: false
objective: "{{objective}}"
source_artifacts:
  - "{{source_artifact}}"
inputs:
  - "{{input}}"
outputs:
  - "{{output}}"
constraints:
  - "{{constraint}}"
allowed_paths:
  - "{{allowed_path}}"
forbidden_paths:
  - "{{forbidden_path}}"
forbidden_changes:
  - "{{forbidden_change}}"
acceptance_criteria:
  - "{{acceptance_criterion}}"
required_tests:
  - "{{required_test}}"
human_approval_required: false
