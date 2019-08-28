import pandas as pd
from .products import columns, data


def products():
    df = pd.DataFrame(data=data, columns=columns)
    return df


def orders(path):
    df = pd.read_csv(path)
    return df








if __name__ == '__main__':
    pass