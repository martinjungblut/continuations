#!/usr/bin/env python3

import continuations


def fibonacci(n):
    @continuations.enable
    def cps_fibonacci(a, b, counter, limit, capture):
        if counter < limit:
            return continuations.new(cps_fibonacci, b, b + a, counter + 1, limit, capture)
        else:
            return continuations.new(capture, b)

    capture = continuations.Capture()
    cps_fibonacci(0, 1, 1, n, capture)
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


# print("1_000_000th fibonacci number...")
# iterative_fibonacci(1_000_000)

# print("1_000_000th fibonacci number...")
# fibonacci(1_000_000)

print("100_000th fibonacci number...")
print(fibonacci(100_000))
