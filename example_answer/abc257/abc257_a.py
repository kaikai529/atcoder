import sys
input = sys.stdin.readline

n, x = map(int, input().split())

if x%n==0:
    print(chr(ord("A")+x//n-1))
else:
    print(chr(ord("A")+x//n))