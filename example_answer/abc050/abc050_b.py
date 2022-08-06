import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

time = sum(t)
for p, x in px:
    print(time-t[p-1]+x)

