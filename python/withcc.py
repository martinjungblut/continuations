#!/usr/bin/env python3


def add1(n, k):
    k(n + 1)


def mul5(n, k):
    k(n * 5)


def withcc(capture_continuation, continuation):
    capture_continuation(continuation)
    return continuation


class ContinuationCapture:
    def __init__(self):
        self.continuation = None

    def __call__(self, continuation):
        self.continuation = continuation


capture = ContinuationCapture()

# same as add1(12, lambda a: mul5(a, print))
# writes 65 to stdout
# also captures the initial continuation as 'capture.continuation'
withcc(capture, lambda a: add1(a, lambda b: mul5(b, lambda c: print(c))))(12)

# same as add1(10, lambda a: mul5(a, print))
# writes 55 to stdout
capture.continuation(10)

# same as add1(3, lambda a: mul5(a, print))
# writes 20 to stdout
capture.continuation(3)

# same as add1(4, lambda a: mul5(a, print))
# writes 25 to stdout
capture.continuation(4)
