import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cum_a = [0]*(n+1)
cum_a2 = [0]*(n+1)

for i in range(n):
    cum_a[i+1] = cum_a[i] + a[i]
    cum_a2[i+1] = cum_a2[i] + a[i]**2

ans = 0
for i in range(1,n):
    ans += (i)*a[i]**2 -2*cum_a[i]*a[i] + cum_a2[i]

print(ans)