import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

if n==2:
    print(max(a[0]+a[1]-x,0))
    exit()
else:
    ans = [a[0] if a[0]<=x else x]
    for i in range(1,n):
        if ans[-1]+a[i]>x:
            ans.append(x-ans[-1])
        else:
            ans.append(a[i])

print(sum(a)-sum(ans))