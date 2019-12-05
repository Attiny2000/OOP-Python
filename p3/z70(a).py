import math

h = int(input("Enter hours (0 - 12): "))
m = int(input("Enter minutes (0 - 60): "))

posh = 12 * 60
posm = 60 * 60

if h > 12:
    h = h - 12
m60 = m * 60
h60 = h * 60

perch = h60/posh*100
perch = perch * 1000
perch = math.ceil(perch)
perch = perch / 1000
perch = math.ceil(perch)

print(perch)
perch = int(perch)

diff = 0
diff = int(diff)

percm = 0

while perch != percm:
    percm = ((m60 + diff * 60) / posm * 100)
    percm = percm * 1000
    percm = math.ceil(percm)
    percm = percm / 1000
    percm = math.ceil(percm)
    diff = diff + 1

print("Стрелки сойдутся через " + str(diff) + " минут.")

input()
