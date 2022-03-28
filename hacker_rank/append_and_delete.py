import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    i = 0
    lenS = len(s)
    lenT = len(t)

    while i < lenS and i < lenT and s[i] == t[i]:
        i += 1

    sLeft = lenS - i
    tLeft = lenT - i

    if sLeft + tLeft > k:
        print("No")
        return "No"
        print("No")
    elif sLeft + tLeft == k:
        print("Yes")
        return "Yes"
    elif abs((lenS + lenT) - k) % 2 == 0:
        print("Yes")
        return "Yes"
    elif lenS + lenT - k <= 0:
        print("Yes")
        return "Yes"
    else:
        return "No"



def main():
    s = "aaaaaaaaaa"

    t = "aaaaa"

    k = 7

    appendAndDelete(s, t, k)

if __name__ == '__main__':
    main()