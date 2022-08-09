import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

count = 0
ans = 0
for d1, d2 in d:
    if d1==d2: count+=1
    else: count = 0
    ans = max(ans, count)

if ans >= 3: print("Yes")
else: print("No")
