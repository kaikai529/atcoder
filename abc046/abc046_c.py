import sys
from math import ceil
input = sys.stdin.readline

n = int(input())
ta = [map(int, input().split()) for _ in range(n)]

takahasi = 1
aoki = 1
for t, a in ta:
    n = max(ceil(takahasi/t), ceil(aoki/a))
    takahasi = n*t
    aoki = n*a    

print(takahasi+aoki)
