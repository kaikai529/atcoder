from bisect import bisect_left, bisect_right
from math import factorial, gcd, inf
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7) # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7

# 自作関数


def lcm(a, b):
    # desc: 最小公倍数を求める関数
    return a*b // gcd(a, b)


def combination(n: int, r: int):
    # desc: nCrを求める関数
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

n = IN()
F = INs(n, list)
P = INs(n, list)

ans = -inf
for i in range(1, 2**10):
    shop_profit = 0
    for shop_idx in range(n):
        cnt = 0
        for j in range(10):
            if i>>j&1 and F[shop_idx][j]:
                cnt += 1
        shop_profit += P[shop_idx][cnt]
    ans = max(ans, shop_profit)

print(ans)
