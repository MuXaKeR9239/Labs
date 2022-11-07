import numpy as np
import matplotlib.pyplot as plt

def formula(x):
    return np.sin(x)*x



x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([formula(x)])

x_avg  = np.mean(x)
y_avg  = np.mean(y)
x2_avg = np.mean(x ** 2)
xy_avg = np.mean(x_avg * y_avg)

a = (xy_avg - x_avg * y_avg) / (x2_avg * x_avg ** 2)
b = y_avg - (a * x_avg)



print('Coefficients')
print('a = ', round(a, 2))
print('b = ', round(b, 2))
print('y = ', y)
print('x =', x)
print('x_avg =', x_avg)
print('y_avg =', y_avg)
print('x2_avg =', x2_avg)
print('xy_avg =', xy_avg)

plt.plot(x, a*x + b, 'r', label='Line')
plt.scatter(x, y,  label='Dot chart')

plt.title('Reult')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()