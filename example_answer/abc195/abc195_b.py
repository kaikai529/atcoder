import sys
from math import ceil, floor
input = sys.stdin.readline

a, b, w = map(int, input().split())
w = w*1000

min_=10**9
max_= 0
for i in range(1000001):
    if(i*a<=w and w<=i*b):
        min_ = min(min_, i)
        max_ = max(max_, i)

if max_==0:
    print("UNSATISFIABLE")
else:
    print(min_, max_)