"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p4.py
"""


def fib(n):
    """Computes the n-th Fibonacci number."""

    # base case for 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Do recursion
    else:
        return fib(n - 1) + fib(n - 2)
