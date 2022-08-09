import sys
input = sys.stdin.readline

d_all = set("0123456789")
n, k = map(int, input().split())
d = set(input().strip().split())

use = d_all - d
for i in range(n, 10*n+1):
    ans = set(str(i)) - use
    if len(ans)==0:
        print(i)
        break

