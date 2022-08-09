import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
condition = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
choice = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for balls in itertools.product(*choice):
    print(balls)
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in condition)
    if ans < cnt:
        ans = cnt

print(ans)