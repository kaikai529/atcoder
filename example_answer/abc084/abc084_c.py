from bisect import bisect_left, bisect_right
from math import ceil, factorial, floor, gcd
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

def dfs(station_idx,this_time):
    # 駅nに到着
    if station_idx >= n-2:
        return this_time
    # 駅mに到着(m<n)
    else:
        # 出発時刻まで待つ
        travel, departure, interval = station_info[station_idx+1]
        
        this_time = max(this_time, departure)
        this_time = departure + ceil((this_time-departure)/interval)*interval
        
        # 移動
        this_time += travel
        return dfs(station_idx+1,this_time)
n = IN()
station_info = INs(n-1, list)
station_info.append([0,0,0])

for i in range(n):
    time = station_info[i][0]+station_info[i][1]
    print(dfs(i, time))