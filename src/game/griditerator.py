# from src.game import Cell, Matrix, Ruleset
from src.game.matrix import Matrix
from src.game.cell import Cell
# from src.game.ruleset import Ruleset
# from src.game.matrix import Matrix
import random

from src.game.ruleset import Ruleset


class GridIterator:
    def __init__(self, width: int, height: int, ruleset: Ruleset):
        self.width: int = width
        self.height: int = height
        self.ruleset: Ruleset = ruleset
        self.current_state: list = self._create_grid()
        self.previous_state: list = []
        self.iter_count: int = 0

    def set_random_state(self):
        sequence = [0, 1]
        weights = [1, 4]
        for column in self.current_state:
            for cell in column:
                cell.state = random.choices(sequence, weights=weights, k=1)[0]

    def _create_grid(self):
        return Matrix(self.width, self.height, Cell).matrix

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_count != 0:
            self.previous_state = self.current_state
            self.current_state = self.ruleset.apply_rules_for_grid(self.previous_state)
        self.iter_count += 1
        return self

    def print_grid(self):
        print()
        for row in self.current_state:
            row_str = ''.join(['|█|' if value.state == 1 else '|_|' for value in row])
            print(row_str)
