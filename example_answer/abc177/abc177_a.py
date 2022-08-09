import sys
input = sys.stdin.readline

d, t, s = map(int, input().split())

if t >= d/s: print("Yes")
else: print("No")