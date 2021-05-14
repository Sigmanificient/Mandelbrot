import math
import random

import numba
import pygame
from pygame import gfxdraw  # Module not present in pygame default import, why ?

win_size_x = 1024
win_size_y = 710

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_size_x, win_size_y))

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)


class App:

    def __init__(self):
        self.is_running = True

    def __call__(self):
        while self.is_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            pygame.display.update()
            clock.tick(-1)


if __name__ == '__main__':
    app = App()
    app()
