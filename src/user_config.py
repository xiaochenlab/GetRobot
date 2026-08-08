import random
import time
import logging
import os
import sys
import json

logger = logging.getLogger(__name__)

_log_configured = False
user_from = {}

def get_user_agent():
    get_user_agent_choice=[
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            ]

    user_agent_choice = input("是否使用工具自带的请求头(y/n): ").strip().lower()
    if user_agent_choice =='y':  
        user_agent =random.choice(get_user_agent_choice)
        sys.stdout.write(f"使用的请求头是:{user_agent}\n")
        logger.info(f"使用系统自带请求头:{user_agent}")
        return user_agent
    
    elif user_agent_choice == 'n':
        while True:

            get_user_agent_choice_need = input("请输入你的请求头:").strip()
            if 'Windows NT' in get_user_agent_choice_need or 'Macintosh' in get_user_agent_choice_need or 'Linux' in get_user_agent_choice_need:
                user_agent = get_user_agent_choice_need
                sys.stdout.write(f"使用的请求头是:{user_agent}\n")
                logger.info(f"使用自定义请求头:{user_agent}")
                return user_agent
            
            elif get_user_agent_choice_need.lower() == "q":
                sys.stdout.write("用户取消自定义请求头，使用默认值\n")
                logger.info("用户取消自定义请求头，使用默认值")
                agent = random.choice(get_user_agent_choice)
                sys.stdout.write(f"使用的请求头是:{agent}\n")
                logger.info(f"使用系统自带请求头:{agent}")
                user_agent = agent
                return user_agent
            
            else:
                sys.stdout.write("请求头可能不对\n")

def CookieType():#原 CookieType
    cookie_input = input(r"请输入cookie(直接回车跳过): ").strip()
    if not cookie_input:  # 用户直接回车
        sys.stdout.write("未输入cookie,使用默认值\n")
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
        sys.stdout.write(f"cookie解析错误: {e}\n")
        logger.info("无可处理的cookie")
        sys.stdout.write("使用默认cookie\n")
        cookies = None
        return cookies

def Referer():#原Referer
    while True:
        web_frist=input("爬取网站的防盗链 :")
        if 'http' in web_frist:
            logger.info("web_frist处理完毕")
            logger.info(f"防盗链是:{web_frist}")
            return web_frist
        else:
            sys.stdout.write("网站中没有找到该防盗链(没有将在5秒后自动返回返回) :")
            time.sleep(5)
            logger.info("网站缺少/不存在/不需要防盗链")
            web_frist = None
            return web_frist



def file_type():#原type
    logger.info("启动爬取文件类型")
    NEED={"1":"文本",
          "2":"图片",
          "3":"音频",
          "4":"视频"}
    for key, value in NEED.items():
        print(f"{key}.{value}")
        logger.info("预加载文件类型成功")
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
        logger.info("content_type加载完毕")
        logger.info(f"content_type:{content_type}")
        extension = info["extension"]#####
        logger.info(f"extension:{extension}")
        logger.info("extension加载完毕")
        mode = info["mode"]
        logger.info("mode加载完毕")
        logger.info("选择爬取内容处理完毕")
        return Ask_Need, content_type, extension, mode

def Url():#原Url
    logger.info("在Url函数加载完成爬取网站")
    while True:
        url = input("输入爬取的网站: ").strip()
        if "http" in url:
            logger.info(f"输入的爬取网站处理完毕:{url}")
            break
        else:
            print("没有找到爬取的网站可能不存在")
            logger.info("处理完毕，但当前网站可能不对")
    return url

TOR=None
def tor_edge():#原tor_edge
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

def log():#原log
    global _log_configured
    if not _log_configured:
        current_file = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_file)

        ymd = time.strftime('%y%m%d', time.localtime())

        log_dir = f"{parent_dir}/logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, f'{ymd}.log')

        logging.basicConfig(level=logging.INFO,
                            filename=log_file,
                            filemode='a',
                            format='%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s',
                            encoding='utf-8'
                            )

    logger = logging.getLogger(__name__)

    logger.info("日志记录初始化成功")
    _log_configured = True
    return logger


if __name__ =='__main__':
    sys.stdout.write("这不是脚本\n")
    pass