import random
import time
import logging

logger = logging.getLogger(__name__)
<<<<<<< HEAD
TOR=None
cookies = None
content_type=None
extension=None
Ask_Need=None
user_from = {}

def User_1():
    user_agents=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    ]
    logging.info("user_agents选择完毕")
    return random.choice(user_agents)#在这里就把请求头选好


def User_2():
    add_user = input("请输入你的请求头:").strip()
    logger.info("add_user处理完毕")
    return add_user

def CookieType():
    cookie_input = input(r"请输入cookie(直接回车跳过): ").strip()
    if not cookie_input:  # 用户直接回车
        logger.info("cookie处理完毕当前状态:NONE")
        return None
    try:
        # 解析 name=value; name2=value2 格式
        cookies = {}  # 创建一个字典
        for item in cookie_input.split(';'):  # 在每个;去除
            if '=' in item:
                key, value = item.strip().split('=', 1)  # 在第一个等号去除=分割完就是键值对
                cookies[key.strip()] = value.strip()  # 字典的用法配对一个键值对
                logger.info(f"cookie处理完毕当前状态:{cookies}")
        return cookies
    except Exception as e:
        logger.info("无可处理的cookie")
        return None

def fistWebf():
    while True:
        web_frist=input("爬取网站的防盗链 :")
        if 'http' in web_frist:
            logger.info("web_frist处理完毕")
            return web_frist
        else:
            print("网站中没有找到该防盗链(没有将在5秒后自动返回返回) :")
            time.sleep(5)
            logger.info("网站缺少/不存在/不需要防盗链")
            return None

def User_3():
    user_ask=input("是否使用工具自带的请求头(y/n)")
    if user_ask == "y":
        user_1=User_1()
        logger.info("系统自带请求头完毕")
        return user_1
    else:
        user_2 = User_2()
        logger.info("自定义请求头处理完毕")
        return user_2

def User_4():
    global content_type, extension, mode, Ask_Need
    NEED={"1":"文本",
          "2":"图片",
          "3":"音频",
          "4":"视频"}
    for key, value in NEED.items():
        print(f"{key}.{value}")
    Ask_Need=input("你想要什么类型的: ").strip()
    accept_headers = {
        "1": {
        "content_type": "application/json, text/html, text/plain",
        "extension": "html",
        "mode": "w"
=======

# 保留模块级变量以兼容现有导入
TOR = None
cookies = None
content_type = None
extension = None
Ask_Need = None
user_from = {}


def User_1():
    """返回一个随机选择的 User-Agent（兼容旧名称）。"""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    ]
    ua = random.choice(user_agents)
    logger.info("User_1: selected user agent")
    return ua


def User_2():
    """让用户自定义 User-Agent（兼容旧名称）。如果用户输入为空，返回 None。"""
    try:
        add_user = input("请输入你的请求头:").strip()
    except Exception:
        add_user = ""
    logger.info("User_2: custom user agent processed")
    return add_user or None


def CookieType():
    """解析用户输入的 cookie（格式: name=value; name2=value2），返回 dict 或 None。
    兼容旧函数名。
    """
    try:
        cookie_input = input(r"请输入cookie(直接回车跳过): ").strip()
    except Exception:
        cookie_input = ""

    if not cookie_input:
        logger.info("CookieType: no cookie provided")
        return None

    cookies = {}
    for item in cookie_input.split(';'):
        item = item.strip()
        if not item:
            continue
        if '=' in item:
            key, value = item.split('=', 1)
            cookies[key.strip()] = value.strip()
    if cookies:
        logger.info(f"CookieType: parsed cookies: {cookies}")
        return cookies
    else:
        logger.info("CookieType: cookie string could not be parsed into pairs")
        return None


def fistWebf():
    """请求用户输入 Referer（防盗链）。如果输入不包含 http 返回 None（兼容旧名称）。"""
    try:
        web_frist = input("爬取网站的防盗链 :").strip()
    except Exception:
        web_frist = ""

    if web_frist and (web_frist.startswith('http://') or web_frist.startswith('https://')):
        logger.info("fistWebf: valid referer provided")
        return web_frist
    else:
        if web_frist:
            print("网站中没有找到该防盗链 (需要以 http/https 开头), 将返回 None")
        else:
            print("未输入防盗链, 将返回 None")
        logger.info("fistWebf: no valid referer")
        time.sleep(1)
        return None


def User_3():
    """选择使用工具自带请求头或自定义请求头（兼容旧名称）。"""
    try:
        user_ask = input("是否使用工具自带的请求头(y/n): ").strip().lower()
    except Exception:
        user_ask = 'y'

    if user_ask == 'y' or user_ask == '':
        ua = User_1()
        logger.info("User_3: using built-in user agent")
        return ua
    else:
        ua = User_2()
        logger.info("User_3: using custom user agent")
        return ua


def User_4():
    """选择要爬取的内容类型并返回 (Ask_Need, content_type, extension, mode)。
    同时更新模块级变量以兼容其他模块导入。
    """
    global content_type, extension, Ask_Need

    NEED = {"1": "文本", "2": "图片", "3": "音频", "4": "视频"}
    for key, value in NEED.items():
        print(f"{key}.{value}")

    try:
        Ask_Need = input("你想要什么类型的: ").strip()
    except Exception:
        Ask_Need = '1'

    accept_headers = {
        "1": {
            "content_type": "application/json, text/html, text/plain",
            "extension": "html",
            "mode": "w",
            "is_binary": False,
>>>>>>> 00accd865a560748080ebb01cec62df098f58239
        },
        "2": {
            "content_type": "image/jpeg, image/png, image/gif, image/webp",
            "extension": "png",
<<<<<<< HEAD
            "mode": "wb"
=======
            "mode": "wb",
            "is_binary": True,
>>>>>>> 00accd865a560748080ebb01cec62df098f58239
        },
        "3": {
            "content_type": "audio/mpeg, audio/wav, audio/ogg",
            "extension": "mp3",
<<<<<<< HEAD
            "mode": "wb"
=======
            "mode": "wb",
            "is_binary": True,
>>>>>>> 00accd865a560748080ebb01cec62df098f58239
        },
        "4": {
            "content_type": "video/mp4, video/webm, video/quicktime",
            "extension": "mp4",
<<<<<<< HEAD
            "mode": "wb"
        }
    }
    logger.info("选择爬取内容预处理完毕")

# 使用方式
    if Ask_Need in accept_headers:
        info = accept_headers[Ask_Need]
        content_type = info["content_type"]#######
        extension = info["extension"]#####
        mode = info["mode"]
        logger.info("选择爬取内容处理完毕")
        return Ask_Need, content_type, extension, mode

def User_5():
    while True:
        url = input("输入爬取的网站: ")
        if "http" in url:
            logger.info("输入的爬取网站处理完毕")
            break
        else:
            print("没有找到爬取的网站可能不存在")
            logger.info("处理完毕，但当前网站可能不对")
    return url

def User_6():
    print("使用须知"
          "1.在使用前请确保有tor浏览器如果没有请访问\"https://torproject.netcologne.de/zh-CN/download/tor/\""
          "2.确保tor浏览器在运行")
    TOR=input("tor是否在运行(Y/N)").strip().lower()
    if TOR == "y":
        logger.info("tor浏览器以开启")
        return TOR
    else:
        print("tor浏览器未开启")
        logger.info("tor浏览器未开启")
        return None
=======
            "mode": "wb",
            "is_binary": True,
        },
    }

    info = accept_headers.get(Ask_Need)
    if info:
        content_type = info['content_type']
        extension = info['extension']
        mode = info['mode']
        logger.info(f"User_4: selected {Ask_Need}, extension={extension}")
        return Ask_Need, content_type, extension, mode
    else:
        # 回退处理：让用户输入扩展名
        try:
            ext = input("未找到文件类型请你输入(例如 png/jpg/mp3): ").strip()
        except Exception:
            ext = 'dat'
        extension = ext or 'dat'
        content_type = '*/*'
        mode = 'wb'
        logger.info("User_4: fallback selection used")
        return Ask_Need, content_type, extension, mode


def User_5():
    """获取要爬取的 URL，确保包含 http/https（兼容旧名称）。"""
    while True:
        try:
            url = input("输入爬取的网站: ").strip()
        except Exception:
            url = ''

        if url and (url.startswith('http://') or url.startswith('https://')):
            logger.info("User_5: valid url provided")
            return url
        else:
            print("没有找到爬取的网站可能不存在或请输入正确的 URL (以 http/https 开头)")
            logger.info("User_5: invalid url input")


def User_6():
    """询问 tor 是否运行（兼容旧名称），并更新模块级 TOR 变量。
    返回 'y' 或 None 保持与原有逻辑兼容。
    """
    global TOR
    print("使用须知:\n1. 在使用前请确保有 tor 浏览器。如果没有请访问 https://torproject.org 下载。\n2. 确保 tor 浏览器在运行")
    try:
        ans = input("tor是否在运行(Y/N): ").strip().lower()
    except Exception:
        ans = 'n'

    if ans == 'y':
        TOR = 'y'
        logger.info("User_6: tor enabled")
        return TOR
    else:
        TOR = None
        logger.info("User_6: tor not enabled")
        return None

>>>>>>> 00accd865a560748080ebb01cec62df098f58239
