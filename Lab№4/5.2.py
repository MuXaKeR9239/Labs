import numpy as np 

matrix = np.matrix(''' 

    2  3  4  1; 

1  2  3  4; 

3  4  1  2; 

4  1  2  3 

''') 

res = np.linalg.det(matrix) 

print(res) 