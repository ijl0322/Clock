import pygame, sys, time
from pygame.locals import *
from datetime import datetime
from math import *

pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Clock")

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (150,0,150)
myfont = pygame.font.SysFont(None, 40)

def updateTime():
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    #hour = 9
    #minute = 30
    h_angle = pi*(1.0/6.0)*((hour+9)%12)
    m_angle = pi*(1.0/6.0)*(((minute/5.0)+9)%12)
    s_angle = pi*(1.0/6.0)*(((second/5.0)+9)%12)
    return h_angle, m_angle, s_angle

def addText():
    for i in range(1,13):
        text = myfont.render(str(i), True, RED)
        textRect = text.get_rect()
        t_angle = pi*(1.0/6.0)*((i+9)%12)  
        textRect.centerx = int(300 + 230*cos(t_angle))
        textRect.centery = int(300 + 230*sin(t_angle)) 
        window.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    h_angle, m_angle, s_angle = updateTime()

            
    window.fill(WHITE)

    pygame.draw.circle(window,BLUE,(300,300),200)
    pygame.draw.circle(window, RED, (int(300 + 200*cos(h_angle)), int(300 + 200*sin(h_angle))), 20)
    pygame.draw.circle(window, GREEN, (int(300 + 200*cos(m_angle)), int(300 + 200*sin(m_angle))), 15)
    pygame.draw.circle(window, PURPLE, (int(300 + 200*cos(s_angle)), int(300 + 200*sin(s_angle))), 10)
    addText()
    pygame.display.update()
    time.sleep(1)
