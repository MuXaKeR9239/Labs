import numpy as np 

N = 2 

M = 3 

a = np.random.randint(0, 5, (N, M)) 

avg = a.mean(1) 

min_avg = min(avg) 

print('matrix\n', a.view()) 

print('avg rows\n', avg.view()) 

print('min avg\n', min_avg) 