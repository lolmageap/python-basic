from functools import partial
from operator import mul


def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


five = partial(mul, 5)
six = partial(five, 6)

if __name__ == "__main__":
    print(factorial(5))
    print(five(10))
    print(six())
