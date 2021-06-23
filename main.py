#!/usr/bin/env python3


class Stop(Exception):
    pass


class Continuation(Exception):
    def __init__(self, callback, *args, **kwargs):
        self.callback, self.args, self.kwargs = callback, args, kwargs

    def __call__(self):
        self.callback(*self.args, **self.kwargs)


def stop():
    raise Stop


def call_continuation(continuation, *args, **kwargs):
    raise Continuation(continuation, *args, **kwargs)


def call_with_tco(callback):
    while True:
        try:
            callback()
        except Continuation as c:
            callback = c
        except Stop:
            break


def add1(n, limit, continuation):
    print(n, limit)
    if n < limit:
        call_continuation(n + 1, limit, continuation)
    else:
        stop()


def with_cps(callback):
    def cps(*args, **kwargs):
        current = lambda: callback(*args, **kwargs)

        while True:
            try:
                current()
            except Continuation as c:
                current = c
            except Stop:
                break

    return cps


@with_cps
def fibonacci(a, b, counter, limit, continuation):
    print(f"Current number: {b}")

    if counter < limit:
        call_continuation(continuation, b, b + a, counter + 1, limit, continuation)
    else:
        stop()



# call_with_tco(lambda: fibonacci(1, 1, 1, 5000, fibonacci))
fibonacci(1, 1, 1, 5000, fibonacci)
