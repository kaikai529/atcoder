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

def this_point(x,y):
    if x%2==y%2==0 or x%2==y%2==1: return "L"
    else: return "R"
    
def ad_dx(idx:str, vec):
    if idx=="L":
        if vec>0: return -1
        else: return 0
    else:
        if vec<0: return -1
        else: return 0
# main
sx, sy = IN()
tx, ty = IN()

dx = tx-sx
dy = ty-sy

# マス目の右か左か
idx = this_point(sx, sy)

# 最初に進行方向にコストを消費しないで動けるかどうか
abs_dx = abs(dx) + ad_dx(idx, dx)

# 上下の移動は必ずコスト1を消費する
abs_dy = abs(dy)
ans = abs_dy

# コストを消費すると必ず，左右に1回動ける
abs_dx-=abs_dy

# 左右に動く必要があるかどうか
if abs_dx<=0:
    print(ans)
else:
    # コスト1で左右に2マス進める
    print(ans+ceil(abs_dx/2))

    
