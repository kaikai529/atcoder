import sys
input = sys.stdin.readline

s = input()

count = 0
for i, c in enumerate(s):
    if c=="R" :
        if count==0 : count+=1
        if s[i+1]=="R":
            count+=1
 
print(count) 