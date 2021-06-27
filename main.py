#!/usr/bin/env python3

import continuations


@continuations.cps
def fibonacci_cps(a, b, counter, limit, capture):
    if counter < limit:
        continuations.call(fibonacci_cps, b, b + a, counter + 1, limit, capture)
    else:
        continuations.call(capture, b)


def fibonacci(n):
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



# print("100th fibonacci number is: ", fibonacci(100))
print("5000th fibonacci number is: ", fibonacci(100_000))
# print("----------")

# print("10th fibonacci number is: ", classic_fibonacci(0, 1, 1, 1000))
# print("5000th fibonacci number is: ", classic_fibonacci(0, 1, 1, 5000))
# print("5000th fibonacci number is: ", classic_fibonacci(0, 1, 1, 5000))
