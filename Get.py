import requests
import random
import time
from art import text2art
import logging
from User import CookieType,fistWebf,User_4,User_5,User_3,content_type,User_6,TOR


"""
——————————————————————————————————
get代码重构，2025年4月24 19点50分开始，
以处理高并发，输出专业为主
——————————————————————————————————
"""


logging.basicConfig(level=logging.INFO,
                    filename='get.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    encoding='utf-8'
                    )

logger = logging.getLogger(__name__)

print("="*50)

text='Get-Robot'
art=text2art(text)
print(art)

user_3=User_3()
cookies = CookieType()
Fistweb=fistWebf()
Ask_Need, accept_value, extension, mode = User_4()
User = accept_value
user_5=User_5()
logger.info("之前的配置初始化成功")

user_from = {
    "User-Agent": user_3,
    "Referer": Fistweb,  # where are your from
    "Accept": User,  # 只返回视频
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
logger.info(f"user_from初始化成功:{user_from}")

class get_robots:
    def __init__(self,web_name,cookies,user_from):
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
            self.response  = requests.get(self.web_name, self.proxies,headers=self.user_from,cookies=self.cookies)
            #print(self.response.status_code)#测试用
            print(self.response.text[:500])
            logger.info(f"网页状态码:{self.response.status_code}")
            return self.response .status_code
        except:
            logging.info("爬虫启动重定向")
            print("网页有一定的反爬措施程序将启动重定向")
            time.sleep(random.randint(1, 5))
            self.response  = requests.get(self.web_name, self.proxies,headers=self.user_from,cookies=self.cookies, allow_redirects=True)
            #print(self.response.status_code)#测试用
            print(self.response.text[:500])
            logger.info(f"网页状态码:{self.response.status_code}")
            return self.response.status_code

    def get_response(self):
        """获取 Response 对象"""
        self.robots()  # 先执行请求
        logger.info("网页执行完毕")
        return self.response

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
