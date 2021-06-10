from needclass import *
import pygame 
import random 
import sys
from pygame.locals import *
from configure import *

def main():
    global snakespeedclock, screen
    pygame.init()
    snakespeedclock = pygame.time.Clock()
    if full_screen:
        screen=pygame.display.set_mode((Field.xlimit,Field.ylimit),FULLSCREEN)
    else:
        screen=pygame.display.set_mode((Field.xlimit,Field.ylimit))
    pygame.display.set_caption('Snake')
    while True:
        runGame()

def addapple(field,snake):
    coincide = True
    while coincide:
        apple=Apple(field)
        coincide=False
        for _pos in snake.pos:
            if _pos.coorx==apple.pos.coorx and _pos.coory==apple.pos.coory:
                coincide=True
        return apple

def runGame():
    field=Field()
    snake=Snake(field)
    apple = addapple(field,snake)

    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            elif event.type==KEYDOWN:
                _dir = snake.direction
                if event.key in [K_RIGHT ,K_d] and _dir!= 'left':
                    snake.direction='right'
                elif event.key in [K_LEFT ,K_a] and _dir!= 'right':
                    snake.direction='left'
                elif event.key in [K_DOWN ,K_s] and _dir!= 'up':
                    snake.direction='down'
                elif event.key in [K_UP,K_w] and _dir!= 'down':
                    snake.direction='up'
                elif event.key==K_ESCAPE:
                    terminate()
                elif event.key in [K_SPACE ,K_p] :
                    pause()
        if snake.crawl(field)=='collide':
            return
        if snake.eat(apple):
            apple = addapple(field,snake)
        else:
            del snake.pos[-1]
        screen.fill(backgound_color)
        field.draw(screen,snake)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()
        snakespeedclock.tick(snake.speed)


def terminate():
    pygame.quit()
    sys.exit()

def pause():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE or event.key==K_p:
                    return
                if event.key==K_ESCAPE:
                    terminate()

if __name__ =='__main__':
    try:
        main()
    except SystemExit:
        pass