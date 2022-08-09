import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()
len_s = len(s)-1
querry = [list(map(int, input().split())) for _ in range(q)]

s_point = 0

for form, num in querry:
    if form==1:
        s_point = (s_point-num)%len_s
    else:
        print(s[(s_point+num-1)%len_s])
