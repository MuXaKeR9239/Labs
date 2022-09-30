import numpy as np
import matplotlib.pyplot as plt

x = np.array([-3, -1, 0, 2])
y = np.array([5, 3, -7, -15])

x2 = np.linspace(np.min(x), np.max(x), 100)
y2 = []

for t in x2:
    res = 0

    for j in range(len(y)):
        p1 = 1
        p2 = 1

        for i in range(len(x)):
            if i != j:
                p1 *= t - x[i]
                p2 *= x[j] - x[i]

        res += y[j] * p1 / p2

    y2.append(res)

plt.plot(x, y, 'o', x2, y2)
plt.grid(True)
plt.title('Graph')
plt.show()
