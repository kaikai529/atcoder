import sys
input = sys.stdin.readline

n = input()
total = 0
for i in n:
    if i=="\n":break
    total += int(i)

if total%9==0: print("Yes")
else: print("No")