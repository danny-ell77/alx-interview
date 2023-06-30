#!/usr/bin/python3
"""A module for working with Pascal's triangle.
"""


def pascals_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    traingle = []
    if not n > 0:
        return
    for i in range(n):
        if i == 0:
            traingle.append([1])
        elif i == 1:
            traingle.append([1, 1])
        else:
            new_row = []
            prev_row = traingle[i - 1]
            for j in range(i):
                if j == 0:
                    new_row.append(1)
                elif j + 1 == i:
                    new_row.append(prev_row[j - 1] + prev_row[j])
                    new_row.append(1)
                else:
                    new_row.append(prev_row[j - 1] + prev_row[j])
            traingle.append(new_row)

    return traingle


# def pascals_triangle(n):
#     triangle = []
#     for i in range(n):
#         row = [1] * (i + 1)  # Initialize each row with 1s
#         if i >= 2:
#             prev_row = triangle[i - 1]
#             for j in range(1, i):
#                 row[j] = prev_row[j - 1] + prev_row[j]
#         triangle.append(row)
#     return triangle


# pprint(pascals_triangle(7))
