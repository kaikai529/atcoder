import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

A.sort()
A.append(n+1)

w = []
k = 10**15
for i in range(m+1):
    x = A[i+1] - A[i] -1
    if x<=0:continue
    k = min(k, x)
    w.append(x)

ans = 0
for w_ in w:
    ans += math.ceil(w/k)
print(ans)