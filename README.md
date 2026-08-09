<<<<<<< HEAD
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
=======
# 🤖 GetRobot - 智能网络爬虫下载工具

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-2.31.0-orange.svg)](https://requests.readthedocs.io/)

## 📖 简介

**GetRobot** 是一个功能强大的网络爬虫下载工具，支持多种文件类型下载，能够自动处理防盗链、Cookie、请求头等反爬机制。

从最初250行单文件脚本，重构为模块化架构，实现了从"脚本"到"工具"的蜕变。

## ✨ 功能特点

| 功能 | 说明 |
|------|------|
| 🚀 **多类型下载** | 支持文本、图片、音频、视频 |
| 🛡️ **反爬处理** | 自动处理防盗链、Cookie、请求头 |
| 📦 **模块化设计** | 三个模块各司其职，易于维护 |
| 💡 **交互友好** | 命令行菜单 + GUI目录选择 |
| 📝 **日志系统** | 完整的日志记录，便于调试 |
| ⚙️ **灵活配置** | 内置/自定义请求头、Cookie支持 |

## 📁 项目结构
GetRobot/
├── getNew.py # 核心爬虫模块
├── User.py # 用户交互模块
├── write.py # 文件保存模块
├── get.log # 运行日志
├── requirements.txt
└── README.md


## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip

### 安装依赖

```bash
pip install -r requirements.txt

是否使用工具自带的请求头(y/n): y
请输入cookie(直接回车跳过): 
爬取网站的防盗链: https://example.com
请选择文件类型: 4 (视频)
输入爬取的网站: https://example.com/video.mp4
输入保存的文件名: myvideo


2026-06-13 10:39:53 - User - INFO - user_agents选择完毕
2026-06-13 10:40:49 - getNew - INFO - 爬虫启动
2026-06-13 10:40:59 - getNew - INFO - 网页状态码:200
2026-06-13 10:41:07 - write - INFO - 文件保存完成



📝 开发历程

从最初的250行单文件脚本，经历：

1.模块化拆分（3个文件各司其职）

2.添加日志系统

3.优化文件类型识别

4.完善异常处理

5.增加图片直链提取

最终形成完整、专业的下载工具。


# 一键安装所有依赖
pip install -r requirements.txt


求求大家给个星星了
>>>>>>> 00accd865a560748080ebb01cec62df098f58239
