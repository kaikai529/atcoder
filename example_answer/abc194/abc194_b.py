import sys
input = sys.stdin.readline

n = int(input())

ans = 10**6
A = list()
B = list() 
for i in range(n):
    a, b = map(int, input().split())
    ans = min(ans, a+b)
    A.append((i, a))
    B.append((i, b))

A.sort(key=lambda x:x[1])
B.sort(key=lambda x:x[1])

if A[0][0]!=B[0][0]:
    ans = min(ans, max(A[0][1], B[0][1]))
else:
    ans = min(ans, max(A[1][1], B[0][1]), max(A[0][1],B[1][1]))

print(ans)
