import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

unlike = []
for b_ in b:
    unlike.append(a[b_-1])

if max(a) == max(unlike):
    print("Yes")
else:
    print("No")
