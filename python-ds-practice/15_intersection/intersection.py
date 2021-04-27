def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    a = {i for i in l1}
    b= {j for j in l2}
    st = a.intersection(b)
    lst = [k for k in st]
    return lst

    #{} with just values is called a set. {} with key value pairs is called a dictionary. Both have different methods.