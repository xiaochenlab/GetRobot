import requests
import random
import time
from art import text2art
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from User import CookieType, fistWebf, User_4, User_5, User_3, User_6, TOR


"""
——————————————————————————————————
get 代码重构：修复 requests 参数传递、增加超时与重试、改进异常处理
2026-07-31
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

text = 'Get-Robot'
art = text2art(text)
print(art)

# 获取用户配置
user_3 = User_3()  # User-Agent
cookies = CookieType()
Fistweb = fistWebf()
Ask_Need, accept_value, extension, mode = User_4()
user_url = User_5()
# 检查 tor 状态（User_6 会设置全局 TOR）
User_6()

logger.info("之前的配置初始化成功")

user_from = {
    "User-Agent": user_3,
    "Referer": Fistweb,  # where are you from
    "Accept": accept_value,  # accept header
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
logger.info(f"user_from初始化成功:{user_from}")


class get_robots:
    def __init__(self, web_name, cookies=None, user_from=None, proxies=None, timeout=15, max_retries=3):
        self.web_name = web_name
        self.cookies = cookies
        self.user_from = user_from or {}
        self.response = None
        self.timeout = timeout

        # 设置 proxies（支持 tor socks5）
        if TOR == 'y':
            self.proxies = proxies or {
                'http': 'socks5h://127.0.0.1:9150',
                'https': 'socks5h://127.0.0.1:9150'
            }
            logger.info("tor 浏览器代理已设置")
        else:
            self.proxies = proxies
            logger.info("未使用代理")

        # 配置会话与重试策略
        self.session = requests.Session()
        retries = Retry(total=max_retries, backoff_factor=0.5,
                        status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET", "POST"])
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def robots(self):
        logger.info("爬虫启动: %s" % self.web_name)
        try:
            time.sleep(random.uniform(1, 3))
            # 使用关键字参数调用 requests
            self.response = self.session.get(
                self.web_name,
                headers=self.user_from,
                cookies=self.cookies,
                proxies=self.proxies,
                timeout=self.timeout,
                allow_redirects=False
            )
            print(self.response.text[:500])
            logger.info(f"网页状态码:{self.response.status_code}")
            return self.response.status_code
        except requests.exceptions.RequestException as e:
            logger.warning("请求出现异常，尝试重定向并允许重定向: %s" % e)
            try:
                time.sleep(random.uniform(1, 3))
                self.response = self.session.get(
                    self.web_name,
                    headers=self.user_from,
                    cookies=self.cookies,
                    proxies=self.proxies,
                    timeout=self.timeout,
                    allow_redirects=True
                )
                print(self.response.text[:500])
                logger.info(f"网页状态码:{self.response.status_code}")
                return self.response.status_code
            except requests.exceptions.RequestException as e2:
                logger.exception("重试也失败: %s" % e2)
                raise

    def get_response(self):
        """获取 Response 对象"""
        if not self.response:
            self.robots()
        logger.info("网页执行完毕")
        return self.response

    @staticmethod
    def summarize_status(code):
        if code == 200:
            logger.info("网页状态码:200")
            return "网站请求成功"
        elif 200 < code <= 300:
            logger.info("网站未处理请求")
            return "网站未处理请求"
        elif 300 < code <= 400:
            logger.info("网站地址移动到新地方,程序已自动处理重定向")
            return "网站地址移动到新地方,程序已自动处理重定向"
        elif code >= 400:
            logger.info("失败")
            return "失败"


# 如果作为脚本直接运行，提供一个简单的调用示例
if __name__ == '__main__':
    spider = get_robots(user_url, cookies=cookies, user_from=user_from)
    status = spider.robots()
    resp = spider.get_response()
    print(get_robots.summarize_status(status))
