import numpy as np 

A = np.matrix(''' 

1 - 1  3  4; 

0 - 1  2  1; 

1  2  3  4; 

0  2  3  3 

''')  

rank = np.linalg.matrix_rank(A) 

print(rank) 