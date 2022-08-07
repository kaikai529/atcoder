import sys
input = sys.stdin.readline

s = input().strip()

a_index = 0
for i in range(len(s)):
    if s[i]=="A":
        a_index = i
        break

z_index = 0
for i in range(len(s)-1,-1,-1):
    if s[i]=="Z":
        z_index = i
        break

print(z_index-a_index+1)