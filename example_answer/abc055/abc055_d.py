import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

S = True
W = False

ans = [-1]
init_animals = [S,S], [S,W], [W,S], [W,W]
for init in init_animals:
    animals = [0]*n
    animals[0:2]=init
    for i in range(1,n-1):
        # 羊の時
        if animals[i]==S:
            animals[i+1]=animals[i-1] if s[i]=="o" else not animals[i-1]
        # 狼の時
        else:
            animals[i+1]=animals[i-1] if s[i]=="x" else not animals[i-1]
    # 最後の動物
    if animals[-1]==S:
        if (s[-1]=="o" and animals[0]==animals[-2])\
            or (s[-1]=="x" and animals[0]!=animals[-2]):
            pass
        else:
            continue
    elif animals[-1]==W:
        if (s[-1]=="x" and animals[0]==animals[-2])\
            or (s[-1]=="o" and animals[0]!=animals[-2]):
            pass
        else:
            continue
    if animals[0]==S:
        if (s[0]=="o" and animals[-1]==animals[1])\
            or (s[0]=="x" and animals[-1]!=animals[1]):
            ans = animals
            break
    elif animals[0]==W:
        if (s[0]=="x" and animals[-1]==animals[1])\
            or (s[0]=="o" and animals[-1]!=animals[1]):
            ans=animals
            break

if len(ans)==1:
    print(-1)
else:
    for animal in ans:
        if animal: print("S", end="")
        else: print("W", end="")    