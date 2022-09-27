import numpy as np 

a = 1 

b = 2 

c = 3 

d = 4 

matrix = np.matrix( 

    [[a, 0, 0, 0], 

    [0, b, 0, 0], 

    [0, 0, c, 0], 

    [0, 0, 0, d]] 

) 

mx_power = np.linalg.matrix_power(matrix, 2) 

print(mx_power) 