import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i]==i+1: cnt += 1

ans = cnt*(cnt-1)//2

cnt = 0
for i in range(n):
    if a[i]==i+1: continue
    if a[a[i]-1]==i+1: cnt += 1

print(ans+cnt//2)