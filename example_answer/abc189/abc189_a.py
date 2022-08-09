import sys
input = sys.stdin.readline

c = input().strip()
 
for i in range(len(c)-1):
    if c[i]!=c[i-1]:
        print("Lost")
        exit()
 
print("Won")

## 別案
#print("Won") if len(set(list(input().strip())))==1 else print("Lost")