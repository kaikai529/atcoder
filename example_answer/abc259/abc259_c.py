import sys
input = sys.stdin.readline

s = list(input())
t = list(input())

for i in range(len(t)):
    if s[i]=="\n": break 
    if s[i]==s[i+1] and s[i]!=s[i+2]:
        if s[i]==t[i] and s[i]==t[i+1] and s[i]==t[i+2]:
            s.insert(i,s[i])

if s==t: print("Yes")
else: print("No")


