#!/usr/bin/python3
"""
0-pascal_triangle.py
"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the given number of rows (n).

    Args:
    - n: an integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


# For testing the function
if __name__ == "__main__":
    # Example usage
    result_triangle = pascal_triangle(5)
    print_triangle(result_triangle)

