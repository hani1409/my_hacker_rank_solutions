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


def timeConversion(s):
    isPM = s.__contains__("PM")
    isAM = s.__contains__("AM")
    s = s[:-2]

    hour = int(s.split(":")[0])
    timeSplit = s.split(":", 1)[1]

    if isPM and hour == 12:
        return s
    elif isPM:
        newHour = int(hour) + 12
        return "%s:%s" % (newHour, timeSplit)
    elif isAM and hour == 12:
        newHour = 00
        return "%s:%s" % (newHour, timeSplit)
    elif isAM:
        return "%s" % s


def main():
    s = "06:40:03AM"
    timeConversion(s)


if __name__ == '__main__':
    main()
