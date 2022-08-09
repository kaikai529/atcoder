import sys
input = sys.stdin.readline

s = input().strip()

for i in range(10):
    if not str(i) in s:
        print(i)
        exit()