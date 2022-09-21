import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

dist = [[0]*m for _ in range(n)]

for i in range(n):
    a, b = ab[i]
    for j in range(m):
        c, d = cd[j]
        dist[i][j]=abs(a-c)+abs(b-d)

for i in range(n): 
    min_dist = min(dist[i])
    print(dist[i].index(min_dist)+1)