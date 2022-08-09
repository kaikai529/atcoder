"""
only pypy3
"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 2**32
for i in range(2**(n-1)):
    now = -1
    tmp = 0
    total = 0
    for j in range(n):
        flag = (i>>j)&1
        if now!=flag:
            total ^= tmp
            tmp = a[j]
        else:
            tmp |= a[j]
        now = flag
    total ^= tmp
    ans = min(ans, total)

print(ans)
            