import numpy as np 

a = np.matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]] ) 

b = np.matrix([[7, 5, 3], [0, 7, 5], [0, 0, 7]] ) 

print(a * b - b * a) 