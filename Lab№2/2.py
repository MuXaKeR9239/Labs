import numpy as np

import math

import matplotlib.pyplot as plt

def f(x):

    return 2 * pow(x,4) - 2 * pow(x,3) - 4 * pow(x,2) + 6 * x + 5

a = 1.

b = 2.

eps = 0.001 

def rec_dyhotom(a, b, eps):

    if abs(f(b) - f(a)) < eps:

        print('Calculate the root')

        return

mid = (a+b)/2

if f(mid) == 0 or abs(f(mid)) < eps:

    print(f'The root is at the point x = {mid}')

elif f(a)*f(mid) < 0:

    rec_dyhotom(a, mid, eps)

else:

    rec_dyhotom(a, mid, eps)

x = np.arange(a, b, 0.01)

plt.plot(x, f(x))

plt.xlabel('x')

plt.ylabel('f(x)')

plt.title('The halving method')

plt.grid()

plt.show()
