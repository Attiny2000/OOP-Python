s = str(input("Введите строку: "))

ss = list(s)

i = 0
k = 0

for i in range(len(ss)):
    if ss[i] == "a" and ss[i+1] == "a":
        k = i
        break
    i = i + 1
print("i: %.2f" % k)