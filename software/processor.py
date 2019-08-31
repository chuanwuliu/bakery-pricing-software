"""
Main processor for processing the order and print the output.
"""

import os
import json
import numpy as np
from .errors import *
from .algos import greedy_allocate, exhaustive_allocate

work_dir = os.path.dirname(__file__)
projects_path = os.path.join(work_dir, 'products.json')


class Processor(object):
    """
    Processor class
    """
    def __init__(self, product_table=None, algorithm='greedy'):
        """
        Processor initialization.

        :param product_table: dict, product table, default None.
        """
        self._product_table = product_table
        self._algorithm = algorithm

    @property
    def algorithm(self):
        return self._algorithm

    @property
    def product_table(self):
        """
        Product data frame.
        """
        if self._product_table is None:
            with open(projects_path) as file:
                self._product_table = json.load(file)
        return self._product_table

    def pack_table(self, code: str):
        """
        Pack data of the given code.

        :param code, str, product code
        :return dict
        """
        return self.product_table[code]

    def pack_volumes(self, code):
        """
        List of volumes/units of units of packs per code.

        :param code: str, product code
        :return: list
        """
        v_list = [pack['units'] for pack in self.pack_table(code)]
        return v_list

    def pack_price(self, code: str, units: int):
        """
        Price of pack with given code and units.

        :param code: str, product code
        :param units: int, number of unit
        :return: int, price
        """
        for pack in self.pack_table(code):
            if pack['units'] == units:
                return pack['price']
        raise ProductError('{} {} <== Pack price not found!'.format(units, code))

    def capacity(self, code: str):
        """
        Maximum production capacity of the bakery.

        :param code: str, product code
        :return: int
        """
        if code in self.product_table['capacity']:
            return self.product_table['capacity'][code]
        else:
            return np.inf

    def order_data(self, path: str):
        """
        Input order data read from the file path. the input file must in JSON format.

        :param path: str, path to order file
        :return: dict
        """
        with open(path) as file:
            order = json.load(file)

        for code, quantity in order.items():
            if code not in self.product_table:
                raise OrderError('{} <== Wrong order code!'.format(code))
            if quantity > self.capacity(code):
                raise OrderError('{} <== Order quantity exceed capacity!'.format(quantity))
            if quantity % 1 > 0 or quantity < 1:
                raise OrderError('{} <== Only positive integers accepted!'.format(quantity))
        return order

    def process_order(self, path: str):
        """
        Process the order from the file path. The input file must be in JSON format.

        :param path: str, path to the input order.
        """
        order = self.order_data(path)
        output = {}

        for code, quantity in order.items():
            # Allocate packs to order using algorithms
            v_list = self.pack_volumes(code)
            price_list = [self.pack_price(code, units) for units in v_list]

            if self.algorithm.lower() == 'greedy':
                remainder, v_list, a_list, pointer = greedy_allocate(quantity, v_list)
                if remainder > 0:
                    raise NoSolution("{} <-- {}".format(v_list, remainder))
            elif self.algorithm.lower() == 'exhaustive':
                v_list, a_list_opt = exhaustive_allocate(quantity, v_list)
                if a_list_opt is None:
                    raise NoSolution()
                a_list = a_list_opt[0]
            else:
                raise ValueError('Wrong Algorithm!')

            output[code] = {}
            total_price = np.dot(a_list, price_list).sum()
            output[code]["price"] = total_price
            output[code]['packs'] = {}
            for i in range(len(a_list)):
                if a_list[i] > 0:
                    pack = '{} $ {}'.format(v_list[i], price_list[i])
                    output[code]['packs'][pack] = a_list[i]

            # This is tweak for printing expected example
            total_price = np.dot(a_list, price_list).sum()
            print("{} {} $ {}".format(quantity, code, total_price.round(2)))
            for i in range(len(v_list)):
                a = a_list[i]
                if a > 0:
                    print('      {} \u2715 {} $ {}'.format(a, v_list[i], price_list[i]))

        return output

if __name__ == '__main__':
    p = Processor()
    path = '/Users/charles_liu/Github/bakery-pricing-software/tests/input_1.csv'
    print(p.process_order(path))

