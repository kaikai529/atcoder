from copy import deepcopy
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


n = IN()
dp = [0]*10001

dp[0] = 1
for _ in range(n):
    score = IN()
    this_dp = deepcopy(dp)
    for idx, flag in enumerate(this_dp):
        if flag:
            dp[idx+score] = 1

for idx, flag in enumerate(dp[::-1]):
    if flag and idx%10!=0:
        print(10000-idx)
        exit()
print(0)
