import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if 2*n > m:
    print(m//2)
else:
    rest = m-2*n
    print(n+rest//4)
