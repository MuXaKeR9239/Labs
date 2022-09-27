from scipy.misc import derivative

def f(x):
    
    return 2*pow(x,4) - 2*pow(x,3) - 4*pow(x,2) + 6*pow(x,1) + 5

a = 1

b = 2

eps = 0.001

c = derivative(f, b, n = 2)

if(f(b)*c>0):

    x = b

else:

    x = a

df = derivative(f, x, n = 1)

x1 = x - f(x)/df

while(abs(x1 - x)> eps):

    x = x1

    x1 = x - f(x)/df

print('Solving the equation by Newton*s method x = ', x1)