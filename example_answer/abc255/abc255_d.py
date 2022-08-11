"""間に合わない
"""
from bisect import bisect_left
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cum_a = [a[0]]
for i in range(1,n): cum_a.append(cum_a[-1]+a[i])

for _ in range(q):
    x = int(input())
    ans = sum(a)-x*n
    if x <= a[0] or a[-1] <= x:
        print(abs(ans))
        continue
    
    left = bisect_left(a,x)
    ans += (x*(left) - cum_a[left-1])*2 
    print(ans)

