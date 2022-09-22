import sys
input = sys.stdin.readline

n = int(input())

ans = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if j==0 and i==j:
            ans[i][j] = 1
        else:
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

for i in range(n): print(*ans[i][:i+1])
