import numpy as np 

matrix = np.matrix(''' 

1  2  0  0  0; 

1  0  2  0  0; 

1  0  0  2  0; 

1  0  0  0  2; 

0  0  1  1  1 

''') 

res = np.linalg.det(matrix) 

print(res) 