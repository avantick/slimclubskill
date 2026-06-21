---
name: 瘦吧小红书选题卡skill
description: This skill should be used after neutral Xiaohongshu hotspots have been tracked and the user provides a product or product library. It matches hotspots against product information, evaluates topic-product fit, and outputs standardized Xiaohongshu topic cards for Shouba content planning.
agent_created: true
---

# 瘦吧小红书选题卡skill

## Purpose

Generate Xiaohongshu topic cards by matching neutral hotspot data with user-provided product or product-library information. This skill is downstream of neutral hotspot tracking: it should only evaluate fit after product information is available.

Do not fetch hotboards in this skill. Do not invent product selling points. Do not force a hotspot to match a product. Use the product library as the only source of product claims, target users, scenarios, pain points, benefits, and risk boundaries.

## Use when

Use this skill when the user asks to:

- 根据热点和产品库生成小红书选题卡。
- 判断 UApiPro 热榜中的哪些热点适合某个产品。
- 将热点转化为可执行的小红书选题方向。
- 输出包含产品匹配、内容角度、风险边界和后续交接的选题卡。
- 为小红书内容智能体准备结构化输入。

## Required inputs

### Hotspot input

Use neutral hotspot data from “瘦吧热点跟踪skill” or user-provided hotboard material:

- 热点标题
- 排名
- 热度值
- 来源
- 原始链接
- 抓取时间
- 页面更新时间

### Product library input

Require at least one product. Each product should include:

| 字段 | 说明 |
|---|---|
| 产品名称 | 产品或服务名称 |
| 产品类别 | 食品、服务、检测、课程、工具等 |
| 核心卖点 | 真实可表达的卖点 |
| 目标人群 | 适合的人群 |
| 使用场景 | 什么时候、什么场景使用 |
| 用户痛点 | 产品解决的问题 |
| 可表达利益点 | 对外内容中可以表达的价值 |
| 风险边界 | 禁止或谨慎表达的内容 |

If product data is missing, ask for product library first. Do not generate topic cards without product basis.

## Matching dimensions

Score each hotspot-product pair from 1 to 5.

| Dimension | Weight | Question |
|---|---:|---|
| 话题语义相关度 | 20% | 热点标题与产品类别、卖点、场景是否相关？ |
| 用户场景匹配度 | 20% | 热点可能触发的场景是否与产品使用场景重合？ |
| 痛点匹配度 | 20% | 热点可延展的问题是否与产品解决的痛点一致？ |
| 内容转化空间 | 15% | 是否能自然生成种草、科普、清单、避坑、案例等内容？ |
| 产品植入自然度 | 15% | 产品出现是否自然，不会硬蹭？ |
| 风险可控度 | 10% | 是否能避开产品风险边界和敏感表达？ |

Weighted score formula:

```text
总分 = 话题语义相关度*4 + 用户场景匹配度*4 + 痛点匹配度*4 + 内容转化空间*3 + 产品植入自然度*3 + 风险可控度*2
满分 = 100
```

Decision levels:

| Score | Decision |
|---:|---|
| 80-100 | 高匹配，生成正式选题卡 |
| 65-79 | 中匹配，生成待验证选题卡 |
| 50-64 | 弱匹配，只记录观察，不生成正式选题卡 |
| <50 | 不匹配，不建议承接 |

Hard stop rules:

- If product insertion is forced, do not generate a formal topic card.
- If risk control score is 1 or 2, do not generate a formal topic card.
- If a needed product claim is not present in the product library, mark it as unavailable instead of inventing it.

## Workflow

### Step 1: Load neutral hotspot data

Use only observed fields from the hotboard:

- title
- rank
- heat
- source
- original_url
- fetched_at
- board_updated_at

### Step 2: Load product library

Normalize product information into:

- product_name
- category
- selling_points
- target_users
- scenarios
- pain_points
- benefits
- risk_boundaries

### Step 3: Match hotspots to products

Evaluate each hotspot-product pair. For multiple products, rank the best product match for each hotspot.

### Step 4: Select topics for cards

Generate topic cards only for high-match and medium-match pairs. For weak or no-match pairs, output a short rejection reason.

### Step 5: Output topic card

Use `references/topic_card_template.md`.

Each card must include:

1. 热点来源信息
2. 匹配产品信息
3. 匹配评分
4. 选题判断
5. 内容方向
6. 标题方向
7. 封面文案方向
8. 风险边界
9. 给小红书内容智能体的交接指令
10. 复盘字段

## Output modes

Default: Markdown topic cards.

If the user asks for batch output, use a summary table first, then cards for selected topics.

## Quality checklist

Before final output, verify:

- Hotspot data is traceable to the tracking source.
- Product information is from user input or explicit product library.
- Matching reason cites product fields.
- Risk boundary is included.
- No final full Xiaohongshu post is written unless the user explicitly asks.
- Topic card can be handed off to a content agent without redoing product matching.
