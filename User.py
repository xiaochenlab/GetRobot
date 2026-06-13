import random
import time
import logging

logger = logging.getLogger(__name__)
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
        },
        "2": {
            "content_type": "image/jpeg, image/png, image/gif, image/webp",
            "extension": "png",
            "mode": "wb"
        },
        "3": {
            "content_type": "audio/mpeg, audio/wav, audio/ogg",
            "extension": "mp3",
            "mode": "wb"
        },
        "4": {
            "content_type": "video/mp4, video/webm, video/quicktime",
            "extension": "mp4",
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
