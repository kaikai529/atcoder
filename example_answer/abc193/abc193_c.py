import sys
from math import log2, sqrt, log2
input = sys.stdin.readline

n= int(input())
limit = int(log2(n))+1

s = set()
for i in range(2, int(sqrt(n))+2):
    x = i*i
    for _ in range(limit):
        if x <= n:
            s.add(x)
            x*=i

print(n-len(s))
        