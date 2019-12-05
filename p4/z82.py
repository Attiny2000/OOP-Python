x = int(input("Enter X: "))

l = 2
k = 1

f = 1
j = 1

while l <= 64:
    f = ((x - l) * f)
    j = ((x - k) * j)
    l = l + l
    k = k + l

if j <= 0 or f <= 0:
    y = 0
else:
    y = (f / j)
print("Y = " + str(y))