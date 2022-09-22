from math import factorial
from collections import Counter, defaultdict
from queue import LifoQueue, Queue
import sys
input = sys.stdin.readline

# 自作関数


def hold(n): return n


def combination(n: int, r: int):
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=hold):
    input_ = input().strip().split()
    return int(*input_) if len(input_) == 1 else hold(map(int, input_))


def STR_IN():
    return input().strip()


def INs(len_n: int, trans_func=list):
    return [trans_func(map(int, input().split())) for _ in range(len_n)]


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main
