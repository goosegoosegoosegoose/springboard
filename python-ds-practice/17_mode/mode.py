def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dct = {i:0 for i in nums}
    st = set(nums)
    for j in st:
        dct[j] = nums.count(j)
    return max(dct, key=dct.get)
    #wat

    # I don't get how that returns the max, will have to ask later
    # theres another way that involves finding the index of the max value in list(dict.values) and returning that index of list(dict.keys), which i think would work
    # seems inelegant though