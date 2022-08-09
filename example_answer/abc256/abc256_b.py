import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cum_a = [a[-1]]
for i in range(n-2,-1,-1): cum_a.append(a[i]+cum_a[-1])

ans = 0
for i in range(n):
    if cum_a[i]>=4:
        ans += 1

print(ans)