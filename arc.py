import pygame, sys
from pygame.locals import *

import math

pygame.init()
screen = pygame.display.set_mode((400,400))

# We need this if we want to be able to specify our
#  arc in degrees instead of radians

def degreesToRadians(deg):
    return deg/180.0 * math.pi


# Draw an arc that is a portion of a circle.
# We pass in screen and color,
# followed by a tuple (x,y) that is the center of the circle, and the radius.
# Next comes the start and ending angle on the "unit circle" (0 to 360)
#  of the circle we want to draw, and finally the thickness in pixels

"""def drawCircleArc(screen,color,radius,startDeg,endDeg,thickness = 4,center = (200,200)):
    (x,y) = center
    rect = (x-radius,y-radius,radius*3,radius*3)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)

    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)
"""
def clockwiseArc(surface, color, point, radius, startAngle, endAngle):
    rect = pygame.Rect(0, 0, radius*2, radius*2)
    rect.center = point

    endRad   = math.radians(-startAngle)
    startRad = math.radians(-endAngle)

    pygame.draw.arc(surface, color, rect, startRad, endRad)

white = (255,255,255);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);

sec_deg = 0
min_deg = 0
hour_deg = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit();


    screen.fill(white);

    # Part of a red circle, arc from 0 to 90 degrees
    # Center is at 100,100, and radius is 50
    clockwiseArc(screen,red,(200,200),50,270,0)

    # Part of a blue circle, arc from 135 to 180 degrees
    # Center is at 200,300, radius is 125, thickness is 2
    clockwiseArc(screen,green,(200,200),60,270,0)


    # Part of a green circle, arc from -45 to +45 degrees
    # Center is at 300,150, radius is 100, thickness is 3
    clockwiseArc(screen,blue,(200,200),70,270,0)



    pygame.display.update()
