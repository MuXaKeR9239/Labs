from scipy import integrate

from math import sin

eps = 0.001

def Int1(x):

    return ((x**2)+2)*sin(x-0.5)

def L(Int1,a,b,n):

    h=(b-a)/n

    sum=0

    for i in range(0,n):

        sum+=Int1(a+i*h)

    return sum*h

v,err = integrate.quad(Int1,1.2,2)

if abs(L(Int1,1.2,2,2*10) - L(Int1,1.2,2,10))/3. <=eps:

    print("left rectangle:",round (L(Int1,1.2,2,10), 5))

def right_rec(Int1,a,b,n):

    h=(b-a)/n

    sum=0

    for i in range(1,n+1):

        sum+=Int1(a+i*h)

    return sum*h

print("right rectangle:",round (right_rec(Int1,1.2,2,10), 5))

def aver_rec(Int1,a,b,n):

    h=0.08

    sum=0

    for i in range(0,n):

        sum+=Int1(a+i*h)

    return sum*h

print("average rectangle:",round (aver_rec(Int1,1.2,2,10), 5))

print("Check for the rectangle method= ",round (v, 5))
