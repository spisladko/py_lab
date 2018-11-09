import pygame
from pygame.locals import *
import random
import copy


class GameOfLife:


    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed


    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


    def cell_list(self, randomize=True) -> list:
        # создание списка клеток
        self.clist = []
        self.clist = [[0] * self.cell_width for i in range(self.cell_height)]
        if randomize:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    self.clist[i][j] = random.randint(0,1)
        else:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    self.clist[i][j] = 0
        return self.clist


    def draw_cell_list(self, clist: list):
        # отображение списка клеток
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                color_cell = pygame.Color('white')
                if self.clist[i][j] == 1:
                    color_cell = pygame.Color('pink')
                rect = Rect(i, j, sefl.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color_cell, rect)


    def get_neighbours(self, cell: tuple) -> list:
        #список соседей для указанной ячейки
        neighbours = []
        x, y = cell
        for i in  range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(0, self.cell_height) and j in range(0, self.cell_width) and (i != x or j != y):
                    neighbours.append(self.clist[i][j])
        return neighbours


    def update_cell_list(self, cell_list: list) -> list:
        #один шаг игры
        new_clist = copy.deepcopy(self.clist)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if sum(self.get_neighbours((i,j))) == 2:
                    if new_clist[i][j] == 1:
                        new_clist[i][j] = 1
                    else:
                        new_clist[i][j] = 0
                elif  sum(self.get_neighbours((i,j))) == 3:
                        new_clist[i][j] = 1
                else:
                    new_clist[i][j] = 0
        self.clist = new_clist
        return self.clist


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
