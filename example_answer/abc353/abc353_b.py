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
n, k = IN()
A = IN(list)

ans = 0
group_idx = 0
while group_idx<n:
    if group_idx==n-1:
        ans+=1
        break
    stack=A[group_idx]
    for j in range(group_idx+1,n):
        group_idx=j
        if stack+A[j]>k:
            ans+=1
            break
        stack+=A[j]

print(ans)
        
