import sys
input = sys.stdin.readline
MOD = 10**9+7

n = int(input())
prime_factor = [0]*(n+1)

for i in range(2,n+1):
    temp = i
    for j in range(2,n+1):
        while temp%j==0:
            temp//=j
            prime_factor[j]+=1

ans = 1
for p in prime_factor: ans*=(p+1)
print(ans%MOD)
