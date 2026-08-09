# Get-Robot 网络爬虫工具

## 项目概述

Get-Robot 是一个基于 Python 的命令行网络爬虫工具，支持自定义请求头、Cookie、防盗链（Referer）、Tor 代理以及多种文件类型下载保存。

## 项目结构

```
src/
├── main.py            # 程序入口，爬取与文件保存流程
├── spider.py          # 爬虫核心，HTTP 请求、代理、状态码处理
├── user_config.py     # 用户交互，请求头/Cookie/URL/Tor 配置
├── data_cleaning.py   # 数据清洗，HTML/JSON/TXT/CSV 文件处理
├── __pycache__/
├── .venv/
└── .vscode/
```

## 文件说明

### main.py — 程序入口

执行流程：
1. 弹出文件夹选择对话框确定保存目录（取消则使用默认 `Downloads/`）
2. 创建爬虫对象，发起请求获取状态码
3. 根据用户选择的类型（文本/图片/音频/视频）确定写入模式
4. 用户输入文件名，写入文件
5. 文本模式使用 `response.text`（UTF-8），二进制模式使用 `response.content`

### spider.py — 爬虫核心模块

`get_robots` 类：
- `__init__(web_name, cookies, user_from)` — 初始化请求参数，Tor 代理配置
- `robots()` — 发起请求，随机等待 1~5 秒反爬，异常自动重定向重试
- `get_response()` — 获取 Response 对象
- `get_robots(robots)` — 状态码解析（200/3xx/4xx）

### user_config.py — 用户交互模块

| 函数 | 功能 |
|------|------|
| `hands()` | 随机返回 4 个内置 User-Agent 之一 |
| `hands2()` | 自定义请求头输入 |
| `UserAgent()` | 请求头入口，选择内置或自定义 |
| `CookieType()` | 解析 `name=value; name2=value2` 格式 Cookie |
| `Referer()` | 防盗链设置 |
| `type()` | 选择爬取内容类型（文本/图片/音频/视频），返回扩展名和写入模式 |
| `Url()` | 输入目标 URL |
| `tor_edge()` | Tor 代理开关 |
| `log()` | 日志初始化，按日期输出到 `logs/YYMMDD.log` |

内容类型映射：

| 选项 | 类型 | 扩展名 | 写入模式 |
|------|------|--------|----------|
| 1 | 文本 | .html | w |
| 2 | 图片 | .png | wb |
| 3 | 音频 | .mp3 | wb |
| 4 | 视频 | .mp4 | wb |

### data_cleaning.py — 数据清洗模块

支持 `.json`、`.html`、`.txt`、`.csv` 文件类型识别与处理。

HTML 文本提取功能：
- 用户输入要提取的标签（支持多个，逗号分隔）
- 可选 class/id 筛选
- 3 种提取模式：纯文本去重 / 不去重 / 带标签标记
- 提取后预览并保存为 `_extracted.txt` 文件

## 使用流程

1. 启动 `main.py` → 显示 ASCII 横幅
2. 选择是否使用内置请求头（y/n）
3. 输入 Cookie（可跳过）
4. 输入防盗链 Referer（可跳过）
5. 选择爬取内容类型（文本/图片/音频/视频）
6. 输入目标 URL
7. 选择是否启用 Tor 代理
8. 选择文件保存目录
9. 输入保存文件名
10. 程序执行爬取并保存文件

## 依赖库

| 库名 | 用途 |
|------|------|
| requests | HTTP 请求 |
| art | ASCII 艺术字输出 |
| bs4 (BeautifulSoup) | HTML 解析 |
| tkinter | 文件/文件夹选择对话框 |
| logging | 日志记录 |
| pandas | 数据处理 |
| random / time / os / json / re / base64 | 标准库辅助 |

## 日志说明

- 路径：`{项目上级目录}/logs/{YYMMDD}.log`
- 格式：`%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s`
- 编码：UTF-8
- 模式：追加写入（`filemode='a'`）

## 启动命令

```bash
# 爬虫主程序
python src/main.py

# 数据清洗
python src/data_cleaning.py
```
