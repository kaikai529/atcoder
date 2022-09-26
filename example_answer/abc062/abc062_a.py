from math import factorial
from collections import Counter, defaultdict
from queue import LifoQueue, Queue
import sys
input = sys.stdin.readline

# 自作関数


def combination(n: int, r: int):
    return factorial(n) // factorial(r) // factorial(n - r)


def IN(trans_func=lambda x: x):
    input_ = input().strip().split()
    return int(*input_) if len(input_) == 1 else trans_func(map(int, input_))


def STR_IN():
    input_ = input().strip()
    return input_ if len(input_) == 1 else input_.split()


def INs(len_n: int, trans_func=list):
    return [trans_func(map(int, input().split())) for _ in range(len_n)]


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]


# main
group_a = set([1, 3, 5, 7, 8, 10, 12])
group_b = set([4, 6, 9, 11])
group_c = set([2])

x, y = IN()
group_xy = set([x, y])

if group_xy & group_a == group_xy:
    print("Yes")
elif group_xy & group_b == group_xy:
    print("Yes")
elif group_xy & group_c == group_xy:
    print("Yes")
else:
    print("No")
