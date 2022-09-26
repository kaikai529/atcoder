from collections import Counter, defaultdict
import sys
input = sys.stdin.readline
# 自作ライブラリ


def IN():
    input_ = input().strip().split()
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    return input().strip()


def INs(len_n: int):
    return [map(int, input().split()) for _ in range(len_n)]


def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

