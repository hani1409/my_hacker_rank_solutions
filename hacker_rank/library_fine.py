#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2




def libraryFine(d1, m1, y1, d2, m2, y2):
    returnDate = datetime.datetime(y1, m1, d1)
    duedate = datetime.datetime(y2, m2, d2)


    if returnDate <= duedate:
        return 0

    elif returnDate.year == duedate.year and returnDate.month == duedate.month:
        amountDue = 15 * (returnDate.day - duedate.day)
        return amountDue

    elif returnDate.year == duedate.year:
        amountDue = 500 * (returnDate.month - duedate.month)
        return amountDue

    else:
        amountDue = 1000
        return amountDue



def main():
    d1 = 2
    m1 = 7
    y1 = 2015
    d2 = 1
    m2 = 2
    y2 = 2014

    libraryFine(d1, m1, y1, d2, m2, y2)


if __name__ == '__main__':
    main()

