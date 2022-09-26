from math import factorial, inf
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

n = IN()
a = IN(list)

cusum_a = [a[0]]
for i in range(n-1):cusum_a.append(cusum_a[-1]+a[i+1])

ans = inf
for i in range(n-1):
    ans = min(ans, abs(cusum_a[-1]-2*cusum_a[i]))
print(ans)
