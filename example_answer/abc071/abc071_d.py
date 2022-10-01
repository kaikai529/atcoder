from math import factorial, gcd
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
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


def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main

n = IN()
s = STR_INs(2)

idx = 0
ans = 0
pattern = -1
while idx < n:
    # pattern 1
    if s[0][idx] == s[1][idx]:
        if pattern == -1:
            ans = 3
        elif pattern == 1:
            ans *= 2
        else:
            ans *= 1
        idx += 1
        pattern = 1
    # pattern 2
    else:
        if pattern == -1:
            ans = 6
        elif pattern == 1:
            ans *= 2
        else:
            ans *= 3
        idx += 2
        pattern = 2

print(ans%MOD)
