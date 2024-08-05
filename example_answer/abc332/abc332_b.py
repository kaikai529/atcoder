from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
# 定数
MOD = 10**9+7
VEC4 = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
VEC9 = list(product([-1, 0, 1], [-1, 0, 1]))
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 入力
input = sys.stdin.readline
def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list: return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)

def STR_IN(trans_func=lambda x: x):
    input_ = input().strip().split()
    return trans_func(input_[0]) if len(input_) == 1 else input_

def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])

def STR_INs(len_n: int, trans_func=None):
    return [STR_IN(trans_func) for _ in range(len_n)] if trans_func else [STR_IN().strip() for _ in range(len_n)]

# 自作関数
def lcm(a, b) -> int:
    """ 最小公倍数を求める関数 """
    return a*b // gcd(a, b)

def prime_numbers(max_n)->list:
    """ 素数数列を返す """
    def is_prime(n):
        # 素数判定
        for p in ps:
            if n % p == 0: return False
            if p ** 2 >= n: break
        return True
    ps = []
    for n in range(2, max_n+1):
        if is_prime(n): ps.append(n)
    return ps

def divisor(n: int)->list:
    """ 約数を返す """
    ans = []
    for i in range(1, ceil(sqrt(n))+1):
        if n % i == 0: ans.extend([i, n//i])
    return ans

def cum(array: list, key=lambda x: x):
    # 累積和
    cum_sum = [key(array[0])]
    for i in range(len(array)-1):
        cum_sum.append(cum_sum[-1]+key(array[i+1]))
    return cum_sum


def nCr(n: int, r: int):
    # desc: nCrを求める関数
    if n<r: return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def rle(s):
    # ランレングス圧縮
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr

def double_range(h, w):
    return product(range(h), range(w))

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
k, g, m = IN()

tg = 0
tm = 0
for _ in range(k):
    if tg==g: 
        tg=0
    elif tm==0: 
        tm=m
    else: 
        tg, tm = min(tg+tm, g), max(0,tm-(g-tg))
print(tg, tm)