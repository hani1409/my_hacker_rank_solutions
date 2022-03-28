
from typing import List


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    timer = 0
    previous = 1
    halfDial = N / 2

    for x in C:
        if previous == x:
            continue
        else:
            diff = abs(previous - x)
            if diff > halfDial:
                timer += abs((previous + N) - x)
            else:
                timer += diff
        previous = x
    return timer


def main():
    N = 20
    M = 6
    C = [11, 5, 13, 4, 9, 19]
    print(getMinCodeEntryTime(N, M, C))


if __name__ == '__main__':
    main()