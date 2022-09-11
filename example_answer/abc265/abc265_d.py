import sys
input = sys.stdin.readline

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

cum_a = [0]
for i in range(n): cum_a.append(cum_a[-1]+a[i])

for i in range(n):
    