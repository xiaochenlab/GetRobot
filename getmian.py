import os
import time
import tkinter as tk
from tkinter import filedialog
from User import User_4,extension,Ask_Need
from Get import *
import logging

logger = logging.getLogger(__name__)
root = tk.Tk()
root.withdraw()  # 隐藏主窗口，只弹选择框





def millisecond():#输出时间
    logger.info("时间初始化成功")
    return time.strftime("[%H:%M:%S]", time.localtime(time.time()))



# 让用户选择保存目录
save_dir = filedialog.askdirectory(
    parent=None,
    title="选择保存目录",
    initialdir="F:\\"
)

# 如果用户取消，使用默认目录
if not save_dir:
    save_dir = r"F:\pythonwj\新建文件夹"
os.makedirs(save_dir, exist_ok=True)

# 测试输出
print("已选择目录：", save_dir)

file_type=None
try:
    #创建爬虫对象
    spider = get_robots(user_5, cookies, user_from)

    # 执行请求，获取状态码
    status_code = spider.robots()

    # 获取响应对象
    test = spider.response

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
    else:
        with open(save_path, "w",encoding="utf-8") as f:
            f.write(test.text)
            print(millisecond() + r'保存完成: ' + str(test.status_code))
            logger.info("文件保存完成:w模式")
except Exception as e:
    print(e)
    logger.info("文件保存失败")
    exit()