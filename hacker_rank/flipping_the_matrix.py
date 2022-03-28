#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#



def flippingMatrix(a):
    n = len(a)
    v = 0
    
    for i in range(len(a)):
        for j in range(len(a)):
            l = []
            l.append(a[i][j])  # current matrix
            l.append(a[2 * n - 1 - i][j])  # bottom left
            l.append(a[i][2 * n - 1 - j])  # top right
            l.append(a[2 * n - 1 - i][2 * n - 1 - j])  # bottom right

            maxv = max(l)
            print(l)
            print(max(l))
            v += maxv

    print(v)




if __name__ == '__main__':

    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    result = flippingMatrix(matrix)


