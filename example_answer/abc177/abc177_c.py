import sys
import numpy as np
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

mod = 10**9+7
total = 0
ans = 0
for i in range(n):
    total += A[i]    


for i in range(n-1):
    total -= A[i]
    ans += A[i]*total

print(ans%mod)
