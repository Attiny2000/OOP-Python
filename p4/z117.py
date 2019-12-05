import math
 
n = int(input('N: '))
z = []
for i in range(1, (n*2), 2):
    z.append(float(i) / (i + 1))
for i in range(1, len(z)):
    z[0] = z[0] * z[i]
print(z[0])
