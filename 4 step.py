import pygame, sys, random
from pygame.locals import *
pygame.init()

mainClock = pygame.time.Clock()

WINDOWWIDTH = 1920
WINDOWHEIGHT = 1020
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_icon(pygame.image.load('img/player.png'))
pygame.display.set_caption('Collision Detection')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

FOODSIZE = 20
player = pygame.Rect(300, 100, 80, 80)
playerImage = pygame.image.load('img/player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (80, 80))
foodImage = pygame.image.load('img/apple.png')
foods = []
for i in range(100):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

foodCounter = 0
NEWFOOD = 4

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 10

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
    windowSurface.fill(WHITE)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    windowSurface.blit(playerStretchedImage, player)

    # pygame.draw.rect(windowSurface, BLACK, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 1, player.height + 1)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))

    for food in foods:
        windowSurface.blit(foodImage, food)
    pygame.display.update()
    mainClock.tick(40)