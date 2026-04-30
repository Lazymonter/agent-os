# Agent OS 维护流程

## 目标

维护通用 Agent OS 仓库，吸收多个项目提交的通用反馈，持续改进 Skill、角色、流程、模板、策略和评审标准。

## 输入

- Learning Proposal
- Cross Repo Change Request
- 项目反馈分支
- Agent OS 回归测试结果
- 维护者评审意见

## 标准步骤

0. 执行 `policies/task-intake-exit-gate-policy.md` 的治理维护 Intake Gate。
1. 接收学习提案。
2. 隔离到 feedback/<project>/<learning-id> 或 PR。
3. 脱敏检查。
4. 判断是否项目专属。
5. 提炼成通用规则。
6. 修改 skill-pack、domain-pack、workflow、policy、template 或 rubric。
7. 运行 Agent OS 校验和回归测试。
8. 执行 Exit Gate，确认脱敏、修改位置、校验和兼容性影响。
9. 生成版本变更说明。
10. 发布新版本。
11. 删除临时反馈分支或过程内容。

## 不允许

- 把项目原始过程内容合并进主干。
- 把项目特例变成通用规则。
- 未经审查发布破坏性流程变更。
- 把敏感日志、凭据、token、私有代码写入 Agent OS。

## 准出条件

- 通用知识已脱敏。
- 修改位置正确。
- 通过 Agent OS 校验。
- 如果影响兼容性，已更新版本和变更说明。
