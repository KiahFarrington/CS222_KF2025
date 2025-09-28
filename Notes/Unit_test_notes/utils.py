# Unit_test_notes/utils.py

def is_even(n: int) -> bool:
    """Return True if n is an even integer."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

def factorial(n: int) -> int:
    """Compute n! (factorial)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def max_min(values: list[int]) -> tuple[int, int]:
    """Return (max, min) of a list of integers."""
    if not values:
        raise ValueError("List cannot be empty")
    return (max(values), min(values))
