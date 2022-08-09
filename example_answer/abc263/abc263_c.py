import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

ans = []
combi_lst = combinations([i for i in range(1,m+1)], n)
for combi in combi_lst:
    list(combi).sort()
    ans.append(combi)

ans.sort()
for i in ans: print(*i)
