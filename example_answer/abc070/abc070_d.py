from math import factorial
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# 定数
MOD = 10**9+7

# 自作関数


def combination(n: int, r: int):
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_


def INs(len_n: int, trans_func=lambda x:x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main


def dfs(this_point, parent, distance):
    depth[this_point] = distance
    for next_point, next_distance in tree[this_point]:
        if next_point == parent: continue
        dfs(next_point, this_point ,distance+next_distance)


n = IN()
tree_data = INs(n-1, list)
q, k = IN()
queries = INs(q, list)

tree = [[] for _ in range(n+1)]
depth = [0]*(n+1)

for a, b, c in tree_data:
    tree[a].append([b,c])
    tree[b].append([a,c])

dfs(k, -1, 0)
for x, y in queries:
    print(depth[x]+depth[y])
