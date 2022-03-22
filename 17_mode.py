def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    dict = {}
    for num in nums:
        dict[num] = nums.count(num)

    highest = 0
    num = 0
    for val in dict.items():
        if val[1] > highest:
            highest = val[1]
            num = val[0]

    return num
