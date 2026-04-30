# 安装与接入说明

Agent OS 不要求特定 Agent Runtime。你可以使用 Codex、Claude Code 或其他 Agent 工具，只要它能读取文件、执行脚本、修改仓库并运行测试。

## 推荐接入方式

1. 将本仓库放在项目仓库旁边，例如：

```text
workspace/
  agent-os/
  proxyq/
```

2. 在目标项目初始化前，让 Agent 读取：

```text
../agent-os/AGENTS.md
../agent-os/.agents/skills/project-bootstrap/SKILL.md
```

3. 初始化完成后，项目仓库会生成：

```text
AGENTS.md
.agent/agent-config.yaml
.agent/agent-os.lock
knowledge/project-pack/
iterations/
```

## 校验

```bash
python3 scripts/verify_agent_os.py .
```
