import os
import time
import tkinter as tk
from tkinter import filedialog
from User import type,extension,Ask_Need,log
from Get import *
import logging
from User import log

logger = log()
root = tk.Tk()
root.withdraw()  # 隐藏主窗口，只弹选择框
root.attributes('-topmost', True)
logger.info("选择窗口初始化成功")

current_file = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_file)
logger.info("文件目录上级初始成功")



def millisecond():#输出时间
    logger.info("时间初始化成功")
    return time.strftime("[%H:%M:%S]", time.localtime(time.time()))



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
print("已选择目录：", save_dir)

file_type=None
try:
    logger.info("爬虫已创建")
    #创建爬虫对象
    spider = get_robots(user_5, cookies, user_from)
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
            print(millisecond() + r'保存完成: ' + str(test.status_code))
            logger.info("文件保存完成:wb模式")
            logger.info(f"文件路径:{save_path}")
    else:
        with open(save_path, "w",encoding="utf-8") as f:
            f.write(test.text)
            print(millisecond() + r'保存完成: ' + str(test.status_code))
            logger.info("文件保存完成:w模式")
            logger.info(f"文件路径:{save_path}")
except Exception as e:
    print(e)
    logger.info("文件保存失败")
    exit()