#!/usr/bin/env python3

from functools import wraps


class Continuation:
    def __init__(self, f, *args, **kwargs):
        self.f, self.args, self.kwargs = f, args, kwargs

    def __call__(self):
        return self.f(*self.args, **self.kwargs)


def enable_tco(callback):
    callback.recurse = lambda *args, **kwargs: Continuation(callback, *args, **kwargs)

    @wraps(callback)
    def with_tco(*args, **kwargs):
        current = lambda: callback(*args, **kwargs)
        while True:
            current = current()
            if not isinstance(current, Continuation):
                return current

    return with_tco


@enable_tco
def cps_fibonacci(limit, a=0, b=1, counter=1):
    if limit == 0:
        return 0
    elif counter == limit:
        return b
    else:
        return cps_fibonacci.recurse(limit, b, b + a, counter + 1)


@enable_tco
def factorial(n, acc=1):
    if n in (0, 1):
        return acc
    else:
        return factorial.recurse(n - 1, acc * n)


print("Fibonacci")
print(cps_fibonacci(2000))


print("Factorial")
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))
