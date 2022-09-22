from collections import Counter, defaultdict
from queue import LifoQueue, Queue
import sys
input = sys.stdin.readline

# 自作ライブラリ


def hold(n): return n


def IN():
    input_ = input().strip().split()
    return int(*input_) if len(input_) == 1 else map(int, input_)


def STR_IN():
    return input().strip()


def INs(len_n: int, trans_func=list):
    return [trans_func(map(int, input().split())) for _ in range(len_n)]
    

def STR_INs(len_n: int):
    return [input().strip() for _ in range(len_n)]

# main
n = IN()

points = INs(n, tuple)
seen = dict()
for point in points:
    seen[point] = 0

vec_dx = [-1, -1, 0, 0, 1, 1]
vec_dy = [-1, 0, -1, 1, 0, 1]

group_num = 0
for point in points:
    if seen[point] == 0:
        group_num += 1
        seen[point] = group_num
    else:
        continue
    q = LifoQueue()
    q.put(point)
    while not q.empty() :
        point = q.get()
        for dx, dy in zip(vec_dx, vec_dy):
            check_point = (point[0]+dx, point[1]+dy)
            if check_point in points and seen[check_point] == 0:
                q.put(check_point)
                seen[check_point] = group_num

print(group_num)
