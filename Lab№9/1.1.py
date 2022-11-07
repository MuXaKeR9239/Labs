import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

x = [0.4,  0.7,  1.1,  1.7,  2.4 ]
y = [2.39, 2.86, 1.55, 3.57, 2.94]

spl = scipy.interpolate.UnivariateSpline(x, y)
xs = np.linspace(0, 10, 100)

plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()


