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