import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt_a = Counter(a)

count = 0
for key in cnt_a.keys():
    if cnt_a[key] >=3:
        cnt_a[key]=1 if cnt_a[key]%2 else 2
    if cnt_a[key]==2:
        count += 1

print(len(cnt_a.keys())-count%2)