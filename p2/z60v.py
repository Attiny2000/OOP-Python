x = input ("input x: ")
y = input ("input y: ")

u = 0.0

x = float(x)
y = float(y)

if ((((x * x) + ((y * y) - 1)) < 1) and (y < (1 - (x*x)))):
    u = x - y
else:
    u = (x * y + 7)
print ("u = %.2f" % u)
