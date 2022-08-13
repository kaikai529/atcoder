"""
heapqを用いることで最小値、最大値をO(LogN)で取り出す
"""
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

q = int(input())
s = defaultdict(int)
mx = []
mn = []
ans = []

for _ in range(q):
    querry = list(map(int, input().split()))

    if querry[0] == 1:
        x = querry[1]
        s[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)
    elif querry[0] == 2:
        x, c = querry[1:]
        s[x] = max(0, s[x]-c)
    else:
        while s[mn[0]] == 0:
            heapq.heappop(mn)
        while s[-mx[0]] == 0:
            heapq.heappop(mx)
        ans.append(mx[0]+mn[0])


for i in range(len(ans)):
    print(-ans[i])

""" 愚直なlist操作ではTLE
for _ in range(q):
    querry = list(map(int, input().split()))

    if querry[0] == 1:
        x = querry[1]
        s[x] += 1
    elif querry[0] == 2:
        x, c = querry[1:]
        s[x] -= min(c, x)
        if s[x] == 0:
            s.pop(x)
    else:
        val = s.keys()
        ans.append(max(val)-min(val))


for i in range(len(ans)):
    print(ans[i])

"""



