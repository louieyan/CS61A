def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n == 0:
        print("Alice wins")
    elif n % 2 == 0:
        play_alice(n-2)
    else:
        play_alice(n-1)

def count_partitions(n, m):
    """Cout the ways to partition N using parts up to M"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

def longest_increasing_suffix(n):
    """
    Return the longest increasing suffix of a positive integer n.
    Parameters:
    m: max value
    suffix: suffix
    k: scaling constant 
    """
    m, suffix, k = 10, 0, 1 
    while n:
        n, last = n // 10, n % 10
        if last < m:
            m, suffix, k = last, suffix + last * k, 10 * k
        else:
            return suffix
    return suffix

def sandwich(n):
    """
    Return True if n contains a sandwich and False otherwise.
    """
    tens, ones = n // 10 % 10, n % 10
    n = n // 100
    while n:
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 100
    return False

def luhn_sum(n):
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + (x % 10)

    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier =  3 - multiplier
    return total

def square(x):
    return x * x

def dog(bird):
    def cow(tweet, moo):
        woof = bird(tweet)
        print(moo)
        return woof
    return cow

cat = dog(square)

batman, superman, ivy = 1, -2, -3


def gcd(m, n):
    """Returns the largest k that divides both m and n.

    k, m, n are all integers.

    >>> gcd(8, 12)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(5, 5)
    5
    """
    if m % n == 0:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)


def mystery(f, x):
    return lambda y: f(x, y)

def fox_says(start, middle, end, num):
    def repeat(k):
        if k == 1:
            return middle
        else:
            return middle + '-' + repeat(k-1)
    return start + '-' + repeat(num) + '-' + end

def combine(n, f, result):
    if n == 0:
        return result
    else:
        return combine(n//10, f, f(n%10, result))

def has_sum(total, n, m):
    if total < n and total < m:
        return False
    elif total % n == 0 or total % m == 0:
        return True
    return has_sum(total-max(n, m), n, m)

def kbonacci(n, k):
    if n < k -1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = n - k
        while i < n:
            total = total + kbonacci(i, k)
            i = i + 1
        return total

def combine(left, right):
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the dights of N in reverse.
    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n%10, reverse(n//10))

def remove(n, digit):
    """Remove all digits of N that are not DIGIT, for 
       DIGIT less than 10
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        i, n = n % 10, n // 10
        if i != digit:
            removed = combine(removed, i)
    return reverse(removed)  
square = lambda x: x * x
double = lambda x: 2 * x
identity = lambda x: x
def memory(x, f):
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

lamb = lambda lamb: lambda: lamb + lamb
lamb(1000)() + (lambda b, c: b() * b() - c)(lamb(2), 1)

from fractions import gcd
def rational(n, d):
    """Construct a rational with numerator N and denominator D"""
    g = gcd(n, d)
    return [n//g, d//g]
def numer(x):
    """Return the numerator of X"""
    return x[0]

def denom(x):
    """Return the denominator of X"""
    return x[1]

def add_rationals(x, y):
    """Add two rationals X and Y"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    """Return true if X is equal to Y"""
    return numer(x) * denom(y) == numer(y) * denom(x)


def count(s, value):
    """Count the number of times that VALUE occured in sequence S.
    >>> count([1, 2, 3, 1, 2, 3], 1)
    2
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def divisors(n):
    """Return a list containing all the divisors of N"""
    return [1] + [i for i in range(2, n) if n%i == 0]


# Implementing the Tree Abstraction
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing all the leaves of the given TREE."""
    if is_leaf(tree):
        return tree
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def partition_tree(n, m):
    """Return a partition of n using parts of up to m"""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left, right = partition_tree(n-m, m), partition_tree(n, m-1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree) # 'tree' is binary
        m = str(label(tree))
        print_parts(left, partition+[m])
        print_parts(right, partition)


def increment_leaves(t):
    """Return a tree like T but with leaf lables incremented."""
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like T but with all lables incremented."""
    new_t = increment_leaves(t)
    return tree(label(new_t)+1, branches(new_t))


from ucb import trace
@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def inf_f():
    return inf_f()

def sum_lst(lst):
    """Return the sum of all elements in LST"""
    if lst == []:
        return 0
    else:
        return lst[0] + sum_lst(lst[1:])

def count(total):
    i = 0
    while i < total:
        i += 1
        print(i)

def balanced(s, depth=0):
    if not s:
        return depth == 0
    if depth < 0:
        return False
    if s[0] == '(':
        return balanced(s[1:], depth + 1)
    elif s[0] == ')':
        return balanced(s[1:], depth - 1)
    else:
        return balanced(s[1:], depth)
    
empty = 'empty'
def is_link(s):
    if s == empty:
        return True
    return len(s) == 2 and is_link(s[1])

def link(first, rest):
    """
    Construct a linked list from its first and rest.
    rest can be `empty`
    """
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def len_link(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link(rest(s))

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i - 1)

def extend_link(s, t):
    """Return a list with elements of s followed by elements of t."""
    assert is_link(s) and is_link(t), "both s and t should be link."
    if s == empty:
        return t
    return link(first(s), extend_link(rest(s), t))

def apply_to_all_link(f, s):
    """Apply f to all elements of s"""
    assert is_link(s), "s should a link."
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s), "s should a link."
    if s == empty:
        return s
    
    kept = keep_if_link(f, rest(s))
    if f(first(s)):
        return link(first(s), kept)
    else:
        return kept

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    assert is_link(s), "s should a link."
    if s == empty:
        return ""
    if rest(s) == empty:
        return str(first(s))
    return str(first(s)) + separator + join_link(rest(s), separator)

def link_partition(n, m):
    if n == 0:
        return link(empty, empty)
    if n < 0 or m == 0:
        return empty
    using_m = link_partition(n-m, m)
    with_m = apply_to_all_link(lambda s: link(m, s), using_m)
    without_m = link_partition(n, m-1)
    return extend_link(with_m, without_m)

def print_link_partition(n, m):
    link_of_links = link_partition(n, m)
    # join every little link of the big link
    strings = apply_to_all_link(lambda s: join_link(s, " + "), link_of_links)
    # join all joined little links
    print(join_link(strings, "\n"))

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

#wd = make_withdraw(20)
#wd(5)
#wd(3)

def letter_generator(stop_letter):
    current = 'a'
    while current <= stop_letter:
        yield current
        current = chr(ord(current) + 1)

def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")
    
    return dispatch

def to_mutable_link(source):
    """Return a functional linked list with the same contents as source"""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

# 2.5 OOP
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

a = Account('Lei')
a.deposit(10)
#a.withdraw(5)
#a.withdraw(10)

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other

        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__
    
    def __float__(self):
        return self.numer / self.denom

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

import functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print('Whee!')

@do_twice
def greet(name):
    print(name)

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Happy new year!")
    else:
        print(from_number)
        countdown(from_number - 1)



def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        reslut = f(*args)
        counted.open_count -= 1
        return reslut
    counted.open_count = 0
    counted.max_count = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

@memo
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

words = ["cat", "window", "defenestrate"]

def foo(n):
    if n > 5:
        pass
    
    
    else:
        print(n)