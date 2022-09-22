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

s = STR_IN()
pwd_req = set()
pwd_pos = set()
for i, _s in enumerate(s):
    if _s == "o":
        pwd_req.add(i)
    elif _s == "?":
        pwd_pos.add(i)

ans = 0
for pwd in range(0, 10000):
    n_place = set()
    for n in range(4):
        n_place.add(pwd % 10)
        pwd //= 10
    
    if (pwd_req&n_place) != pwd_req:
        continue
    if (pwd_req|pwd_pos)&n_place != n_place:
        continue
    ans += 1

print(ans)


        


