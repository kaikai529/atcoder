from collections import Counter
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
strings = [input().strip() for _ in range(n)]

ans = 0
for i in range(2**n+1):
    kinds = set()
    string = []
    for j in range(n):
        if (i>>j)&1:
            string.extend(strings[j])
    str_cnt = Counter(string)

    for key in str_cnt.keys():
        if str_cnt[key] == k:
            kinds.add(key)
    ans = max(ans, len(kinds))

print(ans)
