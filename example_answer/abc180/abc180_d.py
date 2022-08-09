import sys
input = sys.stdin.readline

x, y, a, b = map(int, input().split())

ans = 0
this_x = x
for _ in range(y-x):
    if this_x*a <= this_x+b and this_x*a < y: 
        this_x *= a
        ans += 1
    else: break

print(ans + (y-this_x-1)//b)
