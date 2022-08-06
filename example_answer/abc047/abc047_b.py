import sys
input = sys.stdin.readline

w,h, n = map(int, input().split())
xya = [map(int, input().split()) for _ in range(n)]

square = [[0]*h for _ in range(w)]

x_left, x_right = 0, w
y_up, y_down = 0, h
for x, y, a in xya:
    if a==1:
        x_left = max(x, x_left) 
    elif a==2:
        x_right = min(x,x_right)
    elif a==3:
        y_up = max(y,y_up)
    else:
        y_down = min(y,y_down)

if (x_right-x_left)<=0 or (y_down-y_up)<=0: print(0)
else: print((x_right-x_left)*(y_down-y_up))
