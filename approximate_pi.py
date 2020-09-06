import random
import matplotlib.pyplot as plt

N = 1000

def create_points(n):
    x_values = []
    y_values = []
    num_inside=0

    for _ in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        x_values.append(x)
        y_values.append(y)

        if (x**2+y**2 <= 1): num_inside+=1
    
    return num_inside,x_values,y_values

def color(x,y):
    c=[]
    for i in range(len(x)):
        if x[i]**2+y[i]**2>1: c.append('#E64D2C')
        else: c.append('#4C70E8')
    return c

num,x,y = create_points(N)
pi = 4*num/N

plt.figure()
plt.title(pi)
plt.scatter(x,y,c=color(x,y))
plt.show()