from typing import Callable
import math


def add_func(a: int, b: int, c: float, fn: Callable[[int, int, float], int]) -> int:
    """
    It's possible to use Callable to type a function param

    The first arg in Callable is a list with the types of params
        It is possible to declare the return type of a callable
        without specifying the call signature by substituting a
        literal ellipsis for the list of arguments in the type hint

    The second one is a type of return function
    """
    return fn(a, b, c)


def sum(a: int, b: int, c: float) -> int:
    return math.floor((a + b) - c)


print(sum(10, 15, 5.2))
