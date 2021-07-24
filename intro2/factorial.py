import sys


def factorial(n):
    if n < 0 or n % 1 != 0:
        raise ValueError('Please enter a non-negative integer')
    # Base Case for n=0
    elif n == 0:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)


print(factorial(int(sys.argv[1])))
