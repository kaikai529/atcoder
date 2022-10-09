from bisect import bisect_left, bisect_right
from itertools import product
from math import factorial, gcd
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

h, w = IN()
c = INs(10, list)
a = INs(h, list)


for middle, point1, point2 in product(*[range(10) for _ in range(3)]):
    c[point1][point2] = min(c[point1][point2], c[point1][middle]+c[middle][point2])

ans = 0
for _h in range(h):
    for _w in range(w):
        num =  a[_h][_w]
        if num == -1:
            continue
        ans += c[num][1]

print(ans)