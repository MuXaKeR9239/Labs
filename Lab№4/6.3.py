import numpy as np 

A = np.matrix(''' 

1  2  2; 

2  1 - 2; 

2 - 2  1 

''') 

A_inv = np.linalg.inv(A) 

print(A_inv) 