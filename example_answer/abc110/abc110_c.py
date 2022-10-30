from bisect import bisect_left, bisect_right
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7
VEC4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VEC9 = product([-1, 0, 1], [-1, 0, 1])
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

# 約数を返す


def divisor(n: int):
    ans = []
    for i in range(1, ceil(sqrt(n))):
        if n % i == 0:
            ans.append(i)
            ans.append(n//i)
    return ans


def cum(array: list, key=lambda x: x):
    cum_sum = [key(array[0])]
    for i in range(len(array)-1):
        cum_sum.append(cum_sum[-1]+key(array[i+1]))
    return cum_sum


def combination(n: int, r: int):
    # desc: nCrを求める関数
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().split()
    if trans_func == list:
        return trans_func(map(int, input_))
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN(trans_func=lambda x: x):
    input_ = input().strip().split()
    return trans_func(input_[0]) if len(input_) == 1 else input_


def INs(len_n: int, trans_func=lambda x: x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main

def lan(string):
    re_list = [[string[0],1]]
    for i in range(1, len(string)):
        if re_list[-1][0] == string[i]:
            re_list[-1][1] += 1
        else:
            re_list.append([string[i],1])
    return re_list

s = STR_IN()
t = STR_IN()

flag = True
# condition1
cnt_s = sorted(Counter(s).items(), reverse=True, key=lambda x:x[1])
cnt_t = sorted(Counter(t).items(), reverse=True, key=lambda x:x[1])
if len(cnt_s) == len(cnt_t):
    for _s, _t in zip(cnt_s, cnt_t):
        if _s[1] != _t[1]:
            flag = False
            break
else:
    flag = False

# condition2
lanrengs_s = lan(s)
lanrengs_t = lan(t)
if len(lanrengs_s) == len(lanrengs_t):
    for _s, _t in zip(lanrengs_s, lanrengs_t):
        if _s[1] != _t[1]:
            break
else:
    flag = False

if flag: print("Yes")
else: print("No")