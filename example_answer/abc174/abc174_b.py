import sys
_input = sys.stdin.readline

n, d = map(int, _input().split())
count = 0
for _ in range(n):
    x, y = map(int, _input().split())
    if abs(x + y * 1j) <= d : count += 1
print(count)
