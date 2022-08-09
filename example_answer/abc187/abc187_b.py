import sys
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()

ans = 0
for i in range(n):
    xi, yi = xy[i]
    for j in range(i+1, n):
        xj, yj = xy[j]
        if (xi-xj) > 0:
            if -(xi-xj) <= (yi-yj) and (yi-yj) <= (xi-xj):
                ans += 1
        else:
            if -(xi-xj) >= (yi-yj) and (yi-yj) >= (xi-xj):
                ans += 1

print(ans)