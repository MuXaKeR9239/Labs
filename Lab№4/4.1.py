import numpy as np 

matrix = np.matrix([[2, 3, 4], [1, 0, 6], [7, 8, 9]] ) 

res = np.linalg.det(matrix) 

print(res) 