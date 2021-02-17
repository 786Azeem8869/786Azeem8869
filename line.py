import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
Clock = pygame.time.Clock()
startpoint = pygame.math.Vector2(320, 240)
endpoint = pygame.math.Vector2(170, 0)
angle = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    # % 360 to keep the angle between 0 and 360.
    angle = (angle+1) % 360
    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    current_endpoint = startpoint + endpoint.rotate(angle)

    pygame.draw.line(screen, (255,0,0), startpoint, current_endpoint, 2)

    pygame.display.update()
    Clock.tick(60)

pygame.quit()
sys.exit()
