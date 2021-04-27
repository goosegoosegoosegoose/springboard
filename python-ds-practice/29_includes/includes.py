def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if isinstance(collection, list) or isinstance(collection, str):
        if start != None:
            new = collection[collection.index(start):]
        else:
            new = collection
        if sought in new:
            return True
        return False

    elif isinstance(collection, tuple):
        if start != None:
            new = collection[start:]
        else:
            new = collection
        if sought in new:
            return True
        return False

    elif isinstance(collection, dict):
        values = list(collection.values())
        if sought in values:
            return True
        return False

    elif isinstance(collection, set):
        if sought in collection:
            return True
        return False

    # isinstance is just better than type for a lot