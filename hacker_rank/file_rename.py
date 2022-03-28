#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#

from  itertools import combinations

def renameFile(newName, oldName):
    old = list(oldName)
    # new = newName.split("")
    val = combinations(old, len(newName))
    count = 0
    for i in val:
        if "".join(i) == newName:
            count+= 1

    print(count)
    return count

def main():
    newName = "aba"
    oldName = "ababa"

    renameFile(newName, oldName)

if __name__ == '__main__':
    main()

