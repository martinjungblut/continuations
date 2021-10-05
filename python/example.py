#!/usr/bin/env python3


def add1(n, k):
    k(n + 1)


def mul5(n, k):
    k(n * 5)


def with_cc(capture_continuation, continuation):
    capture_continuation(continuation)
    return continuation


class ContinuationCapture:
    def __init__(self):
        self.continuation = None

    def __call__(self, continuation):
        self.continuation = continuation


capture = ContinuationCapture()
with_cc(capture, lambda a: add1(a, lambda b: mul5(b, lambda c: print(c))))(10)


capture.continuation(3)
capture.continuation(4)
