import math

Radius = float(input("Enter circle radius: "))
Unit = input("Enter measurement unit: ")

print("The circle circumference is", 2 * math.pi * Radius, Unit)
print("The circle area is", math.pi * Radius ** 2, Unit,"^2")
