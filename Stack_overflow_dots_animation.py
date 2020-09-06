import pygame, random


N = 80
dt = 0.05

BLACK = (0,0,0)
GRAY = (40,40,40)


pygame.init()
clock = pygame.time.Clock()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)

screen_size_x , screen_size_y= (infoObject.current_w, infoObject.current_h)

class dot(object):
    
    def __init__(self):
        self.x = random.randint(0,screen_size_x)
        self.y = random.randint(0,screen_size_y)
        self.z = random.randint(1,5)

        self.x_vel = self.z*random.uniform(-4,4)
        self.y_vel = self.z*random.uniform(-4,4)

        self.accel = True

    def accelerate(self):
        if self.accel:
            self.x_vel *= random.uniform(0.999,1.01)
            self.y_vel *= random.uniform(0.999,1.01)
        else:
            self.x_vel *= random.uniform(0.99,1.001)
            self.y_vel *= random.uniform(0.99,1.001)


    def move(self):

        if (self.x_vel**2+self.y_vel**2)**0.5 <20:
            self.accel = True
        elif (self.x_vel**2+self.y_vel**2)**0.5 >50:
            self.accel = False

        self.accelerate()


        self.x += self.x_vel*dt
        self.y += self.y_vel*dt

        if self.x<1 or self.x>screen_size_x-1:
            self.x_vel*=-1
        
        if self.y<1 or self.y>screen_size_y-1:
            self.y_vel*=-1
        
    def draw_line_to_nn(self,dots,pos):
        for dot in dots:
            distance = ( (self.x-dot.x)**2+(self.y-dot.y)**2+(10*(self.z-dot.z)**2))**(0.5)
            if distance>0 and distance < 150:
                pygame.draw.line(screen,GRAY,(int(self.x),int(self.y)),(dot.x,dot.y))
        distance = ( (self.x-pos[0])**2+(self.y-pos[1])**2+(10*(self.z)**2))**(0.5)
        if distance>0 and distance < 200:
            pygame.draw.line(screen,GRAY,(int(self.x),int(self.y)),pos)
    


    
        

    def draw_dot(self):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), int(self.z)) 


dots = [dot() for _ in range(N)]



done = False 
while not done:

    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done = True

    for dot in dots:
        dot.draw_dot()
        dot.move()
        dot.draw_line_to_nn(dots,pygame.mouse.get_pos())

    pygame.display.flip()

pygame.quit()