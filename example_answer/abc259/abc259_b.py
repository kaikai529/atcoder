import sys
import math
input = sys.stdin.readline

a, b, d = map(int, input().split())

x, y = 0, 0
rad = d*2*math.pi / 360

x = a*math.cos(rad) - b*math.sin(rad)
y = a*math.sin(rad) + b*math.cos(rad)

print(x, y)