import numpy as np 

a = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]] ) 

b = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]] ) 

print(a * b - b * a) 