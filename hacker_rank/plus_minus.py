import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    total = len(arr)

    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    zero = [x for x in arr if x == 0]

    print(round(len(pos)/total, 6))
    print(round(len(neg)/total, 6))
    print(round(len(zero)/total, 6))


def main():
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)


if __name__ == '__main__':
    main()
