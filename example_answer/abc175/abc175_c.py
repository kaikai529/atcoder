import sys
import numpy as np

input = sys.stdin.readline
x, k, d = map(int, input().split())

x = abs(x)
if x//d > k:
    print(x-k*d)
else:
    rest_x = x-x//d*d
    rest_k = k-x//d
    if rest_k%2==0:
        print(abs(rest_x))
    else:
        print(abs(rest_x-d))


