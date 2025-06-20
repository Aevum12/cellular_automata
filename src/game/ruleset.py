from src.game.matrix import Matrix
from src.game.cell import Cell

import numpy as np


class Ruleset:
    rules = {'conway': {'full name': 'Conway’s Game of Life (B3/S23)',
                        'birth': [3, ],
                        'survive': [2, 3]},
             'high_life': {'full name': 'High Life (B36/S23)',
                           'birth': [3, 6],
                           'survive': [2, 3, ]},
             'maze': {'full name': 'Maze (B3/S12345)',
                      'birth': [3, ],
                      'survive': [1, 2, 3, 4, 5]},
             'replicator': {'full name': 'Replicator (B1357/S1357)',
                            'birth': [1, 3, 5, 7],
                            'survive': [1, 3, 5, 7]},
             'seeds': {'full name': 'Seeds ((B2/S))',
                       'birth': [2, ],
                       'survive': []}
             }

    def __init__(self, rule_name: str, alive_state: int = 1, dead_state: int = 0):
        '''
        :param rule_name: one of the rules list ['conway', 'high_life', 'maze', 'replicator', 'seeds']
        :param alive_state: choose which state considered as alived state
        :param dead_state: choose which state considered as dead state
        '''
        self.alive_state = alive_state
        self.dead_state = dead_state
        if rule_name in self.rules:
            self.full_name = self.rules[rule_name]['full name']
            self.birth = self.rules[rule_name]['birth']
            self.survive = self.rules[rule_name]['survive']
        else:
            raise ValueError

    # def apply_rules_for_one_cell(self, cell: Cell, matrix: list) -> [bool, int, list]:
    #     temp_grid = Matrix(3, 3, Cell).matrix
    #     width = len(matrix)
    #     height = len(matrix[0])
    #     cell_neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    #     count = 0
    #     is_alive = False
    #     for neighbor in cell_neighbors:
    #         try:
    #             if matrix[(cell.x + neighbor[0]) % width][
    #                 (cell.y + neighbor[1]) % height].state == self.alive_state:
    #                 count += 1
    #                 temp_grid[(neighbor[0] + 1)][(neighbor[1] + 1)].state = self.alive_state
    #             else:
    #                 temp_grid[(neighbor[0] + 1)][(neighbor[1] + 1)].state = self.dead_state
    #         except:
    #             pass
    #     if count in self.birth:
    #         is_alive = True
    #     if count in self.survive and cell.state == self.alive_state:
    #         is_alive = True
    #     return is_alive, count, temp_grid

    def apply_rules_for_one_cell_new(self, matrix: list) -> [bool, int, list]:
        temp_grid = Matrix(3, 3).matrix
        width = len(matrix)
        height = len(matrix[0])
        cell_neighbors = [[-1, -1], [-1, 0], [-1, 1],
                           [0, -1],           [0, 1],
                           [1, -1], [1, 0],  [1, 1]]
        count = 0
        is_alive = False

        for neighbor in cell_neighbors:
            new_x = (cell.x + neighbor[0]) % width
            new_y = (cell.y + neighbor[1]) % height
            neighbor_state = matrix[new_x][new_y].state

            if neighbor_state == self.alive_state:
                count += 1
                temp_grid[(neighbor[0] + 1)][(neighbor[1] + 1)].state = self.alive_state
            else:
                temp_grid[(neighbor[0] + 1)][(neighbor[1] + 1)].state = self.dead_state
        if count in self.birth:
            is_alive = True
        if count in self.survive and cell.state == self.alive_state:
            is_alive = True
        return is_alive, count, temp_grid

    def apply_rules_for_grid(self, matrix: list) -> list:
        width = len(matrix)
        height = len(matrix[0])
        new_matrix = Matrix(width, height, Cell).matrix
        for x, column in enumerate(matrix):
            for y, cell in enumerate(column):
                if self.apply_rules_for_one_cell_new(cell, matrix)[0]:
                    new_matrix[x][y].state = self.alive_state
                else:
                    new_matrix[x][y].state = self.dead_state
        return new_matrix

cell_neighbors = np.array([[-1, -1], [-1, 0], [-1, 1],
                  [0, -1],  [0, 0],  [0, 1],
                  [1, -1], [1, 0],  [1, 1]])


if __name__ == '__main__':
    # m = Matrix(10, 10)
    # m.print_grid()

    mn = np.random.randint(0,9, (5, 5))
    print(mn)
    cell = np.array([2,2])
    # x_start = cell[0]-1
    # x_end = cell[0]+2
    # y_start = cell[1]-1
    # y_end = cell[1]+2
    sub_m = mn[-2:1,-2:1]
    print(sub_m)
    # print(cell_neighbors+cell)
    # print(mn[np.ix_(cell_neighbors)])

