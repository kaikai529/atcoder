import sys
input = sys.stdin.readline

S = input()
T = input()
cnt = 0
min_cnt = len(T)-1

for i in range(len(S)-len(T)+1):
    cnt = 0
    for j in range(len(T)-1):
        if T[j]!=S[i+j]: cnt+=1
    if min_cnt > cnt: min_cnt = cnt

print(min_cnt)


