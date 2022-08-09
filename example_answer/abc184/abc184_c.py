import sys
input = sys.stdin.readline

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# 原点として考える
r = r2 - r1
c = c2 - c1 

# 0手の場合
if (r, c) == (0, 0):
    ans = 0

# 1手の場合
## 直線上
elif r == c or r == -c: 
    ans = 1
## 円内
elif abs(r) + abs(c) <= 3:
    ans = 1

#　２手の場合
## パリティが同じか
elif (r ^ c ^ 1) & 1:
    ans = 2
## Manhattan距離が6以下
elif abs(r) + abs(c) <= 6:
    ans = 2
## 直線上（7個）
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    ans = 2

#　その他
else:
    ans = 3
print(ans)

