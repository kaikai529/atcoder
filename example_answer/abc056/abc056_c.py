"""
1,2,3,...,n-1,nの部分集合の和は
(1+2+3+...+n)までの整数を網羅する
"""
import sys
input = sys.stdin.readline
N_MAX = 10**5

x = int(input())

ans = 0
for i in range(1, N_MAX):
    if i*(i+1)//2 >= x:
        ans = i
        break
print(ans)
