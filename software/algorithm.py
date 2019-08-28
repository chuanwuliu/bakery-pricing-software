"""
This module includes the greedy approximation to bin-packing algorithm. See README for explanation.
"""

from typing import List


def allocate(remainder: int, v_bins: List[int], a_bins: List[int] = None, this_bin: int = 0):
    """
    Allocate remainders to bins (packs).

    :param remainder: int, remainder number.
    :param v_bins: list, bin volumes (number of units of each pack)
    :param a_bins: list, number to each bin
    :param this_bin: int, recursion pointer.

    :return: same as arguments.
    """

    # Sort bin sizes in descending order
    v_bins = sorted(v_bins, reverse=True)

    # number of bin types
    n = len(v_bins)

    # Initialise the bin allocation if it does not exist
    if a_bins is None:
        a_bins = [0] * n

    a_bins[this_bin] = remainder // v_bins[this_bin]
    remainder = remainder % v_bins[this_bin]

    # If the reminder is 0, return the results
    if remainder == 0:
        this_bin = 0
        return remainder, v_bins, a_bins, this_bin

    # If this bin is the last, return
    if this_bin == n - 1:
        this_bin -= 1
        return remainder, v_bins, a_bins, this_bin

    # If not divisible, try next smaller bin
    this_bin += 1
    remainder, v_bins, a_bins, this_bin = allocate(remainder, v_bins, a_bins, this_bin)

    # If still not divisible, remove one this bin and allocate to smaller bins
    if remainder > 0 and a_bins[this_bin] > 0:
        a_bins[this_bin] -= 1
        remainder = remainder + v_bins[this_bin]
        this_bin += 1
        return allocate(remainder, v_bins, a_bins, this_bin)
    else:
        return remainder, v_bins, a_bins, this_bin


if __name__ == '__main__':
    print(allocate(14, [8, 5, 2]))
    print(allocate(10, [5, 2]))
    print(allocate(12, [3, 5, 9]))
