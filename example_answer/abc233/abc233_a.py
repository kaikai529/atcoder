import sys
from math import ceil
input = sys.stdin.readline

x, y = map(int, input().split())
print(max(ceil((y-x)/10),0))
