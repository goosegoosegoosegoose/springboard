def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    d = {}
    if len(keys) >= len(values):
        diff = len(keys) - len(values)
        for i in range(len(values)):
            d.update({keys[i]:values[i]})
        if diff > 0:
            for j in range(diff):
                d.update({keys[-j-1]:None})
    elif len(keys) < len(values):
        for i in range(len(keys)):
            d.update({keys[i]:values[i]})
    return d

    # is there better way?
    # enumerate function
    # double variable for loop? niche for enumerate? confusion