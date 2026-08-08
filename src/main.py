import os
import time
import tkinter as tk
from tkinter import filedialog
from user_config import file_type, extension, Ask_Need, log, Url, get_user_agent, CookieType, Referer
from spider import *
import logging
from user_config import log



def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口，只弹选择框
    root.attributes('-topmost', True)
    logger.info("选择窗口初始化成功")

    current_file = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_file)
    logger.info("文件目录上级初始成功")

    user_from = {
        "User-Agent": UA,
        "Referer": Fistweb,
        "Accept": accept_value,
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    def millisecond():
        return time.strftime("[%H:%M:%S]", time.localtime())

# 让用户选择保存目录
    save_dir = filedialog.askdirectory(
        parent=None,
        title="选择保存目录取消使用工具默认目录",
        initialdir=""
    )

    # 如果用户取消，使用默认目录
    if not save_dir:
        save_dir = f"{parent_dir}/Downloads"
    os.makedirs(save_dir, exist_ok=True)
    logger.info(f"保存地址:{save_dir}")

# 测试输出
    sys.stdout.write(f"已选择目录：{save_dir}\n")

    try:
        logger.info("爬虫已创建")
        #创建爬虫对象
        spider = get_robots(url, cookies, user_from)
        logger.info("创建爬虫对象完成")

        # 执行请求，获取状态码
        status_code = spider.robots()
        logger.info(f"获取状态码完成，状态码为:{status_code}")
        # 获取响应对象
        test = spider.response
        logger.info("获取响应对象成功")

        if Ask_Need =='1':
            is_binary = False
            file=extension
        elif Ask_Need =='2':
            is_binary = True
            file=extension
        elif Ask_Need =='3':
            is_binary = True
            file=extension
        elif Ask_Need =='4':
            is_binary = True
            file=extension
        else:
            file_new=input("未找到文件件类型请你输入: ")
            file=file_new
            is_binary = True
        name_file=input(r"你想保存的文件名 :")#保存爬取文件
        save_path = os.path.join(save_dir, f"{name_file}.{file}")
        logger.info("文件设置完成")
        if is_binary:
            with open(save_path, "wb") as f:
                f.write(test.content)
                sys.stdout.write(millisecond() + r'保存完成: ' + str(test.status_code)+"\n")
                logger.info("文件保存完成:wb模式")
                logger.info(f"文件路径:{save_path}")
        else:
            with open(save_path, "w",encoding="utf-8") as f:
                f.write(test.text)
                sys.stdout.write(millisecond() + r'保存完成: ' + str(test.status_code)+"\n")
                logger.info("文件保存完成:w模式")
                logger.info(f"文件路径:{save_path}")
    except Exception as e:
        sys.stdout.write(e)
        logger.info("文件保存失败")
        exit()

if __name__=="__main__":
    sys.stdout.write("开始执行ing\n")
    logger = log()
    url=Url()
    UA = get_user_agent()
    Fistweb = Referer()
    cookies = CookieType()
    Ask_Need, accept_value, extension, mode = file_type()
    main()
