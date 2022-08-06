""" 考え方
データの平均値（整数）を選択することで
最小値を得ることができる
1. 平均（整数値を求める）
2. 最小値を求める

math.ceil(num) numを超える最小の整数（天井関数）
math.floor(num) numを超えない最大の整数（床関数）
"""
import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 平均値に0.5を足すことで四捨五入を行う
avg_int_a = math.floor(sum(a)/n+0.5)

# 最小値の計算
ans = 0
for a_ in a:
    ans += (a_-avg_int_a)**2

print(ans)