# Rainwater Trapping Algorithm

## Overview
This project implements an efficient algorithm to calculate the amount of rainwater that can be trapped between walls of varying heights. The algorithm uses a two-pointer technique to achieve a time complexity of O(n), making it suitable for large input sizes.

## Table of Contents
- [Introduction](#introduction)
- [Algorithm](#algorithm)
- [Function Implementation](#function-implementation)
- [Usage](#usage)
- [Example](#example)
- [Complexity Analysis](#complexity-analysis)
- [Conclusion](#conclusion)

## Introduction
When it rains, water can accumulate between walls of different heights. This problem is commonly referred to as the "Trapping Rain Water" problem. Given an array of non-negative integers representing wall heights, the goal is to determine how much water can be retained after it rains.

## Algorithm
The algorithm employs a two-pointer approach, which involves:
1. Initializing two pointers (`left` and `right`) at the start and end of the array.
2. Keeping track of the maximum heights encountered from both sides (`left_max` and `right_max`).
3. Iterating through the array while adjusting the pointers based on the maximum heights.
4. Calculating the trapped water based on the difference between the maximum height and the current wall height.

### Steps:
1. If the input list is empty, return 0.
2. Initialize the left and right pointers, as well as the maximum heights and a variable to store the total water trapped.
3. While the left pointer is less than the right pointer:
   - Compare `left_max` and `right_max`.
   - Move the pointer corresponding to the smaller maximum height and update the trapped water.
4. Return the total amount of water trapped.

## Function Implementation
Here’s the implementation of the rainwater trapping algorithm:

```python
def rain(walls):
    """
    Calculate the amount of water retained after it rains, given a list of wall heights.

    Parameters:
    walls (list of int): A list of non-negative integers representing the heights of walls.

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
```

## Usage
To use the `rain` function, simply call it with a list of non-negative integers representing wall heights. 

### Example:
```python
if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 8
```

## Example
Given the wall heights `[0, 1, 0, 2, 0, 3, 0, 4]`, the algorithm will calculate that 6 square units of water can be retained. Similarly, for the input `[2, 0, 0, 4, 0, 0, 1, 0]`, it will return 8.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of walls. Each wall is processed once.
- **Space Complexity**: O(1), as we use a constant amount of space for variables, regardless of the input size.

## Conclusion
The rainwater trapping algorithm effectively calculates the total water retained between walls of varying heights using an efficient two-pointer technique. This method is both optimal and straightforward, making it a suitable solution for the problem.