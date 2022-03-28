import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):
    fact = 1
    for x in range(n+1):
        if x == 0:
            continue
        else:
            fact = fact * x
    return fact

def main():
    extraLongFactorials(25)

if __name__ == '__main__':
    main()
