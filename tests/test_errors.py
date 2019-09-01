import os
import json
import pytest
from software import errors
from software import Processor

work_dir = os.path.dirname(__file__)


def test_no_solution():
    """
    Test input with no solution.
    """
    input_file = os.path.join(work_dir, 'input_no_solution.json')
    assert_error(input_file, errors.NoSolution)


def test_exceed_capacity():
    """
    Test if OrderError is raised when order exceeds the production capacity.
    """
    input_file = os.path.join(work_dir, 'input_exceed_capacity.json')
    assert_error(input_file, errors.OrderError)


def no_integer_order():
    """
    Test if OrderError is raised when order has non-integer number.
    """
    input_file = os.path.join(work_dir, 'input_exceed_capacity.json')
    assert_error(input_file, errors.OrderError)


def no_wrong_code():
    """
    Test if OrderError is raised when order has a unexpected product code.
    """
    input_file = os.path.join(work_dir, 'input_wrong_code.json')
    assert_error(input_file, errors.OrderError)


def assert_error(input_file, error):
    """
    Run the software with input_file and test if the error is raised.

    :param input_file: str, input order data, must be in json format
    :param error: expected error

    Test procedures:
      1. Read input data from the input file
      2. Instantiate a processor and process the input data
      3. Test if the expected error raised
    """

    input_file = os.path.join(work_dir, input_file)
    with open(input_file) as file:
        input_data = json.load(file)

    p = Processor()
    with pytest.raises(error):
        p.process_order(input_data)
