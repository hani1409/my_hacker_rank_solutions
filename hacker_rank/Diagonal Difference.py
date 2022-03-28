#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def getLefIndex(topNum, multipleOf):
    ind = [0]
    x = 0
    while x <= topNum:
        x = x + multipleOf
        if x <= topNum:
            ind.append(x)
    return ind


def getRightIndex(topNum, multipleOf):
    x = multipleOf
    ind = [x]

    while x <= topNum:
        x = x + multipleOf
        if x <= topNum and x != topNum - 1:
            ind.append(x)
    return ind


def diagonalDifference1(arr):
    gridSize = int(len(arr) ** .5)
    leftJump = gridSize + 1
    rightJump = gridSize - 1

    leftSum = 0
    rightSum = 0

    leftInd = [x for x in range(0, len(arr)) if x % leftJump == 0]
    rightInd = [x for x in range(2, len(arr)-1) if x % rightJump == 0]

    for x in leftInd:
        leftSum = leftSum + arr[x]
    for y in rightInd:
        rightSum = rightSum + arr[y]

    print(abs(leftSum - rightSum))
    return abs(leftSum - rightSum)


def diagonalDifference(arr):
    leftSum = 0
    rightSum = 0
    counter = 0
    for x in arr:
        leftSum += x[counter]
        counter += 1
    print(leftSum)

    counter = 0
    for y in arr:
        ind = abs(len(y)-1 - counter)
        rightSum += y[ind]
        counter += 1
    print(rightSum)

    print(abs(leftSum - rightSum))
    return abs(rightSum - leftSum)

if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)

