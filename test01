from collections import namedtuple
from functools import partial
from pygame.locals import *
import pygame
from random import randint
import sys

Point = namedtuple('Point', 'x y')
X_max, Y_max, scale = 40, 25, 20
white, black = (255, 255, 255), (0, 0, 0)


def ranpoint(x_min=0, x_max=X_max-1, y_min=0, y_max=Y_max-1):
    return Point(randint(x_min, x_max), randint(y_min, y_max))


def addpoint(p1, p2): return Point(p1.x+p2.x, p1.y+p2.y)


pygame.init()
speedclock = pygame.time.Clock()
screen = pygame.display.set_mode((X_max*scale, Y_max*scale))

dline = partial(pygame.draw.line, screen, black)


def drect(left, top):
    pygame.draw.rect(screen, black, pygame.Rect(left, top, scale, scale))


# 生成蛇
head = ranpoint(x_min=2, x_max=X_max-3)
snake = []
for i in range(3):
    body = addpoint(head, Point(-1*i, 0))
    snake.append(body)
dirpoint = Point(1, 0)  # 方向
dirs = {'UP': Point(0, -1), 'DOWN': Point(0, 1),
        'LEFT': Point(-1, 0), 'RIGHT': Point(1, 0)}

# 生成苹果


def getapple():
    while(True):
        apple = ranpoint()
        for body in snake:
            if body == apple:
                break
        else:
            return apple


apple = getapple()


def terminate():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_UP and dirpoint != dirs['DOWN']:
                dirpoint = dirs['UP']
            if event.key == K_DOWN and dirpoint != dirs['UP']:
                dirpoint = dirs['DOWN']
            if event.key == K_LEFT and dirpoint != dirs['RIGHT']:
                dirpoint = dirs['LEFT']
            if event.key == K_RIGHT and dirpoint != dirs['LEFT']:
                dirpoint = dirs['RIGHT']

    # 判断蛇是否发生碰撞
    newhead = addpoint(head, dirpoint)
    if 0 <= newhead.x < X_max and 0 <= newhead.y < Y_max:
        pass
    else:
        terminate()
    for body in snake:
        if body == newhead:
            terminate()
    snake.insert(0, newhead)
    head = newhead

    for body in snake:
        if body == apple:
            apple = getapple()
            break
    else:
        del snake[-1]

    screen.fill(white)

    for y in range(1, Y_max):
        dline((0, y*scale), (X_max*scale, y*scale))

    for x in range(1, X_max):
        dline((x*scale, 0), (x*scale, Y_max*scale))

    for body in snake:
        drect(body.x*scale, body.y*scale)

    drect(apple.x*scale, apple.y*scale)
    pygame.display.update()
    speedclock.tick(10)
