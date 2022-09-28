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
checker = {0: 0, 2: 0, 4: 0}

for _a in a:
    if _a%4==0:
        checker[4] += 1
    elif _a%2==0:
        checker[2] += 1
    else:
        checker[0] += 1


if n==2 and (checker[4]>=1 or checker[2]>=2):
    print("Yes")
elif n==3 and (checker[4]>=1 or checker[2]>=3):
    print("Yes")
elif checker[2]==0 and checker[0]-checker[4] <= 1:
    print("Yes")
elif checker[0]-checker[4] <= 0:
    print("Yes")
else:
    print("No")
