from needclass import *
import pygame 
import random 
import sys
from pygame.locals import *

def main():
    global snakespeedclock, screen
    pygame.init()
    snakespeedclock = pygame.time.Clock()
    screen=pygame.display.set_mode((Field.xlimit,Field.ylimit))
    pygame.display.set_caption('Snake')
    while True:
        runGame()

def runGame():
    field=Field()
    snake=Snake(field)
    coincide=True
    while coincide:
        apple=Apple(field)
        coincide=False
        for _pos in snake.pos:
            if _pos.coorx==apple.pos.coorx and _pos.coory==apple.pos.coory:
                coincide=True
        


    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT and snake.direction!= 'left':
                    snake.direction='right'
                elif event.key==K_LEFT and snake.direction!= 'right':
                    snake.direction='left'
                elif event.key==K_DOWN and snake.direction!= 'up':
                    snake.direction='down'
                elif event.key==K_UP and snake.direction!= 'down':
                    snake.direction='up'
                elif event.key==K_ESCAPE:
                    terminate()
        if snake.crawl(field)=='collide':
            return
        if snake.eat(apple):
            coincide=True
            while coincide:
                apple=Apple(field)
                coincide=False
                for _pos in snake.pos:
                    if _pos.coorx==apple.pos.coorx and _pos.coory==apple.pos.coory:
                        coincide=True
        else:
            del snake.pos[-1]
        screen.fill(black)
        field.draw(screen)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()
        snakespeedclock.tick(snake.speed)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ =='__main__':
    try:
        main()
    except SystemExit:
        pass