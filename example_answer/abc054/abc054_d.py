"""
有無の全探索
=> bit探索(今回は間に合わない) or 動的計画法
"""
from math import inf
import sys
input = sys.stdin.readline

n, ma, mb = map(int, input().split())
abc_lst = []
for _ in range(n):
    a, b, c = map(int, input().split())
    abc_lst.append((a,b,c))

# 動的計画法 dp[薬品][Aの重さ][Bの重さ]=値段
dp = [[[inf]*(401) for _ in range(401)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    a,b,c = abc_lst.pop(0)
    for ca in range(401):
        for cb in range(401):
            if dp[i][ca][cb]==inf: continue
            # n番目の薬品を使わない
            dp[i+1][ca][cb] = min(dp[i+1][ca][cb], dp[i][ca][cb])
            
            # n番目の薬品を使う
            dp[i+1][ca+a][cb+b] = min(dp[i+1][ca+a][cb+b], dp[i][ca][cb]+c)

ans = inf
for ca in range(1,401):
    for cb in range(1,401):
        if (ca*mb==cb*ma):
            ans = min(ans, dp[n][ca][cb])

if ans==inf: print(-1)
else: print(ans)