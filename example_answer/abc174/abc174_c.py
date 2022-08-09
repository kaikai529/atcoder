import sys
def IN():
    return int(sys.stdin.readline())
    
def INs():
    return map(int, sys.stdin.readline())


k = int(input())
a = 7
a = a % k
for i in range(k):
    a = a % k
    if a == 0:
        print(i+1)
        exit()
    else:
        a = a * 10 + 7
 
print(-1)
