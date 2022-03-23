#!/usr/bin/env python3


def add1(value, continuation):
    continuation(value + 1)


def mul5(value, continuation):
    continuation(value * 5)


def withcc(capture, continuation):
    capture.continuation = continuation
    return continuation


class Capture:
    def __init__(self):
        self.continuation = None

    def recall(self, value):
        if self.continuation:
            self.continuation(value)


capture = Capture()

# same as add1(12, lambda a: mul5(a, print))
# writes 65 to stdout
# also captures the initial continuation as 'capture.continuation'
withcc(capture, lambda a: add1(a, lambda b: mul5(b, lambda c: print(c))))(12)

# same as add1(10, lambda a: mul5(a, print))
# writes 55 to stdout
capture.recall(10)

# same as add1(3, lambda a: mul5(a, print))
# writes 20 to stdout
capture.recall(3)

# same as add1(4, lambda a: mul5(a, print))
# writes 25 to stdout
capture.recall(4)
