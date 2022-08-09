import sys
input = sys.stdin.readline

t = int(input())

ans = 1
for i in range(t-1,t-12,-1):
    ans *= i

for i in range(2,12):
    ans //= i

print(ans)