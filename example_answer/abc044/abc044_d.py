"""
無理げー
"""
import sys
import math
input = sys.stdin.readline

n ,s = map(int, [input() for _ in range(2)])

def func(b, n):
    if n < b:
        return n
    else:
        return func(b, math.floor(n/b))+(n%b)

for b in range(2,n+1,1):
    if s == func(b, n):
        print(b)
        exit()

print(-1)