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

n = IN()
a = IN(list)
color = defaultdict(int)

for _a in a:
    if 1 <= _a <= 399:
        color["gray"] += 1
    elif 400 <= _a <= 799:
        color["brown"] += 1
    elif 800 <= _a <= 1199:
        color["green"] += 1
    elif 1200 <= _a <= 1599:
        color["light_blue"] += 1
    elif 1600 <= _a <= 1999:
        color["blue"] += 1
    elif 2000 <= _a <= 2399:
        color["yellow"] += 1
    elif 2400 <= _a <= 2799:
        color["orange"] += 1
    elif 2800 <= _a <= 3199:
        color["red"] += 1
    else:
        color["free"] += 1

k = color.keys()
if not "free" in k:
    print(len(k), len(k))
elif len(k) == 1:
    print(1, color["free"])
else:
    min_color = max(1,len(k)-1)
    print(min_color, min_color+color["free"])