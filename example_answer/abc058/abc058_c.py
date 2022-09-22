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


# main
n = IN()
S = STR_INs(n)

cnt_list = []
for s in S:
    cnt_list.append(Counter(s))

ans = dict()
for c_num in range(ord('a'), ord('z')+1):
    ans[chr(c_num)] = 51

for s_cnt in cnt_list:
    for c_num in range(ord('a'), ord('z')+1):
        key = chr(c_num)
        ans[key] = min(ans[key], s_cnt[key]) if key in s_cnt.keys() else 0


for key in ans.keys(): 
    print(key*ans[key], end="")
