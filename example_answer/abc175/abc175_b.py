import sys
import numpy as np

input = sys.stdin.readline

n = int(input())
ls = np.array(sorted(list(map(int, input().split()))))

count = 0
for i in range(n):
    for j in range(i+1, n):
        a, b = ls[i], ls[j]
        if a==b:
            continue
        l = a + b
        for k in range(j+1, n):
            c = ls[k]
            if b==c:
                continue
            if l > ls[k]:
               count+=1

print(count)

