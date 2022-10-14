import matplotlib.pyplot as plt

from math import factorial

x=[0.125, 0.130, 0.135, 0.140, 0.145, 0.150, 0.155, 0.160]

y=[7.9582, 7.6489, 7.3623, 7.0961, 6.8491, 6.6185, 6.3998, 6.1965]

diff = x[1] - x[0]

x_1=0.129

x_2=0.157

q=(x_1 - x[0])/diff

q1 = (x_2-x[-1])/diff

def f(y,j): 

    mas=[]

    for i in range(len(y)):

        mas.append(y[i] - y[i-1])

    mas.pop(0)

    if j == 1:

        return mas

    else:

        j-=1

        return f(mas, j)

F1 = y[0]+q*f(y,1)[0]+q*(q-1)*f(y,2)[0]/factorial(2)

F2 = q*(q-1)*(q-2)*f(y,3)[0]/factorial(3)

F3 = q*(q-1)*(q-2)*(q-3)*f(y,4)[0]/factorial(4)

F4 = q*(q-1)*(q-2)*(q-3)*(q-4)*f(y,5)[0]/factorial(5)

N = F1 + F2 + F3 + F4

print ('Point x1=', x_1, 'Formula:', round(N,5))

plt.grid(True)
plt.title('Результат графіка')

plt.plot(y, x, 'o', linestyle='solid')
plt.show()