# lark-whiteboard-design

一个 [Claude](https://claude.com/claude-code) Agent Skill，用来把飞书 / Lark 画板做得**像被认真设计过**，而不是看起来像 API 随手生成的。它在已有的 `lark-whiteboard` 执行 skill 之上叠加一层「设计能力」：更强的视觉层级、布局、配色、留白，以及可复用的图示范式。

## 适用场景

当你需要：

- 创建、美化、重做、审查飞书 / Lark 画板
- 从优质画板（链接 / token / 截图 / 缩略图 / 原始数据）中**学习风格**
- 把文档、流程、架构、对比、时间线、漏斗、战略等结构化信息，变成一张**高质量画板**而不是普通流程图
- 沉淀并标准化团队的画板设计规范

## 目录结构

```
.
├── SKILL.md                          # Skill 主文件：核心规则、设计工作流、视觉标准、校验清单
├── references/
│   ├── patterns.md                   # 可复用的图示范式（流程 / 架构 / 对比 / 路线图 / 漏斗 …）
│   ├── style-library.md              # 房屋默认风格库，可随团队审美持续沉淀
│   └── sample-intake.md              # 参考素材的采集与解析示例
├── scripts/
│   └── whiteboard_quality_check.py   # 对画板 JSON 做质量自检的脚本
└── agents/
    └── openai.yaml                   # 配套 agent 配置
```

## 安装

把整个仓库克隆到你的 Claude skills 目录，文件夹名保持为 `lark-whiteboard-design`：

```bash
git clone git@github.com:griffent/lark-whiteboard-design.git ~/.claude/skills/lark-whiteboard-design
```

## 核心理念

始终把四件事分开做：

1. **学习** —— 从参考画板中提炼风格特征
2. **规划** —— 设计信息架构
3. **渲染** —— 选定视觉范式后绘制画板
4. **校验与写入** —— 通过 `lark-whiteboard` skill 真正落到飞书画板

> 实际查询、渲染、dry-run、写入飞书画板的能力由配套的 `lark-whiteboard` skill 提供，本 skill 负责其上的设计层。

## 安全与隐私

- 飞书链接、token、资源 ID、原始 JSON、截图、缩略图和画板原文默认按敏感信息处理。
- 查询、导出和预览产物只能放在系统临时目录，或已被忽略的 `work/`、`tmp/` 等目录中，不能写入版本库。
- `style-library.md` 只沉淀匿名化后的通用视觉规则，不保留来源、名称、内部项目、原文、指标、日期或访问状态。
- 提交前检查 `git status --short`，并使用可用的密钥扫描工具检查改动。

## License

[MIT](./LICENSE)
