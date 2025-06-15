import numpy as np
class Matrix:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # self.cell_object = cell_object
        # self.matrix = self._create_grid()
        self.matrix = self._create_grid_numpy()
    def _create_grid(self):
        if self.cell_object:
            matrix = [[self.cell_object(x, y) for y in range(self.height)] for x in range(self.width)]
            matrix = np.array(matrix)
            return matrix
        else:
            return [[0 for _ in range(self.height)] for _ in range(self.width)]

    def _create_grid_numpy(self):
        return np.zeros((self.width, self.height), dtype=int)

    def print_grid(self):
        for row in self.matrix:
            row_str = ' '.join([value.__str__() for value in row])
            print(row_str)


if __name__ == '__main__':
    m = Matrix(10, 10)
    m.print_grid()