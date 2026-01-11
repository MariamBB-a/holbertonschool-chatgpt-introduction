#!/usr/bin/python3
import sys

def factorial(n):
    """Return the factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    # Check integer conversion
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)

    # Check for negative numbers
    if n < 0:
        print("Error: factorial is not defined for negative numbers")
        sys.exit(1)

    print(factorial(n))

