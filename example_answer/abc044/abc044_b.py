import sys
from collections import Counter
input = sys.stdin.readline

"""
collectionsのCounter関数を用いることで
文字列内の種類と利用回数を取得することができます
"""
w = input().strip()
count_w = Counter(w)

for key in count_w:
    if count_w[key]%2!=0:
        print("No")
        exit()

print("Yes")
