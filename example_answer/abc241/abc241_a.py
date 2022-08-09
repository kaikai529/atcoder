import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

point = a[0]
for _ in range(2):
    point = a[point]

print(point)