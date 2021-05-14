"""
old first version written in mid 2017
"""

from numba import jit
from math import sqrt
from random import randrange
from pygame import display, gfxdraw, event, image, time
from pygame.locals import QUIT, KEYDOWN, K_b

display.init()

clock = time.Clock()

cols = {
    # lambda i, n, z: True: lambda rgb, i, n, z: ((c := sqrt((i/n))*255)//2, c//2, c),
    # lambda i, n, z: (i/n) == 1 : lambda rgb, i, n, z: (0, 255, 0),
    lambda i, n, z: True: lambda rgb, i, n, z: ((c:=255 - int((i / n) * 255)), randrange(255), randrange(128))
    # lambda i, n, z: (i/n) % 2: lambda rgb, i, n, z: (i, i, i),
    # lambda i, n, z: (i/n) == 1: lambda rgb, i, n, z: (0, 0, 0)
}


def get_col(i, n, z):
    rgb = [0, 0, 0]
    for k, v in cols.items():
        if k(i, n, z):
            rgb = v(rgb, i, n, z)
    return rgb


@jit(nopython=True)
def mandelbrot(n, pos):
    while True:
        sx, sy = pos
        for x in range(sx):
            for y in range(sy):
                z = 0 + 0j
                c = complex(3.5 * x / (sx - 1) - 2.5, -2.5 * y / (sy - 1) + 1.25)
                i = 0
                while (i < n) and abs(z) < 2:
                    i += 1
                    z = z ** 2 + c

                yield x, i, n, z


def main():
    sx = 1024
    sy = round(.69375 * sx)
    mandelbrot_points = mandelbrot(100, (sx, sy))

    screen = display.set_mode((sx, sy))
    display.set_icon(image.load("icon.png").convert_alpha())

    run, bar_mode = True, True

    while run:
        for y in range(sy):
            x, i, n, z = next(mandelbrot_points)
            gfxdraw.pixel(screen, x, y, get_col(i, n, z))

        if bar_mode:
            gfxdraw.line(screen, x + 1, 0, x + 1, sy, (255, 0, 0))

        for e in event.get():
            if e.type == QUIT:
                quit()
            elif e.type == KEYDOWN:
                if e.key == K_b:
                    bar_mode = False if bar_mode else True

        display.set_caption(get_title(x, y, sx, sy))
        display.update()
        clock.tick(-1)


def get_title(x, y, sx, sy):
    return f"Mandelbrot visualiser | build : {round(((x * y) / (sx * sy)) * 100, 3)} % | fps : {int(clock.get_fps() * sx)}"


if __name__ == "__main__":
    main()
