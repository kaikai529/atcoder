from math import factorial
from collections import Counter, defaultdict
from queue import LifoQueue, Queue
import sys
input = sys.stdin.readline

# 自作関数


def combination(n: int, r: int):
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().strip().split()
    return int(*input_) if len(input_) == 1 else trans_func(map(int, input_))


def STR_IN():
    input_ = input().strip()
    return input_ if len(input_) == 1 else input_.split()


def INs(len_n: int, trans_func=list):
    return [trans_func(map(int, input().split())) for _ in range(len_n)]


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main


h, w = IN()
A = STR_INs(h)
wrap_a = [["#"]*(w+2) for _ in range(h+2)]

for _h in range(h):
    for _w in range(w):
        wrap_a[_h+1][_w+1] = A[_h][_w]

for _h in range(h+2):
    print("".join(wrap_a[_h]))
