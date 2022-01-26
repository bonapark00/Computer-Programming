"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p5.py
"""

# empty global dictionary
dic_fib = {}


def fib_memo(n):
    """Computes the n-th Fibonacci number using memorization."""
    # if nth Fibonacci number is in dictonary
    if n in dic_fib.keys():
        return dic_fib[n]

    # base caes
    elif n == 0:
        dic_fib[0] = 0
        return 0
    elif n == 1:
        dic_fib[1] = 1
        return 1

    # if nth Fibonacci number is not in dictonary
    else:
        dic_fib[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return dic_fib[n]
