n = 6
xx = 1.5

X = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
Y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637]

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

h = 0
i = 1
t = 0
h = (X[i] - X[i - 1])
t = (xx - X[i - 1]) / h

for j in range(1, n):
    print(j)
    y1.append(Y[j] - Y[j - 1])

for j in range(1, n - 1):
    y2.append(y1[j] - y1[j - 1])

for j in range(1, n - 2):
    y3.append(y2[j] - y2[j - 1])

for j in range(1, n - 3):
    y4.append(y3[j] - y3[j - 1])

for j in range(1, n - 4):
    y5.append(y4[j] - y4[j-1])

G = (y1[0] + y2[0] * (2 * t - 1) / 2 + y3[0] * (3 * t * t - 6 * t + 2) / 6 + y4[0] * (4 * t * t * t - 18 * t * t + 22 * t - 6) / 24 + y5[0] * ( 5 * t * t * t * t - 40 * t * t * t + 105 * t * t - 100 * t + 24) / 120) / h
print(G)
L = (y2[0] + y3[0] * (t - 1) + y4[0] * (12 * t * t - 36 * t + 22) / 24 + y5[0] * (20 * t * t * t - 120 * t * t + 210 * t - 100) / 120) / (h * h)
print(L)