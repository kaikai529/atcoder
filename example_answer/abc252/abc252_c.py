import sys
from collections import Counter
input = sys.stdin.readline

# input data
n = int(input())
s = [[0]*10 for _ in range(n)]
for i in range(n):
    input_s = input().strip()
    for j in range(10):
        s[i][j] = int(input_s[j])

ans = []
# 各数字で必要な秒数を算出
for i in range(10):
    # iが何番目か
    idx = [0]*n
    for j in range(n):
        idx[j] = s[j].index(i)

    # どの位置に何個あるかをカウントする
    cnt = Counter(idx) # (index, num)
    
    # values基準で並べ替え 
    cnt = sorted(cnt.items(), key=lambda x:x[0],reverse=True)
    cnt = sorted(cnt, key=lambda x:x[1], reverse=True)
    index, num = cnt[0]
    time = 10*(num-1)+index
    ans.append(time)

print(min(ans))
