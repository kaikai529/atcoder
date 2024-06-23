from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from itertools import combinations, count, permutations, product
from math import ceil, factorial, floor, gcd, inf, sqrt
from collections import Counter, defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)  # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7
VEC4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VEC9 = list(product([-1, 0, 1], [-1, 0, 1]))

# 自作関数
def lcm(a, b) -> int:
    """最小公倍数を求める関数
    """
    return a*b // gcd(a, b)

def prime_numbers(max_n)->list:
    """素数数列を返す
    """
    def is_prime(n):
        # 素数判定
        for p in ps:
            if n % p == 0:
                return False
            if p ** 2 >= n:
                break
        return True
    ps = []
    for n in range(2, max_n+1):
        if is_prime(n):
            ps.append(n)

    return ps

def divisor(n: int)->list:
    """約数を返す
    """
    ans = []
    for i in range(1, ceil(sqrt(n))+1):
        if n % i == 0:
            ans.append(i)
            ans.append(n//i)
    return ans

def cum(array: list, key=lambda x: x):
    # 累積和
    cum_sum = [key(array[0])]
    for i in range(len(array)-1):
        cum_sum.append(cum_sum[-1]+key(array[i+1]))
    return cum_sum


def nCr(n: int, r: int):
    # desc: nCrを求める関数
    if n<r: return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def rle(s):
    # ランレングス圧縮
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr

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


def STR_INs(len_n: int, trans_func=None):
    return [STR_IN(trans_func) for _ in range(len_n)] if trans_func else [STR_IN().strip() for _ in range(len_n)]

def double_range(h, w):
    return product(range(h), range(w))

# main
h, w = IN()

start = []
goal = []
A = [[] for _ in range(h)]
seen = [[True for _ in range(w)] for _ in range(h)]
for _h in range(h):
    A[_h] = STR_IN(list)
    for _w in range(w):
        if A[_h][_w]=="S":
            start = [_h, _w]
        if A[_h][_w]=="T":
            goal = [_h, _w]
        if A[_h][_w]=="#":
            seen[_h][_w] = False
            
n = IN()
item = defaultdict(int)
for _ in range(n):
    r, c, e = IN()
    item[(r-1,c-1)] = e

this_h, this_w = start
act = item[(this_h, this_w)]
stack = [[this_h, this_w, act, item]]
cnt = 0
print("----------")
while len(stack)>0:
    cnt+=1
    #if cnt==20: break
    this_h, this_w, _act, _item = stack.pop()
    print(this_h, this_w, _act)
    if (this_h, this_w)==goal:
        print("Yes")
        exit()
    for dw, dh in VEC4:
        next_h, next_w = this_h+dh, this_w+dw
        if 0<=next_h<h and 0<=next_w<w:
            if seen[next_h][next_w] and _act>0:
                act_tmp = _act+_item[(next_h, next_w)]-1
                item_tmp = deepcopy(_item)
                item_tmp[(next_h, next_w)] = 0
                stack.append([next_h, next_w, act_tmp, item_tmp])
print("No")