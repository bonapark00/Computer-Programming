"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p6.py
"""


def fibcalls(n):
    """
    Computes the number of function calls required
    to compute the n-th Fibonacci number.
    """
    # base case: n is 0 or 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    # get call number value recursively
    else:
        return 1 + fibcalls(n - 1) + fibcalls(n - 2)
