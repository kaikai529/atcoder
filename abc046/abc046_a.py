import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
color = set([a,b,c])

print(len(color))