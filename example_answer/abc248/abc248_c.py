import sys
input = sys.stdin.readline
MOD = 998244353

n, m, k = map(int, input().split())
dp = [[0]*n for _ in range(k)]