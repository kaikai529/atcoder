import sys
from collections import Counter
input = sys.stdin.readline

s = Counter(input().strip())

for key in s.keys():
    if s[key]==1:
        print(key)
        exit()

print(-1)

