import pygame as p
from src.game.griditerator import GridIterator
from src.game.ruleset import Ruleset
from src.game.settings import WIDTH, HEIGHT, CELL_SIZE, FONT_SIZE, BORDER_WIDTH


class App:
    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
        self.clock = p.time.Clock()
        self.running = True
        self.base_font = p.font.Font(None, FONT_SIZE)

    def render_grid(self, grid: GridIterator):
        for index_x, column in enumerate(grid.current_state):
            for index_y, cell in enumerate(column):
                cell.draw_square(self.screen, border_width=BORDER_WIDTH)
        p.display.flip()

    def run(self):
        rules = Ruleset(rule_name='conway', alive_state=0, dead_state=1)
        grid = GridIterator(WIDTH, HEIGHT, rules)
        grid.set_random_state()
        waiting_for_space = False
        while self.running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.running = False
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        waiting_for_space = False
                    # elif event.key == p.K_DOWN:
                    #     waiting_for_down = False
            self.screen.fill("white")
            self.render_grid(next(grid))
            # grid.print_grid()
            # p.time.delay(1000)
            self.clock.tick(10)
            waiting_for_space = True
        p.quit()


if __name__ == '__main__':
    app = App()
    app.run()
