from bisect import bisect_left, bisect_right
from itertools import combinations, count, product
from math import ceil, factorial, floor, gcd
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
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
    return [input().strip() for _ in range(len_n)]


# main

numbers = IN(list)
numbers.sort()

ans = 0

# 最小値と中央値を揃える
sub = numbers[1] - numbers[0]

## 操作1
numbers[0] += 2*(sub//2)
ans += sub//2

## 操作2
numbers[0] += sub%2
numbers[2] += sub%2
ans += sub%2

# 最小値（中央値）と最大値を揃える
## 操作2
sub = numbers[2] - numbers[0]
ans += sub

print(ans)