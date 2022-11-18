from scipy import integrate

from math import sqrt

eps = 0.0001

n = 20

def Int1(x):

    return 1/sqrt((x**2)+4)

def F_Simpson(a,b,n):

    h = (b - a) / n

    integr = Int1(a) + Int1(b)

    for i in range(1,n):

        k = a + i*h

        if i%2 == 0:

            integr += 2 * Int1(k)

    else:

        integr += 4 * Int1(k)

    integr *= h/3

    return integr

if abs(F_Simpson(0.8,1.8,2*8) -F_Simpson(0.8,1.8,8))/ 15. <= eps:

    print("F_Simpsone:",round (F_Simpson(0.8,1.8,8), 5))

v,err = integrate.quad(Int1,0.8,1.8)

print("Check for the F_Simpsone method= ",round(v, 5))
