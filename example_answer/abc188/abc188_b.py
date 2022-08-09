import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for a_, b_ in zip(a,b):
    ans += a_*b_

if ans==0: print("Yes")
else: print("No")