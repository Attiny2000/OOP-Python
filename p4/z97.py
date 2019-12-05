from colorama import *
init(autoreset=True)

print("Задание 88(b) ")
n = input('\033[31m'+"Введите число n ")
n = int(n)
print('\033[32m'+"n = ", n)
x=1
y=1
i = 2
s = x /(1+(abs(y)))
for i in range(n):
    y = x+y
    x = 0.3*x
    s=(s+(x*(1+(abs(y)))))
print('\033[32;1m' + "Sum = " + str(s))
