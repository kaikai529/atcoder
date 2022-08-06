"""
1.隣接行列を求める
2.ワーシャルフロイド法で最短距離を求める
"""
from math import inf
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, c = [], [], []
# 隣接行列表現
dist = [[inf]*n for _ in range(n)]
for i in range(n): dist[i][i]=0
for i in range(m):
    _a, _b, _c = map(int, input().split())
    a.append(_a-1), b.append(_b-1), c.append(_c)
    dist[_a-1][_b-1] = _c
    dist[_b-1][_a-1] = _c

# ワーシャルフロイド法
for k in range(n): # 中継点
    for s in range(n): # 始点
        for g in range(n): # 終点
            dist[s][g] = min(dist[s][g], dist[s][k]+dist[k][g])

# 利用されている辺の計算
ans = m
for i in range(m):
    flag=False
    # i番目の辺がa[i]->b[i]
    for j in range(n):
        # 始点j->a[i]->b[i]に行く事を考える
        if dist[j][a[i]]+c[i]==dist[j][b[i]]:
            flag=True
    if flag:
        ans=ans-1

print(ans)