
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    min_arr = sorted(arr)[:4]
    max_arr = sorted(arr, reverse=True)[:4]

    print("%s %s" % (sum(min_arr), sum(max_arr)))


def main():
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)


if __name__ == '__main__':
    main()
