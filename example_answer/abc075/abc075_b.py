from math import factorial
from collections import Counter, defaultdict
from queue import LifoQueue, Queue
import sys
input = sys.stdin.readline

# 定数
MOD = 10**9+7

# 自作関数


def combination(n: int, r: int):
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func==list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_


def INs(len_n: int, trans_func=list):
    return trans_func([IN() for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main

h, w = IN()
wrap_S = [["."]*(w+2) for _ in range(h+2)]

for _h in range(h):
    s = STR_IN()
    for _w in range(w):
        wrap_S[_h+1][_w+1] = s[_w]

vec = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for _h in range(1,h+1):
    for _w in range(1,w+1):
        cnt = 0
        if wrap_S[_h][_w] == "#":
            continue
        for dx, dy in vec:
            if wrap_S[_h+dy][_w+dx] == "#":
                cnt += 1
        wrap_S[_h][_w] = str(cnt)

for _h in range(1,h+1):
    print("".join(wrap_S[_h][1:-1]))

