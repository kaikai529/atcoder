import sys
input = sys.stdin.readline
MOD = 10**9+7

n = int(input())

this_power = 1
for i in range(1,n+1):
    this_power*=i
    this_power%=MOD

print(this_power)

