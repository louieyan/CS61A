""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    prev, curr = link, link.rest
    while curr is not Link.empty:
        if curr.first == value:
            prev.rest, curr = curr.rest, curr.rest
        else:
            prev, curr = curr, curr.rest
    
    

    

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    curr = link
    while curr is not Link.empty:
        if not isinstance(curr.first, Link):
            curr.first = fn(curr.first)
        else:
            deep_map_mut(fn, curr.first)
        curr = curr.rest
    

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    >>> v = Link(1, Link(2, Link(3)))
    >>> v.rest.rest.rest = v.rest
    >>> has_cycle(v)
    True
    """
    nodes_seen = []
    curr = link
    while curr is not Link.empty:
        nodes_seen.append(curr)
        curr = curr.rest
        if curr in nodes_seen:
            return True

    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    >>> v = Link(1, Link(2, Link(3)))
    >>> v.rest.rest.rest = v.rest
    >>> has_cycle_constant(v)
    True
    """
    if link is Link.empty:
        return False

    prev, curr = link, link.rest
    while curr is not Link.empty:
        if curr.rest is Link.empty:
            return False
        elif curr.rest == prev or curr == prev:
            return True
        else:
            prev, curr = prev.rest, curr.rest.rest
    return False


    

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def helper(t, need_reverse):
        if t.is_leaf():
            pass
        reverse_labels = [b.label for b in t.branches][::-1]
        for i in range(len(t.branches)):
            b = t.branches[i]
            if need_reverse:
                b.label = reverse_labels[i]
            helper(b, not need_reverse)
    
    helper(t, True)
        
    
    
