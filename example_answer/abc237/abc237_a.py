import sys
input = sys.stdin.readline

n = int(input())

if -2**31 <= n < 2**31: print("Yes")
else: print("No")