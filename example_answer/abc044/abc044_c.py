import sys
input = sys.stdin.readline

n, a = map(int, input().split())
x = list(map(int, input().split()))

# 推奨される解法（動的計画法）
# i枚目までのカードでj枚選んで合計がkである組み合わせ

dp = [[[0]*2501 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(2501):
            if dp[i][j][k]:
                # (i+1)枚目を選ばない場合
                dp[i+1][j][k]+=dp[i][j][k]
                # (i+1)枚目を選ぶ場合
                dp[i+1][j+1][k+x[i]]+=dp[i][j][k]

ans = 0
for i in range(1, n+1):
    ans+=dp[n][i][i*a]

print(ans)

# 全列挙による解き方（時間制限で解けない）

# ans = 0
# for i in range(2**n):
#     total = 0
#     cnt = 0
#     for j in range(n):
#         if (i>>j)&1:
#             cnt+=1
#             total+=x[-(j+1)]
#     if cnt==0:
#         continue
#     elif total/cnt==a:
#         ans += 1
# print(ans)



