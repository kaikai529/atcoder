import sys
input = sys.stdin.readline

n = int(input())

ans = 0
for i in range(1,n+1):
    i10 = str(i)
    i08 = oct(i)
    flag10 = True
    flag08 = True
    for j in i10:
        if j=='7':
            flag10=False
            break
    for k in i08:
        if k=='7':
            flag08=False
            break 
    if flag08 and flag10: ans += 1

print(ans)