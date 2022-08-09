import sys
input = sys.stdin.readline

sx, sy, gx, gy = map(int, input().split())

x = sx - (sx-gx)*sy / (sy+gy)
print(x)