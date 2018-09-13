""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def call_functions_n_times(n):
        def compute(x):
            rounds, remainder = n // 3, n % 3
            while rounds != 0:
                x = f3(f2(f1(x)))
                rounds -= 1
            if remainder == 0:
                return x
            elif remainder == 1:
                return f1(x)
            else:
                return f2(f1(x))
        return compute
    return call_functions_n_times


## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(n, k):
        if k == n:
            return True
        elif n % k == 0:
            return False
        else:
            return helper(n, k+1)
    return helper(n, 2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def helper_odd(odd_term, k):
        if k == n:
            return odd_term(n)
        return helper_even(even_term, k+1) + odd_term(k)
    def helper_even(even_term, k):
        if k == n:
            return even_term(n)
        return helper_odd(odd_term, k+1) + even_term(k)  
    
    return helper_odd(odd_term, 1)
        

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper_counts(n, digit, num=0):
        if n == 0:
            return num
        elif n % 10 == digit:
            return helper_counts(n//10, digit, num+1)
        else:
            return helper_counts(n//10, digit, num)
    
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + helper_counts(n//10, 10-(n%10))