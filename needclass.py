import pygame 
from random import randint 
from pygame.locals import *
from configure import *




class Cell:
    "单元类，一个一个的小方格。"
    size=cell_size
    def __init__(self,coorx,coory):
        self.coorx=coorx
        self.coory=coory

class Field:
    "场地类，由若干个小方格组成。"
    coorxlimit,coorylimit=cell_num_x,cell_num_y
    xlimit,ylimit=coorxlimit*Cell.size,coorylimit*Cell.size
    def __init__(self):
        self.Cells=[[0] * Field.coorylimit for i in range(0, Field.coorxlimit)]
        for coorx in range(0,Field.coorxlimit):
            for coory in range(0,Field.coorylimit):
                self.Cells[coorx][coory]=Cell(coorx,coory)
    def draw(self,screen):
        for y in range(0,Field.ylimit,Cell.size):
            pygame.draw.line(screen,lines_color,(0,y),(Field.xlimit,y))
        for x in range(0,Field.xlimit,Cell.size):
            pygame.draw.line(screen,lines_color,(x,0),(x,Field.ylimit))

class Apple:
    "苹果类，占地一个小方格。"
    def __init__(self,field):
        coorx=randint(0,Field.coorxlimit-1)
        coory=randint(0,Field.coorylimit-1)
        self.pos=field.Cells[coorx][coory]
    def draw(self,screen):
        x=self.pos.coorx*Cell.size
        y=self.pos.coory*Cell.size
        rect = pygame.Rect(x, y, Cell.size, Cell.size)
        pygame.draw.rect(screen, apple_color, rect)

class Snake:
    "蛇类，有draw(),crawl(),eat()等方法"
    startspeed=snake_start_speed
    speedadd=snake_speed_addonetime
    def __init__(self,Field):
        start_coorx=randint(snake_length+2,Field.coorxlimit-snake_length-3)
        start_coory=randint(snake_length+2,Field.coorylimit-snake_length-3)
        self.pos=[]
        for i in range(snake_length):
            self.pos.append(Field.Cells[start_coorx-i][start_coory])
        self.head=self.pos[0]
        self.direction='right'
        self.speed=Snake.startspeed
    def draw(self,screen):
        for _pos in self.pos:
            x=_pos.coorx*Cell.size
            y=_pos.coory*Cell.size
            rect = pygame.Rect(x, y, Cell.size, Cell.size)
            pygame.draw.rect(screen,snake_color,rect)
    def crawl(self,field):
        dir=self.direction
        coorx=self.head.coorx
        coory=self.head.coory
        if dir=='right':
            coorx+=1
        elif dir=='left':
            coorx-=1
        elif dir=='down':
            coory+=1
        elif dir=='up':
            coory-=1
        if coorx==-1 or coory==-1 or coorx==Field.coorxlimit or coory==Field.coorylimit:
            return 'collide'
        for _pos in self.pos[1:]:
            if coorx==_pos.coorx and coory==_pos.coory:
                return 'collide'
        self.head=field.Cells[coorx][coory]
        self.pos.insert(0,self.head)
        return 'none'
        
    def eat(self,apple):
        coorx=self.head.coorx
        coory=self.head.coory
        if coorx==apple.pos.coorx and coory==apple.pos.coory:
            self.speed+=Snake.speedadd
            return True
        return False