print("Задание 136 а")
n = int(input("n = : "))
s = 0
i = 1
for i in range(n):
    a = int(input('Введите %d число ' % i))
    s = s+a
print("Сума",s)

print("Задание 136 в")
n = int(input("n = : "))
i = 1
for i in range(n):
    a = int(input('Введите %d число ' % i))
    s = s + abs(a)
print("Сума",s)

