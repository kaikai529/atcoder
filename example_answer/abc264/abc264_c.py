from concurrent.futures.process import _threads_wakeups
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
for i in range(h1): a[i].append(-1)

h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

combis_h = list(combinations([i for i in range(h1)], h2))
combis_w = list(combinations([i for i in range(w1)], w2))

flag = False
for combi_h in combis_h:
    for combi_w in combis_w:
        ans = [[0]*w2 for _ in range(h2)]
        cnt = 0
        for h in combi_h:
            for w in combi_w:
                ans[cnt//w2][cnt%w2] = a[h][w]
                cnt += 1
        if b==ans:
            flag = True
            break

if flag: print("Yes")
else: print("No")

    
