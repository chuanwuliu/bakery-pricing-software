import numpy as np
import pandas as pd
from .errors import *
from .config import CAPACITY, columns, data
from .algorithms import greedy_allocate as allocate


class Processor(object):

    def __init__(self, product_table=None):
        self._product_table = product_table

    @property
    def product_table(self):
        """
        Product data frame.
        """
        if self._product_table is None:
            self._product_table = pd.DataFrame(data=data, columns=columns)
        return self._product_table

    def order_data(self, path):
        """
        path to the oder file. see tests for example order files

        :param path: str, path to order file
        :return: pd.DataFrame, order data
        """
        df = pd.read_csv(path)
        quantity = df['quantity']
        if (quantity > CAPACITY).any():
            raise ExceedCapacity()
        if (quantity % 1 > 0).any():
            raise ValueError('{} <== Only integer number accepted!'.format(quantity))
        if set(df.code.unique()) - set(self.product_table.code.unique()):
            raise ProductCodeError()
        return df

    def process_by_code(self, code, quantity):
        df = self.product_table
        items = df[df['code'] == code]
        v_packs = items['units'].to_list()
        try:
            remainder, v_list, a_list, pointer = allocate(quantity, v_packs)
            if remainder > 0:
                raise NoSolution()
        except:
            v_list, a_list_opt = allocate(quantity, v_packs)
            if a_list_opt is None:
                raise NoSolution()
            a_list = a_list_opt[0]
        return v_list, a_list

    def process_order(self, path):
        df_order = self.order_data(path)
        df_prod = self.product_table
        for index, order in df_order.iterrows():
            code = order['code']
            quantity = order['quantity']
            v_list, a_list = self.process_by_code(code, quantity)
            items = df_prod[df_prod['code'] == code]
            p_list = items.sort_values(by='units', ascending=False)['price'].to_list()
            total_price = np.dot(p_list, a_list)
            print("{} {} $ {}".format(quantity, code, total_price.round(2)))
            for i in range(len(v_list)):
                a = a_list[i]
                if a > 0:
                    print('    {} \u2715 {} $ {}'.format(a, v_list[i], p_list[i]))


if __name__ == '__main__':
    p = Processor()
    path = '/Users/charles_liu/Github/bakery-pricing-software/tests/input_1.csv'
    p.process_order(path)
