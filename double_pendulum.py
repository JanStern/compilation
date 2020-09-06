import numpy as np 
import pygame, time 

pygame.init()
clock = pygame.time.Clock()

l,h=(600,600)
screen = pygame.display.set_mode((l,h))
g = 9.81
dt = 0.1

r1 = 100
r2 = 50
m1 = 10
m2 = 10
a1 = np.pi/2
a2 = np.pi/2
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0

px = []
py = []

def calculate(friction):
    global a1,a2,a1_v,a2_v,a1_a,a2_a
    global g,r1,r2,m1,m2,dt

    part1 = -g*(2*m1+m2)*np.sin(a1)
    part2 = -m2*g*np.sin(a1-2*a2)
    part3 = -2*np.sin(a1-a2)*m2*(a2_v**2*r2+a1_v**2*r1*np.cos(a1-a2))
    den = r1 * (2*m1+m2-m2*np.cos(2*a1-2*a2))

    a1_a = (part1 + part2 + part3)/den

    part1 = 2*np.sin(a1-a2)
    part2 = a1_v**2*r1*(m1+m2)
    part3 = g*(m1+m2)*np.cos(a1)
    part4 = a2_v**2*r2*m2*np.cos(a1-a2)
    den = r2 * (2*m1+m2-m2*np.cos(2*a1-2*a2))

    a2_a = part1*(part2+part3+part4)/den

    a1_v += a1_a*dt
    a2_v += a2_a*dt
    a1 += a1_v*dt
    a2 += a2_v*dt

    if friction:
        a1_v *= 0.995
        a2_v *= 0.995


def draw():
    global px,py

    x1 = l//2 + r1 * np.sin(a1)
    y1 = h//2 + r1 * np.cos(a1)

    x2 = x1 + r2 * np.sin(a2)
    y2 = y1 + r2 * np.cos(a2)

    px.append(x2)
    py.append(y2)
    
    LF = 3

    if len(px)>255*LF:
        px.pop(0)
        py.pop(0)

    for i in range(len(px)):
        if (i>0): pygame.draw.line(screen,(255-i//LF,255-i//(LF+50),255), (int(px[i-1]),int(py[i-1])), (int(px[i]),int(py[i])),2)


    pygame.draw.line(screen,(0,0,0), (l//2,h//2),(int(x1),int(y1)))
    pygame.draw.circle(screen,(0,0,0),(int(x1),int(y1)), m1)

    pygame.draw.line(screen,(0,0,0), (int(x1),int(y1)),(int(x2),int(y2)))
    pygame.draw.circle(screen,(0,0,0),(int(x2),int(y2)), m2)


done = False 
pause = True
friction = False

while not done:

    screen.fill((200,200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            pause = not pause
            a1_v=0
            a2_v=0
            px=[]
            py=[]
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            a1=np.pi
            a2=np.pi
            a1_v=np.random.uniform(-1,1)/10000
            a2_v=np.random.uniform(-1,1)/10000
            px=[]
            py=[]
        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            friction = not friction
        
        
    if not pause:
        screen.fill((255,255,255))
        calculate(friction)
    draw()

    pygame.display.flip()
    clock.tick(120)

    