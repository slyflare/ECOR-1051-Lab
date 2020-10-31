# excerise 4

def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the
    empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
    return s * n


result = repeat("yes", 4)
print(result)


# excersie 5

def total(s1: str, s2: str):
    """ Return the sum of the lengths of s1 and s2.
     >>> total('yes', 'no')
     5
     >>> total('yes', '')
     3
     >>> total('YES!!!!', 'Noooooo')
     14
     """
    return len(s1 + s2)


result = total('YES!!!!', 'Noooooo')
print(result)


# excersise 6

def replicate(s: str):
    """Returns a new string containing the original string copied by a number of times determined by the number of
    characters in the original string
    >>> replicate('no')
    'nono'
    >>> replicate('loom')
    'loomloomloomloom'
    >>> replicate('ma')
    'mama'
    """
    return len(s) * s


result = replicate('yes')
print(result)
