from contextlib import suppress
from functools import wraps


class Stop(Exception):
    pass


class Capture:
    def __call__(self, *args, **kwargs):
        with suppress(IndexError):
            self.value = args[0]
        self.args, self.kwargs = args, kwargs

        raise Stop


class Continuation:
    def __init__(self, _callable, *args, **kwargs):
        self._callable, self.args, self.kwargs = _callable, args, kwargs

    def __call__(self):
        try:
            return self._callable._unwrapped(*self.args, **self.kwargs)
        except AttributeError:
            return self._callable(*self.args, **self.kwargs)


def enable_cps_tco(callback):
    callback._unwrapped = callback

    @wraps(callback)
    def with_cps(*args, **kwargs):
        current = lambda: callback(*args, **kwargs)
        while True:
            try:
                current = current()
            except Stop:
                break

    return with_cps
