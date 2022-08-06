import sys
from collections import Counter
input = sys.stdin.readline
MOD = 10**9+7

n = int(input())
a = list(map(int, input().split()))
cnt_a = Counter(a)

flag = True
if n%2==0:
    for i in range(1,n,2):
        if cnt_a[i]!=2: flag=False
else:
    if cnt_a[0]!=1: flag=False
    for i in range(2,n,2):
        if cnt_a[i]!=2: flag=False



if flag: print(2**(n//2)%MOD)
else: print(0)
        
