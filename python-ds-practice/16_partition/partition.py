def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # a = []
    # b = []
    # ab = []
    # if f"{fn}" == "is_even":
    #     for num in lst:
    #         a.append(num) if is_even(num) == True else b.append(num)
    # elif f"{fn}" == "is_string":
    #     for elm in lst:
    #         a.append(elm) if is_string(elm) == True else b.append(elm)
    # else:
    #     None
    # ab.append(a)
    # ab.append(b)
    # return ab

    #returning empty lists
    #had to look at solution

    a = []
    b = []
    ab = []
    for elm in lst:
        a.append(elm) if fn(elm) == True else b.append(elm)
    ab.append(a)
    ab.append(b)
    return ab

    # if a parameter is defined as a method then you can just do fn(whatever). Does this count as a callback? Was this possible in javascript? Don't remember.
    #also have to remember you can just bracket things in a list/anything and just return it instead of having to append it to a variable and return it.