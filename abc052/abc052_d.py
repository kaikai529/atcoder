import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    dx = x[i+1]-x[i]
    ans += min(dx*a,b)

print(ans)

