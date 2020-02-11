import pygame
import sys
import time

from pygame.locals import *

# Constantes para dibujar en el centro
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

max_iteration = 40
scale = 5.0 / (SCREEN_HEIGHT * 100) # ramas saliendo de la izquierda


def init():
    global screen, atoms, cell, font
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # , pygame.FULLSCREEN
    # font = pygame.font.Font('Vera.ttf', 9)
    #pygame.mouse.set_cursor((8, 8), (0, 0), (0,) * int(64 / 8), (0,) * int(64 / 8))  # Trick, no visible cursor


def cycle():
    return


def update_screen():
    global screen, mouse_pos
    screen.fill((255, 255, 255))
    draw_field(screen)
    pygame.display.flip()


def main():
    #global scale
    while True:
        update_screen()
        time.sleep(1000)


def iteration(c):
    i = 0
    z = 0
    mag = 0.0
    while mag < 4.0 and i < max_iteration:
        z = z ** 2 + c
        mag = z.imag * z.imag + z.real * z.real
        i += 1
    return i


def set_color(i):
    if i == max_iteration:
        col = (0, 0, 0)
        return col
    else:
        c = (i * 15)
        g = 255
        b = 255
        r = 255 - c
        if r < 0:
            r = 0
            g = 255 * 2 - c
            if g < 0:
                g = 0
                b = 255 * 3 - c
                if b < 0:
                    r = g = b = 0
        return (r, g, b)


def draw_field(scr):
    j = 0 + 1j
    for scr_x in range(SCREEN_WIDTH):
        for scr_y in range(SCREEN_HEIGHT):
            x = (scr_x - CENTER_X) * scale - 0.001
            y = (scr_y - CENTER_Y) * scale - 0.75
            c = x + y * j
            iter_value = iteration(c)
            col = set_color(iter_value)
            pygame.draw.line(scr, col, (scr_x, scr_y), (scr_x, scr_y))


init()
main()
