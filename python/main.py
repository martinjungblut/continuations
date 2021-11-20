#!/usr/bin/env python3

from continuations import Capture, Continuation, enable_cps_tco


def fibonacci(n):
    @enable_cps_tco
    def cps_fibonacci(a, b, counter, limit, capture):
        if limit == 0:
            return Continuation(capture, 0)
        elif counter < limit:
            return Continuation(cps_fibonacci, b, b + a, counter + 1, limit, capture)
        else:
            return Continuation(capture, b)

    capture = Capture()
    cps_fibonacci(0, 1, 1, n, capture)
    return capture.value


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
print(fibonacci(5_000))

# print("Standard recursion")
# print(recursive_fibonacci(0, 1, 1, 5_000))
