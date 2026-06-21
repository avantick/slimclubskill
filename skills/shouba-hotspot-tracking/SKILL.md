---
name: 瘦吧热点跟踪skill
description: This skill should be used when neutrally tracking Xiaohongshu hot topics from UApiPro for Shouba. It fetches or organizes the original UApiPro hotboard data and outputs a source-backed raw hotspot list without product matching, brand preference, topic opportunity scoring, or content suggestions.
agent_created: true
---

# 瘦吧热点跟踪skill

## Purpose

Track Xiaohongshu hotspots neutrally from UApiPro and output the original hotboard list as evidence-backed raw data. Keep this skill strictly upstream: collect and normalize hotspot data only.

Do not evaluate product fit. Do not classify topics into Shouba business categories. Do not infer user pain points, user emotions, content angles, or opportunity levels. Downstream product matching and topic-card generation must happen only after the user provides product or product-library information.

## Data source

Primary source:

```text
https://uapis.cn/hotboard/xiaohongshu
```

Treat UApiPro as a public third-party aggregation page, not an official Xiaohongshu API. Always disclose this boundary.

## Use when

Use this skill when the user asks to:

- 跟踪小红书热点。
- 从 UApiPro 获取当前小红书热榜。
- 输出中立的热点榜单。
- 为后续产品匹配、选题卡或智能体生成提供原始热点输入。
- 定期记录小红书热榜变化。

## Compliance rules

Follow these rules strictly:

- Fetch only public, accessible pages or user-provided materials.
- Do not bypass login, captcha, access control, anti-crawling mechanisms, rate limits, or platform rules.
- Do not fabricate titles, rankings, heat values, links, update times, or source evidence.
- Do not claim UApiPro data is official Xiaohongshu data.
- If UApiPro is unavailable, report the failure and ask for user-provided screenshots, copied hotboard text, or an authorized source.

## Workflow

### Step 1: Fetch or read UApiPro hotboard

Use the UApiPro Xiaohongshu hotboard page if web access is available. Extract only visible fields:

- 页面标题 / 平台
- 页面更新时间
- 总条数
- 排名
- 热点标题
- 热度值
- 原始链接
- 数据源 URL
- 抓取时间

If direct fetching is not possible, request the user to paste UApiPro hotboard text or provide a screenshot.

### Step 2: Normalize raw hotspot data

Output one row per hotspot using these fields:

| 字段 | 说明 |
|---|---|
| fetched_at | 本次抓取时间 |
| source | UApiPro 小红书热榜公开聚合页 |
| source_url | https://uapis.cn/hotboard/xiaohongshu |
| board_updated_at | 页面显示的更新时间 |
| rank | 热榜排名 |
| title | 热点标题 |
| heat | 页面显示的热度值 |
| original_url | 页面中的小红书搜索结果链接 |
| evidence_status | 完整 / 部分 / 无法确认 |

### Step 3: Output neutral tracking report

Use `references/hotspot_tracking_template.md` as the output structure. Include:

1. 数据源说明
2. 抓取时间
3. 页面更新时间
4. 原始热榜表格
5. 数据边界说明
6. 下游交接说明

### Step 4: Handoff to downstream product matching

End every report with:

```text
【下游交接说明】
本次仅完成热点中立抓取，未做品牌倾向、产品匹配、用户痛点推断或机会判断。
如需继续生成选题卡，请提供产品名称或产品库信息，再使用“瘦吧小红书选题卡skill”。
```

## Forbidden outputs in this skill

Do not output:

- 变瘦 / 变美 / 变健康分类。
- 产品承接建议。
- 用户痛点推断。
- 用户情绪推断。
- 内容角度或标题建议。
- A/B/C 优先级。
- 是否值得跟进。
- 机会卡或选题卡。

## Quality checklist

Before final output, verify:

- All hotspot rows are traceable to UApiPro or user-provided source material.
- No product or brand preference has been added.
- No downstream opportunity judgment has been made.
- Missing fields are marked as `无法确认` or `待补充`.
