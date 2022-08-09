import sys
input = sys.stdin.readline

s = input().strip()

for i, s_ in enumerate(s):
    i = i+1
    if i%2==0 and ord(s_) <= ord("Z"):
        continue
    elif i%2==1 and ord(s_) >= ord("a"):
        continue
    else:
        print("No")
        exit()

print("Yes")