
from scipy import optimize

import math

x0 = 0.15

y0 = -0.75

delta = 0.1

def f1(y):

    return -math.cos(y + 0.5) - 0.8

def f2 (x):

    return (math.sin(x))/2- 0.8

def iter (x,y,e):

    xn = x

    yn = y

    xn1 = f2(x)

    yn1 = f1(y)

    n = 1

    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):

        xn = xn1

        yn = yn1

        xn1 = f2(yn)

        yn1 = f1(xn)

        n += 1

    print ('Simple iteration:')

    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)

iter(x0,y0,0.0001)

def f3(x):

    return 3*x[0] + math.cos(x[0] + 0.5) - x[1] - 0.8 , (math.sin(x[1]))/2 - 0.8
s = optimize.root(f3, [0.,0.], method = 'hybr') 

print ('Chek',s.x)

print ('Chek',s.x)