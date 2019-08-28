"""
This module includes the greedy approximation to bin-packing algorithm
"""

from typing import List, Tuple


def allocate(remainder: int, v_bins: List[int], a_bins: List[int] = None, this_bin: int = 0):

    print(remainder, v_bins, a_bins, this_bin)
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
        if this_bin > 0:
            this_bin -= 1
            return allocate(remainder, v_bins, a_bins, this_bin)
        else:
            if remainder > 0:
                raise ValueError('No solution!')
            return remainder, v_bins, a_bins, this_bin


if __name__ == '__main__':
    print(allocate(14, [8, 5, 2]))