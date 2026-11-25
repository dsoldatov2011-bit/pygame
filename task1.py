from idlelib.debugobj_r import WrappedObjectTreeItem

import pygame as pg

FPS = 1000000000
WIDTH, HEIGHT = 1000, 600

# цвета выбраны с сайта: https://htmlcolorcodes.com/
MINT = (181, 222, 149)
WHITE = (255, 255, 255)
RED = (255, 39, 0)
BLACK = (0, 0, 0)
ORANGE = (238, 181, 50)
FIRE = (245, 112, 37)
GREEN = (84, 138, 77)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(MINT)  # заливка фона
pg.display.set_caption("Игра")
clock = pg.time.Clock()

r = 250
pg.draw.circle(screen, RED, (WIDTH / 2, HEIGHT / 2), r)
pg.draw.rect(screen, ORANGE, (WIDTH / 2 - r, HEIGHT / 2, r * 2, r))
pg.draw.polygon(screen, BLACK, [[WIDTH / 2, HEIGHT / 2 - r], [WIDTH / 2 - r, HEIGHT / 2], [WIDTH / 2 + r, HEIGHT / 2]])
pg.draw.polygon(screen, GREEN, [[WIDTH / 2 - r, HEIGHT / 2], [WIDTH / 2 + r, HEIGHT / 2], [WIDTH / 2, HEIGHT / 2 + r]])
pg.draw.line(screen, WHITE, [WIDTH, HEIGHT / 2], [WIDTH / 2, HEIGHT / 2 - r], 4)
pg.draw.line(screen, WHITE, [0, HEIGHT / 2], [WIDTH / 2, HEIGHT / 2 - r], 4)

# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
