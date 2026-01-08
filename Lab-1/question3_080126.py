import math

sides = []

for i in range(3):
    side = int(input(f"Enter side {i+1}: "))
    sides.append(side)

s = sum(sides) / 2 

a, b, c = sides

area = round(math.sqrt(s * (s - a) * (s - b) * (s - c)),2)

print(f"Area of triangle: {area}")
