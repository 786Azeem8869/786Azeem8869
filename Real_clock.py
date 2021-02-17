import time,pygame
#initialize pygame library
pygame.init()
theFont=pygame.font.Font(None,72)
Clock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 300])
pygame.display.set_caption('Pi Time')
while True:
    Clock.tick(1)
    theTime=time.strftime("%H:%M:%S", time.localtime())
    timeText=theFont.render(str(theTime), True,(255,255,255),(0,0,0))
    screen.blit(timeText, screen.get_rect())
    pygame.display.update()
