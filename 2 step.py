import pygame, sys, time
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
GREEN = (56, 145, 5)
WHITE = (255, 255, 255)

windowsSurface.fill(WHITE)

b1 = {'rect':pygame.Rect(200, 250, 30, 30), 'color':PURPLE, 'dir':DOWNLEFT}
b2 = {'rect':pygame.Rect(200, 250, 30, 30), 'color':BLUE, 'dir':DOWNRIGHT}
b3 = {'rect':pygame.Rect(200, 250, 30, 30), 'color':RED, 'dir':UPLEFT}
b4 = {'rect':pygame.Rect(200, 250, 30, 30), 'color':GREEN, 'dir':UPRIGHT}
boxes = [b1, b2, b3, b4]

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    for b in boxes:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > 400:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > 500:
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        pygame.draw.rect(windowsSurface, b['color'], b['rect'])
        time.sleep(0.000005)
