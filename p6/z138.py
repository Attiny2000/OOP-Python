print("Задание 138")
mass = [] 
for i in range(1,71):
    mass.append(i)
mass.append(mass[0])
mass.remove(mass[0])
print(mass)
