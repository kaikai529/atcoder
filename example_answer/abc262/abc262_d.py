"""無理げー
"""

import sys
input = sys.stdin.readline
MOD = 998244353

n = int(input())
a = list(map(int, input().split()))
dp = [[[0]*n for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i):
        
