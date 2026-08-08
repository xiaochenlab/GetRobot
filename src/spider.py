import requests
import random
import time
import os
import sys
from art import text2art
import logging
from user_config import *

"""
——————————————————————————————————
get代码重构，2025年4月24 19点50分开始，
以处理高并发，输出专业为主
——————————————————————————————————
"""


if sys.platform=='win32':
    os.system("cls")
else:
    os.system("clear")

text='Get-Robot'
art=text2art(text)
sys.stdout.write(art)

logger=log()
logger.info("日志准备完毕可以写入log文件")


logger.info("在User库里函数加载完成")
logger.info("之前的配置初始化成功")


logger.info(f"user_from初始化成功:{user_from}")

class get_robots:
    logger.info("get_robots定义成功")
    def __init__(self,web_name,cookies,user_from,use_tor='n'):
        self.web_name=web_name
        self.cookies=cookies
        self.user_from=user_from
        self.response = None
        if TOR =='y':
            self.proxies = {
                'http': 'socks5h://127.0.0.1:9150',
                'https': 'socks5h://127.0.0.1:9150'
            }
            logger.info("tor浏览器初始成功")
        else:
            self.proxies = None
            logger.info("tor浏览器未开启或初始化失败")

    def robots(self):
        logger.info("爬虫启动")
        try:
            time.sleep(random.randint(1,5))
            self.response  = requests.get(self.web_name, proxies=self.proxies,headers=self.user_from,cookies=self.cookies,timeout=(10,45))
            #print(self.response.status_code)#测试用
            self.response.encoding='utf-8'      
            sys.stdout.write(self.response.text[:500]+"\n")
            logger.info(f"网页状态码:{self.response.status_code}")
            return self.response.text
        except requests.exceptions.RequestException as e:
            logger.error("爬虫启动重定向")
            print("网页有一定的反爬措施程序将启动重定向")
            time.sleep(random.randint(1, 5))
            self.response  = requests.get(self.web_name, proxies=self.proxies,headers=self.user_from,cookies=self.cookies, timeout=(10,45),allow_redirects=True)
            #print(self.response.status_code)#测试用
            self.response.encoding = 'utf-8'
            print(self.response.text[:500])
            logger.info(f"网页状态码:{self.response.status_code}")
            return self.response.text
        

    def get_response(self):
        """获取 Response 对象"""
        self.robots()  # 先执行请求
        logger.info("网页执行完毕")
        return self.response.text

    def get_robots(self,robots):
        if robots == 200:
            logger.info("网页状态码:200")
            return r"网站请求成功"
        elif 200 < robots <= 300:
            logger.info("网站未处理请求")
            return r"网站未处理请求"
        elif 300 < robots <= 400:
            logger.info("网站地址移动到新地方,程序已自动处理重定向")
            return r"网站地址移动到新地方,程序已自动处理重定向"
        elif robots > 400:
            logger.info("失败")
            return r"失败"

if __name__ =='__main__':
    text='Get-Robot'
    art=text2art(text)
    sys.stdout.write(art)
    UA=get_user_agent()
    cookies = CookieType()
    Fistweb=Referer()
    Ask_Need, accept_value, extension, mode = file_type()#调用 User.py 模块中定义的 type() 函数
    User = accept_value
    TOR = tor_edge()