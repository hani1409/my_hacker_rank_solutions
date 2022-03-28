

def factorial(val):
    if val == 1:
        return 1
    else:
        return val * factorial(val-1)


def main():
    print(factorial(10))


if __name__ == '__main__':
    main()