import sys
input = sys.stdin.readline
MOD = 10**9+7

def power_mod(num:int, mul:int):
    
    ans = 1
    for _ in range(mul):
        ans = (ans*num)%MOD
    return ans

n = int(input())

ans = power_mod(10,n)-2*power_mod(9,n)+power_mod(8,n)
print(ans%MOD)
