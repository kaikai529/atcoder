from math import inf
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    tmp_min = inf
    for a_ in a:
        ax, ay = xy[a_-1]
        x, y = xy[i]
        tmp_min = min(tmp_min, ((x-ax)**2+(y-ay)**2)**0.5 )
    ans.append(tmp_min)

print(max(ans))

