import sys
import itertools 
input = sys.stdin.readline

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

prior = list(itertools.permutations([i+1 for i in range(n-1)]))

ans = 0
for p in prior:
    acc_time=0
    for i in range(n):
        if i==0:
            now = 0
            go = p[i]
            acc_time+=t[now][go]
        elif i==n-1:
            now = p[-1]
            go = 0
            acc_time+=t[now][go]
        else:
            now = p[i-1]
            go = p[i]
            acc_time+=t[now][go]
    if acc_time==k:
        ans += 1

print(ans)



