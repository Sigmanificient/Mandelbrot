import math
import random

import numba
import pygame

win_size_x = 1024
win_size_y = 710

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_size_x, win_size_y))


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
