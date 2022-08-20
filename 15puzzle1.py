# its a 15-puzzle game project
import numpy as np
import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 800, 800
size = (HEIGHT//4)/1.1
color = [(0,0,0), (255,48,48), (255,255,255), (0, 255, 0)] #BLACK, RED, WHITE, GREEN

xlist = [(size*0.05), ((HEIGHT/4) + size*0.05), ((HEIGHT/2) + size*0.05), ((HEIGHT/4)*3 + size*0.05)]
ylist = [(size*0.05), ((HEIGHT/4) + size*0.05), ((HEIGHT/2) + size*0.05), ((HEIGHT/4)*3 + size*0.05)]
xchoice, ychoice = xlist[3], ylist[3]

ax = np.array([[(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])]])
ay = np.array([[(ylist[0]), (ylist[0]), (ylist[0]), (ylist[0])],
               [(ylist[1]), (ylist[1]), (ylist[1]), (ylist[1])],
               [(ylist[2]), (ylist[2]), (ylist[2]), (ylist[2])],
               [(ylist[3]), (ylist[3]), (ylist[3]), (ylist[3])]])

#np.random.ranint()
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("15PUZZLE by Pablo") 

def rect():
    pass

def rarray():
    global num
    num = np.random.choice(16, size=(4, 4), replace=False)
    print(num)

rarray()

#Main Game loop
gameOn = True
screen.fill((color[0]))
while gameOn:
    
    for event in pg.event.get():
        if event.type == K_UP:
            pass
        if event.type == K_DOWN:
            pass
        if event.type == K_RIGHT:
            pass
        if event.type == K_LEFT:
            pass
        elif event.type == QUIT:
            gameOn = False 
    
    for x in range(4):
        for y in range(4):
            if num[x, y] != 0:
                pg.draw.rect(screen, (color[2]),((ax[x ,y]), (ay[x ,y]), size, size), 5, 10,)
            elif num[x, y] == 0:
                pg.draw.rect(screen, (color[1]), ((ax[x ,y]), (ay[x ,y]), size, size), 5, 10)
    pg.display.update()

    


