from typing import Union

# Using new union type
number = int | float

# Using Union type
Number = Union[int, float]


def add(a: number, b: number) -> number:
    return a + b


def make_add_operation():
    a = 15.5
    b = 10
    print(add(a, b))


def sub(a: Number, b: Number) -> Number:
    return a - b


def make_sub_operation():
    a = 105
    c = 5.5
    print(sub(a, c))


def main():
    make_add_operation()
    make_sub_operation()


main()
