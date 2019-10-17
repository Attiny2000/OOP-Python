import math
index = 0.1
result = 1+(math.sin(index))
while index<=10:
    index = index + 0.1
    result = result * (1+(math.sin(index)))
print("Результат", result)
