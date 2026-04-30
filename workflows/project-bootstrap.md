# 项目初始化流程

## 目标

项目初始化流程用于在一个空目录中创建可由任意 Agent Runtime 使用的项目结构。初始化完成后，项目必须具备：项目知识包、Agent 配置、源资产清单、首轮初始化迭代、基础目录、约束规则和后续迭代入口。

## 适用场景

- 创建一个全新软件项目。
- 把已有项目纳入 Agent OS 管理。
- 为项目建立 Project Pack、红线规则、源资产清单和迭代目录。
- 为后续需求迭代、开发迭代、测试迭代提供结构化入口。

## 参与角色

| 角色 | 参与方式 | 责任 |
|---|---|---|
| Workflow Supervisor | owner | 检查初始化输入、生成初始化工件、执行初始化校验。 |
| Product & Requirements | reviewer | 确认产品目标、一期范围、非范围和红线是否清楚。 |
| Solution Architect & Task Planner | reviewer | 确认技术路线、模块目录和首轮任务方向是否合理。 |
| UX/UI Design | consultant | 如果有原型或设计稿，确认源资产被记录并可追踪。 |
| Contract & Data Model | consultant | 如果项目涉及 schema / API，确认预留目录和契约入口。 |
| Security & Risk | reviewer | 检查敏感信息、凭据和高风险能力是否被正确标记。 |

## 输入

项目初始化至少需要以下输入：

```yaml
project_name: string
target_path: string
agent_os_path: string
project_summary: string
project_type: string
phase_scope: []
out_of_scope: []
technical_route: []
selected_domain_packs: []
source_artifacts: []
```

其中 `source_artifacts` 用于登记产品说明、原型、设计稿、评审 PDF、截图、用户研究材料等。项目初始化不一定要复制所有大文件，但必须在 `knowledge/source-assets/source-assets.yaml` 中登记它们的位置、用途和可信度。

## 标准步骤

1. **读取初始化请求**  
   读取用户目标、项目名称、技术路线、一期范围、非范围和源资产。

2. **选择项目模板**  
   根据项目类型选择模板，例如 `base`、`apple-native-shared-core`、`cli-tool`、`mobile-app`。

3. **选择 Domain Pack**  
   根据项目特点选择领域包，例如 Apple 原生应用、CLI 工具、本地文件观测、网络探测等。

4. **生成基础目录**  
   创建 `.agent/`、`knowledge/project-pack/`、`knowledge/source-assets/`、`docs/`、`adr/`、`schemas/`、`iterations/`、`src/`、`tests/`、`golden/`。

5. **生成项目级规则**  
   创建根目录 `AGENTS.md`，记录项目红线、执行规则、敏感信息规则、迭代规则。

6. **生成 Agent 配置**  
   创建 `.agent/agent-config.yaml` 和 `.agent/agent-os.lock`，记录 Agent OS 路径、版本、启用角色和启用领域包。

7. **生成 Project Pack**  
   创建项目概览、产品基线、一期范围、非范围、术语表、技术路线、红线规则。

8. **生成源资产清单**  
   创建 `knowledge/source-assets/source-assets.yaml`，登记产品文档、原型、UI 设计稿、截图、评审材料。

9. **生成 I-0000 初始化迭代**  
   创建 `iterations/I-0000-project-initialization/`，包含初始化目标、迭代简报、介入计划和决策包。

10. **执行初始化校验**  
    检查必需文件是否存在，项目规则是否存在，源资产是否登记，一期范围和红线是否清楚。

11. **输出初始化摘要**  
    输出已生成文件、缺失内容、需要人类确认的事项和建议的第一轮迭代。

## 输出工件

初始化完成后，项目仓库至少应有：

```text
AGENTS.md
.agent/agent-config.yaml
.agent/agent-os.lock
knowledge/project-pack/overview.md
knowledge/project-pack/scope.md
knowledge/project-pack/non-scope.md
knowledge/project-pack/red-lines.md
knowledge/project-pack/terminology.md
knowledge/project-pack/technical-route.md
knowledge/source-assets/source-assets.yaml
iterations/I-0000-project-initialization/goal.yaml
iterations/I-0000-project-initialization/iteration-brief.md
iterations/I-0000-project-initialization/agent-engagement-plan.yaml
iterations/I-0000-project-initialization/decision-pack.md
```

## 源资产登记规则

产品说明、原型、UI 设计稿必须作为“源资产”登记。每个源资产至少记录：

```yaml
id: string
type: product_doc | prototype | ui_screenshot | design_system | review_deck | other
path: string
source: local | external | generated
status: approved | draft | superseded
used_for: []
notes: string
```

如果项目后续实现 UI、CLI 输出、配置表单、报告页面或用户流程，必须从源资产清单中追踪输入。

## 准出条件

- 项目目录结构已生成。
- 根目录 `AGENTS.md` 已生成。
- `.agent/agent-config.yaml` 和 `.agent/agent-os.lock` 已生成。
- Project Pack 至少包含概览、范围、非范围、红线、术语表和技术路线。
- 如果存在产品说明或原型，已登记到 `knowledge/source-assets/source-assets.yaml`。
- I-0000 初始化迭代已生成。
- 需要人类确认的事项已写入 decision-pack。

## 常见失败模式

- 没有登记已有产品原型和 UI 设计稿，导致后续实现偏离评审稿。
- 项目红线没有写入 Project Pack，后续 Agent 容易扩大范围。
- `.agent/agent-os.lock` 没有锁定 Agent OS 版本，导致流程不可复现。
- 只生成目录，不生成迭代入口，导致项目无法进入正常迭代模式。
