import sys
import numpy as np
input = sys.stdin.readline

n, m, x, t, d = map(int, input().split())

if m < x:
    print(t-(x-m)*d)
else:
    print(t)