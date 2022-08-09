import sys
input = sys.stdin.readline

n, x = map(int, input().split())
vp = [list(map(int, input().split())) for i in range(n)]

this_alc = x*100
for i, (v, p) in enumerate(vp):
    this_alc -= v*p

    if this_alc<0: 
        print(i+1)
        exit()
print("-1")