#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countDecreasingRatings' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY ratings as parameter.
#

def isDecreasing(rating, ind):
    '''return true is next rating decreasing'''

    if ind != (len(rating) - 1) and rating[ind] - 1 == rating[ind + 1]:
        return True
    else:
        return False


def countDecreasingRatings(rating):
    ratingSorted = sorted(rating)
    ratingSorted.reverse()
    groups = len(ratingSorted)  # Each single day rating counts as a group

    for x in range(len(ratingSorted)):
        # 2 day period
        if isDecreasing(ratingSorted, x):
            groups += 1
        else:
            continue

    counter = 0

    while isDecreasing(rating, counter):
        # Consecutive groups
        groups += 1
        if counter != len(rating):
            counter += 1
        else:
            break

    return groups


if __name__ == '__main__':
    l = [3, 2, 1, 3]
    countDecreasingRatings(l)
