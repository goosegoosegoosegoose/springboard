def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    nums.sort()
    nums_range = range(nums[0], nums[-1])
    low_msg = f"{lowest} fits" if lowest in nums_range else ""
    high_msg = f"{highest} fits" if highest in nums_range else ""
    print(low_msg)
    print(high_msg)

in_range([10, 20, 30, 40, 50], 15, 30)            
