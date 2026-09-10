"""
dummy.py - A simple dummy Python file for demonstration purposes.
"""


def greet(name: str) -> str:
    """Return a friendly greeting message."""
    return f"Hello, {name}! Welcome to the Dummy_code repository."


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
