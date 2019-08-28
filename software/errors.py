class NoSolution(Exception):
    def __init__(self, message='No solution'):
        super().__init__(message)