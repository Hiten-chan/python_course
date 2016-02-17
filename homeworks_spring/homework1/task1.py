def sum(a, b):
    if type(a) == int and type (b) == int:
        pass
    else:
        raise TypeError
    if a >= 0 and b >= 0:
        pass
    else:
        raise ValueError
    return a + b
