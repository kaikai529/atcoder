""" 考え方
浮動小数点を利用した計算は有効桁数が失われ
計算誤差が生じる

decimalモジュールを利用することで
有効桁数を失わず，計算できる
ただし，計算時間は増加する

"""

import sys
import decimal
from math import ceil, floor, sqrt
input = sys.stdin.readline

x, y, r = map(decimal.Decimal, input().split())

y_max = floor(y+r)
y_min = ceil(y-r)

ans = 0
for y_ in range(y_min, y_max+1, 1):
    d = (r**2-(y-y_)**2).sqrt()
   
    x_max = floor(x+d)
    x_min = ceil(x-d)
    ans += (x_max-x_min+1)

print(ans)