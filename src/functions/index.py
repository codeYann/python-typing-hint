# normal function using typing hints
def add(a: int, b: int) -> int:
    return a + b


def make_add_operation():
    """
    Using typing in vars in most cases is unnecessary because it's possible
    to infer by context
    """
    a = 10
    b = 15
    print(add(a, b))


def main():
    make_add_operation()


main()
