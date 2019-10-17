print("Задание 22 Найти площадь равнобочной трапеции с основаниями а и Ь и углом а при большем основании а. ")
import math
a=float(input("Введите сторону а: "))
b=float(input("Введите сторону b: "))
c=float(input("Введите сторону c: "))
p = (a+b+c)/2
print("Полупериметр = ", p)
H = (2/a)* (math.sqrt(p-a)*(p-b)*(p-c))
print("Длина высот = ", H)
M = (1/2) * (math.sqrt(2*a*a)+(2*b*b-c*c))
print("Длина медианы = ", M)
L = 2*(math.sqrt(a*b*p*(p-c)))/(a+b)+(2*b*b-c*c)
print("Длина бисектриси = ", L)
R_op = (a*b*c) / (4*(math.sqrt(p*(p-a)*(p-b)*(p-c))))
print("Радиус описанной окружности", R_op)
R_vp = (math.sqrt(p-a)*(p-b)*(p-c))/p
print("Радиус вписанной окружности" , R_vp)

