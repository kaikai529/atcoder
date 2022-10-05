from math import factorial, gcd
from collections import Counter, defaultdict
from os import defpath
from queue import LifoQueue, Queue
import sys
sys.setrecursionlimit(10 ** 7) # 再起関数の再起上限
input = sys.stdin.readline
# 定数
MOD = 10**9+7

# 自作関数


def lcm(a, b):
    # desc: 最小公倍数を求める関数
    return a*b // gcd(a, b)


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


def INs(len_n: int, trans_func=lambda x:x):
    return trans_func([IN(trans_func) for _ in range(len_n)])


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main
s = STR_IN()
t = STR_IN()

rev_s = s[::-1]
rev_t = t[::-1]

key_idx = -1


for i in range(len(s)-len(t)+1):
    flag = True
    for j in range(len(t)):
        if rev_s[i+j] == "?":
            continue
        if rev_s[i+j] != rev_t[j]:
            flag = False
            break
    if flag:
        key_idx = len(s) - i - len(t)
        break

if key_idx == -1:
    print("UNRESTORABLE")
    exit()

ans = list("".join([s[:key_idx],t,s[key_idx+len(t):]]))

for i in range(len(s)): 
    if ans[i] == "?":
        ans[i] = "a"
print("".join(ans))