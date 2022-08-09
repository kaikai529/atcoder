import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# 累積和
cum_sum = [0]
for i in range(n): cum_sum.append(A[i] + cum_sum[-1])

# 動作内の最大値
M = [0]
for i in range(n): M.append(max(M[-1],cum_sum[i+1]))

ans, x = 0, 0
for i in range(1, n+1):
    # 現在の位置＋動作内の最大値
    ans = max(ans, x+M[i])
    x += cum_sum[i]

print(ans)

