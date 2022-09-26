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
    return input().strip()


def INs(len_n: int, trans_func=list):
    return [trans_func(map(int, input().split())) for _ in range(len_n)]


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main

a = STR_IN()
b = STR_IN()

if len(a) > len(b):
    print("GREATER")
elif len(a) < len(b):
    print("LESS")
else:
    for _a, _b in zip(a,b):
        if int(_a) > int(_b):
            print("GREATER")
            exit()
        elif int(_a) < int(_b):
            print("LESS")
            exit()
    print("EQUAL")