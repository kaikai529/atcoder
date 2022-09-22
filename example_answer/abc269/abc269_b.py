import sys
input = sys.stdin.readline

S = [input().strip() for _ in range(10)]

min_x = 10
max_x = 0
min_y = 10
max_y = 0
for y in range(10):
    for x in range(10):
        if S[y][x] == "#":
            min_x = min(min_x, x+1)
            max_x = max(max_x, x+1)

            min_y = min(min_y, y+1)
            max_y = max(max_y, y+1)

print(min_y, max_y)
print(min_x, max_x)