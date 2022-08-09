import sys
input = sys.stdin.readline

n, x = map(int, input().split())
s = input().strip()

for s_ in s:
    if s_=="o":
        x+=1
    if s_=="x" and x > 0:
        x-=1

print(x)
