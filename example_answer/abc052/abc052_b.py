import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

max_x = 0
this_x = 0
for s_ in s:
    if s_=="I": this_x+=1
    else: this_x-=1
    max_x = max(max_x, this_x)

print(max_x)