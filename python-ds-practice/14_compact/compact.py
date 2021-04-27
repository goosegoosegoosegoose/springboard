def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # for i in lst:
    #     lst.remove(i) if bool(i) == False else None
    # return lst

    #remove method kept the empty [] and () even though they're false, don't understand.

    new_list = []
    for i in lst:
        new_list.append(i) if bool(i) == True else None
    return new_list