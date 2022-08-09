import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

this_x = n
for i in range(m+1):
    if i==0:
        this_x = max(0, this_x-ab[i][0])
        if this_x==0:
            print("No")
            exit()
        this_x = min(n, this_x+(ab[i][1]-ab[i][0]))
    elif i==m:
        this_x = max(0, this_x-(t-ab[i-1][1]))
        if this_x==0:
            print("No")
            exit()
    else:
        this_x = max(0, this_x-(ab[i][0]-ab[i-1][1]))
        if this_x==0:
            print("No")
            exit()
        this_x = min(n, this_x+(ab[i][1]-ab[i][0]))
print("Yes")
    


