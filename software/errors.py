"""
Bakery pricing errors.
"""


class NoSolution(Exception):
    def __init__(self, message='No solution!'):
        super().__init__(message)


class ExceedCapacity(Exception):
    def __init__(self, message='Exceed production capacity!'):
        super().__init__(message)
