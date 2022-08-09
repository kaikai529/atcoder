import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for a, b in ab:    
    ans += (a+b)*(b-a+1)//2

print(ans)