from math import atan2
import sys
input = sys.stdin.readline

x, y = [0]*4, [0]*4
for i in range(4):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(4):
    p1_idx = (i-1) % 4
    p2_idx = (i+1) % 4

    theta = atan2()
    


print(ans/2/pi*360)
