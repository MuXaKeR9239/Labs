import numpy as np 

matrix = np.matrix([[0, 2, 0], [3, 4, 5], [6, 7, 8]] ) 

res = np.linalg.det(matrix) 

print(res) 