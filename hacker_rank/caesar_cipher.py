#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):

    newStr = []
    for x in s:
        ordValue = ord(x)-96

        if x.isalpha() and x.islower():
            offset = 96
        elif x.isalpha():
            offset = 64

        # If not alpha keep it as it is
        if not x.isalpha():
            newStr.append(x)

        elif ord(x)-offset + k > 26:
            if (ord(x)-offset+k) % 26 == 0:
                if x.islower():
                    newStr.append('z')
                else:
                    newStr.append('Z')
            else:
                newStr.append(chr(((ord(x)-offset+k) % 26) + offset))

        else:
            test = chr(ord(x) - k)
            newStr.append(chr(ord(x)+k))

    print (''.join(newStr))
    return ''.join(newStr)



if __name__ == '__main__':
    s = '!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U'
    k =  62


    result = caesarCipher(s, k)