import sys
from collections import Counter
input = sys.stdin.readline

abc = input().strip()

cnt_abc = Counter(abc)
if cnt_abc["5"]==2 and cnt_abc["7"]==1:
    print("YES")
    exit()
print("NO")
