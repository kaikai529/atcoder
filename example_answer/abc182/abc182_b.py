import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

gcd_list = []
for i in range(n): gcd_list.append([])

ans = 0
num = 0
for i in range(2, max(A)+1):
    cnt = 0
    for j in A:
        if j%i==0: cnt += 1
    if ans < cnt:
        ans = cnt
        num = i

print(num)
