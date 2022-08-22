from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

names = []
for _ in range(n):
    s, t = input().split()
    names.append(s)
    names.append(t)

names_cnt = Counter(names)
for check_idx in range(n):
    family_name = names[2*check_idx]
    last_name = names[2*check_idx+1]
    if family_name == last_name and names_cnt[family_name] == 2:
        continue
    elif names_cnt[family_name]==1 or names_cnt[last_name]==1:
        continue
    else:
        print("No")
        exit()

print("Yes")