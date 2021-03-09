number = int(input('Enter your Number:-'))
nums = (0,1,2,3,4,5,6,7,8,9)

binaries = ([1,1,1,1,1,1,0],[1,1,0,0,0,0,0],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],
[1,1,0,0,1,0,1],[0,1,1,0,1,1,1],[0,1,1,1,1,0,1],[1,1,0,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1])

positions = ([200,110,10,50],[200,170,10,50],[150,220,50,10],[140,170,10,50],[140,110,10,50],[150,100,50,10],[150,160,50,10])

import pygame, sys
pygame.init()

size = width,height = 400,400
running = True
segments = []
screen = pygame.display.set_mode(size)

def draw_rect(x,y,width,height):
    pygame.draw.rect(screen,(0,0,0),(x,y,width,height))

def draw_digit(surf, color, offset, i):
    for j, on in enumerate(binaries[i]):
        if on:
            pygame.draw.rect(surf, color, pygame.Rect(positions[j]).move(offset, 0))

array = []
for i in str(number):
    array.append(int(i))
print(array)

while running:
    screen.fill((148,241,251))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        run = False
        sys.exit()

    for i in array:
        if len(array) == 1:
            draw_digit(screen, 'black', -100,array[0])
        elif len(array) ==2:
            draw_digit(screen, 'black', -100,array[0])
            draw_digit(screen, 'black', 0,array[1])
        elif len(array) == 3:
            draw_digit(screen, 'black', -100,array[0])
            draw_digit(screen, 'black', 0,array[1])
            draw_digit(screen, 'black', 100,array[2])
    pygame.display.update()
