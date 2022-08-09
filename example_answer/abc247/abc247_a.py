import sys
input = sys.stdin.readline

s = input().strip()

print("".join(["0", *s])[:len(s)])
