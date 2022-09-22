import sys
input = sys.stdin.readline

WHITE = "."
BLACK = "#"
n, a, b = map(int, input().split())
ans = [[WHITE]*(b*n) for _ in range(a*n)]

color = WHITE
for h in range(0,a*n, a):
    if h//a%2==0:
        color = WHITE
    else:
        color = BLACK
    for w in range(0, b*n, b):
        for i in range(h,h+a):
            for j in range(w,w+b):
                ans[i][j] = color
        color = WHITE if color==BLACK else BLACK

for i in range(a*n): print("".join(ans[i]))
        