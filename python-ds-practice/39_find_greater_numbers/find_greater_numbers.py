def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # times = 0
    # for num in nums[1:]:
    #     for i in range(len(nums)):
    #         for j in num[i:]:
    #             if num < nums[j]:
    #                 times += 1
    # return times

    # i tried :(

    times = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                times += 1

    return times

    # didn't use range start stop parameters to my advantage
    # need more experience

    #have not done the FS(further study) exercises