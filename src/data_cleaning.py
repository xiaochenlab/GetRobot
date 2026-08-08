from art import text2art
from tkinter import filedialog
from bs4 import BeautifulSoup
import os
import re
import base64
import logging
import json
import sys
import pandas as pd
import tkinter as tk
from user_config import log

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

with open(f'{file_path}','r',encoding='utf-8') as f:
    test=f.read().strip()
    logger.info("文件读取成功")
    #print(test)

# class 版本 — 状态自然共享，不用反复传参
new_path=None
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dir_name = os.path.dirname(file_path)
        self.base_name = os.path.basename(file_path)
        self.name_without_ext = os.path.splitext(self.base_name)[0]
        self.current_ext = os.path.splitext(self.base_name)[1]

    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read().strip()

    def detect_type(self):
        if self.content and self.content[0] in ('{', '['):
            try:
                json.loads(self.content)
                return '.json'
            except json.JSONDecodeError:
                pass
        if '!DOCTYPE html' in self.content:
            return '.html'
        return '.txt'

    def rename_if_needed(self, target_ext):
        if self.current_ext == target_ext:
            return self.file_path
        new_path = os.path.join(self.dir_name, self.name_without_ext + target_ext)
        os.rename(self.file_path, new_path)
        self.file_path = new_path
        self.current_ext = target_ext
        return new_path

    def process(self):
        self.read()
        ext = self.detect_type()
        return self.rename_if_needed(ext)

def html_clean(content):
    """处理HTML文件：让用户选择要提取的标签，提取文本后保存为txt"""
    soup = BeautifulSoup(content, 'html.parser')

    print("\n===== HTML 文本提取 =====")
    print("常用标签: p, div, span, h1-h6, a, li, td, th, article, section")
    print("留空则提取所有 <p> 标签文本")
    print("========================\n")

    tag_input = input("请输入要提取的标签 (多个用逗号分隔, 如 p,h1,h2): ").strip()
    if not tag_input:
        tag_input = "p"
    tags = [t.strip() for t in tag_input.split(",") if t.strip()]

    class_input = input("请输入class筛选值 (留空不筛选): ").strip()
    id_input = input("请输入id筛选值 (留空不筛选): ").strip()

    print("\n提取选项:")
    print("  1. 仅纯文本 (去重)")
    print("  2. 纯文本 (不去重)")
    print("  3. 带标签名标记的文本")
    choice = input("请选择 [1/2/3] (默认1): ").strip() or "1"

    texts = []
    seen = set()
    for tag in tags:
        kwargs = {}
        if class_input:
            kwargs['class_'] = class_input
        if id_input:
            kwargs['id'] = id_input
        elements = soup.find_all(tag, **kwargs) if kwargs else soup.find_all(tag)

        for el in elements:
            text = el.get_text(separator="\n", strip=True)
            if not text:
                continue
            if choice == "1":
                if text not in seen:
                    seen.add(text)
                    texts.append(text)
            elif choice == "3":
                prefix = f"[{tag}]"
                line = f"{prefix} {text}"
                if line not in seen:
                    seen.add(line)
                    texts.append(line)
            else:
                texts.append(text)

    if not texts:
        print("\n未提取到任何文本内容。")
        return None

    result = "\n\n".join(texts)
    print(f"\n共提取到 {len(texts)} 段文本，总长度 {len(result)} 字符。")

    preview = input("是否预览前500字符? (y/n, 默认y): ").strip().lower()
    if preview != "n":
        print("\n--- 预览 ---")
        print(result[:500])
        if len(result) > 500:
            print("...(已截断)")
        print("--- 预览结束 ---\n")

    save = input("是否保存为txt文件? (y/n, 默认y): ").strip().lower()
    if save == "n":
        return result

    # 保存路径：同目录下，文件名加 _extracted.txt
    base = os.path.splitext(file_path)[0]
    txt_path = base + "_extracted.txt"

    # 如果已存在则覆盖确认
    if os.path.exists(txt_path):
        overwrite = input(f"文件已存在: {txt_path}，是否覆盖? (y/n): ").strip().lower()
        if overwrite != "y":
            txt_path = base + "_extracted_new.txt"

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"\n已保存到: {txt_path}")
    logger.info(f"HTML文本提取完成，保存到: {txt_path}")
    return result

fp = FileProcessor(file_path)
exam = fp.process()

# 如果是html文件，启动标签提取流程
if exam and os.path.splitext(exam)[1].lower() == '.html':
    html_clean(test)
else:
    print(f"文件已处理: {exam}")