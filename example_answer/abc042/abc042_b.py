import sys
input = sys.stdin.readline

n, l = map(int, input().split())
s = [input().strip() for _ in range(n)]

s.sort()
for s_ in s: print(s_,end="")
