import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
w = list((map(int, input().split())))

# (w, s)のリストを作る + 大人の人数を数える
a = list()
cnt = 0
for s_, w_ in zip(s, w):
    if s_=="1": cnt+=1
    a.append([w_, s_])

# sort
a.sort()

# N人分の体重で線引きする
x = cnt
ans = cnt
for i in range(n):
    if a[i][1] == "1": x-=1
    else: x +=1
    if i < n-1:
        # 同じ体重が続く場合はパス
        if a[i][0] != a[i+1][0]:
            ans = max(ans, x)
    else:
        ans = max(ans, x)

print(ans)