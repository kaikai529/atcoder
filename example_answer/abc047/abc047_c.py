import sys
input = sys.stdin.readline

w = input().strip()

ans = 0
for i in range(len(w)-1):
    if w[i]!=w[i+1]: ans+=1

print(ans)