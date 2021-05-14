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


def main():
    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        pygame.display.update()
        clock.tick(-1)


if __name__ == '__main__':
    main()
