import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
s_dict = defaultdict(int)

for i in range(n):
    s = input().strip()
    if s_dict[s]==0:
        print(s)
    else:
        print(s+"("+str(s_dict[s])+")")
    s_dict[s]+=1

