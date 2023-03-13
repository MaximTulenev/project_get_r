import pygame, sys
from pygame.locals import *
pygame.init()
windowsSurface = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Second game')

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
MOVESPEED = 2

PURPLE = (50, 2, 232)
BLUE = (30, 143, 202)
RED = (235, 86, 66)
GREEN = (56, 645, 5)

b1 = {'rect':pygame.Rect(200, 80, 50, 100), 'color':PURPLE, 'dir':DOWNLEFT}
b2 = {'rect':pygame.Rect(200, 80, 50, 100), 'color':BLUE, 'dir':DOWNRIGHT}
b3 = {'rect':pygame.Rect(200, 80, 50, 100), 'color':RED, 'dir':UPLEFT}
b4 = {'rect':pygame.Rect(200, 80, 50, 100), 'color':GREEN, 'dir':UPRIGHT}
boxes = [b1, b2, b3, b4]


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()