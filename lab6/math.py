#task1
import math
degree = float(input("degree: "))
radian = degree * (math.pi / 180)
print(f"radian: {radian:.6f}")
#task2
def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area
base1 = float(input("first base: "))
base2 = float(input("second base: "))
height = float(input("height: "))
area = trapezoid_area(base1, base2, height)
print(f"The area is: {area}")

#task3
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area is{area}")
#task4
base = float(input())
height = float(input())
area = base * height
print(f" {area}")
