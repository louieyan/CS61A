def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    
    pre, next = n % 10, (n // 10) % 10
    while n > 0:
        n //= 10
        if pre > next:
            return False
        else:
            if n > 10:
                pre, next = next, (n // 10) % 10 
            else:
                pre, next = next, n
        
    return True

def mario_number(level):
    """
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    if level == 11:
        return 1
    elif  :
    
    else: