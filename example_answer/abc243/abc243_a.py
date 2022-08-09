import sys
input = sys.stdin.readline

v, a, b, c = map(int, input().split())

family = [("F", a),("M", b),("T", c)]

this_v = v
cnt = 0
while this_v>=0:
    name, s = family[cnt%3]
    this_v -= s
    if this_v<0:
        print(name)
        break
    cnt += 1