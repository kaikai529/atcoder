import sys
from collections import Counter
input = sys.stdin.readline

x, y = [], []
for _ in range(3):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

x_cnt = Counter(x)
y_cnt = Counter(y)

ans = [0, 0]
for key in x_cnt:
    if x_cnt[key]==1: ans[0]=key

for key in y_cnt:
    if y_cnt[key]==1: ans[1]=key

print(*ans)