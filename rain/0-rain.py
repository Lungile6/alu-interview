#!/usr/bin/python3
"""Rain trap calculation """


def rain(walls):
    """
    Calculate the amount of water retained after it rains,
    given a list of wall heights.

    Parameters:
    walls (list of int): A list of non-negative integers
    representing the heights of walls.

    Returns:
    int: The total amount of rainwater retained (in square units).
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, walls[left])
            water_trapped += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water_trapped += right_max - walls[right]

    return water_trapped
