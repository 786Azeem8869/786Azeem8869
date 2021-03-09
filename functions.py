import pygame, sys
from data import *

pygame.init()
nums = (0,1,2,3,4,5,6,7,8,9)

binaries = ([1,1,1,1,1,1,0],[1,1,0,0,0,0,0],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],
[1,1,0,0,1,0,1],[0,1,1,0,1,1,1],[0,1,1,1,1,0,1],[1,1,0,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1])

positions = ([200,110,10,50],[200,170,10,50],[150,220,50,10],[140,170,10,50],[140,110,10,50],[150,100,50,10],[150,160,50,10])

size = width,height = 400,400
run = True
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def draw_digit(surf, color, offset, i):
    for j, on in enumerate(binaries[i]):
        if on:
            pygame.draw.rect(surf, color, pygame.Rect(positions[j]).move(offset, 0))

count = 0
while run:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((148,241,251))
    draw_digit(screen, "black", 0, count // 10)
    draw_digit(screen, "black", 100, count % 10)
    count += 1
    if count >= 100:
        count = 0
    pygame.display.update()
