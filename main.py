import inspect

import pygame
from pygame import gfxdraw  # Module not present in pygame default import, why ?
from numba import njit

win_size_x = 1024
win_size_y = 710
RED = (255, 0, 0)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_size_x, win_size_y))

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)


class Filter:

    def __init__(self, condition, modifier):
        self.condition = condition
        self.modifier = modifier
        self.active = True

        self.needed_parameters = {
            'condition': tuple(inspect.signature(condition).parameters.keys()),
            'modifier': tuple(inspect.signature(modifier).parameters.keys())
        }

        print(self.needed_parameters)

    def apply(self, **kwargs):
        if not self.active:
            return kwargs['rgb']

        cond_args = [
            kwargs[kwarg] for kwarg in kwargs if kwarg in self.needed_parameters['condition']
        ]

        if not self.condition(*cond_args):
            return kwargs['rgb']

        modifier_args = [
            kwargs[kwarg] for kwarg in kwargs if kwarg in self.needed_parameters['modifier']
        ]

        return self.modifier(*modifier_args)


class App:

    def __init__(self):
        self.is_running = True
        self.show_progress_bar = True
        self.filters = [
            Filter(lambda i, n: (i / n) % 2, lambda i: (i, i, i)),
            Filter(lambda i, n: (i / n) == 1, lambda: (0, 0, 0)),
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_SPACE:
            self.show_progress_bar = not self.show_progress_bar

    def run(self):
        mandelbrot_points = get_points(100)
        x, y = 0, 0

        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)

            for y in range(win_size_y):
                x, i, n, z = next(mandelbrot_points)
                gfxdraw.pixel(screen, x, y, get_color(i, n, z))

            if self.show_progress_bar:
                gfxdraw.line(screen, x + 1, 0, x + 1, win_size_y, RED)

            pygame.display.set_caption(f"Mandelbrot - {((x * y) / (win_size_x * win_size_y)) * 100:0>2.0f}% done")
            pygame.display.update()
            clock.tick(-1)


@njit
def get_points(n):
    while True:
        for x in range(win_size_x):
            for y in range(win_size_y):
                z = 0 + 0j
                c = complex(
                    3.5 * x / (win_size_x - 1) - 2.5,
                    -2.5 * y / (win_size_y - 1) + 1.25
                )

                i = 0

                while i < n and abs(z) < 2:
                    z = z ** 2 + c
                    i += 1

                yield x, i, n, z


def get_color(i, n, z):
    rgb = [0] * 3

    for _filter in app.filters:
        rgb = _filter.apply(rgb=rgb, i=i, n=n, z=z)

    return rgb


if __name__ == '__main__':
    app = App()
    app.run()
