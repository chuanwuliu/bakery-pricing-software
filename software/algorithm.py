"""
This module includes the greedy approximation to bin-packing algorithm. See README for explanation.
"""

import numpy as np


def greedy_allocate(remainder, v_list, a_list=None, pointer=0):
    """
    Allocate order remainder to packs - greedy approximation.

    :param remainder: int, remainder number
    :param v_list: list, pack volumes (number of units of each pack)
    :param a_list: list, allocated number to each pack
    :param pointer: int, recursion pointer
    :return: same as arguments.

    Examples:
    >>> greedy_allocate(10, [5, 2])
    (0, [5, 2], [2, 0], 0)
    >>> greedy_allocate(14, [8, 5, 2])
    (0, [8, 5, 2], [1, 0, 3], 1)
    >>> greedy_allocate(13, [5, 3])
    (0, [5, 3], [2, 1], 0)
    """

    # Sort bin sizes in descending order
    v_list = sorted(v_list, reverse=True)

    # number of bin types
    n = len(v_list)

    # Initialise the bin allocation if it does not exist
    if a_list is None:
        a_list = [0] * n

    a_list[pointer] = remainder // v_list[pointer]
    remainder = remainder % v_list[pointer]

    # If this bin is the last, return the result
    if pointer == n - 1:
        pointer -= 1
        return remainder, v_list, a_list, pointer

    # If not divisible, try next smaller bin
    if remainder > 0:
        pointer += 1
        remainder, v_list, a_list, pointer = greedy_allocate(remainder, v_list, a_list, pointer)

    # If the reminder is 0, return the result
    if remainder == 0:
        return remainder, v_list, a_list, pointer

    # If still not divisible, remove one of this pack and allocate to smaller bins
    if a_list[pointer] > 0:
        a_list[pointer] -= 1
        remainder = remainder + v_list[pointer]
        pointer += 1
        remainder, v_list, a_list, pointer = greedy_allocate(remainder, v_list, a_list, pointer)

    return remainder, v_list, a_list, pointer


def exhaustive_allocate(remainder, v_list, a_list=None, pointer=0, a_list_opt=None):
    """
    Exhaustive pack allocation algorithm.

    :param remainder: int, remainder number
    :param v_list: list, pack volumes (number of units of each pack)
    :param a_list: list, allocated number to each pack
    :param pointer: int, recursion pointer
    :param a_list_opt: list, current optimal allocation list
    :return: list, current optimal allocation list

    Examples:
    >>> exhaustive_allocate(14, [8, 5, 2])
    [0, 0, 0] 0
    [0, 0, 0] 0
    [0, 0, 0] 0
    [0, 0, 1] 2
    [0, 0, 2] 4
    [0, 0, 3] 6
    [0, 0, 4] 8
    [0, 0, 5] 10
    [0, 0, 6] 12
    [0, 0, 7] 14 <== Potential Solution
    [0, 1, 7] 19
    [0, 1, 0] 5
    [0, 1, 1] 7
    [0, 1, 2] 9
    [0, 1, 3] 11
    [0, 1, 4] 13
    [0, 2, 4] 18
    [0, 2, 0] 10
    [0, 2, 1] 12
    [0, 2, 2] 14 <== Potential Solution
    [1, 2, 2] 22
    [1, 0, 2] 12
    [1, 0, 0] 8
    [1, 0, 1] 10
    [1, 0, 2] 12
    [1, 0, 3] 14 <== Potential Solution
    [1, 1, 3] 19
    [1, 1, 0] 13
    [[0, 2, 2], [1, 0, 3]]
    """
    n = len(v_list)
    if a_list is None: a_list = [0] * n
    v = v_list[pointer]
    m = remainder - np.dot(a_list[:pointer], v_list[:pointer]).sum()
    for k in range(0, (int(m) // v) + 1):
        a_list[pointer] = k
        if np.dot(a_list, v_list).sum() == remainder:
            print(a_list, np.dot(a_list, v_list).sum(), "<== Potential Solution")
            if a_list_opt is None:
                a_list_opt = [a_list.copy()]
            elif np.sum(a_list) == np.sum(a_list_opt[0]):
                a_list_opt.append(a_list.copy())
            elif np.sum(a_list) < np.sum(a_list_opt[0]):
                a_list_opt = [a_list.copy()]
            else:
                pass
        else:
            print(a_list, np.dot(a_list, v_list).sum())
        if pointer < n - 1:
            a_list_opt = exhaustive_allocate(remainder, v_list, a_list, pointer + 1, a_list_opt)
    return a_list_opt


if __name__ == '__main__':
    allocate = greedy_allocate
    print(allocate(14, [8, 5, 2]))
    print(allocate(10, [5, 2]))
    print(allocate(12, [3, 5, 9]))
