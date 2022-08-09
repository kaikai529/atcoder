import sys
input = sys.stdin.readline

n = int(input())

ans = 10**9+1
for _ in range(n):
    a, p, x = map(int, input().split())
    if x-a>0:
        ans = min(ans, p)

if ans==10**9+1: print(-1)
else: print(ans)