import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
v = list(map(int, input().split()))

# i番目以下の商品から
dp = [[(0,0)]*(n+1) for _ in range(n+1)]

dp[0][0]=0
for i in range(n):
    for k in range(n):
        # i番目を使わない
        dp[i+1][k]=dp[i][k]