from typing import Callable, Sequence


def apply_unpack(fn: Callable[[any], any], x: Sequence[Sequence[any]]):
    if type(x) not in (tuple, list):
        raise TypeError("x must be a tuple or list.")
    return type(x)([fn(*element) for element in x])


def apply(fn: Callable[[any], any], x: Sequence[any]):
    if type(x) not in (tuple, list):
        raise TypeError("x must be a tuple or list.")
    return type(x)([fn(element) for element in x])


def unzip(x: Sequence[any]):
    return list(zip(*x))