def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    results = []
    for el in lst:
        results.append(f'{type(el)}')
    for i in results:
        if i != "<class 'list'>":
        # if not "<class 'list'>"
            return False
    return True

    # there has to be a better way to do this
    # looked at answer
    # isinstance(i, list) would have worked
    # does an if statement not need an else?
