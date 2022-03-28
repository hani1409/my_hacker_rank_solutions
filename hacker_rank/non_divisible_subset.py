#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    count = [0] * k

    for i in s:
        remainder = i % k
        count[remainder] += 1

    ans = min(count[0], 1)  # Handling case 1

    if k % 2 == 0:  # Handling case even exception case
        ans += min(count[k // 2], 1)

    for i in range(1, k // 2 + 1):  # Check for the pairs and take appropriate count
        if i != k - i:  # Avoid over-counting when k is even
            ans += max(count[i], count[k - i])

    print(ans)
    return ans


def main():
    k = 7
    s = [576, 771, 282, 718, 496, 209, 338, 436, 149, 278, 727, 410, 124, 702, 575]

    nonDivisibleSubset(k, s)

if __name__ == '__main__':
    main()

