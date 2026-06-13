from art import text2art
from tkinter import filedialog
import os
import re
import base64
import logging
import json
import sys
import pandas as pd
import tkinter as tk
from User import log

""""此脚本是以jkw为设计的"""
print("欢迎使用数据清洗")

text='DataCleaning'
art=text2art(text)
print(art)

logger=log()
root=tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
logger.info("DataCleaning启动成功")

current_file=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.dirname(current_file)
logger.info("文件上级启动完成")

try:
    file_path=filedialog.askopenfilename(
        parent=None,
        title="选择文件",
        initialdir="",
        filetypes=[
            ("数据文件", "*.json;*.html;*.txt;*.csv")
        ]
    )
    if not file_path:
        logger.info("用户取消文件选择")
        logger.info("程序将自己退出")
        exit()
except PermissionError:
    print("该程序无法打开这个文件可能没权限")
    logger.info("没权限打开这个文件")
    exit()
class TxtFile:
    def __init__(self,file_path):
        self.file_path=file_path
        self.file=""
        self.mylist=[]

    def read_file(self):
        with open(file_path,"r",encoding="utf-8") as f:
            self.content = f.read()  # 读取内容并保存
            print(self.content[:500])  # 打印内容
        return self.content

    def Detectfile(self):
        if '!DOCTYPE html' in self.content:
            print("该文件包含\'<!DOCTYPE html>\',以被判定为html文件")
            logger.info("txt文件改为html文件")
            dir_name = os.path.dirname(file_path)  # 目录
            base_name = os.path.basename(file_path)  # 带后缀的文件名
            name_without_ext = os.path.splitext(base_name)[0]#除去带后缀的文件名
            new_file_name = name_without_ext + '.html'#改为html文件名
            new_path = os.path.join(dir_name, new_file_name)#合成新路径
            os.rename(file_path, new_path)
            print(f"已修改: {file_path} -> {new_path}")
            logger.info(f"已将{file_path}改为{new_path}")
            return new_path

# 创建对象
txt = TxtFile(f"{file_path}")

# 读取文件
content = txt.read_file()  # 会打印内容，并返回内容
content_1 = txt.Detectfile()