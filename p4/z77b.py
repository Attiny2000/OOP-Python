a = input ("input a: ")

a = int(a)
s = 2

i = 1

if (a == 0):
    s = 1
elif (a < 0):
    s = a/s
else:
    while (i <= a):
        s = s * s
        i=i+1

print(s)
