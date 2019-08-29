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

    print(a_list)
    # If the reminder is 0, return the result
    if remainder == 0:
        return remainder, v_list, a_list, pointer - 1

    # If divisible, allocate the reminder to the bin and return
    if remainder % v_list[pointer] == 0:
        a_list[pointer] = remainder // v_list[pointer]
        remainder = 0
        return remainder, v_list, a_list, pointer - 1

    # if not divisible but reach the last bin, return
    if pointer == n - 1:
        return remainder, v_list, a_list, pointer - 1

    # Otherwise try next smaller bin
    else:
        a_list[pointer] = remainder // v_list[pointer]
        remainder = remainder % v_list[pointer]
        pointer += 1
        remainder, v_list, a_list, pointer = greedy_allocate(remainder, v_list, a_list, pointer)

    # If still not divisible, remove one of this pack and allocate to smaller bins
    if remainder > 0 and a_list[pointer] > 0:
        a_list[pointer] -= 1
        remainder = remainder + v_list[pointer]
        pointer += 1
        remainder, v_list, a_list, pointer = greedy_allocate(remainder, v_list, a_list, pointer)

    return remainder, v_list, a_list, pointer - 1


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
    [0, 0, 7] 14 <== Potential Solution
    [0, 2, 2] 14 <== Potential Solution
    [1, 0, 3] 14 <== Potential Solution
    [[0, 2, 2], [1, 0, 3]]
    """
    n = len(v_list)
    # Initialise allocation list
    if a_list is None: a_list = [0] * n

    # Volume of current pack
    v = v_list[pointer]

    # Unallocated remainder
    m = remainder - np.dot(a_list[:pointer], v_list[:pointer]).sum()

    # Exhaustive search Loop
    for k in range(0, (int(m) // v) + 1):
        a_list[pointer] = k
        # If the allocation satisfy the requirement.
        if np.dot(a_list, v_list).sum() == remainder:
            print(a_list, np.dot(a_list, v_list).sum(), "<== Potential Solution")
            # Compare with optimal results, if better, update the optimal allocation
            if a_list_opt is None:
                a_list_opt = [a_list.copy()]
            elif np.sum(a_list) == np.sum(a_list_opt[0]):
                a_list_opt.append(a_list.copy())
            elif np.sum(a_list) < np.sum(a_list_opt[0]):
                a_list_opt = [a_list.copy()]
            else:
                pass

        if pointer < n - 1:
            v_list, a_list_opt = exhaustive_allocate(remainder, v_list, a_list, pointer + 1, a_list_opt)
    return v_list, a_list_opt


if __name__ == '__main__':
    allocate = exhaustive_allocate
    #allocate = greedy_allocate
    print("test 14:")
    print(allocate(14, [8, 5, 2]))
    print("test 11:")
    print(allocate(11, [8, 5, 2]))
    # print(allocate(10, [5, 2]))
    # print(allocate(12, [3, 5, 9]))
