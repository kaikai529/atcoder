import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
square = [[0]*w for _ in range(h)]
vector = [[1,0],[-1,0],[0,1],[0,-1]]

for j in range(h):
    s = input().strip()
    for i in range(w):
        if s[i]=="#":
            square[j][i]=-1


ans = -3
for h_, w_ in vector:
    this_w = y-1
    this_h = x-1
    while 0 <= this_h < h and 0 <= this_w < w:
        if square[this_h][this_w]==-1:
            break
        ans+=1

        this_h += h_
        this_w += w_

print(ans)


