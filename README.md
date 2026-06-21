# slimclubskill

瘦吧 WorkBuddy Skill 归档仓库，用于保存小红书热点跟踪与小红书选题卡生成相关 Skill。

## 仓库内容

```text
slimclubskill/
├── README.md
├── .gitignore
├── skills/
│   ├── shouba-hotspot-tracking/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/
│   └── shouba-xhs-topic-card/
│       ├── SKILL.md
│       ├── references/
│       └── scripts/
├── docs/
│   ├── 瘦吧热点跟踪skill_使用说明.md
│   └── 瘦吧小红书选题卡skill_使用说明.md
└── dist/
    ├── shouba-hotspot-tracking.zip
    └── shouba-xhs-topic-card.zip
```

## Skill 列表

### 1. 瘦吧热点跟踪skill

目录：`skills/shouba-hotspot-tracking`

定位：中立热点跟踪 Skill。

主要用于：

- 从 UApiPro 获取小红书热榜；
- 输出原始、可追溯的热点列表；
- 保留排名、标题、热度值、链接、抓取时间等字段；
- 不做产品匹配；
- 不做用户痛点推断；
- 不做机会判断；
- 不生成选题卡。

推荐调用：

```text
请使用“瘦吧热点跟踪skill”，从 UApiPro 获取当前小红书热榜。
只输出原始热榜列表，不要做产品匹配、用户痛点推断和机会判断。
```

### 2. 瘦吧小红书选题卡skill

目录：`skills/shouba-xhs-topic-card`

定位：基于热点与产品库的小红书选题卡生成 Skill。

主要用于：

- 接收热点数据；
- 接收产品库或单个产品信息；
- 评估热点与产品的匹配度；
- 输出标准化小红书选题卡；
- 为后续小红书内容智能体提供结构化输入。

推荐调用：

```text
请使用“瘦吧小红书选题卡skill”，基于以下热点和产品信息生成小红书选题卡。
```

## 推荐工作流

```text
瘦吧热点跟踪skill
↓
获取 UApiPro 小红书热榜原始数据
↓
输入产品库 / 单个产品信息
↓
瘦吧小红书选题卡skill
↓
评估热点与产品匹配度
↓
生成小红书选题卡
↓
交给小红书内容智能体生成标题、封面、正文、评论引导
```

## 使用说明

详见：

- `docs/瘦吧热点跟踪skill_使用说明.md`
- `docs/瘦吧小红书选题卡skill_使用说明.md`

## 版本说明

当前版本为归档初版，主要用于培训展示和后续迭代。

- `v0.1.0`：归档两个基础 Skill：热点跟踪 Skill、选题卡 Skill。

## 注意事项

1. 热点跟踪 Skill 只负责公开热榜数据整理，不代表小红书官方数据。
2. 选题卡 Skill 的匹配判断依赖用户输入的产品库质量。
3. 生成内容用于内部策划参考，正式发布前仍需人工审核品牌表达、产品合规和风险边界。
