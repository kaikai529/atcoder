import sys
input = sys.stdin.readline

l1, r1, l2, r2 = map(int, input().split())
x1 = set([i for i in range(l1,r1+1)])
x2 = set([i for i in range(l2,r2+1)])

print(max(len(x1&x2)-1, 0))

