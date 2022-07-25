import sys
input = sys.stdin.readline

n, k, x, y = map(int, [input().strip() for _ in range(4)])

if n >= k:
    print(x*k+y*(n-k))
else:
    print(x*n)