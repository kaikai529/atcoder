import sys
input = sys.stdin.readline

n = int(input())
dishes = list(map(int, input().split()))

ans = 0
cnt = [0]*n
for i, dish in enumerate(dishes):
    # 回す回数を数える
    cnt[((i-1)-dishes[i]+n)%n] += 1
    cnt[(i-dishes[i]+n)%n] += 1
    cnt[((i+1)-dishes[i]+n)%n] += 1

ans = max(cnt)
print(ans)