class Matrix:
    def __init__(self, width: int, height: int, cell_object: None):
        self.width = width
        self.height = height
        self.cell_object = cell_object
        self.matrix = self._create_grid()

    def _create_grid(self):
        if self.cell_object:
            return [[self.cell_object(x, y) for y in range(self.height)] for x in range(self.width)]
        else:
            return [[0 for _ in range(self.height)] for _ in range(self.width)]

    def print_grid(self):
        for row in self.matrix:
            row_str = ''.join([value.__str__() for value in row])
            print(row_str)
