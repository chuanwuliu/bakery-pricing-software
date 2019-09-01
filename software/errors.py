"""
Bakery pricing errors.
"""


class NoSolution(Exception):
    def __init__(self, message='No solution!'):
        super().__init__(message)


class ProductError(Exception):
    def __init__(self, message='Product Error!'):
        super().__init__(message)


class OrderError(Exception):
    def __init__(self, message='Order Error!'):
        super().__init__(message)
