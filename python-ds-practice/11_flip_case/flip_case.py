def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = list(phrase)
    idx = []
    string = ""
    
    for i in range(len(lst)):
        idx.append(i) if lst[i].upper() == to_swap.upper() else None
    for j in idx:
        if lst[j].isupper() == True:
            lst[j] = lst[j].lower()
        else:
            lst[j] = lst[j].upper()
    return string.join(ltr for ltr in lst)

    # .join() method does not change original string, so "string" variable was still an empty string. Remembering this is going to be hard.
    # if statement seems to need else, otherwise syntax error.
    # could have used swapcase() I feel stupid