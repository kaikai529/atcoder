import sys
input = sys.stdin.readline

n = int(input())

ans = 0
# A < B
for a in range(1,int(n**0.5)+1):
    for b in range(a+1,n):
        if a*b < n: ans+=1
        else: break
ans*=2

# A=B
for a in range(1, int(n**0.5)+1):
    if a*a < n: ans+=1

print(ans)

"""# recommended answer
ans = 0
for i in range(1,n):
    ans += (n-1)//i
print(ans)

"""


