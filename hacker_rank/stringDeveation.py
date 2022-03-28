#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxFreqDeviation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def getMaxFreqDeviation(s):
    charCounter = {}

    # Get the count of each occurrence if each character
    for x in s:
        charCounter[x] = s.count(x)

    # If string has all the same characters return 0
    if len(charCounter) == 1:
        return 0

    # Sort the number instances a char appears
    counter = list(charCounter.values())
    counter.sort()

    # Take the difference between the highest and lowest
    return counter[-1] - counter[0]

if __name__ == '__main__':
    s = 'abdbcdacbcadbbc'
    print(getMaxFreqDeviation(s))
