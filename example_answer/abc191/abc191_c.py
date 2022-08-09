import sys
input = sys.stdin.readline

h, w = map(int, input().split())
square = [[0]*h for _ in range(w)] # square=(w,h)

WHITE = 0
BLACK = 1

for h_ in range(h):
    s = input().strip()
    for w_ , s_ in enumerate(s):
        if s_==".":
            square[w_][h_]=WHITE
        else:
            square[w_][h_]=BLACK

ans = 0
for h_ in range(h-1):
    for w_ in range(w-1):
        cnt = square[w_][h_]+square[w_+1][h_]+square[w_][h_+1]+square[w_+1][h_+1]
        if cnt==1 or cnt==3:
            ans+=1

print(ans)