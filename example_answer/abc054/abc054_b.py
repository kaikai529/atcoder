import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

for a_y in range(n-m+1): 
    for a_x in range(n-m+1):
        flag=True
        for i in range(m):
            if a[a_y+i][a_x:a_x+m]!=b[i]:
                flag=False
                break
        if flag:
            print("Yes")
            exit()

print("No")  