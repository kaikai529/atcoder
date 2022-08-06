"""
都市間の連結判定
"""
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, k, l = map(int, input().split())

graph_road = [[] for _ in range(n)]
graph_rail = [[] for _ in range(n)]

for i in range(k):
    p, q = map(int, input().split())
    graph_road[p-1].append(q-1)
    graph_road[q-1].append(p-1)

for i in range(l):
    r, s = map(int, input().split())
    graph_rail[r-1].append(s-1)
    graph_rail[s-1].append(r-1)

road = [0]*n
rail = [0]*n

# 各都市の連結した道路数
road_index = 1
for i in range(n):
    # 未連結の都市を探索する
    if road[i]: continue

    # 都市iに番号indexを振る
    road[i] = road_index

    # 探索を行う
    q = deque([i])
    while q:
        p = q.pop()
        for node in graph_road[p]:
            # 未連続の都市を探索する
            if road[node]: continue

            # 都市iと連結する都市に番号indexを振る
            road[node] = road_index
            # 都市nodeと連結する都市を追加する
            q.append(node)
    
    road_index += 1
    

# 鉄道も同様に行う
rail_index = 1
for i in range(n):
    if rail[i]: continue

    rail[i] = rail_index
    q = deque([i])
    while q:
        p = q.pop()
        for node in graph_rail[p]:
            if rail[node]: continue

            rail[node] = rail_index
            q.append(node)
    
    rail_index += 1

cnt = defaultdict(int)
for i in range(n):
    # 都市の連結道路番号と連結鉄道番号
    cnt[(road[i], rail[i])] += 1

ans = []
for i in range(n):
    ans.append(cnt[(road[i], rail[i])])

print(*ans)