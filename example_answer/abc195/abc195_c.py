import sys
input = sys.stdin.readline

n = int(input())
min_ = "1"
max_ ="999"
cnt = 0

for i in range(5):
    if n<=int(max_): break
    
    cnt += ( int(max_)-int(min_)+1 )*i
    min_ = "".join([min_, "000"])
    max_ = "".join([max_, "999"])
    

cnt += ( n - int(min_)+1 )*i 
if n==10**15: cnt+=1
print(cnt)

