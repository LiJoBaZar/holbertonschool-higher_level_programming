#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""

   if type(m_a) is not list:
        raise TypeError('m_a must be a list')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    if m_a == [] or m_a == [[]]:
        raise ValueError(r"m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError(r"m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a[0]) != len(m_b):
        raise ValueError(r"m_a and m_b can't be multiplied")

    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            a = sum([m_a[i][k] * m_b[k][j]
                    for k in range(len(m_a[i]))])
            row.append(a)
        res.append(row)
    return (res)
