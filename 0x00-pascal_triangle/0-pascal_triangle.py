# This module represents a function that returns the pascal triangle.

def pascal_triangle(n):
    if (n <= 0):
        return []

    triangle = [[1]]

    for i in range(1, n):
        e = [triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)]
        row = [1] + e + [1]
        triangle.append(row)

    return triangle
