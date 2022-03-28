#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    numOfA = s.count('a')
    lenS = len(s)
    div, mod = divmod(n, lenS)

    aCounter = ((div) * numOfA) + s[:mod].count('a')

    print(aCounter)
    return(aCounter)





def main():
    n = 549382313570
    s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"

    repeatedString(s, n)

if __name__ == '__main__':
    main()

