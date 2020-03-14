#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''此脚本是用来从维基辞典页面提取电码对应表，并保存为json文件的。
   根目录里的 data.json 即为此脚本生成的。

   作者：欧剃（@游荡的坎德人）
'''
#----------------------

# 因为众所周知的网络原因，我把 html 直接保存下来，才用脚本解析
# 文件内容来自 https://zh.wiktionary.org/wiki/附录:中文电码/中国大陆1983
localFileName = '中文电码1983.html'
# 另存为 “仅HTML”以后，将文件名填在上面

#----------------------

from bs4 import BeautifulSoup
import json

try:
    file = open(localFileName,'r',encoding='utf-8')
except:
    print("读取待解析的 HTML 文件失败！")
    print("请先访问 https://zh.wiktionary.org/wiki/附录:中文电码/中国大陆1983，")
    print("另存为 “仅HTML”以后，将文件名改成“中文电码1983.html”，再运行此脚本。")
    a = input("<已停止，请按任意键退出>")
    quit()


htmlhandle = file.read()

soup = BeautifulSoup(htmlhandle,'lxml')

data = {}

# 对应表每个单元格 <td> 里是一个电码对
result = soup.find_all('td')

for item in result:
    text = item.get_text().strip() #行末居然有 "\n" ?
    if len(text) ==4:
        data[text] = "☒" # 无此字占位符
    else:
        data[text[:4]]=text[-1] # 最后一位是全角字符

# TODO: 这里其实有个 bug，原文中 9992 9993 9994 9995 有意义，
#       但找不到对应的字符，所以我手动修改了一下 data.json。

data["9932"] = " "  # 半角空格
data["9992"]= "〚"  # 起始着重号
data["9993"]= "〛"  # 末尾着重号)
data["9994"]= "「"  # 起始专名号
data["9995"]= "」"  # 末尾专名号

with open('data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)

file.close()