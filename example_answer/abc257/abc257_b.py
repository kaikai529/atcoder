import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
A = list((map(int, input().split())))
L = list((map(int, input().split())))

array = [0]*n
for i in A: array[i-1]=1


for l in L:
    if A[l-1]==n:
        continue
    if array[A[l-1]]==0:
        array[A[l-1]-1]=0
        array[A[l-1]]=1
        A[l-1]+=1
for i in A: print(i, end=" ")