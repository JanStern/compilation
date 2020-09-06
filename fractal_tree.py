import pygame
import numpy as np 

pygame.init()

l=600
h=600
screen = pygame.display.set_mode((l,h))

factor=np.pi/10

def branch(x,y,l,alpha):
    global factor
    pygame.draw.line(screen,(0,0,0), (x,y), (x-l*np.sin(alpha),y-l*np.cos(alpha)), 1)

    x= x-l*np.sin(alpha)
    y= y-l*np.cos(alpha)
    l*=0.67
    if(l>1):
        branch(x,y,l,alpha+factor)
        branch(x,y,l,alpha-factor)
        

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            factor-=0.1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            factor+=0.1

    screen.fill((205,205,205))
    branch(l//2,h,175,0)
    pygame.display.flip()