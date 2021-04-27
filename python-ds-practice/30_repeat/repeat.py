def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    string = ''
    if isinstance(num, int) and num >= 0:
        rg = range(num)
        for i in rg:
            string += phrase
        return string
    else:
        return None

    # remember greater less than symbols