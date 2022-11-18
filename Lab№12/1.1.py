from scipy import integrate

import math

eps = 0.001

def int1(x):

    return 1/math.sqrt(x+2.5)

def trapezium_method(int1,a,b,n):

    h=(b-a)/n

    sum=0.5*(int1(a)+int1(b))

    for i in range(1,n):

        sum+=int1(a+i*h)

    return sum*h

v,err = integrate.quad(int1,1.6,2.2)    

if abs (trapezium_method(int1, 1.6, 2.2, 2*10) -trapezium_method(int1, 1.6, 2.2, 10))/3. <= eps:

    print("Trapetzia method:",round (trapezium_method(int1,1.6,2.2,10), 5))

print("Check for the trapetzia method= ",round(v, 5))
