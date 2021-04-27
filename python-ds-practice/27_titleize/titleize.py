def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    a = phrase.split()
    b = []
    c = ' '
    for word in a:
        b.append(word.capitalize())
    return c.join(b)

    # split then join method
    # join is a string method, if want spaced words use a string with a empty space in it