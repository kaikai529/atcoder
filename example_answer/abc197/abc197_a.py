import sys
input = sys.stdin.readline

s = input().strip()
print("".join([s[1:4], s[0]]))