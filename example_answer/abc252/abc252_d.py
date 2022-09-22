from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cnt = [0]*(2*10**5+1)
for i in range(n):
    cnt[a[i]] += 1

for i in range(2*10**5):
    cnt[i+1] += cnt[i]

ans = 0
for i in range(n):
    ans += cnt[a[i]-1]*(n-cnt[a[i]])

print(ans)