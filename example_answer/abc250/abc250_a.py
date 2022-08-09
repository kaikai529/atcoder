import sys
input = sys.stdin.readline

h, w = map(int, input().split())
r, c = map(int, input().split())

if h==1 and w==1:
    print(0)
elif h==1 or w==1:
    if 1 < r < h or 1 < c < w:
        print(2)
    else:
        print(1)
else:
    if 1 < r < h and 1 < c < w:
        print(4)
    elif (r==1 and c==1) or (r==h and c==1)\
        or (r==1 and c==w) or (r==h and c==w):
        print(2)
    else:
        print(3)