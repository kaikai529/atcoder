from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 頂点iの連結する頂点を表現
road = [[] for _ in range(n)]
for _ in range(m):
    a_, b_ = map(int, input().split())
    road[a_-1].append(b_-1)
    road[b_-1].append(a_-1)

# print(road)

# 深さ優先探索を行う
ans = 0
seen = [False]*n
todo = deque([(0, seen)])
while todo:
    # 次の頂点を取得
    (next, seen) = todo.pop()

    # 探索済み(True) or 未探索(False)
    if seen[next]==True: continue
    else: seen[next]=True

    # 全てを探索したかどうか
    if all(seen):
        ans+=1
        continue

    # 次の頂点を追加
    for i in road[next]:
        todo.append((i, seen.copy()))

print(ans)