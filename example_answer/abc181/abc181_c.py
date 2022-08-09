import sys
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 == x2 * y1:
                print("Yes")
                exit() 

print("No")