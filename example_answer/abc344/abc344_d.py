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
T = STR_IN()
tl = len(T)
n = IN()
bags = STR_INs(n, list)

dp = [[inf for _ in range(tl+1)] for _ in range(n+1)]

dp[0][0] = 0
for i in range(n):
    # 何も末尾に付けない時
    for j in range(tl):
        dp[i+1][j] = dp[i][j]
    
    # bags[i]から一つ選びsを末尾に付ける
    for s in bags[i][1:]:
        sl = len(s)
        # j=0から付けれる文字列を探索
        j=0
        while j+sl<=tl:
            # 文字列を付けられるか
            for k in range(sl):
                if(T[j+k]!=s[k]):
                    flag=False
                    break
            if flag:
                dp[i+1][j+sl]=min(dp[i+1][j+sl],dp[i][j]+1)
            j+=1

if dp[n][tl]==inf:
    print(-1)
else:
    print(dp[n][tl])
""" ゴミコード
TT = [set() for _ in range(len(T))]

for i in range(n):
    for s in bags[i][1:]:
        idx = T.find(s)
        if idx==-1: continue
        
        TT[idx].add((s, len(s), 0, 0))

Q = []
Q.extend(TT[0])
ans = inf
while Q:
    s, len_s, idx_s, cost_s = Q.pop()
    if idx_s==len(T):
        ans = min(ans, cost_s)
    if cost_s>=ans:
        continue
    for ss, len_ss, _, _ in TT[idx_s]:
        Q.append([ss, len_ss, idx_s+len_ss, cost_s+1])
    print(Q)
    
print(ans) if ans!=inf else print(-1)
"""