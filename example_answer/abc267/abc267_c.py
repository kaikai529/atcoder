import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
cum_a = [0]
for i in range(n): cum_a.append(cum_a[-1]+a[i])

# 初期値
b_sum = 0
for a_idx in range(m): 
    b_sum += (a_idx+1)*a[a_idx]

# 比較
ans = b_sum
for i in range(1,n-m+1):
    b_sum += -(cum_a[m+i-1]-cum_a[i-1]) + m*a[m+i-1]
    ans = max(ans, b_sum)

print(ans)

    
