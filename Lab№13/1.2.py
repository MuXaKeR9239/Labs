import math 
import numpy as np 
import matplotlib.pyplot as plt 
 
def f(x,y): 
    return x+math.cos(y/math.sqrt(10)) 
 
x0=0.6 
b=1.6 
h=0.1 
x=np.arange(x0,b+h,h) 
n=len(x)-1 
y=np.empty(n+1) 
y[0]=0.8
for i in range(n): 
   y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2 
y_r=np.round_(y,4) 
print('x=',x,'\n y=', y_r) 
plt .plot(x,y,'o',x,y,'purple') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Euler-Cauchy method') 
plt.legend(['points ','x+cos(y/3)']) 
plt.grid() 
plt.show()
