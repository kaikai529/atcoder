import sys
input = sys.stdin.readline

n = int(input())
a = ["" for _ in range(n)]


for i in range(n): a[i]=input().strip()

for i in range(n):
    for j in range(i+1,n):
        if a[i][j]=="D" and a[i][j]==a[j][i]: continue
        elif a[i][j]=="L" and a[j][i]=="W": continue
        elif a[i][j]=="W" and a[j][i]=="L": continue
        print("incorrect")
        exit()

print("correct")