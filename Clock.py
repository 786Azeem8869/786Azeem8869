import pygame, time, math
pygame.init()

#Screen
size = width, height = 700, 300 #Make sure background image is same size
screen = pygame.display.set_mode(size)

done = False

Second = int(time.strftime("%S", time.localtime()))
Minute = int(time.strftime("%M", time.localtime()))
Hour = int(time.strftime("%H", time.localtime()))

sec_deg = 270 + Second*6
min_deg = 270 + Minute*6
hour_deg = 270 + Hour*30

#Colour
Black = (0,0,0)
White = (255, 255, 255)

#Fonts
Font = pygame.font.SysFont("Trebuchet MS", 25)

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

def hands(point, color, angle):
    startpoint = pygame.math.Vector2((280,160))
    endpoint = pygame.math.Vector2(point)
    angle = (angle+6) % 360
    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    current_endpoint = startpoint + endpoint.rotate(angle)
    pygame.draw.line(screen, color, startpoint, current_endpoint, 3)
    pygame.display.update()

def clockwiseArc(surface, color, point, radius, startAngle, endAngle):
    rect = pygame.Rect(500, 300, radius*2.5, radius*2.5)
    rect.center = point

    endRad   = math.radians(-startAngle)
    startRad = math.radians(-endAngle)
    pygame.draw.arc(surface, color, rect, startRad, endRad, 4)
    pygame.display.update()


white = (255,255,255);
red = (217, 102, 255);
green = (255, 214, 51);
blue = (51, 173, 255);


screen.fill(White)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == CLOCKTICK: # count up the clock
            #Timer
            Second += 1
            sec_deg += 6
            if Second == 60:
                Minute += 1
                min_deg += 6
                Second= 0
                sec_deg = 270
            if Minute==60:
                Hour += 1
                hour_deg += 6
                Minute = 0
                min_deg = 270
            if Hour == 12:
                hour_deg = 270
            if Hour >= 12:
                Hour -= 12
                hour_deg = 270 + Hour * 30
            # redraw time
            screen.fill(White)

            Time=time.strftime("%I:%M:%S %p", time.localtime())
            TimeText=Font.render(f"Time {str(Time)}", True,Black,white)
            screen.blit(TimeText, screen.get_rect())

            clockwiseArc(screen,red,(280,160),60,270,sec_deg)
            clockwiseArc(screen,blue,(280,160),70,270,min_deg)
            clockwiseArc(screen,green,(280,160),80,270,hour_deg)

            hands((25,0),red,sec_deg)
            hands((45,0),blue,min_deg)
            hands((35,0),green,hour_deg)
            pygame.display.flip()

    Clock.tick(60) # ensures a maximum of 60 frames per second

pygame.quit()
