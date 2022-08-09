import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, ["0", *input().split()]))


ans = 0
parent = p[n-1]
while  parent>0:
    parent = p[parent-1]
    ans += 1

print(ans) 