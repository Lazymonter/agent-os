# 禁止行为策略

## Agent 禁止行为

- 未执行或未记录 Task Intake Gate 就修改文件、生成正式工件或更新 golden。
- 未读 Task Packet 就修改文件。
- 未读取对应 Skill、相关 workflow、policy、rubric 就执行任务包。
- 任务结束时未执行 Exit Gate 却声称任务完成。
- 擅自扩大范围。
- 擅自修改 schema。
- 忽略人类决策点。
- 把不确定结论写成确定结论。
- 为通过测试直接改 golden files。
- 删除未关闭迭代目录。
- 把项目私有内容写进 Agent OS。

## 触发后处理

- 标记任务为 `rework_required`。
- 生成 Review Finding。
- 必要时生成 Learning Proposal。
