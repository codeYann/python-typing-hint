def greetings(message: str) -> str:
    return f"Hello {message}"


if __name__ == "__main__":
    msg: str = "world!"
    print(greetings(msg))
