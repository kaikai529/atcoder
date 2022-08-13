import sys
input = sys.stdin.readline

h, w = map(int, input().split())

point = []
for h_ in range(h):
    s = input().strip()
    for w_, s_ in enumerate(s):
        if s_ == "o":
            point.append([h_, w_])

(sx, sy), (gx, gy) = point[0], point[1]
print(abs(sx-gx)+abs(sy-gy))
