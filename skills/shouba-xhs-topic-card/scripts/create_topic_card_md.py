#!/usr/bin/env python3
"""Create an empty Shouba Xiaohongshu topic card Markdown template."""
import sys
from pathlib import Path

TEMPLATE = """# 瘦吧小红书选题卡

## 一、热点来源信息

- 热点标题：
- 热点排名：
- 热度值：
- 数据来源：
- 原始链接：
- 抓取时间：
- 页面更新时间：

## 二、匹配产品信息

- 产品名称：
- 产品类别：
- 产品核心卖点：
- 目标人群：
- 使用场景：
- 产品解决痛点：
- 风险边界：

## 三、匹配评分

| 维度 | 分数 1-5 | 理由 |
|---|---:|---|
| 话题语义相关度 |  |  |
| 用户场景匹配度 |  |  |
| 痛点匹配度 |  |  |
| 内容转化空间 |  |  |
| 产品植入自然度 |  |  |
| 风险可控度 |  |  |

综合分：/100
判断结果：

## 四、选题判断

- 是否生成正式选题卡：
- 推荐理由：
- 不建议承接原因：

## 五、内容方向

- 内容角度：
- 用户切入点：
- 产品自然植入方式：
- 适合内容形式：

## 六、标题方向

1. 
2. 
3. 

## 七、封面文案方向

1. 
2. 
3. 

## 八、风险表达边界

- 禁止表达：
- 谨慎表达：
- 推荐替代表达：

## 九、给小红书内容智能体的交接指令

请基于本选题卡生成标题、封面文案、正文结构、评论区引导和风险表达检查清单。

## 十、复盘字段

- 发布时间：待补充
- 内容链接：待补充
- 曝光：待补充
- 点赞：待补充
- 收藏：待补充
- 评论：待补充
- 私信/咨询：待补充
- 复盘结论：待补充
"""


def main():
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("shouba_xhs_topic_card.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEMPLATE, encoding="utf-8")
    print(str(output))


if __name__ == "__main__":
    main()
