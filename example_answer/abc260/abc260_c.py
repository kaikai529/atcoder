import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())

red = [0]*n
blue = [0]*n

red[-1] = 1
cnt = n-1
while sum(red[1:n+1]) + sum(blue[1:n+1]) > 0:
    # change red
    red[cnt-1] += red[cnt]
    blue[cnt] += red[cnt]*x
    red[cnt] = 0

    # change blue
    red[cnt-1] += blue[cnt]
    blue[cnt-1] += blue[cnt]*y
    blue[cnt] = 0
    
    cnt -= 1

print(blue[0])
