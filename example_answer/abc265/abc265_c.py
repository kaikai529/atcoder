import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = [[None]*(w+2) for _ in range(h+2)]
for i in range(h):a[i+1][1:-1] = input().strip()

i, j = 1, 1
while True:
    dx, dy = 0, 0
    if a[i][j] == "U": dy = -1
    elif a[i][j] == "D": dy = 1
    elif a[i][j] == "R": dx = 1
    elif a[i][j] == "L": dx = -1
    if a[i+dy][j+dx] == None:
        print(i,j)
        exit()
    elif a[i+dy][j+dx]=="1":
        print(-1)
        exit()
    a[i][j] = "1"
    i += dy
    j += dx


     