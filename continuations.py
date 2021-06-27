from contextlib import suppress
from functools import wraps


class Continuation(Exception):
    def __init__(self, _callable, *args, **kwargs):
        self._callable, self.args, self.kwargs = _callable, args, kwargs

    def __call__(self):
        self._callable(*self.args, **self.kwargs)


def call(continuation, *args, **kwargs):
    raise Continuation(
        getattr(continuation, "_original_callable", continuation), *args, **kwargs
    )


class CPSError(ValueError):
    pass


class Stop(Exception):
    pass


def stop(*args, **kwargs):
    raise Stop


def cps(callback):
    err = CPSError("Last positional argument must be a continuation.")
    callback._original_callable = callback

    @wraps(callback)
    def with_cps(*args, **kwargs):
        try:
            if not callable(args[-1]):
                raise err
        except IndexError:
            raise err

        current = lambda: callback(*args, **kwargs)

        while True:
            try:
                current()
            except Continuation as c:
                current = c
            except Stop:
                break

    return with_cps


class Capture:
    def __call__(self, *args, **kwargs):
        with suppress(IndexError):
            self.value = args[0]

        self.args, self.kwargs = args, kwargs

        call(stop)
