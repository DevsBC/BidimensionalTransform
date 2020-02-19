import pygame
import time

# Constantes para dibujar en el centro
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

max_iteration = 40
scale = 5.0 / (SCREEN_HEIGHT * 100)  # ramas saliendo de la izquierda


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Mi Fractal')

    while True:
        draw_field(screen)
        pygame.display.update()
        time.sleep(1000)


def draw_field(screen):
    # Configuracion de font y size
    font_my_name = pygame.font.Font('freesansbold.ttf', 24)
    font_title = pygame.font.Font('freesansbold.ttf', 24)
    font_definition = pygame.font.Font('freesansbold.ttf', 16)
    font_source = pygame.font.Font('freesansbold.ttf', 12)

    # Colores para mis letras
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # Establece texto y posicion
    my_name = font_my_name.render('Juan Carlos Aranda Alonso', True, green, blue)
    text_rect = my_name.get_rect().center = (450, 0)

    title = font_title.render('Fractales', True, white, black)
    second_text_rect = title.get_rect().center = (550, 200)

    definition = font_definition.render('Objeto geometrico compuesto de elementos de aspecto similar', True, white, black)
    third_text_rect = definition.get_rect().center = (300, 300)

    source = font_source.render('Mandelbrot, B. (1988). The Fractal Geometry of Nature', True, white, black)
    fourth_text_rect = source.get_rect().center = (450, 350)

    for scr_x in range(SCREEN_WIDTH):
        for scr_y in range(SCREEN_HEIGHT):
            x = (scr_x - CENTER_X) * scale - 0.001
            y = (scr_y - CENTER_Y) * scale - 0.75
            c = x + y * 1j
            iter_value = iteration(c)
            col = set_color(iter_value)

            screen.blit(my_name, text_rect)
            screen.blit(title, second_text_rect)
            screen.blit(definition, third_text_rect)
            screen.blit(source, fourth_text_rect)

            pygame.draw.line(screen, col, (scr_x, scr_y), (scr_x, scr_y))


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


main()
