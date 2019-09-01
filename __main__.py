import os
import sys
import json
import argparse

#
work_dir = os.path.dirname(__file__)
sys.path.append(work_dir)


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', dest='input_file', required=True, help='Path to input json file')
    parser.add_argument('-output', dest='output_file', help='Path to store output json file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    work_dir = os.path.dirname(__file__)
    sys.path.append(work_dir)

    from software import Processor

    p = Processor()

    input_file = args().input_file
    input_data = p.order_data(input_file)
    output = p.process_order(input_data)

    output_file = args().output_file
    if output_file:
        with open(output_file, 'w') as file:
            json.dump(output, file, indent=4)
    else:
        print(json.dumps(output, indent=4))
