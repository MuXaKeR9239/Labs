
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x+math.sin(y/2.8)

x0 = 1.4
b = 2.4
h = 0.1

x = np.arange(x0,b+h,h)
n = len(x)-1
y = np.empty(n+1)

y[0] = 2.2

for i in range(n):
    y[i+1]=y[i]+f(x[i],y[i])*h

y_r=np.round_(y,4)

print('x =',x)
print('y =',y_r)

plt.plot(x, y,'o',x,y, 'green')
plt.xlabel('x')
plt.ylabel('y')
plt. title( 'Euler*s method')
plt.legend(['points','x+cos(y/sqrt(0.3))'])
plt.grid()
plt.show()