
import sys
input = sys.stdin.readline

x = list(map(int, list(input().strip())))
m = int(input())

if len(x)==1:
    print(1 if x[0]<=m else 0)
else:
    d = max(x)
    left = d
    right = m+1
    for i in range(61):
        middle = (left+right)//2
        total = 0
        for x_ in x:
            total *= middle
            total += x_
        if total <= m:
            left=middle
        else:
            right=middle

        print(left, right, total)
        if left-right==1:
            break

print(left-d)
