#!/usr/bin/python3
""" Encode / Decode Morse Code into / out of English, 
    non-aplhabet characters will be encode as 4-digit unicode hex string
    before feed into Morse decode function.
    Morse Code divided by spaces, English string shall not contain space.    
    User can use this script in 2 ways: 
    import morse => morse.decode(); morse.encode() 
    ./morse.py --- .. -.-. . 

    Author: Oicebot （@游荡的坎德人）
    2017.01.09 init build
    2020.03.11 add python2 and 3 compatibility.
"""
import time
import sys

decode_dict = { '.-'   : "A", '-...' : "B",
                '-.-.' : "C", '-..'  : "D",
                '.'    : "E", '..-.' : "F",
                '--.'  : "G", '....' : "H",
                '..'   : "I", '.---' : "J",
                '-.-'  : "K", '.-..' : "L",
                '--'   : "M", '-.'   : "N",
                '---'  : "O", '.--.' : "P",
                '--.-' : "Q", '.-.'  : "R",
                '...'  : "S", '-'    : "T",
                '..-'  : "U", '...-' : "V",
                '.--'  : "W", '-..-' : "X",
                '-.--' : "Y", '--..' : "Z",
                '.----': "1", '..---': "2",
                '...--': "3", '....-': "4",
                '.....': "5", '-....': "6",
                '--...': "7", '---..': "8",
                '----.': "9", '-----': "0", }

encode_dict = dict((y,x) for x,y in decode_dict.items())

def decode(instr='--- .. -.-. .'):
    """ decode(string) -> string input string ".-" split with space , output string chars """
    global decode_dict
    textlist = instr.split()
    outstr = ''
    for char in textlist:
        try:
            nextchar = decode_dict[char]
        except KeyError:
            return '[ERROR] No such code %s in Morse Code.' % char

        outstr = outstr + nextchar

    return outstr

def encode(instr="Oicebot"):
    """encode(string) -> string input chars, output string '.-' split with space """
    global encode_dict
    instr = instr.upper()
    outstr = ''
    for char in instr:
        try:
            nextchar = encode_dict[char]
        except KeyError:
            if char == ' ':
                #return '[Error] Please do not contain spaces in input string.'
                continue # ignore spaces
            else:
                return '[ERROR] Unknown character %s in input string.' % char

        outstr = outstr + nextchar + " "

    return outstr


if __name__ == '__main__':
    if not sys.argv[1:]:
        try:
            a= raw_input("Please enter a string or a morse code:")
        except:        
            a = input("Please enter a string or a morse code:")
        if a:
            intext = a.upper()
        else:
            print('[ERROR] Please enter a string or a morse code.')
    else:
        intext = ' '.join(sys.argv[1:]).upper()

    if all([i in '-. ' for i in intext]):
        temptext = decode(intext)
        print("OUT: ", temptext)
        if len(temptext) % 4 == 0:
            splited = [temptext[i*4:i*4+4] for i in range(len(temptext)// 4)]
            try:
                outtext = [chr(int(i,16)) for i in splited]
                print("CHR: ",''.join(outtext))
            except:
                pass
    else:
        if all([i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for i in intext]):
            print("OUT: ",encode(intext))
        else:
            temptext = ''.join([hex(ord(i))[2:].upper() for i in intext])
            print("HEX: ",temptext)
            print("OUT: ",encode(temptext))
