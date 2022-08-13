import sys
input = sys.stdin.readline

def func(a, b):
    return max(len(str(a)), len(str(b)))

n = int(input())

ans = 10
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        ans = min(ans, func(i,n//i))
print(ans)