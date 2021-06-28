#!/usr/bin/env python3

import continuations
from continuations import Continuation


def fibonacci(n):
    @continuations.cps
    def fibonacci_cps(a, b, counter, limit, capture):
        if counter < limit:
            return Continuation(fibonacci_cps, b, b + a, counter + 1, limit, capture)
        else:
            return Continuation(capture, b)

    capture = continuations.Capture()
    fibonacci_cps(0, 1, 1, n, capture)
    return capture.value


def classic_fibonacci(a, b, counter, limit):
    if counter < limit:
        return classic_fibonacci(b, b + a, counter + 1, limit)
    else:
        return b


def iterative_fibonacci(limit):
    a, b, counter = 0, 1, 1
    while counter < limit:
        c = b + a
        a, b, counter = b, c, counter + 1
    return b


print("1_000_000th fibonacci number...")
iterative_fibonacci(1_000_000)

# print("1_000_000th fibonacci number...")
# fibonacci(1_000_000)

# print("10th fibonacci number is: ", classic_fibonacci(0, 1, 1, 1000))
# print("5000th fibonacci number is: ", classic_fibonacci(0, 1, 1, 5000))
# print("5000th fibonacci number is: ", classic_fibonacci(0, 1, 1, 5000))
