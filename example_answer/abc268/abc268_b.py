import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

if t.startswith(s):
    print("Yes")
else:
    print("No")