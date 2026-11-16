import math
import sys
from sys import stdin

def cyclic_polygon_area(sides):
    n = len(sides)
    if n < 3:
        return 0.0
    s = sum(sides) / 2.0
    area = 1.0
    for i in range(n):
        area *= (s - sides[i])
    return math.sqrt(area)

def is_cyclic_polygon(sides):
    n = len(sides)
    if n < 3:
        return False
    angles_sum = (n - 2) * 180.0
    for i in range(n):
        angle_i = math.degrees(math.acos((sides[(i-1)%n]**2 + sides[(i+1)%n]**2 - sides[i]**2) / (2*sides[(i-1)%n]*sides[(i+1)%n])))
        angles_sum -= angle_i
    return abs(angles_sum) < 1e-9

def area_diff(sides, target_area):
    if not is_cyclic_polygon(sides):
        return float('inf')
    return cyclic_polygon_area(sides) - target_area

def find_cyclic_polygon(t):
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        sides = [float(sys.stdin.readline().strip()) for j in range(n)]
        target_area = cyclic_polygon_area(sides)
        if abs(target_area) < 1e-9:
            print("0.000")
        else:
            left = 0.0
            right = 1e9
            while right - left > 1e-9:
                mid = (left + right) / 2.0
                diff = area_diff(sides, mid)
                if diff < 0:
                    left = mid
                else:
                    right = mid
            print("{:.3f}".format(left))

# Ejemplo de uso
t = int(stdin.readline().strip())
find_cyclic_polygon(t)
