import os
import json
from software import Processor

work_dir = os.path.dirname(__file__)


def test_input_example():
    """
    Test input from the specification.
    """
    input_file = os.path.join(work_dir, 'input_example.json')
    output_file = os.path.join(work_dir, 'output_example.json')
    assert compare_outputs(input_file, output_file)


def test_input_large():
    """
    Test input with large number of orders.
    """
    input_file = os.path.join(work_dir, 'input_large.json')
    output_file = os.path.join(work_dir, 'output_large.json')
    assert compare_outputs(input_file, output_file)


def compare_outputs(input_file, output_file):
    """
    Compare the data derived with input_file with the expected data from output_file with
    :param input_file: str, input order data, must be in json format
    :param output_file: str, expected output, must be in json format

    Test procedures:
      1. Read input data from the input file
      2. Instantiate a processor, process the order data to get the derived output
      3. Read expected output from the output file
      4. Test the derived output is the same as expected
    """

    input_file = os.path.join(work_dir, input_file)
    with open(input_file) as file:
        input_data = json.load(file)

    p = Processor()
    derived_output = p.process_order(input_data)

    output_file = os.path.join(work_dir, output_file)
    with open(output_file) as file:
        expected_output = json.load(file)

    return derived_output == expected_output
