def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


def findSum(arr):
    if not arr:
        return 0
    else:
        return (arr.pop() + findSum(arr))


if __name__ == '__main__':


    arr = [1,2,5,6,3,3,6,32,6,4,546,34,5,346,34]


    result = findSum(arr)
    print(result)

