#!/usr/bin/python3
"""
Pascal's Triangle Module

This module provides a function to generate Pascal's Triangle, a triangular array
of the binomial coefficients. Each number in the triangle is the sum of the two
numbers directly above it in the previous row.

Functions:
----------
- pascal_triangle(n): Generates Pascal's Triangle up to the n-th row.

Usage:
------
To generate Pascal's Triangle for a specific number of rows, call the `pascal_triangle` 
function with an integer argument representing the desired number of rows. 
The function returns a list of lists, where each inner list corresponds to a row 
in Pascal's Triangle.

Example:
--------
>>> triangle = pascal_triangle(5)
>>> print(triangle)
[[1], 
[1, 1], 
[1, 2, 1], 
[1, 3, 3, 1], 
[1, 4, 6, 4, 1]]
"""

def pascal_triangle(n):
    if (n <= 0):
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [
            triangle[i - 1][j - 1] + triangle[i - 1][j] 
            for j in range(1, i)
            ] + [1]
        triangle.append(row)

    return triangle
