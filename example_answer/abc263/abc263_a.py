import sys
from collections import Counter
input = sys.stdin.readline

card = list(map(int, input().split()))
card_cnt = Counter(card)

if 2 in card_cnt.values() and 3 in card_cnt.values():
    print("Yes")
else: print("No")
