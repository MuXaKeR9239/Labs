import numpy as np 

matrix = np.matrix( 

    [[-1, 2], 

    [0, 1]] 

) 

mx_power = np.linalg.matrix_power(matrix, 2) 

print(mx_power) 