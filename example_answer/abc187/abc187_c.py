import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

S = []
S_ = []

for i in range(n):
    s = input().rstrip()
    if s[0]=="!":
        S_.append(s[1:])
    else: S.append(s)

S = set(S)
S_ = set(S_)

ans = S & S_

if len(ans)==0: print("satisfiable")
else: print(ans.pop())