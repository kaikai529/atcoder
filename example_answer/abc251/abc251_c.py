import sys
from typing import Counter
input = sys.stdin.readline

n = int(input())

strings, scores = [], []
for _ in range(n):
    string, score = input().split()
    strings.append(string)
    scores.append(int(score))

strings_cnt = Counter(strings)

most_string = strings[0]
most_score = scores[0]
most_index = 1
strings_cnt.pop(strings[0])
for i in range(1,n):
    if strings_cnt[strings[i]]!=0:
        strings_cnt.pop(strings[i])
        if most_score < scores[i]:
            most_string = strings[i]
            most_score = scores[i]
            most_index = i+1

print(most_index)
