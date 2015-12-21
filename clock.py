import pygame, sys, time
from pygame.locals import *
from datetime import datetime

pygame.init()

now = datetime.now()
hour = now.hour % 12
minute = now.minute

WHITE = (255,255,255)
BLUE = (0,0,255)


window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Clock")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    window.fill(WHITE)

    pygame.draw.circle(window,BLUE,(300,300),200)
    
    pygame.display.update()
    time.sleep(0.02)
