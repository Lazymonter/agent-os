# 内容完整性检查

## 已补齐

- workflow 文件已补齐为可执行流程。
- skill-packs 已按角色分别编写，不再重复。
- policies 已按策略分别编写，不再重复。
- schemas 已扩展为有约束的 JSON Schema。
- docs 只保留项目无关内容。
- ProxyQ 相关内容已移入 examples/proxyq。
- 新增完整 ProxyQ 示例。
- 新增 Agent OS 自我迭代示例。
- 新增 UI 原型设计产出 Skill。
- 新增迭代关闭和文件膨胀控制机制。
- 新增 Agent 执行线程与实例化模式，明确 inline、isolated_task、isolated_worktree、independent_review 和 human_decision。

## 仍建议在真实项目中补充

- 项目的真实源资产路径。
- 项目真实 Project Pack。
- 项目真实 schema。
- 项目真实测试命令。
- UI 截图生成工具链。
- 运行时具体调用方式说明。

## 第一轮迭代前检查

运行：

```bash
python3 scripts/verify_agent_os.py .
```

并确认项目仓库中：

```text
AGENTS.md
knowledge/project-pack/
knowledge/source-assets/source-assets.yaml
iterations/I-0000-project-initialization/
```
