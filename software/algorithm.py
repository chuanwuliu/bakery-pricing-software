"""
This module includes the greedy approximation to bin-packing algorithm. See README for explanation.
"""

import numpy as np


def greedy_allocate(remainder, v_list, a_list=None, pointer=0):
    """
    Allocate remainders to bins (packs).

    :param remainder: int, remainder number.
    :param v_list: list, bin volumes (number of units of each pack)
    :param a_list: list, number to each bin
    :param pointer: int, recursion pointer.

    :return: same as arguments.
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

    # If still not divisible, remove one this bin and allocate to smaller bins
    if a_list[pointer] > 0:
        a_list[pointer] -= 1
        remainder = remainder + v_list[pointer]
        pointer += 1
        return greedy_allocate(remainder, v_list, a_list, pointer)


def exhaustive_allocate(remainder, v_list, a_list=None, pointer=0):
    n = len(v_list)
    if a_list is None: a_list = np.zeros(n)
    v_list = np.array(v_list)
    v = v_list[pointer]
    m = remainder - (a_list * v_list)[:pointer].sum()
    for k in range(0, (int(m) // v) + 1):
        a_list[pointer] = k
        if (a_list * v_list).sum() == remainder:
            print(a_list, (a_list * v_list).sum(), "Found")
        else:
            print(a_list, (a_list * v_list).sum())
        if pointer < n - 1:
            exhaustive_allocate(remainder, v_list, a_list, pointer + 1)
    a_list[pointer] = 0


if __name__ == '__main__':
    allocate = greedy_allocate
    print(allocate(14, [8, 5, 2]))
    print(allocate(10, [5, 2]))
    print(allocate(12, [3, 5, 9]))
