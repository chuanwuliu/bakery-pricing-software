"""
Bakery pricing errors.
"""


class NoSolution(Exception):
    def __init__(self, message='No solution!'):
        super().__init__(message)


class ExceedCapacity(Exception):
    def __init__(self, message='Exceed production capacity!'):
        super().__init__(message)

class ProductCodeError(Exception):
    def __init__(self, message='Code error in order!'):
        super().__init__(message)
