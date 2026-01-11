#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculate the factorial of a non-negative integer using recursion.
        The factorial of n (denoted n!) is the product of all positive integers ≤ n.
        By definition, factorial(0) is 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read input from command line argument and convert to integer
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)

