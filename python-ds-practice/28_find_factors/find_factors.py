def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    rg = range(1, num + 1)
    factors = []
    for x in rg:
        if num % x == 0:
            factors.append(x)
    return factors

    # forgot how % worked for a second
    # still don't know which if statements require an else if at all