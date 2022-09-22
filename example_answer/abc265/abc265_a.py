import sys
input = sys.stdin.readline

x, y, n = map(int, input().split())

if x*3 < y:
    ans = x*n
else:
    num = n//3
    ans = num*y + (n-3*num)*x

print(ans)   