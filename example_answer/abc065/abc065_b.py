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
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_


def INs(len_n: int, trans_func=list):
    return trans_func([IN() for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main
n = IN()
a = INs(n)
seen = [False]*n


button = a[0]
cnt = 0
while not seen[button-1]:
    # this button
    seen[button-1] = True
    cnt += 1
    if button == 2:
        print(cnt)
        exit()
    # next button
    button = a[button-1]
    
print(-1)

