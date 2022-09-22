import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = [0]*n
for _ in range(m):
    x, y = map(int, input().split())
    bonus[x-1] = y

this_time = t
for i in range(n-1):
    this_time += bonus[i]
    this_time -= a[i]
    if this_time<= 0:
        print("No")
        exit()

print("Yes")