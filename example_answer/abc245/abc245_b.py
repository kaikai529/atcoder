import sys
input = sys.stdin.readline

n = int(input())
a = set(list(map(int, input().split())))
a = list(a)
a.sort()

for i in range(len(a)):
    if a[i]!=i:
        print(i)
        exit()
print(len(a))