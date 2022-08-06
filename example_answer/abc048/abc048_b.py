import sys
input = sys.stdin.readline

a, b, x = map(int, input().split())

print(b//x-(a-1)//x)