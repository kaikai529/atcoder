import sys
input = sys.stdin.readline

n = int(input())
s = [input().strip() for _ in range(n)]

def dfs(a):
    if a==n: return 1
    if s[a]=="AND":
        return dfs(a+1)
    else:
        return 2**(a+1)+dfs(a+1)

print(dfs(0))
    

