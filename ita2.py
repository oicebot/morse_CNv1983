#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''此脚本是用来解析传入的 ITA2 标准电码 (大端序），将其转换成英文字符。
   
   作者：欧剃（@游荡的坎德人）
'''

import sys

decode_ls = {
    '00000': "",   '00100': " ",
    '10111': "Q",    '10011': "W",
    '00001': "E",    '01010': "R",
    '10000': "T",    '10101': "Y",
    '00111': "U",    '00110': "I",
    '11000': "O",    '10110': "P",
    '00011': "A",    '00101': "S",
    '01001': "D",    '01101': "F",
    '11010': "G",    '10100': "H",
    '01011': "J",    '01111': "K",
    '10010': "L",    '10001': "Z",
    '11101': "X",    '01110': "C",
    '11110': "V",    '11001': "B",
    '01100': "N",    '11100': "M",
    '01000': "\r",   '00010': "\n",
    '11011': False,   '11111': True,
}

encode_ls = dict((y,x) for x,y in decode_ls.items())

decode_fs = {
    '00000': "",   '00100': " ",
    '10111': "1",    '10011': "2",
    '00001': "3",    '01010': "4",
    '10000': "5",    '10101': "6",
    '00111': "7",    '00110': "8",
    '11000': "9",    '10110': "0",
    '00011': "–",    '00101': "@",     #Bell
    '01001': "$",    '01101': "!",
    '11010': "&",    '10100': "#",
    '01011': "'",    '01111': "(",
    '10010': ")",    '10001': '"',
    '11101': "/",    '01110': ":",
    '11110': ";",    '11001': "?",
    '01100': ",",    '11100': ".",
    '01000': "\r",   '00010': "\n",
    '11011': False,   '11111': True,
}

encode_fs = dict((y,x) for x,y in decode_fs.items())

def decode(instr='11111 10100 10000 10000 10110 11011 01110 11101 11101'):
    """ decode(ITA2) -> Text
    """
    global decode_ls
    global decode_fs

    textlist = instr.replace("-",'1').replace(".",'0').split()

    ls_stat = True  # True -> LTRS ; False -> FIGS

    outstr = ""

    for char in textlist:
        try:
            if ls_stat:
                nextchar = decode_ls[char]
            else:
                nextchar = decode_fs[char]

        except KeyError:
            return '[ERROR] No such code %s in ITA2 Code.' % char

        if type(nextchar) != str:
            ls_stat = nextchar
        else:
            outstr += nextchar

    return outstr


def encode(instr="HTTP://"):
    """encode(Text) -> ITA2
    """
    global encode_fs
    global encode_ls

    instr = instr.upper()

    outstr = "11111"

    ls_stat = True  # True -> LTRS ; False -> FIGS

    for char in instr:
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and not ls_stat:
            outstr += " 11111"
            ls_stat = True
        elif char in "1234567890-@$!&#'()\"/:;?,." and ls_stat:
            outstr += ' 11011'
            ls_stat = False

        try:
            if ls_stat:
                outstr = outstr + " " + encode_ls[char]
            else:
                outstr = outstr + " " + encode_fs[char]
        except KeyError:
            return '[ERROR] Unknown character %s in input string.' % char

    return outstr
        


if __name__ == '__main__':
    if not sys.argv[1:]:
        try:
            a= raw_input("Please enter a string or a ITA2 code:")
        except:        
            a = input("Please enter a string or a ITA2 code:")
        if a:
            intext = a.upper()
        else:
            print('[ERROR] Please enter a string or a ITA2 code.')
    else:
        intext = ' '.join(sys.argv[1:]).upper()

    if all([i in '-. 10' for i in intext]):
        temptext = decode(intext)
        print("OUT: ", temptext)
    else:
        if all([i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-@$!&#\'()"/:;?,.' for i in intext]):
            print("OUT: ",encode(intext))
        else:
            pass
