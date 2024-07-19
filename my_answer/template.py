from bisect import bisect, bisect_left, bisect_right
from itertools import count
from math import ceil, factorial, floor, gcd, inf
from collections import Counter, defaultdict
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限

# 定数
MOD = 10**9+7
MOD = 10**9+7

# 入出力
input = sys.stdin.readline
def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list: return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)

def STR_IN():
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_

def INs(len_n: int, trans_func=lambda x: x): return trans_func([IN(trans_func) for _ in range(len_n)])
def STR_INs(len_n: int): return [input().strip() for _ in range(len_n)]

# 自作関数
def lcm(a, b):
    """ 最小公倍数を返す """
    return a*b // gcd(a, b)

def prime_numbers(max_n):
    """ 素数数列を返す """
    def _is_prime(ps, n):
        for p in ps:
            if n % p == 0: return False
            if p ** 2 >= n: break
        return True
    ps = []
    for n in range(2, max_n+1):
        if _is_prime(ps, n): ps.append(n)
    return ps


def cum(array: list):
    """ 累積和を返す """
    cum_sum = [array[0]]
    for i in range(len(array)-1): cum_sum.append(cum_sum[-1]+array[i+1])
    return cum_sum

def combination(n: int, r: int):
    """ nCrを求める関数 """
    return factorial(n) // factorial(r) // factorial(n - r)

# グラフ理論
def dijkstra(E, s):
    """ ダイクストラ法 """
    dist = [inf] * len(E)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, v = heappop(pq)
        if d > dist[v]:
            continue
        for u, weight in E[v]:
            nd = u + weight
            if dist[u]>nd:
                dist[u]=nd
                heappush(pq, (nd, u))
    return dist

def warshall_floyd(G):
    """ ワーシャルフロイド法 """
    node = len(G)
    for m in range(node): # 中継点
        for s in range(node): # 始点
            for g in range(node): # 終点
                G[s][g] = min(G[s][g], G[s][m]+G[m][g])
    return G

# main