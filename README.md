根据提供的三份代码文件内容，以下是生成的 Markdown 文档：


Get-Robot 网络爬虫工具文档

项目概述

Get-Robot 是一个基于 Python 的命令行网络爬虫工具，支持自定义请求头、Cookie、防盗链（Referer）、Tor 代理以及多种文件类型下载保存。项目由三个核心模块组成，采用模块化设计。

项目启动时间： 2025年4月24日 19:50 开始重构


项目结构

文件	说明
User.py	用户交互模块，负责收集请求头、Cookie、Referer、文件类型、目标 URL 及 Tor 配置
Get.py	爬虫核心模块，封装 HTTP 请求、代理设置、状态码处理等逻辑
主程序（入口脚本）	程序入口，调用上述模块完成爬取与文件保存


模块说明

一、User.py — 用户交互模块

该模块负责所有用户输入的采集与预处理，提供以下功能函数：

1. hands() — 自动选择请求头

    内置 4 个主流浏览器的 User-Agent（Chrome、Firefox，覆盖 Windows / macOS / Linux）
    随机返回其中一个


2. hands2() — 自定义请求头

    用户手动输入请求头
    输入内容须包含 Windows NT 字段，否则提示重新输入
    输入 q 可退出并回退到默认请求头


3. CookieType() — Cookie 处理

    用户输入格式：name=value; name2=value2
    自动解析为字典格式
    直接回车跳过则返回 None


4. Referer() — 防盗链（Referer）设置

    输入内容须包含 http，否则提示不正确
    若网站不需要防盗链，等待 5 秒后返回 None


5. UserAgent() — 请求头入口

    询问用户是否使用工具自带请求头
    y 调用 hands()，其他调用 hands2()


6. type() — 爬取内容类型选择

    提供 4 种类型供选择：


选项	类型	默认扩展名	写入模式	Content-Type
1	文本	.html	w（文本写入）	application/json, text/html, text/plain
2	图片	.png	wb（二进制写入）	image/jpeg, image/png, image/gif, image/webp
3	音频	.mp3	wb（二进制写入）	audio/mpeg, audio/wav, audio/ogg
4	视频	.mp4	wb（二进制写入）	video/mp4, video/webm, video/quicktime

    返回值：(Ask_Need, content_type, extension, mode)


7. Url() — 目标 URL 输入

    输入须包含 http，否则提示可能不存在并要求重新输入


8. tor_edge() — Tor 代理配置

    提示用户确认 Tor 浏览器已安装并运行
    输入 y 启用 Tor 代理，否则返回 None
    Tor 下载地址：https://torproject.netcologne.de/zh-CN/download/tor/



二、Get.py — 爬虫核心模块

全局初始化

在模块加载时自动完成以下初始化：

    日志配置：日志文件按日期命名（格式 YYMMDD.log），存放于上级目录的 logs/ 文件夹
    配置项加载：调用 User.py 中的函数获取 User-Agent、Cookie、Referer、内容类型、URL、Tor 配置等
    请求头组装：将各项配置组装为 user_from 字典


get_robots 类

__init__(self, web_name, cookies, user_from)

参数	说明
web_name	目标 URL
cookies	Cookie 字典或 None
user_from	请求头字典

    若 Tor 已启用，配置 SOCKS5 代理：socks5h://127.0.0.1:9150
    否则代理为 None


robots(self) — 发起请求

    请求前随机等待 1~5 秒（反爬策略）
    第一次使用 requests.get() 发起请求
    若发生异常，等待 1~5 秒后启用 allow_redirects=True 重试
    打印响应内容前 500 个字符
    返回 HTTP 状态码


get_response(self) — 获取响应对象

    调用 robots() 发起请求后返回 self.response


get_robots(self, robots) — 状态码解析

状态码范围	返回信息	日志级别
== 200	网站请求成功	INFO
200 < code <= 300	网站未处理请求	INFO
300 < code <= 400	网站地址移动到新地方，程序已自动处理重定向	INFO
code > 400	失败	INFO


三、主程序（入口脚本）

执行流程

    1.
    选择保存目录：通过 tkinter 弹出文件夹选择对话框；用户取消则使用默认目录 {上级目录}/Downloads/
    2.
    创建爬虫对象：实例化 get_robots，传入 URL、Cookie、请求头
    3.
    发起请求：调用 robots() 获取状态码
    4.
    确定文件类型：根据 Ask_Need 值判断写入模式：
        1（文本）→ 二进制模式 False，w 写入
        2（图片）、3（音频）、4（视频）→ 二进制模式 True，wb 写入
        其他 → 用户手动输入扩展名，二进制模式写入
    5.
    用户输入文件名，拼接为完整保存路径
    6.
    写入文件：
        二进制模式：response.content 写入
        文本模式：response.text 写入（UTF-8 编码）
    7.异常捕获：打印错误信息并退出



依赖库

库名	用途
requests	HTTP 请求
art	ASCII 艺术字输出（启动横幅）
tkinter	文件夹选择对话框
logging	日志记录
random / time / os / json	标准库辅助功能


日志说明

    日志路径：{项目上级目录}/logs/{YYMMDD}.log
    格式：%(asctime)s - %(name)s - %(levelname)s - %(message)s
    编码：UTF-8
    模式：追加写入（filemode='a'）
    记录内容包括：配置初始化状态、请求头设置、Cookie 处理、网页状态码、文件保存结果等



使用流程简述

text

1. 启动程序 → 显示 Get-Robot ASCII 横幅
2. 选择是否使用内置请求头（y/n）
3. 输入 Cookie（可跳过）
4. 输入防盗链 Referer（可跳过）
5. 选择爬取内容类型（文本/图片/音频/视频）
6. 输入目标 URL
7. 选择是否启用 Tor 代理
8. 选择文件保存目录
9. 输入保存文件名
10. 程序执行爬取并保存文件



