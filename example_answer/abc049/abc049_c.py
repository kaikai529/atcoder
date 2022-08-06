import sys
input = sys.stdin.readline

s = input().strip()

cnt = 0
while cnt < len(s):
    if s[cnt:cnt+6]=="eraser":  
        cnt+=6
    elif s[cnt:cnt+5]=="erase": 
        cnt+=5
    elif s[cnt:cnt+7]=="dreamer" and\
         (s[cnt+7:cnt+9]=="er" or s[cnt+7:cnt+8]=="d" or s[cnt+7:cnt+8]==""):
            cnt+=7
        
    elif s[cnt:cnt+5]=="dream":
        cnt+=5
    else:
        print("NO")
        exit()

print("YES")
