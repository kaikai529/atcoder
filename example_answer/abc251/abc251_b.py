import sys
input = sys.stdin.readline

n, w = map(int, input().split())
a = list(map(int, input().split()))

ans = [0]*(w+1)
for i in range(len(a)):
    if a[i] <= w:
        ans[a[i]] = 1
    for j in range(i+1, len(a)):
        if a[i]+a[j] <= w:
            ans[a[i]+a[j]] = 1
        for k in range(j+1, len(a)):
            if a[i]+a[j]+a[k] <= w:
                ans[a[i]+a[j]+a[k]] = 1

print(sum(ans))
