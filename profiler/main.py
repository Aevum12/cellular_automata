import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pygame as p
from line_profiler import profile

from src.main import App
from src.game.griditerator import GridIterator
from src.game.ruleset import Ruleset
from src.game.settings import WIDTH, HEIGHT, CELL_SIZE, FONT_SIZE, BORDER_WIDTH

import timeit

CYCLE_AMOUNT = 50


def measure_time(func, func_name, log_file_name, cycle_amount=50):
    average_execution_time_per_cycle = timeit.timeit(func, number=cycle_amount) / cycle_amount
    log_string = f"Среднее время выполнения {func_name}: {average_execution_time_per_cycle} секунд"
    print(log_string)
    with open(log_file_name, 'a') as log_file:
        log_file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': ' + log_string + '\n')


def write_to_log(log_file_name, log_string, comment=''):
    with open(log_file_name, 'a') as log_file:
        log_file.write(log_string + ' ' + comment + '\n')


if __name__ == '__main__':
    app = App()
    rules = Ruleset(rule_name='conway', alive_state=0, dead_state=1)
    grid = GridIterator(WIDTH, HEIGHT, rules)
    grid.set_random_state()

    write_to_log('log.txt', f'Start {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 'conway')
    measure_time(lambda: app.render_grid(grid=grid), 'app.render_grid', 'log.txt')
    measure_time(lambda: next(grid), 'next(grid)', 'log.txt')
    measure_time(lambda: rules.apply_rules_for_grid(grid.current_state), 'rules.apply_rules_for_grid', 'log.txt')
    measure_time(lambda: rules.apply_rules_for_one_cell_new(grid.current_state[0][0], grid.current_state),
                 'rules.apply_rules_for_one_cell_new', 'log.txt')
    write_to_log('log.txt', f'End {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
