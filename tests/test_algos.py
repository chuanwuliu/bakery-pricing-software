import numpy as np

from software.algos import greedy_allocate, exhaustive_allocate


def test_examples():
    """
    Test example inputs from the specification.

    Test criteria:
      * if pack sizes is [5, 3], and order is 10. the allocation output is [2, 0]
      * if pack sizes is [8, 5, 2], and order is 14. the allocation output is [1, 0, 3]
      * if pack sizes is [9, 5, 3], and order is 13. the allocation output is [0, 2, 1]
    """

    # Test 10 VS5 order
    v_list = [5, 3]
    quantity = 10
    # greedy method
    reminder, v_list, a_list, _ = greedy_allocate(quantity, v_list)
    assert reminder == 0
    assert v_list == [5, 3]
    assert a_list == [2, 0]
    # exhaustive method
    v_list, a_list_opt = exhaustive_allocate(quantity, v_list)
    assert v_list == [5, 3]
    assert a_list_opt == [[2, 0]]

    # Test MB11 order
    v_list = [8, 5, 2]
    quantity = 14
    # greedy method
    reminder, v_list, a_list, _ = greedy_allocate(quantity, v_list)
    assert reminder == 0
    assert v_list == [8, 5, 2]
    assert a_list == [1, 0, 3]
    # exhaustive method
    v_list, a_list_opt = exhaustive_allocate(quantity, v_list)
    assert v_list == [8, 5, 2]
    assert a_list_opt == [[0, 2, 2], [1, 0, 3]]

    # Test CF order
    v_list = [9, 5, 3]
    quantity = 13
    # greedy method
    reminder, v_list, a_list, _ = greedy_allocate(quantity, v_list)
    assert reminder == 0
    assert v_list == [9, 5, 3]
    assert a_list == [0, 2, 1]
    # exhaustive method
    v_list, a_list_opt = exhaustive_allocate(quantity, v_list)
    assert v_list == [9, 5, 3]
    assert a_list_opt == [[0, 2, 1]]


def test_greedy():
    """
    Greedy allocation algorithm calculates right number breads. Test number of order up to 1000.

    Test criteria:
      * The total number of items from all packs is the same as order required
    """
    for v_list in ([5, 3], [8, 5, 2], [9, 5, 3]):
        for quantity in range(1000):
            reminder, v_list, a_list, _ = greedy_allocate(quantity, v_list)
            assert np.dot(a_list, v_list) + reminder == quantity


def test_greedy_with_exhaustive():
    """
    test greedy method with exhaustive method for given pack sizes. Test order quantity up to 100.

    Criteria: for an valid order:
       1. If the exhaustive method finds at least one answer, greedy will find a answer.
       2. If the greedy method finds a answer. exhaustive method will find at least one answer.
    """
    for v_list in ([5, 3], [8, 5, 2], [9, 5, 3]):
        for quantity in range(100):
            v_list, a_lists_opt = exhaustive_allocate(quantity, v_list)
            reminder, v_list, a_list, _ = greedy_allocate(quantity, v_list)
            if a_lists_opt is not None:
                assert reminder == 0
            if reminder != 0:
                assert a_lists_opt is None
