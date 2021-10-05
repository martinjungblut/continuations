#!/usr/bin/env python3


def add1(n, k):
    return k(n + 1)


def mul5(n, k):
    return k(n * 5)


def with_cc(capture_continuation, continuation):
    capture_continuation(continuation)
    return continuation


captured_continuation = None

def capture(cont):
    global captured_continuation
    captured_continuation = cont


print(with_cc(capture, lambda a: add1(a, lambda a: mul5(a, lambda a: a)))(10))

print(captured_continuation(3))
print(captured_continuation(4))
