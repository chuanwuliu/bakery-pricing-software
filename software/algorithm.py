"""
This module includes the greedy approximation to bin-packing algorithm. See README for explanation.
"""

import numpy as np
from typing import List


def greedy_allocate(remainder: int, v_list: List[int], a_list: List[int] = None, this_bin: int = 0):
    """
    Allocate remainders to bins (packs).

    :param remainder: int, remainder number.
    :param v_list: list, bin volumes (number of units of each pack)
    :param a_list: list, number to each bin
    :param this_bin: int, recursion pointer.

    :return: same as arguments.
    """

    # Sort bin sizes in descending order
    v_list = sorted(v_list, reverse=True)

    # number of bin types
    n = len(v_list)

    # Initialise the bin allocation if it does not exist
    if a_list is None:
        a_list = [0] * n

    a_list[this_bin] = remainder // v_list[this_bin]
    remainder = remainder % v_list[this_bin]

    # If the reminder is 0, return the results
    if remainder == 0:
        this_bin = 0
        return remainder, v_list, a_list, this_bin

    # If this bin is the last, return
    if this_bin == n - 1:
        this_bin -= 1
        return remainder, v_list, a_list, this_bin

    # If not divisible, try next smaller bin
    this_bin += 1
    remainder, v_list, a_list, this_bin = greedy_allocate(remainder, v_list, a_list, this_bin)

    # If still not divisible, remove one this bin and allocate to smaller bins
    if remainder > 0 and a_list[this_bin] > 0:
        a_list[this_bin] -= 1
        remainder = remainder + v_list[this_bin]
        this_bin += 1
        return greedy_allocate(remainder, v_list, a_list, this_bin)
    else:
        return remainder, v_list, a_list, this_bin


def exhaustive_allocate(m, v_list, a_list=None, i=0):
    n = len(v_list)
    if a_list is None: a_list = np.zeros(n)
    v_list = np.array(v_list)
    v = v_list[i]
    mi = m - (a_list * v_list)[:i].sum()
    for k in range(0, (int(mi) // v) + 1):
        a_list[i] = k
        if (a_list * v_list).sum() == m:
            print(a_list, (a_list * v_list).sum(), "Found")
        else:
            print(a_list, (a_list * v_list).sum())
        if i < n - 1:
            exhaustive_allocate(m, v_list, a_list, i + 1)
    a_list[i] = 0


if __name__ == '__main__':
    allocate = greedy_allocate
    print(allocate(14, [8, 5, 2]))
    print(allocate(10, [5, 2]))
    print(allocate(12, [3, 5, 9]))
