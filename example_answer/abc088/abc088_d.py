from bisect import bisect_left, bisect_right
from copy import deepcopy
from itertools import count, product
from math import ceil, factorial, floor, gcd
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import queue
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7

# 自作関数


def lcm(a, b):
    # desc: 最小公倍数を求める関数
    return a*b // gcd(a, b)


# 素数数列を返す
def prime_numbers(max_n):
    ps = []

    def is_prime(n):
        for p in ps:
            if n % p == 0:
                return False
            if p ** 2 >= n:
                break
        return True

    for n in range(2, max_n+1):
        if is_prime(n):
            ps.append(n)

    return ps


def cum(array: list, key= lambda x:x):
    cum_sum = [key(array)[0]]
    for i in range(len(key(array))-1):
        cum_sum.append(cum_sum[-1]+key(array)[i+1])
    return cum_sum


def combination(n: int, r: int):
    # desc: nCrを求める関数
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    input_ = input().strip().split()
    return input_[0] if len(input_) == 1 else input_


def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [list(input().strip()) for _ in range(len_n)]


# main

h, w = IN()
s = STR_INs(h)
sharp = 0
for _h, _w in product(range(h),range(w)):
    if s[_h][_w] == "#": sharp += 1

seen = [[False]*(w) for _ in range(h)]
dp = [[0]*w for _ in range(h)]
vec = [(1,0),(-1,0),(0,1),(0,-1)]

q = Queue()
q.put((0,0))
seen[0][0] = True
dp[0][0] = 1

while not q.empty():
    y, x = q.get()
    for dy, dx in vec:
        if 0 <= y+dy < h and 0<= x+dx < w:
            if s[y+dy][x+dx] == "." and seen[y+dy][x+dx]==False:
                dp[y+dy][x+dx] = dp[y][x] + 1
                seen[y+dy][x+dx] = True
                q.put((y+dy,x+dx))

min_distance = dp[h-1][w-1]
if min_distance == 0:
    print(-1)
else:
    print(h*w-sharp-min_distance)

