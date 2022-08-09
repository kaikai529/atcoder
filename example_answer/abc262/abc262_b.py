import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1

ans = 0
for p1 in range(n):
    for p2 in range(p1+1,n):
        for p3 in range(p2+1,n):
            if matrix[p1][p2]*matrix[p2][p3]*matrix[p3][p1]:
                ans += 1

print(ans)

