#!/usr/bin/env python3

from continuations import enable_tco


@enable_tco
def cps_fibonacci(limit, a=0, b=1, counter=1):
    if limit == 0:
        return 0
    elif counter < limit:
        return cps_fibonacci.recurse(limit, b, b + a, counter + 1)
    else:
        return b


def recursive_fibonacci(a, b, counter, limit):
    if limit == 0:
        return 0
    elif counter < limit:
        return recursive_fibonacci(b, b + a, counter + 1, limit)
    else:
        return b


def iterative_fibonacci(limit):
    if limit == 0:
        return 0
    a, b, counter = 0, 1, 1
    while counter < limit:
        c = b + a
        a, b, counter = b, c, counter + 1
    return b


print("Iterative")
print(iterative_fibonacci(5_000))

print("CPS-based TCO")
print(cps_fibonacci(5_000))

# print("Standard recursion")
# print(recursive_fibonacci(0, 1, 1, 5_000))
