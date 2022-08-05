import sys
input = sys.stdin.readline

h, w = map(int, input().split())

for i in range(h):
    c = input().strip()
    print(c+"\n"+c)

