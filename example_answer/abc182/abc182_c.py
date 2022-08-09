import sys
input = sys.stdin.readline

n = input().rstrip()

ans = 0
for i in range(2**len(n)):
    total = 0
    cnt = 0
    for j in range(len(n)):
        if (i >> j)&1:
            cnt += 1
            total += int(n[len(n)-1-j])
    if total!=0 and total%3==0 and ans < cnt:
        ans = cnt

if ans==0: print(-1)
else: print(len(n)-ans)
