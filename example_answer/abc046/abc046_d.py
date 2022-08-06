import sys
input = sys.stdin.readline

s = input().strip()

g = 0
p = 0
ans = 0
for i, s_ in enumerate(s):
    # 初手
    if i==0: 
        g+=1
        if s_=="p": ans-=1
        continue
    # 初手以降
    if s_=="p":
        if g > p:
            p+=1
        else:
            g+=1
            ans-=1
    else:
        if g > p:
            p+=1
            ans+=1
        else: g+=1
print(ans)
    