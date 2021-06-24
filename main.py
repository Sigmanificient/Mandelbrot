import inspect
import pygame
from pygame import gfxdraw  # Module not present in pygame default import, why ?
from numba import njit

RATIO = .69375

win_size_x = 1280
win_size_y = int(win_size_x * RATIO)

RED = (255, 0, 0)
WHITE = (255, 255, 255)
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_size_x, win_size_y))

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)


class Filter:

    def __init__(self, name, condition, modifier):
        self.name = name
        self.condition = condition
        self.modifier = modifier

        self.needed_parameters = {
            'condition': tuple(inspect.signature(condition).parameters.keys()),
            'modifier': tuple(inspect.signature(modifier).parameters.keys())
        }

    def apply(self, **kwargs):
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
        """Initialize App Filters."""
        self.is_running = True
        self.show_progress_bar = True
        self.flush = False

        self.filters = [
            Filter('default', lambda i, n: (i / n) % 2, default_filter),
            # Add your filters here !

            Filter('blue', lambda: True, lambda r, g, b: (r, g, (b * 5) % 255))
        ]

        if len(self.filters) > 10:
            print("Warning: Too many filters, all filters that have an index >10, will not be able to be applied")

        self.active_filters = [0]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_f:
            self.flush = not self.flush
            return

        if event.key == pygame.K_SPACE:
            self.show_progress_bar = not self.show_progress_bar
            return

        if not event.unicode.isdigit():
            return

        key = int(event.unicode)

        if len(self.filters) <= key:
            return

        if key in self.active_filters:
            self.active_filters.remove(key)
            return

        self.active_filters.append(key)

    def get_color(self, i, n, z, x, y):
        rgb = [0] * 3

        for filter_index in self.active_filters:
            r, g, b = rgb
            rgb = self.filters[filter_index].apply(rgb=rgb, i=i, n=n, z=z, r=r, g=g, b=b, x=x, y=y)

        return rgb

    def run(self):
        mandelbrot_points = get_points(100)
        progress = 0
        x, y = 0, 0

        while self.is_running:
            if self.flush and progress == 0.0:
                screen.fill(0)

            for event in pygame.event.get():
                self.handle_event(event)

            for y in range(win_size_y):
                x, i, n, z = next(mandelbrot_points)
                gfxdraw.pixel(screen, x, y, self.get_color(i, n, z, x, y))

            if self.show_progress_bar:
                gfxdraw.line(screen, x + 1, 0, x + 1, win_size_y, RED)

            filter_text = ', '.join(self.filters[filter_index].name for filter_index in self.active_filters)
            if not filter_text:
                filter_text = 'none'

            progress = ((x * y) / (win_size_x * win_size_y)) * 100
            pygame.display.set_caption(f"Mandelbrot - {progress:0>2.0f}% done - filters: {filter_text}")

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


def default_filter(i, n):
    i *= (i/n) % 2 != 1
    return i, i, i


if __name__ == '__main__':
    app = App()
    app.run()
