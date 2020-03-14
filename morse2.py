#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''在原有 morse.py 的基础上进行修改，取消了用 UTF-8 编码处理中文字符的做法。
   现在使用1983年《标准电码本》中的汉字对应表进行编码。
   数字转换成摩尔斯码的函数来自 morse.py 使用的是长码。

   作者：欧剃（@游荡的坎德人）
'''

import json
import sys

try:
    import morse
    import ita2
except:
    print("读取模块失败！请将所有脚本放在同个文件夹里。")
    a = input("<已停止，请按任意键退出>")
    quit()

try:
    with open('data.json' , 'r') as fp:
        decode_table = json.load(fp)
except:
    print("读取电码本文件 data.json 失败！请先运行 scraper.py 生成电码本。")
    a = input("<已停止，请按任意键退出>")
    quit()


# ------- --------- --------
# 在这里修改你想要的编码方案，默认 morse，可选 ita2

transcript_method = ita2 # morse

# ------- --------- --------

encode_table =  dict((y,x) for x,y in decode_table.items())

for i in range(26):
    # A a => 9874 兼容半角英文字母
    encode_table[chr(65+i)] = str(9874+i)
    encode_table[chr(97+i)] = str(9874+i)

for i in range(10):
    # 0 => 9960 兼容半角数字
    encode_table[str(i)] = str(9960+i)

if __name__ == '__main__':
    if not sys.argv[1:]:
        try:
            a= raw_input("请输入汉字电码或中文字符：")
        except:        
            a = input("请输入汉字电码或中文字符：")
        if a:
            intext = a.upper()
        else:
            print('[错误] 请输入汉字电码或中文字符。')
    else:
        intext = ' '.join(sys.argv[1:]).upper()

    if all([i in '-. 01' for i in intext]):
        temptext = transcript_method.decode(intext)
        print("EN: ",temptext)

        temptext = temptext.replace(" ","")

        if temptext.isalnum():
            # 每隔 4 个字符分割一下
            splited = [temptext[i*4:i*4+4] for i in range(len(temptext)// 4)]
            try:
                outtext = [decode_table[i] for i in splited]
                print("CN: ",''.join(outtext))
            except:
                # 查不到？忽略忽略
                pass
    else:
        if all([i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for i in intext]):
            print("EN: ",morse.encode(intext))
        elif all([i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -@$!&#\'()"/:;?,.' for i in intext]):
            print("EN: ",ita2.encode(intext))
        else:
            temptext = ''.join([encode_table[i] for i in intext])

            print("CN: ",transcript_method.encode(temptext))
