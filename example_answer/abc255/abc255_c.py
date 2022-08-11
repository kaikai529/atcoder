import sys
from math import ceil, floor
input = sys.stdin.readline

x, a, d, n = map(int, input().split())

if d==0:
    print(abs(x-a))
else:
    c = ceil((x-a)/d)

    if 1<=c<=n:
        f_num = a + d*(c-1)
        c_num = a + d*c

        print(min(abs(f_num-x), abs(c_num-x)))
    else:
        num = a + d*(n-1)
        print(min(abs(num-x), abs(x-a)))
