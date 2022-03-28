#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cutStick(shortenedArr):
    firstItem = shortenedArr[0]
    newArr = []

    for x in shortenedArr:
        newLength = x - firstItem
        if newLength > 0:
            newArr.append(newLength)

    return newArr


def cutTheSticks(arr):
    sortedArr = sorted(arr)
    iterCount = [len(arr)]

    while sortedArr and max(sortedArr) > sortedArr[0]:
        sortedArr = cutStick(sortedArr)
        iterCount.append(len(sortedArr))

    return iterCount


def main():
    arr = [1, 2, 3, 4, 3, 3, 2, 1]

    cutTheSticks(arr)


if __name__ == '__main__':
    main()

