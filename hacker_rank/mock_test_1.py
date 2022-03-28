import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def findMedian(arr):
    sortedArr = sorted(arr)
    length = len(arr)
    middle = int(length/2)
    return sortedArr[middle]

def main():
    arr = [5, 3, 1, 2, 4]

    findMedian(arr)

if __name__ == '__main__':
    main()
