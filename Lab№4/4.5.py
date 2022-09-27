import numpy as np 

matrix = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]] ) 

res = np.linalg.det(matrix) 

print(res) 