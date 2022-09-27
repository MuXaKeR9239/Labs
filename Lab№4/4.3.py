import numpy as np 

matrix = np.matrix([[2, 4, 5], [1, 1, 2], [2, 4, 3]] ) 

res = np.linalg.det(matrix) 

print(res) 