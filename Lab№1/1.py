from math import sqrt 

import string 

A1 = sqrt(38)
A2 = 5/3

B1 = 6.16
B2 = 1.667

C1 = abs(A1 - B1)
C2 = abs(A2 - B2)

print('The first equality is more accurate' if C1 < C2 else 'The secend equality is more accurate')