from functools import wraps


class Continuation:
    def __init__(self, c, *args, **kwargs):
        self.c, self.args, self.kwargs = c, args, kwargs

    def __call__(self):
        return self.c(*self.args, **self.kwargs)


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
