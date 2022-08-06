import sys
input = sys.stdin.readline

n, k = map(int, input().split())

print(k*(k-1)**(n-1))