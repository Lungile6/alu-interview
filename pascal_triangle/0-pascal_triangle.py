#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(x):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Parameters:
    x (int): The number of rows in Pascal's triangle to generate. 
             Must be a positive integer.

    Returns:
    list: A list of lists, where each inner list represents a row 
           in Pascal's triangle.
    """
    # Check if the input is less than or equal to 0
    if x <= 0:
        return []  # Return an empty list for non-positive input

    triangle = []  # Initialize the list to hold the rows of the triangle

    # Loop through the number of rows specified by x
    for row in range(x):
        new_row = [1] * (row + 1)  # Start each row with 1s
        # Calculate the values for the current row based on the previous row
        for y in range(1, row):
            new_row[y] = triangle[row - 1][y - 1] + triangle[row - 1][y]
        triangle.append(new_row)  # Add the completed row to the triangle
    return triangle  # Return the completed Pascal's triangle
