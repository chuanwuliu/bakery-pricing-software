import pandas as pd
from .products import columns, data


def product_table():
    df = pd.DataFrame(data=data, columns=columns)
    return df


def order_table(path):
    """
    path to the oder file. see tests for example order files
    :param path:
    :return:
    """
    df = pd.read_csv(path)
    return df









if __name__ == '__main__':
    pass