
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#


def isWholeRoot(x):
    result = math.sqrt(x)
    intResult = int(result)
    if result - intResult == 0:
        return True
    else:
        return False


def squares(a, b):
    square1 = a ** (.5)
    if (square1 != int(square1)):
        a1 = int(square1) + 1
    else:
        a1 = int(square1)
    square2 = b ** (.5)
    b1 = int(square2)
    count = b1 - a1 + 1
    print(count)





def main():
    a = 24
    b = 30

    squares(a, b)


if __name__ == '__main__':
    main()
