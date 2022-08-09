import sys
import numpy as np
input = sys.stdin.readline

n = int(input())
A = np.array(list(map(int, input().split())))

h_max = 0
total = 0
for i in range(n-1):
    if h_max < A[i]:
        h_max = A[i]
    if h_max > A[i+1]:
        total += h_max-A[i+1]

print(total)
