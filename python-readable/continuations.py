from functools import wraps


class Continuation:
    def __init__(self, c, *args, **kwargs):
        self.c, self.args, self.kwargs = c, args, kwargs

    def __call__(self):
        return self.c(*self.args, **self.kwargs)


def enable_tco(callback):
    def recurse(*args, **kwargs):
        return Continuation(callback, *args, **kwargs)

    callback.recurse = recurse

    @wraps(callback)
    def with_cps(*args, **kwargs):
        current = lambda: callback(*args, **kwargs)
        while True:
            current = current()
            if not isinstance(current, Continuation):
                return current

    return with_cps
