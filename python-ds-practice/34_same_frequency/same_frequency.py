def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    st1 = str(num1)
    st2 = str(num2)
    set1 = set(list(st1))
    set2 = set(list(st2))
    di1 = {}
    di2 = {}

    for num in set1:
        di1.update({num:st1.count(num)})
    for num in set2:
        di2.update({num:st2.count(num)})
    if di1 == di2:
        return True
    return False

    # somehow worked
    # they made a whole new def in answers
    # get function?