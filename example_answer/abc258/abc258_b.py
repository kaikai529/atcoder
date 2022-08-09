# review this program
import sys
import numpy as np
input = sys.stdin.readline

n = int(input())
A = np.array([list(map(int,input()[:-1])) for _ in range(n)])

p, q = np.array([1,1,1,0,0,-1,-1,-1]), np.array([1,0,-1,1,-1,1,0,-1])
ans = 0

for i in range(n):
    for j in range(n):
        for k in range(8):
            now = 0
            x, y= i, j
            for l in range(n):
                now*=10
                now+=A[x,y]
                x+=p[k]
                y+=q[k]
                x = (x+n)%n
                y = (y+n)%n
            ans = max(ans, now)

print(ans)
