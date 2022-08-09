import sys
input = sys.stdin.readline

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

# 最小のブロック数の取得
min_block=100
for i in A: min_block=min(min_block, min(i))

# 累積
ans = 0
for i in A: 
    for j in i:
        ans += j - min_block

print(ans)