from math import cos, pi, sin, atan
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if a==0:
    if b < 0:
        print(0,-1)
    else:
        print(0,1)
else:
    theta = atan(b/a)
    print(cos(theta), sin(theta))