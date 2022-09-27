from scipy.misc import derivative
def f(x):
    return 2 * pow(x,4) - 2 * pow(x,3) - 4 * pow(x,2) + 6 * x + 5
def hord (a, b, eps):

    if abs(b - a) < eps:
        
        print('There is no root')

        return

    if (f(a)*derivative(f, a, n = 2)):

        x0 = a

        xi = b

    else:

        x0 = b
        
        xi = a

    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))

    while (abs(xi_1 - xi) > eps):

        xi = xi_1

        xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))

    else: 

        print(f'The root is at the point x= ', xi_1)

hord(0, 100, 0.0001)
