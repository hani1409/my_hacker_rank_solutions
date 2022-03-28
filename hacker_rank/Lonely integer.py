#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    counter = {}
    for x in a:
        counter[x] = counter.get(x,0) + 1

    for k,v in counter.items():
        if v == 1:
            return k
        else:
            continue



if __name__ == '__main__':
    a = [1,2,3,4,3,2,1]

    result = lonelyinteger(a)
