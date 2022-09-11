from math import ceil
import sys
input = sys.stdin.readline

n = int(input())

b = ceil(n**(1/3))
ans = []

for i in range(b, ):
    if 4*b**3 < n:
        break
    a = b
    while True:
        if (a+b)*(a**2+b**2) < n:
            break
        a -= 1
    ans.append((a+b)*(a**2+b**2))

print(min(ans))
