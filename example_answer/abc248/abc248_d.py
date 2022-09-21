from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())



for _ in range(q):
    l, r, x = map(int, input().split())