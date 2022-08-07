import sys
input = sys.stdin.readline

x = int(input())
n = x//11

if x%11==0: print(2*n)
elif x%11<=6: print(2*n+1)
else: print(2*n+2)