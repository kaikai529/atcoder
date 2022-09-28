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
    if trans_func == list:
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
n = IN()
colors = IN(list)

grid = [0]*(h*w)
this_idx = 0
for color_num, color in enumerate(colors):
    for _ in range(color):
        grid[this_idx] = color_num+1
        this_idx += 1

_h = 0
for idx in range(0,h*w,w):
    if _h%2==0: 
        print(*grid[idx:idx+w])
    else:
        print(*grid[idx:idx+w][::-1])
    _h += 1

